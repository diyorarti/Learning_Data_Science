"""
Recursive CTEs
    Recursive CTS is a query that calls iteslf repeatedly

Common rules:
    1. the first SELECT and second SELECT must return the same number of columns in the same order.
    
"""

-- generate numbers from 1 to 5
WITH RECURSIVE cte_name AS (
    -- 1. Anchor query
    SELECT ...
    FROM table
    WHERE starting_condition

    UNION ALL

    -- 2. Recursive query
    SELECT ...
    FROM table
    JOIN cte_name
        ON table.id = cte_name.parent_id
    WHERE stopping_condition
)
SELECT *
FROM cte_name;

-- Find all employees under manager 1
WITH RECURSIVE employee_tree AS (

    -- Base: top manager
    SELECT employee_id, manager_id
    FROM employees
    WHERE employee_id = 1

    UNION ALL

    -- Recursive: find subordinates
    SELECT e.employee_id, e.manager_id
    FROM employees e
    JOIN employee_tree et
        ON e.manager_id = et.employee_id

)
SELECT * FROM employee_tree;


d