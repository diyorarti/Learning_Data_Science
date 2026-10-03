-- Overview
"""
What is Stored prodedure ?
    A stored procedure is a group of SQL statements that is saved inside the databse and can be executed whenever we need it.
    Think of it like a function in Python, but stored inside the databse
""";

-- creating
CREATE OR REPLACE PROCEDURE  change_order_status( -- this creates producure "OR REPLACE" allows us to modify leter the producure
    p_order_id VARCHAR(50), -- parameter: which order ?
    p_new_status TEXT -- parameter: what new status ?
)
LANGUAGE plpgsql -- the procedure body is written using PostgreSQL's procedural langauge, PL/pgSQL
AS $$  -- marking the beginning of procedure body
BEGIN 
    UPDATE orders --  updating table  
    SET order_status = p_new_status -- updating order status
    WHERE order_id = p_order_id; -- selecting order by order id
END;
$$; -- marking the end of procedure body


-- Testing we have order_id "d3c8851a6651eeff2f73b0e011ac45d0" with "preprocessing" status
CALL change_order_status(
    'd3c8851a6651eeff2f73b0e011ac45d0',
    'shipped'
);

-- checking the change
SELECT
    order_id,
    order_status
FROM orders
WHERE order_id = 'd3c8851a6651eeff2f73b0e011ac45d0';

-- Advatages
"""
1.Reusability
    it allows to perform the same operation many times

2. Combine multiple operations
    Procedure
        ├── SELECT
        ├── INSERT
        ├── UPDATE
        ├── DELETE
        ├── IF
        ├── LOOP
        └── transaction logic

3. Business logic inside the databse
    IF customer has enough balance
        make payments
    ELSE
        reject payment
""";

-- Disadvantages
"""
1. Database-specific syntax 
    Stored procedures differ among PostgreSQL, MySQL, Oracle
2. Hard to maintain 
    Suppose:
        an application has Python code, JavaScript code and SQL stored procedure
        Developers must understand both application code and database procedure code.
3. Hard to debug

""";


