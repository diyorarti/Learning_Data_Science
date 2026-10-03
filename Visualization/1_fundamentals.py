"""
WHY Visualization matters
    Data in raw format is diffcult to undersnt

Understanding Data (EDA Exploratory Data Analysis)
    - detect patterns
    - find outliers
    - check distributions

Communicating insights 
    Non-technical people don't read tables, they see visuals

Decision making
    track KPIs
    compare performance
    predict trends

TYPES of Plotas:

| Goal           | Best Plot              |
| -------------- | ---------------------- |
| Compare        | Bar chart              |
| Trend          | Line chart             |
| Distribution   | Histogram / Boxplot    |
| Relationship   | Scatter plot           |
| Composition    | Pie / Stacked          |
| Correlation    | Heatmap                |
| Ranking        | Sorted bar chart       |
| Multi-variable | Pair plot / Facet grid |


""" 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Comparing plot (Bar chart)
data = {
    "Category": ["Electronics", "Clothing", "Home", "Books", "Sports"],
    "Sales": [15000, 8000, 12000, 5000, 9000]
}
df = pd.DataFrame(data)

# plt.bar(df['Category'], df['Sales'])
# plt.title("Sales By Category")
# plt.xlabel('Category')
# plt.ylabel('Sales')
# plt.show()


# plt.figure(figsize=(8, 5))
# plt.bar(
#     df["Category"],
#     df["Sales"]
# )

# plt.title("Sales Comparison by Category", fontsize=14)
# plt.xlabel("Category")
# plt.ylabel("Sales")

# plt.xticks(rotation=30)

# plt.tight_layout()
# plt.show()

# # adding labels on Bars 
# plt.figure(figsize=(8, 5))
# bars = plt.bar(df['Category'], df['Sales'])
# for bar in bars:
#     height = bar.get_height()
#     plt.text(
#         bar.get_x() + bar.get_width()/2,
#         height,
#         str(height),
#         ha='center',
#         va='bottom'
#     )
# plt.title('Sales comparision by Category')
# plt.xlabel("Category")
# plt.ylabel("Sales")
# plt.show()

# Trend (Line Chart)
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [1000, 1500, 1300, 1800, 2200, 2600]
}

df = pd.DataFrame(data)

# plt.figure(figsize=(8, 6))
# # plt.plot for line chart
# plt.plot(
#     df['Month'],
#     df['Revenue'],
#     marker='o' # show data points 
# )
# plt.title("Monthly Revenue Trend", fontsize=14)
# plt.xlabel("Month")
# plt.ylabel("Revenue")
# plt.grid()  # VERY IMPORTANT for readability

# plt.tight_layout()
# plt.show()

"""
The difference Matplotlib and Seaborn
Matplotlib -> funcdation (low level) -> raw tools
Seaborn -> built on top of Matplotlib (high-level) -> smart tools with automation

Main difference is Level of control :
    Matplotlib:
        Everything can be controlled manually
    
    Seaborn:
        Handles many things automatically

Visual Apperance:
    Matplotlib:
        Basic look by default 
        Needs styling
    
    Seaborn:
        Beautiful out-of-the-box
        Better color paletters & themes

Data Handling:
    Matplotlib:
        works mainly with:
            lists
            arrays

    Seaborn:
        works directly with DataFrame

Statistical Featues 
    Matplotlin:
        No built-in statistics
    
    Seaborn:
        Regression lines
        Distributions
        Confidence intervals

Complexity and Simplicity:
| Feature        | Matplotlib | Seaborn |
| -------------- | ---------- | ------- |
| Learning curve | Medium     | Easy    |
| Code length    | Long       | Short   |
| Flexibility    | Very high  | High    |
| Speed of use   | Slower     | Faster  |

WHEN to use which:
    Matplotlib:
        Custom dashboards
        Fine control (exact colors, layout)
        Complex plots
        PRoduction systems
    
    Seaborn:
        Data Analysis (EDA)
        Quick Insights
        Statistical Visualizations
        Interviews / presentations

TO use Both together
    Matplotlib -> customize and control the plot -> Editing & Polishing the picture 
    Searbonr -> create the plot (smart & fast)  -> Drawing the picture

WHY to use together 
| Problem                             | Solution                 |
| ----------------------------------- | ------------------------ |
| Seaborn is easy but limited control | Use Matplotlib to adjust |
| Matplotlib is powerful but verbose  | Use Seaborn to simplify  |
| You want both beauty + control      | Combine both             |

Seaborn internally uses Matplotlib. 

WHICH does what:
    Matplotlib:
        Titles
        Labels
        Figure size
        Layout
        Fine Control
    
    Seaborn:
        Plot type (scatter, bar, heatmap ...)
        Data mapping (DataFrame -> axes)
        Colors & Styles
        Statistical features

Avdantages of Seaborn

Colors & Styles
| Feature        | Code                |
| -------------- | ------------------- |
| Style          | `sns.set_style()`   |
| Palette        | `sns.set_palette()` |
| Color grouping | `hue=`              |

Statistical Featues
| Feature             | Function         |
| ------------------- | ---------------- |
| Regression          | `sns.regplot()`  |
| Confidence interval | `ci=`            |
| Distribution        | `sns.histplot()` |
| Summary stats       | `sns.boxplot()`  |


"""

# Stles 
# sns.set_style("dark")
# sns.scatterplot(x=[1,2,3,4], y=[10, 20, 30, 40])
# plt.show()

# # Color palettes
# sns.set_palette("dark")
# sns.scatterplot(x=[1,2,3,4], y=[10,20,25,30])
# plt.show()

# color for categories
df = pd.DataFrame({
    "x": [1,2,3,4,5,6],
    "y": [10,20,15,25,30,35],
    "group": ["A","A","B","B","A","B"]
})

# sns.scatterplot(data=df, x="x", y="y", hue="group")
# plt.show()

# Statistical Features 
# regression line
# sns.regplot(data=df, x="x", y="y")
# sns.scatterplot(data=df, x="x", y="y", hue="group")
# plt.show()

# Confidence Interval
# sns.regplot(df, x='x', y='y', ci=95)
# plt.show()

# distribution (kde)
# sns.histplot(df['y'], kde=True)
# plt.show()

# Box plot
# sns.boxplot(data=df, x="group", y="y")
# plt.show()