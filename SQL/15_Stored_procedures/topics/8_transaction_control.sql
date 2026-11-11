-- TRANSACTION CONTROL 
"""
Transaction Control as a safety mechanism for several related databse changes
A transaction is a group of SQL statements that should be treated as one unit. In PostgeSQL, we either keep all the changes with "COMMIT"
or discard with "ROLLBACK".
    Example:
        a bank transfer:
            Ali has 1000
            Bob has 500
            Ali sends 200 to Bob
        Databse changes are required:
            1. Ali: 1000 → 800
            2. Bob: 500 → 700
        if both succed:
            Ali -200 ✓
            Bob +200 ✓
                ↓
            COMMIT → keep all changes made in the current transaction
        if something is wrong:
            Ali -200 ✓
            Bob +200 ✗
                ↓
            ROLLBACK → cancel all changes made in the current transaction

the Core Idea:
TRANSACTION:
        Statement 1
        Statement 2
        Statement 3
            ↓
            valid?
           /    \
        YES      NO
        ↓        ↓
        COMMIT   ROLLBACK
"""

-- Practice Problem
"""
Create a stored procedure called: transfer_money:
    The procedure must do:
        first, get the sender's current balance and store it in a varible
        then check whether:
            p_amount > 0 AND sender has enough money

        Case-1 Valid transfer:
                Ali = 1000
                Bob = 500
                Transfer request 200
            Perform:
                1.substract 200 from ALi
                2.add 200 to Bob
                3.COMMIT
            Result:
                Ali:800
                Bob:700
            Print:
                Transfer successful
        
        Case-2 Insufficient balance:
                Ali = 1000
                Bob = 500
                Transfer request = 1500 
            Peform:
                this transfer must not happen
                ROLLBACK
            Result:
                Ali = 1000
                Bob = 500
            Print:
                Transfer failed: insufficient balance
            
        Case-3 Invalid amount:
                Ali = 1000
                Bob = 500
                Transfer request <= 0
            Peform:
                this is invalid transfer request
                ROLLBACK
            Print:
                Transfer failed: invalid amount
                
        Table:
        CREATE TABLE accounts (
            account_id INTEGER PRIMARY KEY,
            owner_name TEXT,
            balance NUMERIC(12,2)
        );
        test data 
        INSERT INTO accounts
        VALUES
            (1, 'Ali', 1000.00),
            (2, 'Bob', 500.00);
"""