"""
ROW_NUMBER()
    assigns an unique number to each row
        starts from 1
        no duplicates
        always unique
"""
-- Basic Syntax
ROW_NUMBER() OVER(ORDER BY column)

-- giving ranking of order items by price, no duplicates, all unique ranking even for the same prices
SELECT
    order_id,
    price,
    ROW_NUMBER() OVER(ORDER BY price DESC) AS ranking_price
FROM order_items


-- PARTITION BY reset number per group , 
-- ranking items inside each product
SELECT 
    order_id,
    price,
    ROW_NUMBER() OVER(
        PARTITION BY order_id 
        ORDER BY price DESC) AS ranking
FROM order_items
ORDER BY ranking 

-- Get top 1 most expensive item per product 
SELECT * 
FROM (
    SELECT 
        product_id,
        price,
        ROW_NUMBER() OVER(
            PARTITION BY product_id
            ORDER BY price DESC
        ) AS rank 
    FROM order_items 
) t
WHERE rank = 1

-- Get top 3 items per prudct 
SELECT *
FROM (
    SELECT
        product_id,
        price, 
        ROW_NUMBER() OVER(
            PARTITION BY product_id
            ORDER BY price DESC
        ) AS rn
    FROM order_items
) t 
WHERE rn <= 3

-- Remove duplicates
SELECT
    *
FROM (
    SELECT
        order_id,
        customer_id,
        ROW_NUMBER() OVER(
            PARTITION BY order_id
            ORDER BY order_purchase_timestamp
        ) AS rn
    FROM orders
)
WHERE rn = 1;

-- latest order per customer 
SELECT
    *
FROM (
    SELECT
        order_id,
        customer_id,
        order_purchase_timestamp,
        ROW_NUMBER() OVER(
            PARTITION BY customer_id
            ORDER BY order_purchase_timestamp DESC
        ) AS rank
    FROM orders
)
WHERE rank=1

-- Assign row number to all order_items based on price (highest first)
SELECT 
    order_id,
    product_id,
    ROW_NUMBER() OVER(
        PARTITION BY order_item_id 
        ORDER BY price DESC 
    ) AS rank,
    price
FROM order_items

-- Get top 2 most expensive items per product
SELECT *
FROM (
    SELECT
        order_id,
        order_item_id,
        ROW_NUMBER() OVER(
            PARTITION BY product_id
            ORDER BY price DESC
        ) AS rank,
        price
    FROM order_items
) t
WHERE rank BETWEEN 1 AND 2

-- Get latest order per customer
SELECT *
FROM (
    SELECT
        order_id,
        ROW_NUMBER() OVER(
            PARTITION BY customer_id
            ORDER BY order_purchase_timestamp DESC
        ) AS rank
    FROM orders
) t 
WHERE rank = 1

