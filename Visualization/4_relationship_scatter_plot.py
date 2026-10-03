"""
Relationship Plots:
    1.Scatter plot:
        two numerical variales 
        checking correlation
        example: age and income
    
    2. Line plot:
        trends over time
        Continuous progression
        example: date and sales
    
    3. Regression plot 
        seeing the overall direction 
        understanding linear relationship
        example: ad spend and sales with trend line 
    
    4. Bubble plot
        3 variables at once
        example: GDP vs life expectancy , bubble size = population 
    
    5. Heatmap of correlation 
        many numerical columns
        example: correlation among salary, age, experience, score
    
    6. Pair plot 
        Quick EDA
        exploring multiple numerical columns at once 

Summary Table:
| Plot type           | Best for                      | Variables            |
| ------------------- | ----------------------------- | -------------------- |
| Scatter plot        | direct relationship           | 2 numerical          |
| Line plot           | trend / ordered relationship  | 2, usually with time |
| Regression plot     | relationship + fitted line    | 2 numerical          |
| Bubble plot         | 3-variable relationship       | 2 numerical + size   |
| Correlation heatmap | many relationships at once    | many numerical       |
| Pair plot           | multiple variable exploration | many numerical       |
    


"""
import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# custom data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
exam_score = [45, 50, 55, 60, 65, 72, 78, 85]

# # scatter plot with only Maptlotlib
# plt.scatter(hours_studied, exam_score)
# plt.title("Study hours vs Exam Score correlation")
# plt.xlabel("Hours")
# plt.ylabel("Scores")
# plt.show()

df = pd.DataFrame({
    "hours_studied":hours_studied,
    "exam_score":exam_score
})

# # scatter plot with onyl Seaborn
# sns.scatterplot(df, x='hours_studied', y='exam_score')
# plt.show()

# scatter plot wiht Seaborn and Matplotlib 
# plt. constrils figure size
plt.figure(figsize=(8, 5))
# sns. creates the plot 
sns.scatterplot(df, x='hours_studied', y='exam_score')
# plt. customizes the plot 
plt.xlabel("Hours")
plt.ylabel("scores")
plt.title("Scatter plto with Searborn and Matplotlib")
plt.grid(True)
plt.show()