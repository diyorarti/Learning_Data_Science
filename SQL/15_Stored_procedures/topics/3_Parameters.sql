-- Parameters
"""
What is a parameter ?
    A parameter is a value that a procedure receives from outside.
    we don't to create:
        update_order_1()
        update_order_2()
        update_order_3()
        ...
    instead, we do 
        change_order_status(
            p_order_id, 
            p_new_status
        )
    we provided two parameters p_order_id and p_new_status
    So we can call now:
        CALL change_order_status('order_1', 'delivered');
        CALL change_order_status('order_2', 'shipped');
        CALL change_order_status('order_3', 'canceled');
""";
CREATE OR REPLACE PROCEDURE  change_order_status(
    p_order_id VARCHAR(50), -- one parameter
    p_new_status TEXT  -- second parameter
)
LANGUAGE plpgsql 
AS $$  
BEGIN 
    UPDATE orders  
    SET order_status = p_new_status 
    WHERE order_id = p_order_id; 
END;
$$; 


-- IN parameters
"""
IN parameter
the most common tyoe of parameter and In parameter means A value comes into procedure
Example:
    CREATE OR REPLACE PROCEDURE change_order_status(
        IN p_order_id VARCHAR(50),
        IN p_new_status TEXT
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN

        UPDATE orders
        SET order_status = p_new_status
        WHERE order_id = p_order_id;

    END;
    $$;
    
    IN is actually optional because PostgreSQL assumes IN by default. So we can drop the in 
    CREATE OR REPLACE PROCEDURE change_order_status(
        p_order_id VARCHAR(50),
        p_new_status TEXT
    )

    p_ is used for naming conversion. It helps prevent ambiguity.
    For example
        WHERE order_id = order_id;
        here which means table column and which means the parameter
        WHERE order_id = p_order_id;
        here: order_id → table column, p_order_id → procedure parameter
""";

-- OUT parameters
"""
Now direction changes, OUT means the procedure send a value out.
    in the following example, "OUT p_total_orders BIGINT" means the procedure will produce a "BIGINT" value
    The procedure calculates "COUNT(*)" and places into "p_total_orders"
    
    Calling an OUT procedure
    with PostgreSQL procedures, we will commonly cal this by supplying "NULL" for the "OUT" position
""";
CREATE OR REPLACE PROCEDURE get_total_orders(
    OUT p_total_orders BIGINT
)
LANGUAGE plpgsql
AS $$
BEGIN 
    SELECT COUNT(*)
    INTO p_total_orders
    FROM orders;
END;
$$;

CALL get_total_orders(NULL)


-- INOUT parameters
"""
INOUT parameters 
    a value enters the procedure, is modified and comes back out.
    value → Procedure → modified value

""";
CREATE OR REPLACE PROCEDURE double_number(
    INOUT p_number INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    p_number := p_number * 2;
END;
$$;

CALL double_number(10);

 