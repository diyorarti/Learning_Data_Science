"""
RANK() 
    assigns rank to rows
    same values get the same rank,
Example
| price | rank |
| ----- | ---- |
| 100   | 1    |
| 100   | 1    |
| 90    | 3    |
| 80    | 4    |
Skip numbers after ties
USED when position matters:
    competition ranking
    leaderboard with gaps
"""
SELECT 
    order_id,
    RANK() OVER(ORDER BY price DESC) AS rank,
    price
FROM order_items


"""
DENSE_RANK()
    same with RANK(), but no gaps
| price | rank |
| ----- | ---- |
| 100   | 1    |
| 100   | 1    |
| 90    | 2    |
| 80    | 3    |
no gaps
USED when grouping matters:
    top categories
    segmentation
    ranking groups
"""
SELECT 
    order_id,
    DENSE_RANK() OVER(ORDER BY price DESC) AS rank,
    price
FROM order_items

-- RANK() with PARTITION BY 
SELECT 
    product_id,
    price,
    RANK() OVER(
        PARTITION BY product_id
        ORDER BY price DESC
    ) AS rank
FROM order_items

-- DENSE_RANK() with PARTITION BY 
SELECT 
    product_id,
    price,
    DENSE_RANK() OVER(
        PARTITION BY product_id
        ORDER BY price DESC
    ) AS rank
FROM order_items


"""
THE DIFFERENCE RANK, DENSE_RANK, ROW_NUMBER

| price | ROW_NUMBER | RANK | DENSE_RANK |
| ----- | ---------- | ---- | ---------- |
| 100   | 1          | 1    | 1          |
| 100   | 2          | 1    | 1          |
| 90    | 3          | 3    | 2          |
| 80    | 4          | 4    | 3          |

"""

-- Top priced items per product (handling ties)
SELECT *
FROM (
    SELECT 
        product_id,
        DENSE_RANK() OVER(
            PARTITION BY product_id
            ORDER BY price DESC 
        ) AS rank,
        price
    FROM order_items
)
WHERE rank = 1

-- Top 3 products per category
SELECT *
FROM (
    SELECT 
        product_id,
        price,
        RANK() OVER(
            PARTITION BY product_id
            ORDER BY price DESC
        ) AS rnk
    FROM order_items
) t
WHERE rnk <= 3;

