"""
👉 Task 1:
Get all products where:
    weight between 500 and 2000
    photos more than 2
"""
SELECT *
FROM products
WHERE product_weight_g BETWEEN 500 and 2000
  AND product_photos_qty > 2

"""
👉 Task 2:
Get unique states where customers live
"""
SELECT DISTINCT customer_state
FROM customers

"""
👉 Task 3:
Get top 5 most expensive order items
"""

SELECT *
FROM order_items
ORDER BY price DESC
LIMIT 5