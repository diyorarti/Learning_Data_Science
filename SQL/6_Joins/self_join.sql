"""
SELF JOIN 
    treating one table as it it were two different tables, using alieases

Basic syntax:
    SELECT
        a.column,
        b.column
    FROM table_name a
    JOIN table_name b
      ON a.column_name = b.column_name 



Simple Example

| id | first_name | salary | manager_id |
| -- | ---------- | ------ | ---------- |
| 1  | John       | 5000   | NULL       |
| 2  | Alice      | 4000   | NULL       |
| 3  | Bob        | 6000   | 1          |
| 3  | Ali        | 6000   | 2          |
| 3  | Vali       | 6000   | 2          |

"""
-- LEFT JOIN (left self join)  Find employees and their manager names.
SELECT 
    e.first_name AS employee,
    m.first_name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id 
"""
employees e -> employee table
employees m -> manager table (same table but treated as manager table)
LOGIC:
    e.manager_id = m.od
    So output -> employee -> their manager
"""

-- INNER JOIN (inner self join ) only employees who have managers
SELECT 
    e.first_name AS employee,
    m.first_name AS manager
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id

-- RIGHT JOIN (right self join ) Employee vs Manager salary comparison, employees earning more than their managers
SELECT 
    e.first_name,
    e.salary,
    m.salary AS manager_salary
FROM employees e
JOIN employees m
ON e.manager_id = m.id
WHERE e.salary > m.salary;


