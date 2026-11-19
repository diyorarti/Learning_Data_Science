-- creating practice tables
CREATE TABLE products_inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    stock_quantity INTEGER,
    price NUMERIC(10,2)
);

CREATE TABLE order_requests (
    request_id BIGSERIAL PRIMARY KEY,
    batch_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    status TEXT DEFAULT 'pending'
);

-- some products
INSERT INTO products_inventory
VALUES
    (1, 'Laptop', 10, 2500.00),
    (2, 'Mouse', 50, 80.00),
    (3, 'Keyboard', 20, 150.00);



-- report table
CREATE TABLE order_processing_report (
    report_id BIGSERIAL PRIMARY KEY,
    batch_id INTEGER,
    request_id BIGINT,
    product_id INTEGER,
    quantity INTEGER,
    total_value NUMERIC(12,2),
    result TEXT,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE OR REPLACE PROCEDURE process_order_batch(
    p_batch_id INTEGER,
    p_chunk_size INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_current_request RECORD; -- Stores the information about the current order retrieved from order_requests
    v_current_product RECORD; -- Stores the current product's information when you use a FOR loop at the end of the procedure

    v_stock_stock INTEGER; -- stores the available stock of the requested product before processing
    v_product_price NUMERIC(10, 2); -- stores the price of a single product 

    v_requested_quantity INTEGER; -- stores how many units the customer wants to buy
    v_remaining_quantity INTEGER; -- track how many units still need to be deducted from ivertory
    v_current_chunk INTEGER; -- stores the number of units deducted during the current WHILE interation

    v_total_order_value NUMERIC(10, 2); -- stores the total monetary value of the order

    v_batch_failed BOOLEAN: FALSE; -- tracks whether a critical error occured during batch processing
    v_failure_reason TEXT; -- Stores the reason why batch processing failed


BEGIN
    -- before processing the batch, delete the previous report for the batch
    DELETE FROM order_processing_report
    WHERE batch_id = p_batch_id

    LOOP 
        SELECT 
            request_id,
            product_id,
            quantity
        INTO 
            v_current_request
        FROM order_requests
        WHERE batch_id = p_batch
          AND status = 'pending'
        LIMIT 1;

    END LOOP;

