-- =========================================================
-- 1. PRACTICE TABLES
-- =========================================================

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


-- =========================================================
-- 2. SAMPLE PRODUCTS
-- =========================================================

INSERT INTO products_inventory
VALUES
    (1, 'Laptop', 10, 2500.00),
    (2, 'Mouse', 50, 80.00),
    (3, 'Keyboard', 20, 150.00);


-- =========================================================
-- 3. STORED PROCEDURE
-- =========================================================

CREATE OR REPLACE PROCEDURE process_order_batch(
    p_batch_id INTEGER,
    p_chunk_size INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE

    -- Stores one current order request
    v_current_request RECORD;

    -- Used by the final FOR loop
    v_current_product RECORD;


    -- Current product information
    v_product_stock INTEGER;
    v_product_price NUMERIC(10,2);


    -- WHILE-loop variables
    v_remaining_quantity INTEGER;
    v_current_chunk INTEGER;


    -- Current order value
    v_total_order_value NUMERIC(12,2);


    -- Transaction-control variables
    v_batch_failed BOOLEAN := FALSE;
    v_failure_reason TEXT;

BEGIN

    -- =====================================================
    -- STEP 1: Validate chunk size
    -- =====================================================

    IF p_chunk_size IS NULL OR p_chunk_size <= 0 THEN

        v_batch_failed := TRUE;
        v_failure_reason := 'Chunk size must be greater than 0';

    END IF;


    -- =====================================================
    -- Only process the batch when initial validation passes
    -- =====================================================

    IF v_batch_failed = FALSE THEN


        -- =================================================
        -- STEP 2: Delete previous report for this batch
        -- =================================================

        DELETE FROM order_processing_report
        WHERE batch_id = p_batch_id;


        -- =================================================
        -- STEP 3: BASIC LOOP
        -- Process one pending request at a time
        -- =================================================

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
            ORDER BY request_id
            LIMIT 1;


            -- If no pending request exists, stop the loop
            EXIT WHEN NOT FOUND;


            -- =================================================
            -- STEP 4: Non-critical validation
            -- Invalid quantity → skip request
            -- =================================================

            IF v_current_request.quantity <= 0 THEN

                UPDATE order_requests
                SET status = 'skipped'
                WHERE request_id =
                    v_current_request.request_id;


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


                -- Immediately start next LOOP iteration
                CONTINUE;

            END IF;


            -- =================================================
            -- STEP 5: Get product information
            -- =================================================

            SELECT
                stock_quantity,
                price
            INTO
                v_product_stock,
                v_product_price
            FROM products_inventory
            WHERE product_id =
                v_current_request.product_id;


            -- =================================================
            -- STEP 6: Critical validation
            -- Product does not exist
            -- =================================================

            IF NOT FOUND THEN

                v_batch_failed := TRUE;

                v_failure_reason :=
                    'Product does not exist';

                EXIT;

            END IF;


            -- =================================================
            -- STEP 7: Critical validation
            -- Insufficient stock
            -- =================================================

            IF v_current_request.quantity >
               v_product_stock THEN

                v_batch_failed := TRUE;

                v_failure_reason :=
                    'Insufficient stock';

                EXIT;

            END IF;


            -- =================================================
            -- STEP 8: Calculate total order value
            -- =================================================

            v_total_order_value :=
                v_current_request.quantity *
                v_product_price;


            -- =================================================
            -- STEP 9: Prepare WHILE loop
            -- =================================================

            v_remaining_quantity :=
                v_current_request.quantity;


            -- =================================================
            -- STEP 10: WHILE LOOP
            -- Reduce inventory in chunks
            -- =================================================

            WHILE v_remaining_quantity > 0 LOOP


                -- Determine the current chunk
                IF v_remaining_quantity >= p_chunk_size THEN

                    v_current_chunk := p_chunk_size;

                ELSE

                    v_current_chunk :=
                        v_remaining_quantity;

                END IF;


                -- Deduct current chunk from stock
                UPDATE products_inventory
                SET stock_quantity =
                    stock_quantity - v_current_chunk
                WHERE product_id =
                    v_current_request.product_id;


                -- Reduce remaining quantity
                v_remaining_quantity :=
                    v_remaining_quantity -
                    v_current_chunk;


            END LOOP;


            -- =================================================
            -- STEP 11: Mark request as processed
            -- =================================================

            UPDATE order_requests
            SET status = 'processed'
            WHERE request_id =
                v_current_request.request_id;


            -- =================================================
            -- STEP 12: Insert processing report
            -- =================================================

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
                'Processed'
            );


        END LOOP;

    END IF;


    -- =====================================================
    -- STEP 13: TRANSACTION CONTROL
    -- Important: this happens AFTER the whole batch loop
    -- =====================================================

    IF v_batch_failed = TRUE THEN

        -- Cancel ALL changes made during this transaction
        ROLLBACK;

        RAISE NOTICE
            'Batch % rolled back.',
            p_batch_id;

        RAISE NOTICE
            'Reason: %',
            v_failure_reason;


    ELSE

        -- Save ALL changes made during this transaction
        COMMIT;

        RAISE NOTICE
            'Batch % processed successfully.',
            p_batch_id;

    END IF;


    -- =====================================================
    -- STEP 14: FOR LOOP
    -- Display final inventory
    -- =====================================================

    FOR v_current_product IN

        SELECT
            product_id,
            product_name,
            stock_quantity,
            price
        FROM products_inventory
        ORDER BY product_id

    LOOP

        RAISE NOTICE
            'Product ID: %, Name: %, Stock: %, Price: %',
            v_current_product.product_id,
            v_current_product.product_name,
            v_current_product.stock_quantity,
            v_current_product.price;

    END LOOP;


END;
$$;

CALL process_order_batch(
    101,
    2
);

SELECT *
FROM products_inventory;

SELECT *
FROM order_requests
WHERE batch_id = 101;

SELECT *
FROM order_processing_report
WHERE batch_id = 101;