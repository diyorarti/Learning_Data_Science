"""
UNION in SQL is used to combine rows(vertically) from two or more SELECT queries into one result

STRUCTURE: 
        Query 1 result
        +
        Query 2 result
        =
        One combined result
BASIC SYNTAX:
    SELECT column1, column2
    FROM table1

    UNION

    SELECT column1, column2
    FROM table2;

UNION --> removes Duplicates and keeps matchings
    Example:
        Query 1:
            A
            B
        UNION 
        Query 2:
            B
            C
        OUTPUT:
            A
            B 
            C

UNION ALL --> keeps all rows
    Example:
        Query 1:
            A
            B
        UNION ALL 
        Query 2:
            B
            C
        OUTPUT:
            A
            B 
            B
            C
        


NOTE: the selecting number of columns must be the same 
    example if first query selects two columsn col1, col2, the second must select two columns too.
"""
