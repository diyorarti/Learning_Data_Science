"""
LEAD() / LAG()
    THey are heavily used in time-series analysis, customer behavior, finance etc.
    They allow to access another row's value without JOIN 

LAG() -> look BACK (previous row)
LEAD() -> look FORWARD (next row)

BASIC SYNTAX:
LAG(column) OVER (ORDER BY column)
LEAD(column) OVER (ORDER BY column)
"""

-- show previous order date
SELECT
    order_id,
    order_purchase_timestamp,
    LAG(order_purchase_timestamp) OVER(
        ORDER BY order_purchase_timestamp
    ) AS prev_order_date
FROM orders

-- show next order date
SELECT
    order_id,
    order_purchase_timestamp,
    LEAD(order_purchase_timestamp) OVER(
        ORDER BY order_purchase_timestamp
    ) AS next_order_date
FROM orders

-- Time difference between rows
SELECT
    order_id,
    order_purchase_timestamp,
    order_purchase_timestamp - LAG(order_purchase_timestamp) OVER(
        ORDER BY order_purchase_timestamp 
    ) AS time_diff
FROM orders

-- LAG()/LEAD() with PARTITION BY, analyze per customer
SELECT 
    customer_id,
    order_id,
    order_purchase_timestamp,
    LAG(order_purchase_timestamp) OVER(
        PARTITION BY customer_id
        ORDER BY order_purchase_timestamp
    ) AS prev_order
FROM orders;


-- REAL USE CASES
-- 1. Customer behavior: time between purchases
SELECT 
    customer_id,
    order_id,
    order_purchase_timestamp,
    order_purchase_timestamp -
    LAG(order_purchase_timestamp) OVER(
        PARTITION BY customer_id
        ORDER BY order_purchase_timestamp
    ) AS gap_between_orders
FROM orders;

-- Detect price changes
SELECT 
    product_id,
    price,
    price - LEAD(price) OVER(
        PARTITION BY product_id
        ORDER BY price
    ) AS price_diff
FROM order_items io