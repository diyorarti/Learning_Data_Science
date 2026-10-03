"""
Wildcards are special symbols used with the LIKE operator to search for patterns in text columns 

    | Wildcard | Meaning                                  | Example    |
    |   %      | Any number of characters, including zero | 'iPhone%'  |
    |   _      | Exactly one character                    | 'iPhone _' |

% wildcard
    start with: 
        WHERE interface LIKE 'iPhone%'
    Ends with:
        WHERE name LIKE '%bek'
    Contains:
        WHERE name LIKE '%or%'

_ wildcard
    exactly one character 
        WHERE name LIKE 'A_i'

| Pattern     | Meaning                    |
| 'A%'      | starts with A              |
| '%A'      | ends with A                |
| '%A%'     | contains A                 |
| 'A_'      | A + exactly one character  |
| 'A__'     | A + exactly two characters |
| '_a%'     | second character is `a`    |
| '%phone%' | contains `phone`           |

"""
-- Write your query here
SELECT 
    interface,
    SUM(CASE 
            WHEN is_successful_post = TRUE THEN 1
            ELSE 0
        END ) AS post_success,
    COUNT(*) AS post_attempt, 
    ROUND(SUM(CASE WHEN is_successful_post = TRUE THEN 1 ELSE 0
        END)* 100.0 / COUNT(*), 2) AS post_success_rate 
FROM post
WHERE interface LIKE 'Iphone%'
GROUP BY interface
ORDER BY post_success_rate DESC 