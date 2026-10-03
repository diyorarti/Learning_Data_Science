"""
1. Checking Missing Values:
                        df.isnull()
                        df.isna()
                        counting with sum() df.isnull().sum()
                        percentage of missing values df.isnull().mean() * 100

2. Droppoing Missing Values:
                        df.dropna():
                            axis=1-> droping columns
                            how='all' dropping if all values are missing
                            subset=['column name'] drop rows based on a specific column
3. Filling missing values:
                        df['column_name'].fillna('value') with mean|mode|median|
                            method='ffill'|'bfill'

4.Replacing speficifc missing-values
                        df.replace(['values'], 'with value')
df.isnull()
df.isnull().sum()
df.dropna()
df.fillna()
df.replace()
df.ffill()
"""

import pandas as pd
import numpy as np

data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": ["Ali", "Vali", np.nan, "Sara", "John", "Marta", np.nan, "Tom", "Anna", "Sami"],
    "age": [20, 21, np.nan, 22, 23, np.nan, 20, 21, 24, np.nan],
    "gender": ["Male", "Male", "Male", np.nan, "Male", "Female", "Female", np.nan, "Female", "Male"],
    "study_hours": [5, np.nan, 6, 7, np.nan, 8, 4, 5, np.nan, 6],
    "exam_score": [80, 85, np.nan, 90, 70, np.nan, 60, 75, 95, np.nan],
    "city": ["Tashkent", "Samarkand", "Tashkent", np.nan, "Bukhara", "Tashkent", np.nan, "Samarkand", "Bukhara", "Tashkent"]
}

df = pd.DataFrame(data)

# number of missing values by each column
missing_by_column = df.isna().sum()

# total missing values in df
total_missings = df.isnull().sum().sum()

# Percentage of missing values each column Approach 1
percentage_by_columns = df.isnull().sum()/len(df)*100

# Percentage of missing values each column Approach 2
percentage_by_columns_mean = df.isnull().mean()*100

# filling missing values in 'name' column with 'Unknown' value
df['name'] = df['name'].fillna('Unknown')

# FIlling missing values in 'age' column with median age
median_age = df['age'].median()
df['age'] = df['age'].fillna(median_age)

# filling missing values in 'gender' column with .mode() value (most frequent value)
mode_gender = df['gender'].mode()[0]
df['gender'] = df["gender"].fillna(mode_gender)

# Filling missing values in 'study_hours' column with mean/Average 
mean_study_hours = df['study_hours'].mean()
df['study_hours'] = df['study_hours'].fillna(mean_study_hours)

#fillling missing values in 'exam_score' column with Median
median_exam_score = df['exam_score'].median()
df['exam_score'] = df['exam_score'].fillna(median_exam_score)

# Filling mising values in 'city' column with most frequent city
mode_city = df['city'].mode()[0]
df["city"] = df['city'].fillna(mode_city)

# checking again after clearning
missing_values_by_column = df.isnull().sum()

# Creating a new column named 'performance' that contains values "High"-exam_score >= 85, "Medium"-exam_score >= 70 and "Low"-exam_score < 70
def assign_performance(score):
    if score >= 85:
        return "High"
    elif score >= 70:
        return "Medium"
    else:
        return "Low"

df['performance'] = df['exam_score'].apply(assign_performance)
print(df)