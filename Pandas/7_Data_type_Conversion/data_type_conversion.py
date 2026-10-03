"""
"25"          # string
25            # integer
25.5          # float
"2024-01-01"  # string date

.dype/.dtypes

.astype()
.to_data_time
.to_numeric()
"""

import pandas as pd

data = {
    "student_id": [101, 102, 103, 104, 105, 106],
    "name": ["Ali", "Vali", "Sara", "John", "Marta", "Tom"],
    "age": ["20", "21", "unknown", "23", "22", "twenty"],
    "score": ["85.5", "90", "78.5", "error", "88", "75"],
    "passed": ["True", "True", "False", "True", "False", "True"],
    "registration_date": [
        "2024-01-10",
        "2024-02-15",
        "wrong_date",
        "2024-03-20",
        "2024-04-05",
        "2024-05-12"
    ],
    "city": ["Tashkent", "Samarkand", "Tashkent", "Bukhara", "Tashkent", "Samarkand"]
}

df = pd.DataFrame(data)

print(df.dtypes)

# converting student_id from int to string 
df['student_id'] = df['student_id'].astype(str)

# converting age from string to numeric
df['age'] = pd.to_numeric(df['age'])
