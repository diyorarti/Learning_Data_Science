"""
Create a stored procedure called generate_seller_performance_report
    The procedure should analyze all orders handled by one seller during a spefcified period, 
    classify each order, save each result into a reporting table, and finally print a summary of the seller's performance.

    Part-1 Create a reporting table
        CREATE TABLE seller_performance_report (
            report_id BIGSERIAL PRIMARY KEY,
            seller_id VARCHAR(50),
            order_id VARCHAR(50),
            order_status TEXT,
            item_count BIGINT,
            total_sales NUMERIC(12,2),
            average_item_price NUMERIC(12,2),
            classification TEXT,
            requires_attention BOOLEAN DEFAULT FALSE,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )

    Part-2 Parameters the procedure should accept
        p_seller_id VARCHAR(50)
        p_start_date TIMESTAMP
        p_end_date TIMESTAMP

    Part-3 Variables the procedure should have
        v_order RECORD;
        v_item_count BIGINT;
        v_order_sales NUMERIC(12,2);
        v_average_price NUMERIC(12,2);
        v_classification TEXT;
        v_total_orders BIGINT := 0;
        v_total_items BIGINT := 0;
        v_total_sales NUMERIC(12,2) := 0;
        v_high_value_orders BIGINT := 0;
        v_problem_orders BIGINT := 0;
        v_seller_level TEXT;
    
    Part-4 DELETE 
        before generating a new report, delete the previous report for this seller.

    Part-5  FOR loop + SELECT
        loop through all distinct orders in which the seller sold something during the requested date range.
        
    Part-6 Calculate information for each order
        For the current order and seller, calculate:
            number of ites
            total sales
            average price

    Part-7 Handle NULL
        if v_order_sales is NULL, use conditional statement to set it to: 0

    Part-8 Classify each order
        Rules:
            IF order_status = 'canceled'                   → 'Canceled Order'
            ELSIF order_status != 'delivered'              → 'Incomplete Order'
            ELSIF total_sales >= 500 AND item_count >= 3   → 'Large High-Value Order'
            ELSIF total_sales >= 500                       → 'High-Value Order'
            ELSIF item_count >= 3                          → 'Large Order'
            ELSE                                           → 'Normal Order'
        store in v_classification

    PART-9 INSERT
        For every processed order, insert a row into: seller_performance_report
            seller_id
            order_id
            order_status
            item_count
            total_sales
            average_item_price
            classification

    Part-10 UPDATE
        after inserting the row, set: requires attention = True
        when the classificatio is:
            Canceled Order
            Incomplete Order
        UPDATE must modify only the current seller/current order, not every row in the table.

    Part-11 UPDATE counters
        for every order: v_total_orders + 1
        add the current item's count to: v_total_items
        add the current order sales to: v_total_sales
        if v_order_sales >= 500, increase: v_high_value_orders
        if classification is Canceled Order or Incomplete Order, increase: v_problem_orders

    Part-12 Print each processed order
        inside the loop print:
            Order ID:
                Status:
                Items sold:
                Order sales:
                Average item price:
                Classification:
    Part-13 Classify the seller:
        after END LOOP, classify the entire seller:
            IF total_orders = 0 → 'No Activity'
            ELSIF total_sales >= 10000 AND total_orders >= 20 → 'Top Seller'
            ELSIF total_sales >= 5000 OR total_orders >= 10 → 'Active Seller'
            ELSIF problem_orders >= 3 → 'Needs Attention'
            ELSE → 'Small Seller'
        store this in v_seller_level

    Part-14 Final summary
        print:
            Seller ID:
            Total orders:
            Total items:
            Total sales:
            High-value orders:
            Problem orders:
            Seller level:
"""

-- creating a report table
CREATE TABLE seller_performance_report(
    report_id BIGSERIAL PRIMARY KEY,
    seller_id VARCHAR(50),
    order_id VARCHAR(50),
    order_status TEXT,
    item_count BIGINT,
    total_sales NUMERIC(12,2),
    average_item_price NUMERIC(12,2),
    classification
)

CREATE OR REPLACE PROCEDURE generate_seller_performance_report(
    p_seller_id VARCHAR(50),
    p_start_date TIMESTAMP,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS $$
DECLARE 
    v_order RECORD;

    v_item_count BIGINT;
    v_order_sales NUMERIC;
    v_average_price NUMERIC;
    v_classification TEXT;

    v_total_orders BIGINT := 0;
    v_total_items BIGINT := 0;
    v_total_sales NUMERIC(12, 2) := 0;
    v_high_value_orders BIGINT := 0;
    v_problem_orders BIGINT := 0;

    v_seller_level TEXT;

BEGIN 
    -- DELETE before generating a new reprot for a seller, first delete it's report
    DELETE FROM seller_performance_report
    WHERE seller_id = p_seller_id;

    -- FOR loop + SELECT looping through all distinct orders in which the seller sold something during the requested date range.
    FOR v_order IN 
        SELECT 
            o.order_id
        FROM order_items oi
        JOIN orders o ON oi.order_id = o.order_id
        WHERE oi.seller_id = p_seller_id 
          AND o.order_purchase_timestamp BETWEEN p_start_date AND end_date
    LOOP

        -- Calculating information for each order
        SELECT 
            COUNT(*),
            SUM(pyment_value),
            AVG(payment_value),
        INTO
            v_item_count,
            v_order_sales,
            v_average_price
        FROM order_payment
        WHERE order_id = v_order.order_id;

        -- Handling NULL if v_order_sales is NULL
        IF v_order_sales is NULL THEN 
            v_order_sales := 0;
        END IF;

        -- classifying each order