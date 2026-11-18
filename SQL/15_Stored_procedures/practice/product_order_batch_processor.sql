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
    v_current_request RECORD; -- is a RECORD 
    v_current_product TEXT;

    v_stock_stock INTEGER;
    v_product_price NUMERIC(10, 2);

    v_requested_quantity INTEGER;
    v_remaining_quantity INTEGER;
    v_current_chunk INTEGER;

    v_total_order_value NUMERIC(10, 2);

    v_batch_failed BOOLEAN: FALSE;
    v_failure_reason TEXT;


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

