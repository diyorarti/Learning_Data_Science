"""
Subquery 
    a subqueyr is a query inside another query
"""
SELECT
    order_id,
    price
FROM order_items
WHERE price > (
    SELECT AVG(price)
    FROM order_items
)

-- Types of Subqueries

-- Single row subqueyr
SELECT 
    *
FROM orders
WHERE order_purchase_timestamp = (
    SELECT 
        MAX(order_purchase_timestamp) -- returns one value 
    FROM orders
)

-- Multiple row subqueries
SELECT *
FROM orders 
WHERE order_status IN (
    SELECT DISTINCT order_status -- returns multiple values
    FROM orders
)

-- Correlated subquery -> Subquery depends on outer query
SELECT *
FROM order_items io
WHERE price > (
    SELECT 
        AVG(price)
    FROM order_items
    WHERE product_id = io.product_id
)

-- Subqueries in WHERE 
SELECT *
FROM orders 
WHERE customer_id IN (
    SELECT customer_id
    FROM customers 
    WHERE customer_state = 'RJ'
)

-- Subqueries in SELECT 
SELECT 
    product_id,
    price,
    (SELECT AVG(price) FROM order_items) AS avg_price
FROM order_items;

-- Tasks

-- Get order_items where price is greater than average price
SELECT *
FROM order_items
WHERE price > (
    SELECT AVG(price)
    FROM order_items
)

-- Get orders made by customers from 'SP'
SELECT *
FROM orders 
WHERE customer_id IN (
    SELECT customer_id
    FROM customers 
    WHERE customer_state = 'SP'
)

-- Get products whose price is above average for that product (correlated)
SELECT *
FROM order_items io
WHERE price > (
    SELECT AVG(price)
    FROM order_items
    WHERE product_id = io.product_id 
)

-- Get customers who made more orders than average customer
SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM orders 
GROUP BY customer_id
HAVING COUNT(*) > (
    SELECT 
        AVG(total_orders) AS avg_orders
    FROM (
        SELECT
            COUNT(*) AS total_orders
        FROM orders 
        GROUP BY customer_id 
    )
)
-- Get top 5 sellers by revenue using subquery
