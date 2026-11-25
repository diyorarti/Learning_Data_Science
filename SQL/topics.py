# Topics

"""============================================================
 SQL ROADMAP FOR DATA SCIENTIST
 ============================================================
 1. SQL Fundamentals
 ------------------------------------------------------------
    SELECT
    FROM
    WHERE
    DISTINCT
    ORDER BY
    LIMIT
    Aliases
    Arithmetic expressions
    Comparison operators
    AND / OR / NOT
    IN
    BETWEEN
    LIKE


 2. NULL Handling
 ------------------------------------------------------------
 IS NULL
 IS NOT NULL
 COALESCE()
 NULLIF()
 Understanding NULL in comparisons
 Understanding NULL in aggregations


 3. Aggregations
 ------------------------------------------------------------
 COUNT()
 SUM()
 AVG()
 MIN()
 MAX()
 COUNT(DISTINCT ...)
 GROUP BY
 HAVING
 Grouping by multiple columns


 4. JOINs
 ------------------------------------------------------------
 INNER JOIN
 LEFT JOIN
 RIGHT JOIN
 FULL OUTER JOIN
 SELF JOIN
 Multiple-table JOINs

 Understand:
 One-to-one relationships
 One-to-many relationships
 Many-to-many relationships
 Duplicate rows caused by JOINs


 5. Conditional Logic
 ------------------------------------------------------------
 CASE WHEN
 Multiple WHEN conditions
 CASE inside SELECT
 Conditional aggregation

 Example concepts:
 SUM(CASE WHEN ... THEN ... END)
 COUNT(CASE WHEN ... THEN ... END)
 Creating flags and categories


 6. Subqueries
 ------------------------------------------------------------
 Scalar subqueries
 Subqueries in WHERE
 Subqueries in FROM
 Subqueries in SELECT
 Correlated subqueries
 EXISTS
 NOT EXISTS
 IN / NOT IN


 7. Common Table Expressions (CTEs)
 ------------------------------------------------------------
 WITH ... AS (...)
 Multiple CTEs
 Chained CTEs
 Using CTEs to simplify complex queries

 Lower priority:
 Recursive CTEs


 8. Window Functions
 ------------------------------------------------------------
 VERY IMPORTANT FOR DATA SCIENCE

 ROW_NUMBER()
 RANK()
 DENSE_RANK()
 LAG()
 LEAD()

 Aggregate window functions:
 SUM() OVER()
 AVG() OVER()
 COUNT() OVER()

 Concepts:
 PARTITION BY
 ORDER BY inside OVER()
 Window frames
 Running totals
 Rolling averages
 Ranking within groups


 9. Date and Time Functions
 ------------------------------------------------------------
 DATE
 TIMESTAMP
 EXTRACT()
 DATE_TRUNC()
 INTERVAL
 Date differences
 Adding/subtracting dates
 Grouping by day/week/month/year
 Customer recency calculations


 10. String Functions
 ------------------------------------------------------------
 LOWER()
 UPPER()
 TRIM()
 REPLACE()
 SUBSTRING()
 LENGTH()
 CONCAT()
 Pattern matching
 Basic regular expressions


 11. Set Operations
 ------------------------------------------------------------
 UNION
 UNION ALL
 INTERSECT
 EXCEPT


 12. Data Cleaning with SQL
 ------------------------------------------------------------
 Finding duplicates
 Removing duplicates
 Handling missing values
 Standardizing categories
 Detecting invalid values
 CAST()
 Data type conversion
 Cleaning strings
 Cleaning dates

 Important technique:
 ROW_NUMBER() for deduplication


 13. Analytical SQL Patterns
 ------------------------------------------------------------
 VERY IMPORTANT FOR DATA SCIENCE

 Top N per group
 First event per customer
 Last event per customer
 Month-over-month growth
 Year-over-year growth
 Running totals
 Rolling averages
 Customer Lifetime Value (CLV)
 Customer retention
 Cohort analysis
 Conversion funnels
 Conversion rates
 Repeat purchases
 Churn indicators
 Event/session analysis


 14. Experimentation and Statistical SQL
 ------------------------------------------------------------
 IMPORTANT FOR STATISTICAL DATA SCIENCE

 Control vs treatment groups
 Sample sizes
 Means
 Proportions
 Variance
 Conversion rates
 Group differences
 Pre/post metrics
 Experiment metric preparation

 Typical workflow:
 SQL -> prepare experiment data
 Python -> hypothesis tests / confidence intervals / statistics


 15. Feature Engineering with SQL
 ------------------------------------------------------------
 VERY IMPORTANT FOR MACHINE LEARNING

 Examples:
 orders_last_30_days
 orders_last_90_days
 total_spent
 average_order_value
 days_since_last_purchase
 purchase_frequency
 customer_tenure
 complaint_count
 cancellation_count
 average_review_score
 rolling statistics
 ratios
 binary behavioral flags

 Typical workflow:
 Database
 -> SQL feature table
 -> Python / Pandas
 -> Machine Learning model


 16. Views and Temporary Tables
 ------------------------------------------------------------
 CREATE VIEW
 Temporary tables
 Intermediate result tables
 CTE vs temporary table
 When to use each


 17. Database Design Basics
 ------------------------------------------------------------
 Primary Keys
 Foreign Keys
 UNIQUE constraints
 Relationships between tables
 One-to-one
 One-to-many
 Many-to-many
 Normalization basics

 Data warehouse basics:
 Fact tables
 Dimension tables
 Star schema


 18. Query Performance Basics
 ------------------------------------------------------------
 Index concepts
    Avoid unnecessary SELECT *
    Filtering efficiently
    Avoid Cartesian products
    Efficient JOINs
    Basic EXPLAIN
    Understanding expensive aggregations
    Basic query optimization


 19. Data Modification
 ------------------------------------------------------------
    INSERT
    UPDATE
    DELETE


 20. Transactions
 ------------------------------------------------------------
 Basic knowledge is enough for Data Science

    BEGIN
    COMMIT
    ROLLBACK
    Transaction concept
    Atomicity
    Multiple changes as one operation


 21. Stored Procedures
 ------------------------------------------------------------
 Basic to intermediate knowledge is enough

    Stored Procedure Overview
        CREATE PROCEDURE
        Parameters
        Variables
        Conditional Statements

    Loops:
        LOOP
        WHILE
        FOR
        EXIT
        CONTINUE

    Queries inside procedures:
        SELECT
        INSERT
        UPDATE
        DELETE

    Transaction control:
        COMMIT
        ROLLBACK

    Error handling:
        EXCEPTION
        RAISE NOTICE
        RAISE WARNING
        RAISE EXCEPTION

    Understand:
    Procedure vs Function
    CALL vs SELECT

    Do NOT need deep expertise for Data Science


 22. Functions
 ------------------------------------------------------------
 CREATE FUNCTION
 Parameters
 Return values
 RETURNS
 RETURN
 RETURN QUERY
 Functions vs Procedures


 23. Error and Exception Handling
 ------------------------------------------------------------
    Basic knowledge is enough

    EXCEPTION
    WHEN
    RAISE NOTICE
    RAISE WARNING
    RAISE EXCEPTION


 24. Security and Permissions Basics
 ------------------------------------------------------------
    Basic awareness is enough

    Database users
    Roles
    GRANT
    REVOKE
    EXECUTE permission
    Read permissions
    Write permissions


 25. JSON / Arrays / Semi-Structured Data
 ------------------------------------------------------------
    Learn after mastering relational SQL

    JSON basics
    JSONB basics in PostgreSQL
    Extracting JSON fields
    Filtering JSON data
    Arrays
    UNNEST()


 26. Cloud / Data Warehouse SQL
 ------------------------------------------------------------
    Learn later

    Examples:
    BigQuery
    Snowflake
    Amazon Redshift
    Databricks SQL

    Main analytical SQL concepts remain similar.


 ============================================================
 PRIORITY FOR DATA SCIENTIST
 ============================================================

 MUST BE STRONG
 ------------------------------------------------------------
    SQL Fundamentals
    NULL handling
    Aggregations
    JOINs
    CASE WHEN
    Subqueries
    CTEs
    Window Functions
    Date/Time functions
    Data Cleaning
    Analytical SQL
    Experimentation SQL
    Feature Engineering


 SHOULD KNOW WELL
 ------------------------------------------------------------
 String functions
 Set operations
 Views
 Temporary tables
 Database relationships
 Query performance basics


 BASIC KNOWLEDGE IS ENOUGH
 ------------------------------------------------------------
 INSERT / UPDATE / DELETE
 Transactions
 Stored Procedures
 Functions
 Exception Handling
 Permissions


 LOW PRIORITY FOR DATA SCIENTIST
 ------------------------------------------------------------
 Complex triggers
 Advanced stored procedures
 Advanced database administration
 Replication
 Sharding
 Backup/recovery administration
 Deep index engineering
 Database server administration
 
"""