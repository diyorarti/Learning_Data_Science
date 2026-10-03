-- Creating a stored procedure Basic Synatx
CREATE OR REPLACE PROCEDURE procedure_name() -- this tells PostgreSQl: create a stored procedure with this name. Why "OR REPLACE" If the procedure already exists and you want to change its code, PostgreSQL can replace its definition.
LANGUAGE plpgsql -- What language the procedure body uses. plpgsql menas Procedural Language/PostgreSQL
AS $$ -- procedure body starting
BEGIN 
    -- SQL / procedural statements
END;
$$; -- procedure body ending


-- Sample
CREATE OR  REPLACE PROCEDURE welcome_message()
LANGUAGE plpgsql
AS $$
BEGIN 
    RAISE NOTICE 'Welcome to Stored Procedure!';
END;
$$;


-- calling
CALL welcome_message();

