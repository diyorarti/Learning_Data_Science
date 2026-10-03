"""
NTILE()
    Divides rows into N equal groups
    Syntax:
        NTILE(N) OVER(ORDER BY column)

"""
-- Divide order_items into 4 groups (quartiles)
SELECT 
    price,
    NTILE(4) OVER(ORDER BY price) AS quartile
FROM order_items;

-- ORDER BY price DESC 
SELECT 
    price,
    NTILE(4) OVER(ORDER BY price DESC) AS quartile
FROM order_items;

-- with PARTITION BY , divide data inside each group 
SELECT 
    product_id,
    price,
    NTILE(4) OVER(
        PARTITION BY product_id
        ORDER BY price
    ) AS quartile
FROM order_items;

-- Customer segmentation: Divide customers into 5 spending groups
SELECT
    customer_id,
    SUM(io.price) AS total_spend,
    NTILE(5) OVER(
        ORDER BY SUM(io.price) DESC
    ) AS spending_group
FROM order_items io 
INNER JOIN orders o ON io.order_id = o.order_id
GROUP BY o.customer_id


