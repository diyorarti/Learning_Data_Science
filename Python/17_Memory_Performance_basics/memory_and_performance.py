# Memory and Performance Basic (Python + Data Science)
"""
Memory 
    RAM that program uses while running
    In Python every variable uses memory, bigger data leads more memory
Performance
    how fast that program code runs

"""

# Slow 
# for i in range(len(df)):
#     df["x"][i] = df["x"][i] * 2

# Fast
# df["x"] = df["x"] * 2
"""
In Data Science Avoid loops because loop-> slow, vectorized operations -> fast
"""

# The reason Vectorization operations are fast
"""
Libraries NumPy, Pandas are written in C(very fast)
"""
