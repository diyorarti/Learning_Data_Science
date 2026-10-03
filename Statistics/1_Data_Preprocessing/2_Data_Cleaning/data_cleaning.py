"""
Handling Missing Data
    The types of missing data:
        1. Missing Completely At Random (MCAR)  
        2. Missing At Random (MAR)
        3. Missing Not At Random (MNAR)
        4. General missing detection flow

    Outliers:
        1. Univariate 
        2. Multivariate
        3. Contextual
        4. Collective
"""


# Missingness
"""
    The types of missing Data:
        1. Missing Completely At Random(MCAR):
                A Value is missing for a completely random reason, and the missingness is not related to any other variable in the dataset. 
                Example:
                    | student | study_hours | exam_score |
                    | ------- | ----------: | ---------: |
                    | Ali     |           5 |         80 |
                    | Vali    |           6 |        NaN |
                    | Sara    |           4 |         75 |
                    | John    |         NaN |         90 |
                    | Anna    |           7 |         88 |
                They may be missing because of a random techinical problem.
                The missing values are not related to other variables (Student name, Study hours, or Exam Score)
                Real Life Example:
                    1. Survery mistake: Some people accidenylly skipped a question because the page was not loaded
                    2. Data Entry error: Worker may forget to enter
                    3. File Corruption: some cells may disappear because of a Software problem
            MCAR --> these values can be dropped if small amount, because it will not effect , analysis is unually not strong biased
            
            Detection methods:
                1. Creating a new column(missing indicator) with missing values and Comparing the columns with other columns
                    Question : are the missing values mostly from one group ? if No it is likely MCAR, if Yes it is likely MAR

            Treatement methods:
                1. Dropping when missing percentage is small
                2. Mean/Median/Mode/Any Advanced Imputation

        2. Missing At Random (MAR)
                A value is missing because of another observed column in the data. The Missingness has a pattern, we can explain the pattern using exit columns
                Exampl:
                    | student | age | job_status | income |
                    | ------- | --: | ---------- | -----: |
                    | Ali     |  20 | Student    |    NaN |
                    | Vali    |  22 | Student    |    NaN |
                    | Sara    |  28 | Worker     |   4000 |
                    | John    |  35 | Worker     |   5000 |
                    | Anna    |  40 | Worker     |   5500 |
                Here, income is missing mostly for students. So the missingness is related to job_status
                Another Example:
                    | patient | age_group | blood_pressure |
                    | ------- | --------- | -------------: |
                    | A       | Young     |            NaN |
                    | B       | Young     |            NaN |
                    | C       | Old       |            145 |
                    | D       | Old       |            150 |
                Maybe younger pations skipped blood pressure measuremnt more often. So missingness is related to age_group
            MAR --> Dropping these columns are dangerous

            Detection methods:
                1. Creating a new column(missing indicator) with missing values and Comparing the columns with other columns
                    Question : are the missing values mostly from one group ? if No it is likely MCAR, if Yes it is likely MAR
                2. Logistic Regression


            Treatement:
                1.Group-based Imputation
                2. Regression/KNN Imputation

        3. Missing Not At Random (MNAR)
                A value is missing because of the value itself. The reason the value is missing is directly connnected to the hidden value.
                Example:
                    | person | age | job     | income |
                    | ------ | --: | ------- | -----: |
                    | Ali    |  25 | Worker  |   3000 |
                    | Sara   |  35 | Manager |   7000 |
                    | John   |  45 | CEO     |    NaN |
                    | Anna   |  40 | CEO     |    NaN |
                maybe CEOs don't want to share their income because their uncome is very high
                Other Example:
                    Exam score: low-performing students refuse to submit their exam results
                    Customer feedback: Very angry customers don't complete the feedback form
            MNAR --> Most Dangerous, leads bias

            Detection methods:
                1. Domain Knowledge
                2. Related-variable clues
                3. Sensitivity analysis 

            Treatement:
                1. Missing indicator column 
                2. Sensitive Analysis
                3. Domain-based impulation
                4. Advanced methods
        
        | Missingness type | Meaning                                |   Risk | Treatment                                             |
        | ---------------- | -------------------------------------- | -----: | ----------------------------------------------------- |
        | MCAR             | Missing randomly                       |    Low | Drop rows or simple imputation                        |
        | MAR              | Missing depends on observed columns    | Medium | Group-based, KNN, regression imputation               |
        | MNAR             | Missing depends on hidden value itself |   High | Missing indicator, sensitivity analysis, domain logic |
"""


