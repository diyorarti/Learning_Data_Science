"""
Create a stored procedure: customer_value_summary
    it should analyze one customer during a specific period.

Parameters:
    p_customer_id VARCHAR(50)
    p_start_date TIMESTAMP
    p_end_date TIMESTAMP

Variables:
    v_order_count BIGINT -> number of distinct orders
    v_total_payment NUMERIC(12, 2) -> Total amount paid
    v_last_order_date TIMESTAMP -> Most recent order date
    v_customer_level TEXT -> customer classification
"""

CREATE OR REPLACE PROCEDURE customer_value_summary(
    p_customer_id VARCHAR(50),
    p_start_date TIMESTAMP,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS $$
DECLARE 
    v_order_count BIGINT;
    v_total_payment NUMERIC(12, 2);
    v_last_order_date TIMESTAMP;
    v_customer_level TEXT;

BEGIN 
    SELECT
    FROM orders o 


SELECT *
FROM orders