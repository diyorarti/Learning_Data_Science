"""
Aggregate Functions
Aggregate functions that summarize multiple rows into one value

| Function  | Purpose                 | Example       |
| --------- | ----------------------- | ------------- |
| `COUNT()` | Counts rows or values   | `COUNT(*)`    |
| `SUM()`   | Adds numeric values     | `SUM(salary)` |
| `AVG()`   | Calculates the average  | `AVG(salary)` |
| `MIN()`   | Finds the minimum value | `MIN(salary)` |
| `MAX()`   | Finds the maximum value | `MAX(salary)` |
"""

-- COUNT() -> counts the number of rows in a group
SELECT
    COUNT(*) AS total_delivered_orders
FROM orders
WHERE order_status = 'delivered'

-- SUM() -> sums the values in a group
SELECT
    product_id,
    SUM(price) AS total_revenue
FROM order_items
GROUP BY product_id
ORDER BY total_revenue DESC



