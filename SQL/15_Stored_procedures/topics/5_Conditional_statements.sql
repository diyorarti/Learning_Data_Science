-- Conditional statemnt IF ... ELSE ...
"""
Conditional Statements:
    Conditional Statements adds decision-making to Procedure
""";

CREATE OR REPLACE PROCEDURE seller_performance_summary1(
    p_seller_id VARCHAR(50),
    p_start_date TIMESTAMP,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS
$$

DECLARE 
    v_order_count BIGINT;
    v_items_sold BIGINT;
    v_total_sales NUMERIC(12, 2);
    v_average_price NUMERIC(12, 2);

BEGIN
    SELECT

        COUNT(DISTINCT o.order_id),
        COUNT(*),
        COALESCE(SUM(oi.price), 0),
        COALESCE(AVG(oi.price), 0)

        INTO 

        v_order_count,
        v_items_sold,
        v_total_sales,
        v_average_price

    FROM orders_items oi 
    JOIN orders o 
      ON oi.order_id = o.order_id
    WHERE oi.seller_id = p_seller_id
      AND o.order_purchase_timestamp >= p_start_date
      AND o.order_pruchase_timestamp < p_end_date
      AND o.order_status = 'delivered';

    RAISE NOTICE 'Total orders: %', v_order_count;
    RAISE NOTICE 'Total items sold: %', v_items_sold;
    RAISE NOTICE 'Total Sales: %', v_total_sales;
    RAISE NOTICE 'Average item price: %', v_averag_price;

    IF v_order_count = 0 THEN
        RAISE NOTICE 'Seller performance: No sales';
    ELSIF v_total_sales >= 100000 THEN 
        RAISE NOTICE 'Seller performance: High';
    ELSIF v_total_sales >= 50000 THEN 
        RAISE NOTICE 'Seller performance: Medium';
    ELSE
        RAISE NOTICE 'Seller performance: Low';

    END IF;
END;
$$;

CALL seller_performance_summary(
    '48436dade18ac8b2bce089ec2a041202',
    '2017-01-01',
    '2018-01-01'
);