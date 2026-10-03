# Functinal VS Imperative programming

"""
Functional Programming Concepts
    Writing code using functions that transforms data without changin it or relying on hidden state
    Rules:
        1. Immutability 
        2. No side effect (pure functions)
        3. Building programms by combining functions
"""

# Functional programming
nums = [1, 2, 3, 4, 5]
res_functional = list(
    map(lambda x: x**2, 
        filter(lambda x: x > 2, nums) 
    )
)

# Imperative version 
res_imperative = []
for i in nums:
    if i > 2:
        res_imperative.append(i**2)

# Functional Programming in Data Analysis/Science 
"""
In Data work 
    raw data -> clean -> transform -> analyze -> result
"""

import pandas as pd

df = pd.read_csv("data.csv") # imperative programming

def clean(df): # functional programming
    return df.dropna()

def filter_adults(df): # functional programming
    return df[df["age"] > 18]

def add_feature(df): # functional programming 
    return df.assign(score=lambda x: x.points * 2)

df = add_feature(filter_adults(clean(df))) # imperative programming