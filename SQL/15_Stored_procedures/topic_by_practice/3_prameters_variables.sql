-- Problem - 1
"""
create a PostgreSQL stored procedure called 'customer_purchase_summary'
This procedure should receive one parameter: customer_id and calculate the information about that customer's orders
Requirements:
    input parameter: p_customer_id VARCHAR(50)
    Variables:
        v_order_count  = total number of orders placed by the customer
        v_total_payment = total amount the customer paid
        v_last_order_date = date/time of the customers' most recent order
""";
CREATE OR REPLACE PROCEDURE customer_purchase_summary(
    p_customer_id VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
DECLARE 
    v_order_count INTEGER;
    v_total_payment BIGINT;
    v_last_order_date TIMESTAMP;

BEGIN
    SELECT 
        COUNT(o.order_id),
        SUM(p.payment_value), 
        MAX(o.order_purchase_timestamp)

        INTO 

        v_order_count,
        v_total_payment,
        v_last_order_date

    FROM orders o 
    INNER JOIN order_payments p ON o.order_id = p.order_id
    WHERE o.customer_id = p_customer_id;

    RAISE NOTICE 'total number of orders of the customer: %', v_order_count;
    RAISE NOTICE 'total paid amount of the customer: %', v_total_payment;
    RAISE NOTICE 'the last order data of the customer: %', v_last_order_date;
END;
$$;

CALL customer_purchase_summary('9ef432eb6251297304e76186b10a928d')


-- Problem-2
"""
Seller sales summary
    create a procedure called 'seller_sales_summary'
    the procedure should analyze one seller during a specified data range.

    Parameters that procedure should receive:
        p_seller_id
        p_start_date
        p_end_date

    Variables that procedure should has:
        v_order_count -> number of distinct orders handled by the seller
        v_items_sold -> number of items sold
        v_total_sales -> sum of item prices
        v_average_price -> average item price
        v_last_order_date -> seller's latest order within the specified period
""";

CREATE OR REPLACE PROCEDURE seller_sales_summary(
    p_seller_id VARCHAR(50),
    p_start_date TIMESTAMP,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS
$$
DECLARE 
    v_order_count  BIGINT;
    v_items_sold BIGINT;
    v_total_sales NUMERIC(12, 2);
    v_average_price NUMERIC(12, 2);
    v_last_order_date TIMESTAMP;

BEGIN 
    SELECT 
        COUNT(DISTINCT o.order_id),
        COUNT(*),
        SUM(i.price),
        AVG(i.price),
        MAX(o.order_purchase_timestamp)

        INTO 

        v_order_count,
        v_items_sold,
        v_total_sales,
        v_average_price,
        v_last_order_date

    FROM order_items i
    JOIN orders o ON i.order_id = o.order_id
    WHERE o.order_purchase_timestamp > p_start_date 
     AND o.order_purchase_timestamp < p_end_date 
     AND i.seller_id = p_seller_id 
     AND i.seller_id = p_seller_id;

    RAISE NOTICE 'total orders: %', v_order_count;
    RAISE NOTICE 'total sold orders: %', v_items_sold;
    RAISE NOTICE 'Total sales: %', v_total_sales;
    RAISE NOTICE 'average price: %', v_average_price;
    RAISE NOTICE 'last order date: %', v_last_order_date;

END;
$$;

CALL seller_sales_summary(
    '48436dade18ac8b2bce089ec2a041202',
    '2017-12-12',
    '2018-12-12'
)


-- Problem-3
"""
Create a procedure called: product_category_sales_summary
    it should analyze one product category during a specified date range.

    the procedure should receive these parameters:
        p_category_name - TEXT
        p_start_date - TIMESTAMP
        p_end_date - TIMESTAMP

    the procedure should have these variables
        v_order_count - number of distinct orders containing this category
        v_items_sold - Total number of item rows sold
        v_product_count - Number of distict products sold
        v_seller_count - number of distinct sellers who sold the category
        v_total_sales - total value of price
        v_average_price - average item price
    
""";
CREATE OR REPLACE PROCEDURE product_category_sales_summary(
    p_category_name TEXT,
    p_start_date TIMESTAMP,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS 
$$
DECLARE 
    v_order_count BIGINT;
    v_items_sold BIGINT;
    v_product_count BIGINT;
    v_seller_count BIGINT;
    v_total_sales NUMERIC(10, 2);
    v_average_price NUMERIC(10, 2);

BEGIN
    SELECT 
        COUNT(DISTINCT o.order_id),
        COUNT(*),
        COUNT(DISTINCT p.product_id),
        COUNT(DISTINCT oi.seller_id),
        SUM(oi.price),
        AVG(oi.price)

        INTO 

        v_order_count,
        v_items_sold,
        v_product_count,
        v_seller_count,
        v_total_sales,
        v_average_price

    FROM products p 
    JOIN order_items oi ON p.product_id = oi.product_id
    JOIN orders o ON oi.order_id = o.order_id
    WHERE p.product_category_name = p_category_name
      AND o.order_purchase_timestamp > p_start_date 
      AND o.order_purchase_timestamp < p_end_date;

    RAISE NOTICE 'Number of distinct orders containing this category %', v_order_count;
    RAISE NOTICE 'Total number of item rows sold %', v_items_sold;
    RAISE NOTICE 'Number of distinct products sold %', v_product_count;
    RAISE NOTICE 'Number of distinct sellers who sold the category %', v_seller_count;
    RAISE NOTICE 'Total value of price %', v_total_sales;
    RAISE NOTICE 'Average item price %', v_average_price;

END;
$$;
CALL product_category_sales_summary(
    'perfumaria',
    '2017-12-12',
    '2020-12-12'
)

