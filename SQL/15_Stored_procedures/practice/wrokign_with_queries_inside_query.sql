"""
create a stored procedure process_customer_orders
    the procedure should analyze all orders of one customer during a specified period, classify each order and 
    save the results into a seperate reporting table

First create this practice table
    customer_order_report(
    report_id BIGSERIAL PRIMARY KEY,
    customer_id VARCHAR(50),
    order_id VARCHAR(50),
    order_status TEXT,
    payment_amount NUMERIC(12,2),
    review_score NUMERIC(4,2),
    classification TEXT,
    requires_attention BOOLEAN DEFAULT FALSE,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
The procedure will manipulate this table

Parameters(the procedure should receive)
    p_customer_id VARCHAR(50)
    p_start_date TIMESTAMP
    p_end_date TIMESTAMP

Variables
    v_order RECORD;
    v_payment NUMERIC(12, 2);
    v_review_score NUMERIC(4, 2);
    v_classification TEXT;

    v_total_orders BIGINT :=0;
    v_total_spent NUMERIC(12, 2) :=0;
    v_high_value_orders BIGINT :=0;
    v_problem_orders BIGINT :=0;

Part-1 DELETE
    before generating a new report for the customer, remove their previous report rows
        CALL procedure first time
                ↓
        report generated

        CALL again
                ↓
        old report removed
                ↓
        fresh report generated

Part-2 FOR loop + SELECT 
    loop through the customer's orders from the specified period.


"""

-- Creating practice table
CREATE TABLE customer_order_report (
    report_id BIGSERIAL PRIMARY KEY,
    customer_id VARCHAR(50),
    order_id VARCHAR(50),
    order_status TEXT,
    payment_amount NUMERIC(12,2),
    review_score NUMERIC(4, 2),
    classification TEXT,
    requires_attention BOOLEAN DEFAULT FALSE,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

CREATE OR REPLACE PROCEDURE process_customer_orders(
    p_customer_id VARCHAR(50),
    p_start_date TIMESTAMP,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS $$
DECLARE 
    v_order RECORD;
    v_payment NUMERIC(12, 2);
    v_review_score NUMERIC(4, 2);
    v_classification TEXT;

    v_total_orders BIGINT:=0;
    v_total_spent NUMERIC(12, 2):=0;
    v_high_value_orders BIGINT:=0;
    v_problem_orders BIGINT:=0;

BEGIN 
    -- DELETE previous report rows
    DELETE FROM customer_order_report
    WHERE customer_id = p_customer_id 

    -- loop customer's orders for the specified period
    FOR v_order IN 
        SELECT
            customer_id,
            order_status,
            order_purchase_timestamp
        FROM orders
        WHERE customer_id = p_customer_id AND 
        order_purchase_timestamp BETWEEN p_start_date AND p_end_date

        