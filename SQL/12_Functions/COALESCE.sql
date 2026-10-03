"""
COALISCE -> returns non-null values from a list 

REAL Use Cases:
    1.replace NUll with default
        COALESCE(phone_number, 'no number')

    2.Aggregation 
        COALESCE(SUM(sales), 0)
    
    3.Multiple fallback values
        COALESCE(email, phone, 'no contact')
        use eamil, if no email, take phone, if both of no, set default
NOTE:
    All values should be the same type
    COALESCE(NULL, 'text', 10) ❌ (type conflict)
    
"""
-- example
SELECT COALESCE(NULL, NULL, 10, 20);