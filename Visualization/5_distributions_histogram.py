import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
"""
Distribution -> how values are spread 
Distributions helps to understand:
    data shape
    central tendency (mean, median)
    spread (variance)
    outliers
    skewness

1.Histogram
    splits data into bins
    shows frequency
"""
df = pd.read_csv("https://github.com/anvarnarz/praktikum_datasets/blob/main/uybor_scrapping.csv?raw=true")

# Histogram with Matplotlib
# plt.hist(df['price'], bins=20)
# plt.show()

# Histogram with Seaborn 
# sns.histplot(df['price'], bins=20)
# plt.show()
