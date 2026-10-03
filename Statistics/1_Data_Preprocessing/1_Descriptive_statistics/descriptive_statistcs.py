# Content Table:
"""
    Descriptive Statistics:
        1. Distribution 
        2. Normal Distribution:     Bell Shape 
                                    Symmetic shape: left side ≈ right side
                                    Mean-Median-Mode: mean ≈ median ≈ mode
                                    68-95-99.7 rule:68%-1 std, 95%-2 std, 99.7%-3 std
        3. Skewness:
                    Positve (Right) Skewed
                    Negative (Left) Skewed
        4. Kurtosis:
                    Positive Kustosis
                    Negative Kurtosis
        5. Measures of Centeral Tendeny
                    Mean
                    Median
                    Mode
        6. Measures of Variablity:
                    Standard Diviation
                    Variance
                    Range
                    Correlation and Coveriance
"""

# Distribution
"""
Descriptive Statistics 
    used to summarize, describe and understand data

1. Distribution:
    Distribution --> shows how values are spread in a dataset.
    Example:
        Exam scores: 50, 60, 60, 70, 70, 70, 80, 90
            50 appears 1 time
            60 appears 2 times
            70 appears 3 times
            80 appears 1 time
            90 appears 1 time
        Most students scored around 70, this pattern is called Distribution

2. Normal Distribution:
    Methods to know whether data is normally distributed: 
        1. Histogram:
            Distributed:        █
                              █ █ █
                            █ █ █ █ █
                          █ █ █ █ █ █ █

            Not distrubuted:█
                            █ █
                            █ █ █
                            █ █ █ █
                            █ █ █ █ █
        2. KDe plot: for distribued data, plot should look like this
                            /\
                           /  \
                          /    \
                         /      \
        3. Mean vs Median comparisation
            mean ≈ median ≈ mode

        4. Skewness tell whether the data is symmetric or not
            skewness close to 0  → approximately symmetric
            positive skewness    → right-skewed
            negative skewness    → left-skewed

    68-95-99.7 rule:
        68% - About 68% of the data is between 1 standard deviation below the mean and 1 standard deviation above the mean.
        Formula:
            mean ± 1 * std
            Example:
                Mean = 70, 
                Standard deviation = 10 
                70 - 1 * 10 = 60
                70 + 1 * 10 = 80
                68% of students scored between 60 and 80.
        95% - About 95% of the data is between 2 standard deviations below the mean and 2 standard deviations above the mean.
        Formula:
            mean ± 2 * std
            Example:
                Mean = 70
                Standard Deviation = 10
                70 - 2 * 10 = 50
                70 + 2 * 10 = 90
                95% of students scored between 50 and 90.
        99.7% - About 99.7% of the data is between 3 standard deviations below the mean and 3 standard deviations above the mean.
        Formula:
            mean ± 3 * std
            Example:
                Mean = 70
                Standard Deviation = 10
                70 - 3 * 10 = 40
                70 + 3 * 10 = 100
                99.7% of students scored between 40 and 100.


    Main the properties of Normal :
        1. It is symmetric - the left side and rigght side are balanced

"""

# Skewness and Kurtosis 
"""
3. Skewness:  measures asymmetry of the distribution , skewness shows the direction of tail
    Formula:
        skewness = Σ((xᵢ - x̄) / s)³ / n
        Meaning:
            xᵢ = each value
            x̄ = mean
            s = standard deviation
            n = number of values
    Interpretation:
        Skewness > 0  → right-skewed / positive skew  
        Skewness < 0  → left-skewed / negative skew
        Skewness ≈ 0 (-0.5 to 0.5)  → approximately symmetric

    |   Absolute skewness | Interpretation                             |
    | ------------------: | ------------------------------------------ |
    |          0.00-0.50  | Approximately symmetric or slightly skewed |
    |          0.50-1.00  | Moderately skewed                          |
    | Greater than `1.00  | Strongly skewed                            |


    1. Positive (right) skewed --> when the tail on the right of the distribution is longer or flatter than the tail on left
                                   Simple: most values are small, a few values are very large
                                   Example: Household income, Customer spending, house price
                                   Frequency| ███████████
                                            | ████████
                                            | ████
                                            | ██
                                            |________________________________Values


    2. Negative (left) skewed --> When the tail on the left of the distribution is longer and flatter than the tail on right
                                  Simple: Most Values are high, a few values are very low
                                  Example: exam scores, product ratings
                                  Frequency |               █
                                            |            █████
                                            |          ████████
                                            |________███████████______Values
                            

    3. Symmetric: 
                   Frequency|
                            |       █
                            |      ███
                            |     █████
                            |____███████______ Vales

4. Kurtosis: 
    1. Pearson Kurtosis:  Measures how heavy the tail of the distribution
        Formula:
            kurtosis = Σ((xᵢ - x̄) / s)⁴ / n
            Meaning:
                xᵢ = each value
                x̄ = mean
                s = standard deviation
                n = number of values

        Interpretation:
            Kurtosis Value ≈ 3 (2.5-3.5) → Mesokurtic similar to normal distribution
            Kurtosis Value > 3           → Leptokurtic heavy tails, more extreme values/outliers
            Kurtosis Value < 3           → Platykurtic light tails, fewer extreme values/outliers

    2. Fisher/Excess Kurtosis Kurtosis 
        NOTE: Pandas .kurt/.kurtosis function retuns Fisher Kurtosis
        Fisher kurtosis = Pearson kurtosis - 3
        Interpretation:
            Kurtosis = 0 → Mesokurtic
            Kurtosis > 0 → Leptokurtic heavy tails, more extreme values/outliers
            Kurtosis < 0 → Platykurtic light tails, fewer extreme values/outliers
"""

