"""\
🎯 Task
Write a Python script that:

    ✅ 1. Load Data (File Handling + JSON)
        read JSON file
        Convert it into Python data (list of dict)

    ✅ 2. Clean Data (Exception Handling)
        Remove records where: points is None
        Handle missing keys safely (no crashes)

    ✅ 3. Filter Data (Control Flow)
        Keep only: 
            People with age >= 18
            City = "Warsaw"

    ✅ 4. Transform Data (Functions + FP + Comprehensions)
        For each remaining user:
            Add a new field: score = points * 2
            Convert name to uppercase

    ✅ 5. Aggregation (Algorithmic Thinking)
        Compute:
            Total users
            Average score
            Highest score user

    ✅ 6. Use Functions (Code Organization)
        Split your code:
            def load_data(...):
            def clean_data(...):
            def filter_data(...):
            def transform_data(...):
            def analyze_data(...):

    ✅ 7. Use CLI Arguments
        Run like:
            python script.py 
            python customers.json

    ✅ 8. Use Generator (Memory concept)
        Create a generator that yields users one by one instead of storing all at once.

    ✅ 9. Add Error Handling
        File not found
        Invalid JSON

    ✅ 10. Output Results
        print:
            Total users: X
            Average score: X
            Top user: NAME (score)
"""

import json

# 1.loading json
def load_data(path):
    try:
        with open(path) as file:
            data =  json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
        return []

# 2. cleaning data
def clean_data(data):
    cleaned_data = [x for x in data if x.get('points') != None]
    return cleaned_data

# 3. filtering
def filter_data(data):
    adults_in_Warsaw = list(map(
        lambda x: x
        ,filter(
            lambda x: x.get('age') >=18, 
            filter(
                lambda x: x.get('city') == 'Warsaw', data
            )
        )
    ))
    return adults_in_Warsaw

# 4. transforming data 

def transforming_data(data):
    return [
            {
            **x,
            "score":x['points']*2,
            'name':x['name'].upper()
        }
        for x in data
    ]
# 5. Aggregation 
def analyze_data(data):
    total_users = len(data)
    avg_score = sum(user['score'] for user in data) /len(data)
    top_score_user = max(data, key=lambda user:user['score'])
    highest_score = {
        top_score_user['name']:top_score_user['score']
    }


    return {
        "total_users":total_users,
        "average_score":avg_score,
        "highest_score":highest_score
    }

# loading data 
data = load_data('Python/Problems_ChatGPT/files/customers.json')
# cleaning data
cleaned_data = clean_data(data)
# filterinf data 
filtered_data = filter_data(cleaned_data)
# transforming data 
transformed_data = transforming_data(filtered_data)
# Agrregation 
agrregations = analyze_data(transformed_data)
print(agrregations)