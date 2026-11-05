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
        /      \
        YES      NO
        ↓        ↓
        COMMIT   ROLLBACK
"""

