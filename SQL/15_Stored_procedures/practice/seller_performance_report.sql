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
        

"""