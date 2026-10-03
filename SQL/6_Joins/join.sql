"""
CROSS JOIN (CARTESIAN JOIN)
    Every row from table A is combinded with every row from B
"""
-- SELECT 
--     c.customer_id, 
--     s.seller_id
-- FROM customers c
-- CROSS JOIN sellers s

"""
SELF JOIN 
    self join is when table is joined with itself, joining the same table using different aliases
"""
-- Find customers who live in the same state
SELECT
    c1.customer_id,
    c2.customer_id,
    c1.customer_city AS city
FROM customers c1
JOIN customers c2 
  ON c1.customer_city = c2.customer_city
 AND c1.customer_id <> c2.customer_id

-- Find customers who have the same zip code 
SELECT 
    c1.customer_id
    c2.customer_id
    c1.cusomer_zip_code_prefix
FROM customers c1
JOIN customers c2
  ON c1.cusomer_zip_code_prefix = c2.cusomer_zip_code_prefix
 AND c1.customer_id <> c2.customer_id

-- Find customers who have the same customer_unique_id
SELECT
    c1.customer_id
    c2.customer_id
    c1.customer_unique_id
FROM customers c1
JOIN customers c2
  ON c1.customer_unique_id = c2.customer_unique_id
 AND c1.customer_id <> c2.customer_id

