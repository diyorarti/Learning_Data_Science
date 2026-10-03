"""
CTEs(Common table expression)
    A CTE is a temporary result set that defines using WITH 

Syntax:

    WITH cte_name AS (
        SELECT ...
    )
    SELECT *
    FROM cte_name;

Why use CTEs?
    Readability:
        instead of writing nested queries
    Reusability:
        use same result miultiple times in the same query
    Debugging:
        easier to test and debug individual parts of a query
"""

-- Find high-priced itmes without CTEs, using subquery
SELECT *
FROM (
    SELECT *
    FROM order_items
    WHERE price > 100
) t;

-- Find high-priced items with CTEs
WITH high_price AS (
    SELECT *
    FROM order_items
    WHERE price > 100
)
SELECT *
FROM high_price;

-- REAL USE CASES 
-- Revenue per seller → filter high performers
WITH seller_revenue AS (
    SELECT 
        seller_id,
        SUM(price) AS revenue
    FROM order_items
    GROUP BY seller_id
)
SELECT *
FROM seller_revenue
WHERE revenue > 10000;

-- Top 3 items per product (with ROW_NUMBER)
WITH ranked_items AS (
    SELECT 
        product_id,
        price,
        ROW_NUMBER() OVER(
            PARTITION BY product_id
            ORDER BY price DESC
        ) AS rn
    FROM order_items
)
SELECT *
FROM ranked_items
WHERE rn <= 3;

-- Customer total spending
WITH customer_spending AS (
    SELECT 
        o.customer_id,
        SUM(oi.price) AS total_spent
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY o.customer_id
)
SELECT *
FROM customer_spending
ORDER BY total_spent DESC;


-- MULTIPLE CTEs
WITH 
customer_orders AS (
    SELECT customer_id, COUNT(*) AS total_orders
    FROM orders
    GROUP BY customer_id
),
customer_spending AS (
    SELECT o.customer_id, SUM(oi.price) AS total_spent
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY o.customer_id
)
SELECT 
    co.customer_id,
    co.total_orders,
    cs.total_spent
FROM customer_orders co
JOIN customer_spending cs
ON co.customer_id = cs.customer_id;
