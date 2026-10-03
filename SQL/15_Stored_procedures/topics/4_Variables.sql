-- Variables
"""
A variable is a temprorary named storage location used while a procedure is running
example:
    v_total_orders = 99441
    v_customer_name = 'John'
    v_total_payment = 125.50

    Parameter = value coming into or going out of a procedure
    Variable = temorary value used internally inside the procedure
"
CREATE OR REPLACE PROCEDURE procedure_name()
LANGUAGE plpgsql
AS $$
DECLARE
    -- variables here
BEGIN
    -- executable statements here
END;
$$;
" 
""";

-- Declaring a variable
"""
basic syntax:
    variable_name data_type;
    example:
        "
        DECLARE 
            v_total_orders INTEGER
        "
    v_ is used for the prefic
    := menas assignment in PL/pgsql

    instead of: 
        "DECLARE
            v_number INTEGER;
        BEGIN
            v_number := 10;
        "
    WE can do:
        "
        DECLARE
            v_number INTEGER := 10;
        ";
    
    "RAISE NOTICE" with variables

    "SELECT ... INTO"
    THis is one of the most important concepts in variable
    example:
    "
        SELECT COUNT(*)
        INTO v_total_order
        FROM orders;
    "
    databse example
    "
    CREATE OR REPLACE PROCEDURE show_total_orders()
    LANGUAGE plpgsql
    AS $$
    DECLARE
        v_total_orders BIGINT;
    BEGIN
        SELECT COUNT(*)
        INTO v_total_orders
        FROM orders;
        
        RAISE NOTICE 'total number of orders: %', v_total_orders;
    END;
    $$;
    "
    Calling
    "CALL show_total_orders()"

    Variable data types:
    "
    DECLARE
        v_count INTEGER;
        v_total BIGINT;
        v_price NUMERIC(10,2);
        v_name TEXT;
        v_id VARCHAR(50);
        v_date DATE;
        v_time TIMESTAMP;
        v_active BOOLEAN;
    "
""";

CREATE OR REPLACE PROCEDURE variable_example()
LANGUAGE plpgsql
AS $$
DECLARE
    v_number INTEGER;
BEGIN 
    v_number := 10;
    RAISE NOTICE 'The number is %', v_number;
END;
$$;
CALL variable_example()


