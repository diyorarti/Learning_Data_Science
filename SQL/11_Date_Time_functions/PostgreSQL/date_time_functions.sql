"""CURRENT DATE & TIME """
SELECT CURRENT_DATE; -- only date example: 2026-04-20
SELECT CURRENT_TIME; -- only time example: 11:52:32.389035+02
SELECT NOW();        -- both data and time example: 2026-04-20 11:52:32.389035+02 

"""EXRACT"""
SELECT EXTRACT(YEAR FROM order_date) FROM orders -- extracting year
SELECT EXTRACT(MONTH FROM order_date) FROM orders -- extracting month
SELECT EXTRACT(DAY FROM order_date) FROM orders -- extracting day
SELECT EXTRACT(DOW FROM order_date) FROM orders -- extracting DOW(stads for day of week) , 0-> Sunday, 1->Monday ...

""" 
DATE_TRUNC -> used for grouping 

examples:
    input -> 2026-05-04 14:35:20
    Code -> DATE_TRUNC('day', order_approved_at)
    output -> 2026-05-04 00:00:00

    input -> 2026-05-04 14:35:20
    Code -> DATE_TRUNC('month', order_approved_at)
    output -> 2026-05-00 00:00:00

    input -> 2026-05-04 14:35:20
    Code -> DATE_TRUNC('year', order_approved_at)
    output -> 2026-00-00 00:00:00
"""
SELECT DATE_TRUNC('year', order_approved_at) FROM orders -- grouping yearly 
SELECT DATE_TRUNC('month', order_approved_at) FROM orders -- grouping monthly
SELECT DATE_TRUNC('day', order_approved_at) FROM orders -- grouping daily

"""AGE() -> difference between dates """
SELECT AGE(order_estimated_delivery_date, order_approved_at) AS delivery_time FROM orders  -- ouput: 26 years 4 mons 26 days


""" INTERVAL (add/subtract time)"""
SELECT NOW() + INTERVAL '7 days'; -- adding days
SELECT NOW() + INTERVAL '1 year'; -- adding year
SELECT NOW() - INTERVAL '1 year'; -- subtract year
SELECT NOW() - INTERVAL '1 month'; -- subtract month
SELECT NOW() - INTERVAL '11 days'; -- subtract days

""" TO_CHAR() -> format date"""
SELECT TO_CHAR(order_approved_at, 'YYYY-MM-DD') AS year FROM orders -- output: 2026-04-25
SELECT TO_CHAR(order_approved_at, 'MM') AS year FROM orders         -- output:01, 02, ... 12
SELECT TO_CHAR(order_approved_at, 'month') AS year FROM orders      -- output: january, february ...december
SELECT TO_CHAR(order_approved_at, 'DD') AS year FROM orders         -- output: 01, 02, ... 31
SELECT TO_CHAR(order_approved_at, 'day') AS year FROM orders        -- output: monday, teusday, ... sunday


