"""
Sorting And Filtering

this section includes:
    1.ORDER BY (DESC, ASC)
    2.filtering with multiple conditions
    3.pattern matching with LiKE
    4. wildcards % and _
"""

-- ORDER BY (ASC / DESC)
"""
ORDER BY used to sort results 
    numerically
    alphabetically
    date/time
"""
-- aphabetically
SELECT 
    customer_id,
    customer_city
FROM customers
ORDER BY customer_city -- default value ASC

-- numerically
SELECT 
    order_id,
    payment_value
FROM order_payments
ORDER BY payment_value DESC

-- date/time
SELECT 
    order_id,
    order_estimated_delivery_date
FROM orders
WHERE order_status = 'delivered'
ORDER BY order_estimated_delivery_date ASC


-- FILTERING 
"""
WHERE is the key word used to filter with
    OR 
    AND 
    NOT

"""

-- Pattern matching with LIKE
"""
LIKE is used to search text patterns
"""
SELECT 
    product_id, 
    product_category_name
FROM products
WHERE product_category_name LIKE 'automotivo';

-- WILDCARDS 
"""
WILDCARDS 
    wildcards are special symbols used with LIKE
        % - any number of characters
        _ - exactly one character 
"""
-- % wildcard
SELECT 
    customer_id,
    customer_city
FROM customers
WHERE customer_city LIKE

SELECT 
    payment_type
FROM order_payments
WHERE payment_type LIKE "%credit%"

-- _ wildcard
SELECT DISTINCT customer_state
FROM customers
WHERE customer_state LIKE '_P';

SELECT DISTINCT customer_city
FROM customers
WHERE customer_city LIKE 'ri_';

-- Tasks
"""
Task 1

Get all customers from state SP, sorted by city A to Z.
"""
SELECT * 
FROM customers
WHERE customer_state LIKE 'SP'

"""
Task 2

Get all order items where:
    price > 100
    freight_value < 30

Sort by price from highest to lowest.
"""
SELECT *
FROM order_items
WHERE price > 100 
  AND freight_value < 30
ORDER BY price DESC

"""
Task 3

Get all cities from customers that start with rio.
"""
SELECT *
FROM customers
WHERE customer_city LIKE 'rio%'

"""
Task 4

Get all sellers whose city contains the word paulo.
"""
SELECT * 
FROM sellers
WHERE seller_city LIKE '%paulo%'

"""
Task 5

Get all orders where:
    status is delivered or shipped
    purchase date is after 2018-01-01

Sort by newest purchase date first.
"""
SELECT *
FROM orders
WHERE order_status = 'delivered'
  AND order_purchase_timestamp > '2018-01-01'