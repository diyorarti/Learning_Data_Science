"""
1. checking duplicates    -> df.duplicated() retursn True/False 
2. show duplicate rows    -> df.[df.duplicated()]
3. count duplicate rows   -> df.duplicated().sum()
4. Remove duplicate rows  -> df.drop_duplicates()
5. check duplicates based on column -> df.duplicated(subset=['column_name'])
6. keep first/last, or remove all duplicates by keep parameters 
                                                            df.drop_duplicates(keep='first')
                                                            df.drop_duplicates(keep='last')
                                                            df.drop_duplicates(keep=False)
                                                            df.drop_duplicates(keep=True)
df.duplicated()
df[df.duplicated()]
df.duplicated().sum()
df.drop_duplicates()
df.drop_duplicates(subset=["column_name"])
df.drop_duplicates(keep="first")
df.drop_duplicates(keep="last")
df.drop_duplicates(keep=False)
"""
import pandas as pd

data = {
    "student_id": [101, 101, 103, 102, 104, 105, 106, 106, 107, 108, 109, 109],
    "name": ["Ali", "Vali", "Sara", "Vali", "John", "Marta", "Tom", "Tom", "Anna", "Sami", "Bob", "Bob"],
    "subject": ["Math", "English", "Math", "English", "Science", "Math", "Science", "Science", "English", "Math", "Math", "Math"],
    "score": [85, 78, 90, 78, 70, 88, 75, 75, 95, 60, 82, 82],
    "city": ["Tashkent", "Samarkand", "Tashkent", "Samarkand", "Bukhara", "Tashkent", "Andijan", "Andijan", "Bukhara", "Samarkand", "Tashkent", "Tashkent"]
}

df = pd.DataFrame(data)
print(df)
print("------------------------------")
# checking duplicated rows count in data
num_duplicaed_rows = df.duplicated().sum()
#print(num_duplicaed_rows)

# extrcting duplicated rows
duplicated_rows = df[df.duplicated()]

# romeving duplicated rows
no_duplicated_df = df.drop_duplicates()

# duplicates based on 'student_id' column
student_id_duplicated_rows = df[df.duplicated(subset='student_id')]

# showing all the rows where student_id is duplicated
all_student_id_duplicated_rows = df[df.duplicated(subset='student_id', keep=False)]

# removing duplicats based on student_ids, keeping only first occurrence
df_unique_student_first = df.drop_duplicates(keep='firstt')

# removing duplicats based on student_ids, keeping only last occurrence
df_unique_student_last = df.drop_duplicates(keep='last')
print(df_unique_student_last)