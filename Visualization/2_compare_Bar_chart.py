"""
Bar Chart is used to compare values accorss different categories
    each bar -> one category
    Height of bar -> value

When to use 
    have categorical data
    to compare quantities between groups

Example
| Country | Sales |
| ------- | ----- |
| USA     | 100   |
| UK      | 80    |
| Germany | 90    |


"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

countries = ["USA", "UK", "Germany", "France"]
sales = [100, 80, 90, 70]
# bar chart with Matplotlib
# plt.bar(countries, sales)
# plt.xlabel("Country")
# plt.ylabel("sales")
# plt.show()

# Bar chart with Only Seaborn 
df = pd.DataFrame({
    "country":countries,
    "sales":sales
})
# sns.barplot(df, x='country', y='sales')
# plt.show()

# Bar chart with Matplotliba and Seaborn
# plt.figure(figsize=(8,5))

# sns.barplot(data=df, x="country", y="sales")

# plt.title("Sales Comparison by Country")
# plt.xlabel("Country")
# plt.ylabel("Sales")
# plt.grid(axis="y")

# plt.show()