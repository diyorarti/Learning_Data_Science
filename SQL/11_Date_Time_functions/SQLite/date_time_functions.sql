"""
SQLite stores dates/times as TEXT, REAL or INTEGER , not DATE or DATETIME types

| Function      | Purpose                                            |
| ------------- | -------------------------------------------------- |
| `date()`      | Returns date only                                  |
| `time()`      | Returns time only                                  |
| `datetime()`  | Returns date + time                                |
| `julianday()` | Converts date to Julian day number                 |
| `unixepoch()` | Converts date/time to Unix timestamp               |
| `strftime()`  | Formats/extracts parts of date/time                |
| `timediff()`  | Calculates difference between two date/time values |

"""

-- 1. date() -> retunrs only date  
SELECT date('now') -- output: 2026-05-14
-- modifiers can be applied, common modifiers
SELECT date('now', '+1 day');
SELECT date('now', '-7 days');
SELECT date('now', '+1 month');
SELECT date('now', '-1 year');
SELECT datetime('now', '+3 hours');
SELECT date('now', 'start of month');
SELECT date('now', 'start of year');

-- 2. time() -> returns only time 
SELECT time('now') -- output: 08:30:45

-- 3. datetime() returns both date and time 
SELECT datetime('now') -- output: 2026-05-14 08:30:45

-- 4. julianday() -> returns a date/time as Julian day number (instead of 2026-5-15, 2461175.5 days ). Useful for calculating differences
SELECT julianday('2026-05-15') - julianday('2004-08-02') AS difference_days

-- 5. unixepoch() -> returns the number of seconds since 1970-01-01 00:00:00 UTC.
SELECT unixepoch('now');

"""
-- 6. strftime() -> it formats date/time values 
    | Format | Meaning      | Example                |
    | ------ | ------------ | ---------------------- |
    | `%Y`   | Year         | `2026`                 |
    | `%m`   | Month        | `05`                   |
    | `%d`   | Day          | `14`                   |
    | `%H`   | Hour         | `08`                   |
    | `%M`   | Minute       | `30`                   |
    | `%S`   | Second       | `45`                   |
    | `%w`   | Day of week  | `0` Sunday, `1` Monday |
    | `%W`   | Week of year | `00-53`                |

"""
SELECT strftime('%Y', 'now') AS year; -- output: 2026

-- 7. timediff() -> retunrs the difference between two time values
SELECT timediff('2026-05-14 12:00:00', '2026-05-14 10:30:00');