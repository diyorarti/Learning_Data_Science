"""
A Line plots is mainly used to visualize trends over an ordered variable (usually time)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# custom data
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [20, 22, 25, 23, 26, 28, 30]

# # line plot with only Matplotlib 
# plt.plot(days, temperature)
# plt.title("Line plot with Matplotlib")
# plt.xlabel("Days")
# plt.ylabel("Temperatue")
# plt.grid()
# plt.show()

df = pd.DataFrame({
    "days":days,
    "temperature":temperature
})

# # line plot with seaborn 
# sns.lineplot(df, x='days', y='temperature')
# plt.show()

# Seaborn and Matplotlib together
plt.figure(figsize=(8, 5))
sns.lineplot(df, x='days', y='temperature')
plt.title("Temperature trend over days")
plt.xlabel("days")
plt.ylabel('temperature')
plt.grid()
plt.show()