# Outliers
"""
Outliers types:
Checking at first impossible values:
    For example:
        age = 150
        Exam_score 199
    Tretment methods:
        1. Replacing with Nan
        2. reomve the column

1. Univariate means one variable. Checking one column at a time
        An unsual value in one sinle column.
        Example: exam_score = [55, 60, 65, 70, 75, 80, 300]. Here 300 is a univariate outlier , because it is extremenly different
                    age = [18, 19, 20, 21, 22, 150]. 150 is an outlier. Most ages are 18-22, but 150 is extremely high
        Detection methods:
            Visual Methods: 
                1. Visualizations:
                    Boxplot 
                    Histogram
                    Scatter plot
                2. IQR 
                        IQR = Q3 - Q1
                        Lower bound = Q1 - 1.5 * IQR
                        Upper bound = Q3 + 1.5 * IQR
                3. Z-score
                    z = (x - μ) / std
                    Threshold for univariate outlier detection is 3 
                        becase in normal distribution:
                        - About 68% → within ±1 SD
                        - About 95% → within ±2 SD
                        - About 99.7% → within ±3 SD
                4. Modified Z-score:
                    Mᵢ = 0.6745 * (xᵢ - x̃) / MAD
                    MAD = median(|xᵢ - x̃|)
                        xᵢ = individual data value
                        x̃  = median of the data
                        MAD = Median Absolute Deviation
                        Mᵢ = Modified Z-score
                
        Treatment methods:
            1. Keep the outlier. If the values are real, logically possible.
            2. Correct the outliers. If real source information is avialiable. never guess.
            3. Remove the outliers (Trimming). If the values are erroneous, unreliable
            4. Winsorization . Replacing extreme values with a boundary value.
            5. Transformation. Log transformation, Sqoure-root Transformation, Box-Cox transfromation.
            6. Imputation.  Mean, Median, Mode, Group-based median.

2. Multivariate means more than one variable. A data point looks unsusal when we consider multiple columns together
        Example:
            | person | age | monthly_income |
            | ------ | --: | -------------: |
            | Ali    |  25 |           3000 |
            | Vali   |  30 |           4000 |
            | Sara   |  35 |           5000 |
            | John   |  40 |           6000 |
            | Mike   |  18 |         100000 |
            here, age column 18 years old , ok no problem it may be, but 100000 monthly income, 
            but when we combine both age and monthly income, it seems unusual. So this row may be a multivariate outlier.
        Another example:
            | transaction | amount | location | time  | device     |
            | ----------- | -----: | -------- | ----- | ---------- |
            | T1          |     20 | Poland   | 14:00 | iPhone     |
            | T2          |     50 | Poland   | 16:00 | iPhone     |
            | T3          |     35 | Poland   | 18:00 | iPhone     |
            | T4          |   3000 | Brazil   | 03:00 | New Device |
            The transaction T4 may be suspicious because of the combination: high amount | unusual country | unusual time | new device
        Detection methods:
            1. Identifying Mutlivarite column groupds 
            2. Scatter plots
            3. Mahalanobis distance: how unusual is a record(all column values together) compared to the center and covariance structure of all records.
        Treatment methods:
            1. Keep observations
            2. correct/replace erroneous values
            3. Remove observations
            4. Transform
            5. Robust methods : Median, Robust median, Huber Regression
        
3. Contextual: A data point that is unusual only in a specific context.
        The value itself may look normal, but when you consider the situation, time, place, or condition, it becomes ususual.
        Contextual outlier = normal value in one situation, strange value in another situation
        Example:
            Temperature = 35°C
            | Context              | Is 35°C an outlier? |
            | -------------------- | ------------------- |
            | Summer in Uzbekistan | No, maybe normal    |
            | Winter in Poland     | Yes, very unusual   |
        Another Example:
            | day       | context      | visits |
            | --------- | ------------ | -----: |
            | Monday    | normal day   |  1,000 |
            | Tuesday   | normal day   |  1,100 |
            | Wednesday | normal day   |    950 |
            | Friday    | Black Friday | 20,000 |
            20,000 visits on a normal day → outlier
            20,000 visits on Black Friday → maybe normal
        Detection Methods:
            1. Workflow:
                1-step: define Context-behavior relationships.
                2-step: descriptive statistics
                3-step: visualizations
                4-step: IQR
            1. Domain knowledge
            2. Time-Series Analysis
        Treatment methods:
            1. Domain-specifc treatment.
            2. Keep the outlier if it is real

4. Collective: A group of data points that look unusual together
        Example: a factory produces products every day.
            | day       | defective_products |
            | --------- | -----------------: |
            | Monday    |                  3 |
            | Tuesday   |                  4 |
            | Wednesday |                  2 |
            | Thursday  |                  5 |
            | Friday    |                100 |
            | Saturday  |                120 |
            | Sunday    |                110 |
            3-5 defective products normal for a day, but suddenly 100, 120, and 110 , This group of high defective products is unusual.
        Credit Card Transactions
            a person usually makes 1-2 transactions per day. But suddenly 20 transactions happen in 10 minutes

        Dectection Methods
            1. Clustring 
            2. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
            3. Time-Window Analysis
        Treatment methods:
            1. Investigate the root couse
"""