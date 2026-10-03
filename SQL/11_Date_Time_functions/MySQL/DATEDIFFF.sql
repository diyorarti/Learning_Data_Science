"""
campaign table:
    upsell_campaign_id: integer	
    date_start: timestamp	
    date_end: timestamp
"""

SELECT 
    AVG(DATEDIFF(date_end, date_start)) AS average_duration
FROM campaign