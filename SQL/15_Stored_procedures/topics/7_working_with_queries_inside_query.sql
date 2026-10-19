-- SELECT inside a procedure
"""
General pattern
"
SELECT 
    expression 
    INTO
    Variables
FROM table
WHERE condition;
"
Position of selecting columns must match with variables
"""

-- INSERT inside a procedure
"""
WE can insert rows directly
"
CREATE TABLE procedure_logs(
    log_id BIGSERIAL PRIMARY KEY,
    message1 TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"
Then a procedure
"
CREATE OR REPLACE PROCEDURE add_log(
    p_message TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO procedure_logs(message)
    VALUES (p_message);
END;
$$;
"
"""


-- UPDATE inside aa procedure
"""
suppose we want to update order status
"
CREATE OR REPLACE PROCEDURE change_order_status(
    p_order_id VARCHAR(50),
    p_new_status TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE orders
    SET order_status = p_new_status
    WHERE order_id = p_order_id;
END;
$$;
"
"""


-- DELETE inside a procedure
"""
a procedure can also delete rows

"
CREATE OR REPLACE PROCEDURE delete_log(
    p_log_id BIGINT
)
LANGUAGE plpgsql
AS $$
BEGIN

    DELETE FROM procedure_logs
    WHERE log_id = p_log_id;

END;
$$;
"
"""


-- Combining multiple SQL statements
"""
this is one of the main purposes of a stored procedure.
Suppose one business operation requires:
    1. Read information
    2. Update something
    3. Insert a log
    4. Maybe delete ngsomething
A procedure can perform all of them in sequence
"""