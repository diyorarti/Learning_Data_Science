import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

data = {
    "student_id": range(1, 26),
    "study_hours": [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 12, 13, 14, 15, 16, 20],
    "exam_score": [42, 48, 52, 55, 55, 42, 63, 66, 68, 70, 72, 75, 77, 80, 82, 85, 85, 90, 91, 93, 94, 96, 97, 55, 100],
    "sleep_hours": [5.0, 5.5, 6.0, 6.0, 6.5, 6.5, 7.0, 7.0, 7.5, 7.5, 8.0, 8.0, 8.0, 7.5, 7.0, 7.0, 6.5, 6.5, 6.0, 6.0, 5.5, 5.5, 5.0, 4.5, 4.0],
    "attendance_rate": [55, 60, 62, 65, 67, 70, 72, 75, 76, 78, 80, 82, 84, 85, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99],
    "assignments_completed": [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 12, 12, 12]
}
data = pd.DataFrame(data)

def mean(data, colm):
    return sum(data[colm]) / len(data[colm])

def mode(data, colm):
    value = data[colm].mode()[0]
    count = data[colm].value_counts().max()

    return value, count

def median(data, colm):
    return data[colm].median()

def variance(data, colm):
    n = len(data[colm])
    mean = sum(data[colm]) / n

    sum_values = 0
    for i in data[colm]:
        diff = i - mean
        sum_values += diff ** 2
    variance = sum_values / (n - 1)
    return variance

def standard_deviation(data, colm):
    n = len(data[colm])
    mean = sum(data[colm]) / n

    sum_value = 0
    for i in data[colm]:
        diff = i - mean
        sum_value += diff **2 
    variance = sum_value / (n - 1)

    return variance ** 0.5

def value_range(data, colm):
    return max(data[colm]) - min(data[colm])

def skewness(data, colm):
    n = len(data[colm])
    mean = sum(data[colm]) / n
    std = standard_deviation(data, colm)

    sum_values = 0

    for i in data[colm]:
        diff = i - mean
        sum_values += (diff / std )** 3

    return sum_values / n

def kurtosis(data, colm):
    n = len(data[colm])
    mean = sum(data[colm]) / n
    std = standard_deviation(data, colm)

    sum_values = 0
    for i in data[colm]:
        diff = i - mean
        sum_values += (diff / std )** 4
    return sum_values / n

    return max(data[colm]) - min(data[colm])

def covariance(data, col1, col2):
    if len(data[col1]) != len(data[col2]):
        raise ValueError("two columns length must be the same")
    n = len(data[col1])
    col1_mean = sum(data[col1]) / n
    col2_mean = sum(data[col2]) / n

    sum_values = 0

    for i in range(n):
        col1_diff = data.loc[i, col1] - col1_mean
        col2_diff = data.loc[i, col2] - col2_mean
        sum_values += col1_diff * col2_diff

    return sum_values / (n-1)

def correlation(data, col1, col2):
    cov = covariance(data, col1, col2)
    col1_std = standard_deviation(data, col1)
    col2_std = standard_deviation(data, col2)
    return cov / (col1_std * col2_std)


print("Descriptive Statistics for 'exam_score' column")
print("1. Central Tendencies of Exam scores:")
print("-------------------------------------")
print(f"Average Exam Score:=============== {mean(data, 'exam_score')}")
print(f"Most Frequent Exam Score:=============== {mode(data, 'exam_score')}")
print(f"Middle score in exam scores:=============== {median(data, 'exam_score')} ")
print("2. Varibilities in Exam socres:")
print("-------------------------------------")
print(f"Variance how spread exam scores are from the Average exam socre on squared average:=============== {variance(data, 'exam_score')} ")
print(f"Standard Deviation how spread exam scores are from the Average exam score on average:=============== {standard_deviation(data, 'exam_score')}")
print(f"THe range of Exam scores:=============== {value_range(data, 'exam_score')}")
print("3. Distribution Measures: ")
print("-------------------------------------")
print(f"Skewness the tail direction of data:=============== {skewness(data, 'exam_score')}")
print(f"Kurtosis how heavy the tail is:=============== {kurtosis(data, 'exam_score')}")
print(f"4. Relationship between Exam scores and Study hours: ")
print(f"Covariance whether the exam scores and study hours move together:=============== {covariance(data, 'exam_score', 'study_hours')}")
print(f"Correlation the linear relationshiop between exam socre and study hours:=============== {correlation(data, 'exam_score', 'study_hours')}")

"""
CONCLUTIONS:
Average exam socre: 73.32 
Middle exam score: 75.0
Most Frequest exam score: 55   (3 times)
We can't say exam score data is normal distributed because 
Average exam score , middle exam score most frequent exam score are not near each other. It may be ther is no big gap but still there a bit diffenrence. 
Especially Most frequent value is lower than Average and Middlem but Average and Middle scores are very near each other

Variance: 327.81 
Exam scores are a bit spread out from Average exam socre, because we can say 327.81 on squared average is bigger than noraml distributed value

Standard deviation: 18.105524018928588
Most Exam scores are between Average Exam Score - Standard Deviation and Average Exam Score + Standard Deviation 
most exam scores are in 73.32-18.10 and 73.32+18.10
Exam scores are in ±standard Deviation

Rnage: 58
the difference between minimum and maximum exam socres is 58 

Skewness: -0.22060733906315946
Slightly left/negative tail because the exam scores has -0.22 skewness which is not exactly 0 or very near to 0. But the negavtive skewness < -0.5 
which it is near to normal distribution

Kurtosis: 1.687703860665191
Exam scores has a very light tail becuase kurtosis is very lower than 3

Exam scores and study hours Covariance: 69.08333333333333
The two columns move together , the effect each others strongly , because coveraince value is positive and big

Exam scores and study hours Correlation:0.776164561591788
THere is a string linear relationship between the two columns, because corr is positibe and greater than 0.5 
"""


"""

CONCLUSIONS:

Average exam score: 73.32
Median exam score: 75.0
Most frequent exam score: 55, appearing 3 times.

The mean and median are close to each other, which suggests that the exam_score distribution is approximately symmetric. 
However, the mode is lower than the mean and median. 
Therefore, we cannot say that the data is perfectly normally distributed only by looking at mean, median, and mode.

Variance: 327.81
The variance shows that exam scores are spread out around the mean. 
Because variance is measured in squared units, it is harder to interpret directly.

Standard deviation: 18.11
The standard deviation shows that exam scores differ from the mean by about 18.11 points on average. 
If the data is approximately normal, many scores are expected to fall between 55.22 and 91.43.

Range: 58
The difference between the minimum and maximum exam scores is 58 points.

Skewness: -0.22
The exam_score distribution is slightly negatively skewed. 
However, because the skewness is between -0.5 and 0.5, the distribution can be considered approximately symmetric.

Kurtosis: 1.69
The kurtosis is lower than 3, which means the exam_score distribution has lighter tails than a normal distribution. 
This is called a platykurtic distribution.

Covariance between exam_score and study_hours: 69.08
The covariance is positive, which means exam_score and study_hours tend to move in the same direction. 
When study_hours increases, exam_score also tends to increase. However, covariance does not clearly show the strength of the relationship.

Correlation between exam_score and study_hours: 0.776
There is a strong positive linear relationship between exam_score and study_hours. 
Students who study more hours tend to get higher exam scores. However, correlation does not prove causation.

"""