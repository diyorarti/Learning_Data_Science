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

    v_batch_failed BOOLEAN:= FALSE; -- tracks whether a critical error occured during batch processing
    v_failure_reason TEXT; -- Stores the reason why batch processing failed


BEGIN
    -- before processing the batch, delete the previous report for the batch
    DELETE FROM order_processing_report
    WHERE batch_id = p_batch_id;

    LOOP 
        SELECT 
            request_id,
            product_id,
            quantity
        INTO 
            v_current_request
        FROM order_requests
        WHERE batch_id = p_batch_id
          AND status = 'pending'
        LIMIT 1;

        EXIT WHEN NOT FOUND;

        -- Non-critical validation
        IF v_current_request.quantity <= 0 THEN 
            UPDATE order_requests
            SET status = 'skipped'
            WHERE request_id = v_current_request.request_id;

            INSERT INTO order_processing_report (
                batch_id,
                request_id,
                product_id,
                quantity,
                total_value,
                result
            )
            VALUES (
                p_batch_id,
                v_current_request.request_id,
                v_current_request.product_id,
                v_current_request.quantity,
                0,
                'Skipped - Invalid quantity'
            );
            CONTINUE;
        END IF;

        -- Critical Validation
        SELECT
            stock_quantity,
            price
        INTO 
            v_product_stock,
            v_product_price
        FROM product_inventory
        WHERE product_id = v_current_request.product_id;

        -- Check whether the product exists
        IF NOT FOUND THEN
            v_batch_failed := TRUE;
            v_failure_reason := "Product does not exist";
            EXIT;
        END IF;

        -- Check whether enough stock is available
        IF v_current_request.quantity > v_product_stock THEN 
            v_batch_failed := TRUE;
            v_failure_reason := "Insufficient stock";
            EXIT;
        END IF;

        -- Calculate total order value
        v_total_order_value := v_current_request.quantity * v_product_price;

        -- recude inventory using a WHILE Loop
        v_remaining_quantity := v_current_request.quantity; -- assigning the requested quantity to v_remaining_quantity

        WHILE v_remaining_quantity > 0 LOOP

            -- Determine the current chunk
            IF v_remaining_quantity >= p_chunk_size THEN
                v_current_chunk := p_chunk_size;
            ELSE
                v_current_chunk := v_remaining_quantity;
            END IF;

            -- Update inventory
            UPDATE products_inventory
            SET stock_quantity  = stock_quantity - v_current_chunk
            WHERE product_id = v_current_request.product_id;

            -- Reduce remaining quantity
            v_remaining_quantity := v_remaining_quantity - v_current_chunk

        END LOOP;

        -- Update Order Status and Insert Processing Report
        UPDATE order_requests
        SET status = 'processed'
        WHERE request_id = v_current_request.request_id;

        -- INSERT a processing report
        INSERT INTO order_processing_report (
            batch_id,
            request_id,
            product_id,
            quantity,
            total_value,
            result
        )
        VALUES (
            p_batch_id,
            v_current_request.request_id,
            v_current_request.product_id,
            v_current_request.quantity,
            v_total_order_value,
            "Processed"
        );
        
    END LOOP;


