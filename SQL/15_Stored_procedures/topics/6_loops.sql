"""
Loop:
    EXIT
    WHILE 
    FOR 
    CONTINUE
    Loops with variables
    loops with conditions
    looping through query results
"""

-- basic LOOP
"""
The basic PostgreSQL PL/pgSQL syntax
"
LOOP 
    statements;
END  LOOP;
"
this is an infinite loop unless we tell PostgreSQL when to stp.
"
LOOP
    RAISE NOTICE "Hello !";
END LOOP;
"
this would keep running continuously. 
"""


-- LOOP with EXIT
"""
"
CREATE OR REPLACE PROCEDURE loop_example()
LANGUAGE plpgsql
AS $$ 
DECLARE 
    v_number INTEGER := 1;
BEGIN 
    LOOP
        RAISE NOTICE 'Number: %', v_number;
        v_number := v_number + 1
        EXIT WHEN v_number > 5;
    END LOOP;
END;
$$;
"
this loop stops when number > 5
"""


-- WHILE loop
"""
WHILE loop repeats while a condition is true.
Syntax
"
WHILE condition LOOP
    statement;
END LOOP;
"
example
"
CREATE OR REPLACE PROCEDURE while_example()
LANGUAGE plpgsql
AS $$
DECLARE
    v_number INTEGER := 1;
BEGIN

    WHILE v_number <= 5 LOOP

        RAISE NOTICE 'Number: %', v_number;

        v_number := v_number + 1;

    END LOOP;

END;
$$;
"
"""

-- Difference between LOOP and WHILE
"""
Basic LOOP: Use LOOP when you want more flexibility.
"
LOOP
    ...
    EXIT WHEN condition;
END LOOP;
"

WHILE loop: Use WHILE when the stopping condition is simple and clear.
"
WHILE condition LOOP
    ...
END LOOP;
"
"""


-- FOR loop
"""
FOR loop is very useful when we know the range in advance.
"
CREATE OR REPLACE PROCEDURE for_example()
LANGUAGE plpgsql
AS $$
DECLARE
    v_number INTEGER;
BEGIN

    FOR v_number IN 1..5 LOOP

        RAISE NOTICE 'Number: %', v_number;

    END LOOP;

END;
$$;
"
output: 
1
2
3
4
5
"""


-- REVERSE with FOR loop
"""
"
FOR v_number IN REVERSE 5..1 LOOP

    RAISE NOTICE 'Number: %', v_number;

END LOOP;
"
ouput:
5
4
3
2
1
"""


-- CONTINUE 
"""
CONTINUE skips the rest of the current iteration and moves to the next one.
"
FOR v_number IN 1..5 LOOP

    IF v_number = 3 THEN
        CONTINUE;
    END IF;

    RAISE NOTICE 'Number: %', v_number;

END LOOP;
"
output:
1
2
4
5
"""


-- CONTINUE WHEN
"""
we can also write 
"
CONTINUE WHEN v_number = 3;
"
instead of 
"
IF v_number = 3 THEN
    CONTINUE;
END IF;
"
"""