# Measures of Centeral tendency and Measures of Variablity         
"""
5. Measures of Centeral tendency:
    1. Mean --> Average Value
                Formula : Mean = sum of all values / number of values

    2. Median --> Middle value after sorting the data
                Example: 10, 20, 30, 40, 1000 -> Median=30

    3. Mode --> Most frequent value: 
                Example: 10, 20, 20, 80, 30, 30, 20 10, 50, 70 -> Mode=20


6. Measures of Variablity:
    1. Standard diviation --> measures how far values are from the mean on average
                            Simple: Standard Deviation tells how spread out data is: 
                                                                                if StandD is small, values are close to mean
                                                                                if StandD is large, values are far from mean
                            Formula:
                                s = √ [Σ(xᵢ - x̄)² / (n - 1)]
                                Meaning:
                                    s = sample standard deviation
                                    xᵢ = each value
                                    x̄ = mean
                                    n = number of values

                                Interpretation: the most values range --> from (mean - std) to (mean + std)
                                Example:
                                        mean = 50
                                        std  = 15
                                    most values between 50-15=35 and 50+15=65

    2. Variance  --> measures hwo spread out the data values are from the mean on squarted average.
                    Simple: Variance tell how far the values from the mean but using spuared distance
                    Formula:
                         s² = Σ(xᵢ - x̄)² / (n - 1)
                        Meaning:
                            s² = sample variance
                            xᵢ = each value
                            x̄ = mean
                            n = number of values

                        Interpretation:
                            Variance close to 0 → values are very close to the mean
                            Higher variance     → values are more spread out
                            Lower variance      → values are more consistent

    3. Range --> The difference between the highest value and the lowest value in a dataset

    4. Correlation and Coveriance --> Both used to understand the relationship between two numerical Variables
                                Simple: one variable changes what happens to the other variable

                        1. Covariance --> Shows whether two variables moes together or movie in opposite directions
                                    Positive Covariance - both Variables move in the same direction:
                                        Example:
                                            Study hours increase → Exam score increases
                                            Study hours decrease → Exam score decreases
                                    Negative Coveriance - One variable increases and the another decreases
                                        Example:
                                            Absences increase → Exam score decreases
                                            Price increases → Demand decreases
                                    
                                    Formula:
                                        Cov(X, Y) = Σ((xᵢ - x̄)(yᵢ - ȳ)) / (n - 1)
                                        Meaning:
                                            xᵢ = each value of X
                                            yᵢ = each value of Y
                                            x̄ = mean of X
                                            ȳ = mean of Y
                                            n = number of observations

                                    Interpretation:
                                        Covariance Value > 0 → Positive covariance
                                        Covariance Value < 0 → Negative covariance
                                        Covariance Value ≈ 0 → No Linear Relationship


                        2. Correlation --> Shows how strongly two variables are connected, always between -1 and +1
                                    Formula:
                                        Correlation = Cov(X, Y) / (std(X) * std(Y))

                                    Interpretation:
                                        range of correlation value -1 to 1
                                            Correlation close to +1  → strong positive relationship
                                            Correlation close to 0   → no clear linear relationship
                                            Correlation close to -1  → strong negative relationship
                     
"""
 

def calculating_mean(data, colm):
    return sum(data[colm]) / len(data[colm])

def finding_median(data, colm):
    values = list(data[colm])
    values.sort()
    n = len(values)

    if n % 2 == 1:
        return values[n // 2]
    else:
        left = values[n // 2 - 1]
        right = values[n // 2]
        return (left + right) / 2

def measuring_kurtosis(data, colm):
    n = len(data[colm])
    mean = sum(data[colm]) / n
    std = data[colm].std()

    kurtosis = 0
    for i in data[colm]:
        m = (i - mean) / std
        kurtosis += m ** 4

    return kurtosis / n

def measuring_skewness(data, colm):
    n = len(data[colm])
    mean = sum(data[colm]) / n

    std = data[colm].std()

    value = 0
    for i in data[colm]:
        m = (i - mean) / std
        value += m ** 3

    return value / n

def variance(data, colm):
    n = len(data[colm])
    mean = sum(data[colm]) / n
    sum_squared_diff = 0
    
    for i in data[colm]:
        diff = i - mean
        sum_squared_diff += diff ** 2
    var = sum_squared_diff / (n-1)
    return var

def standard_deviation(data, colm):
    n = len(data[colm])
    mean = sum(data[colm]) /n
    sum_squared_diff = 0

    for i in data[colm]:
        diff = i - mean
        sum_squared_diff += diff ** 2
    
    var = sum_squared_diff / (n - 1)
    std = var ** 0.5
    return std

def coveriance(data, colm1, colm2):
    if len(data[colm1]) != len(data[colm2]):
        raise ValueError("two columns' lengths must be the same")
    
    n = len(data[colm1])
    mean_colm1 = sum(data[colm1]) / n
    mean_colm2 = sum(data[colm2]) / n

    sum_products = 0

    for i in range(n):
        diff1 = data.loc[i, colm1] - mean_colm1
        diff2 = data.loc[i, colm2] - mean_colm2
        sum_products += diff1 * diff2

    return sum_products / (n-1)

def correlation(data, colm1, colm2):
    std_col1 = standard_deviation(data, colm1)
    std_col2 = standard_deviation(data, colm2)

    cov = coveriance(data, colm1, colm2)

    corr = cov / (std_col1 * std_col2)
    return corr