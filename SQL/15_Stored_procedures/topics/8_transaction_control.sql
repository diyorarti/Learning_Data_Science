-- TRANSACTION CONTROL 
"""
Transaction Control as a safety mechanism for several related databse changes
A transaction is a group of SQL statements that should be treated as one unit. In PostgeSQL, we either keep all the changes with "COMMIT"
or discard with "ROLLBACK".
    Example:
        a bank transfer:
            Ali has 1000
            Bob has 500
            Ali sends 200 to Bob
        Databse changes are required:
            1. Ali: 1000 → 800
            2. Bob: 500 → 700
        if both succed:
            Ali -200 ✓
            Bob +200 ✓
                ↓
            COMMIT → keep all changes made in the current transaction
        if something is wrong:
            Ali -200 ✓
            Bob +200 ✗
                ↓
            ROLLBACK → cancel all changes made in the current transaction

the Core Idea:
TRANSACTION:
        Statement 1
        Statement 2
        Statement 3
            ↓
            valid?
           /    \
        YES      NO
        ↓        ↓
        COMMIT   ROLLBACK
"""


-- creating a report table:
CREATE TABLE transfer_batch_report(
    report_id BIGSERIAL PRIMARY KEY,
    batch_id INTEGER,
    request_id BIGINT,
    result TEXT,
    processed_amount NUMERIC(12, 2),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- creating a stored procedure , Its job is to process all pending money-transfer requests belonging to one batch.
CREATE OR REPLACE process_transfer_batch(
    p_batch_id VARCHAR(50), --  which batch should be processed
    p_chunk_size VARCHAR(50) --  maximum amount that can be transferred during one WHILE-loop iteration
)
LANGUAGE plpgsql
AS $$
DECLARE 
    v_request RECORD; -- current transfer request
    
    v_sender_account INTEGER; -- sender account
    v_receiver_account INTEGER; -- receiver account
    
    v_sender_balance NUMERIC(12, 2); -- sender balance
    v_receiver_balance NUMERIC(12, 2); -- receiver balance

    v_transfer_amount NUMERIC(12, 2); -- transfer amount
    v_remaining_amount NUMERIC(12, 2); -- remaining amount
    v_current_chunk NUMERIC(12, 2); -- current chunk amount

    v_batch_failed BOOLEAN := FALSE; -- batch failed?
    v_failure_reason TEXT; -- failure reason

BEGIN 
    -- DELETE before generating a fresh report for this batch
    DELETE FROM transfer_batch_report
    WHERE 