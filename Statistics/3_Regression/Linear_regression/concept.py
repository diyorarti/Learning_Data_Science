# Linear Regression
"""
Ordinary Least Squares
Ordinary least squares Assumptions:
    Linearity
    Independenc of errors
    Normality of errors
    Homoscedasticity
    Absence of severe multicollinearity

Common techniques:
    Residual analysis
    Cook's distance
    Variance inflation factor (VIF)

Univariate Feature Selection:
    F-test
    Mututal Information
    Chi-square

Stepwise Feature Selection
    Forward Selection   
    Backward Elimination
    Bidirectional Elimination

Dimensionality Reduction:
    PCA
    SVD

Model Intepretation:
    Interpreting Coefficients:
        Assessing the significance of coefficients
        Evaluating the magnitude of coefficients
        Evaluating the direction of coefficients
    Assesing the model fit:
        R-squared (Coefficient of determination)
        Adjusted R-squared
        Root mean squared error RMSE
        F-statistic
        Akaike information criterion (AIC)
        Bayesion information criterion (BIC)
    Overfitting
    Bias variance tradeoff
        Bias
        Variance  
"""


# Ordinary least squares and Key Assumptions
"""
Ordinary Least Squares is A Statistical method (algorithm) for choosing the best linear regression coefficients and intercept.
    Formula: 
        1-step: Calculating the OLS parameter vector (intercept and coefficients)
            β̂ = (Xᵀ @ X) @ Xᵀ @ y
        2-step: Make predictions on the training data
            ŷ = X @ β̂
        3-step: SSE(sum of squared error)
            SSE(Sum of squared error) SSE = Σᵢ₌₁ⁿ eᵢ²


    Key Assumptions of OLS 
        1. Linearity:
            Means the relationship between the independet variables(features) and the dependent variable(target). 
            Detection methods:
                1. scatter plots (one features vs target)
                2. Residual scatter plot (one feature vs residuals )
            Treatement methods:
                1. Tranform features by (Logarithmic, Square root, Box-Cox)
                2. Add Polynomial features

        2. Independence of errors:
            If one error helps predict another error, the errors are dependent/correlated.
            If one error provides no information about another error, the errors are independent.
            OLS generally requires independent—or at least uncorrelated—errors.
            Dependent errors cause problems, especially for standard errors, p-values and confidence intervals.

            Detection methods:
                1. Residuals vs observation order
                2. Lag plot (comparing each residuals with previous residual)
                3. Autocorrelation function (AFC)
                4. Durbin-Watson statistic
                5. Bruesch-Godfrey test
                6. Ljuing-Box test
            Treatment methods:
                1. Add missing explanatory variables 
                2. Add appropriate lagged variables
                3. Newey-West/Hac standard errors
                4. Cluster-robust standard Errors 
                5. Generalized Least squares

        3. Normality of errors
                    Measures the distribution of erros
                    Detection methods:
                        1. Histogram
                        2. Q-Q plot
                        3. Skewness
                        4. Kurtosis
                        5. Jarque-Bera test or Shapiro-Wilk test

        4. Homoscedasticity -> measures how Residuals have approximately constant spread
            The residual changes depending on the predicted value of feature value
                Simple example: A hourse predictor model
                                For cheaper houses: Predicted price: $100,000 -> Errors: -5,000, +3,000, -7,000, +4,000
                                For expensive houses: Predicted price: $500,000 -> Errors: -60,000, +80,000, -90,000, +70,000
                                Here the residuals are more spread about for expensive apartments
                Visualizations: 
                    r   |                                  This residuals look like a random cloud around zero,
                    e + |     .  . .   . .  . .            the spread is approximately the same from left to right
                    s 0 |----------------------------      This is good case called Homoscedasticity
                    i - |   . .   . . .   .  .
                    d   |
                    u   |____________________________
                    l         predicted values
                        residuals
                              |
                            + |                 .       .          This rediaduals from a funnel shape: at low predicted values, 
                              |             .      .       .       residuals are close together, at high predicted values,
                            0 |--------------------------------    residuals become more spread out 
                              |       .   .      .        .        THis means the variance of residuals is not constant,
                            - |   .             .       .          this is problem case called Heteroscedasticity
                              |
                              |_________________________________
                                    predicted values
                Detection Methods:
                    1. Visualization: Scatter plot (residuals vs predicted values, 
                                                    absolute residuals vs predicted values, 
                                                    absolute residuals vs predicted values correlation)
                    2. Statistical method: Breusch-Pagan Test: 
                        Breusch-Pegat test answers the question: Does the variance/spread of residuals depend on the feature values ?

        5. Absence of multicollinearity 
            occurs when one predictor is strongly explained by several other predictors together   
            Detection methods:
                1. Correlation Heatmap plot
                2. Variance inflation factor (VIF)
                    Mearues: how much variance of a regression coefficients is increased beause the feature is linearly related to the other predictor variables.
                    In Simple: VIF checks whether a feature contains enough unique information, or most of it's information is already contained in others
                    VIF is diagnostic measure used to detect multicollinearity among the predictors in a regression model
                        Formula:                      1
                                            VIF = ──────────
                                                    1 - R²
                                        VIF = 1 / (1 - (1 - R²))
                                        R² = residuals ** 2
                        Interpretation 
                            VIF ≈ 1 -> No multicollinearity problem
                            VIF 1-5 -> Usually acceptable
                            VIF 5-10 -> Moderate / concerning multicollinearity
                            VIF > 10 -> Strong multicollinearity problem      
                        Implementation steps:
                            1. Choose a target feature
                            2. Train a model
                            3. Calculate R² (residuals ** 2)
                            4. Calculate Tolerance (1 - R²)
                            5. Calculate VIF  (1 / tolerance)
                            6. Repeat this process for each feature

                
            Treatment methods:
                1. Remove one of the redundant features
                2. Combine strongly related features
                3. Use Ridge Regression / Lasso Regression / Elastic Net
                4. PCA - Principal Component Analysis 

"""

# Common techniques
"""
Residual analysis:
    1. Scatter plots Residuals vs predictions:
        | Appearance               | Interpretation                        |
        | ------------------------ | ------------------------------------- |
        | Random cloud around zero | Good general result                   |
        | Curved LOWESS line       | Possible nonlinearity                 |
        | Funnel shape             | Possible heteroscedasticity           |
        | Separate groups          | Missing group or categorical variable |
        | Isolated points          | Potential outliers                    |

    2. Residuals vs each pridictor
    3. Breusch-Pagan test
    4. Normality of residuals by histogram
    5. Q-Q plot
    6. Skewness, Kurtosis, Jarque-Bera


Cook's Distance:
    Cook's Distance is a regression diagnostic used to influential observations 
    it asks: How much would the regresion model results change if an observation were removed ?
    It combines two important ideas:
        1. Residual -> How far is the actual target from it's prediction
                    residual = (eᵢ² / (p * MSE)) 
        2. Leverage -> How unusual is an observation's predictor value
                    levarage = (hᵢᵢ / (1 - hᵢᵢ)²)

    Formula:
            Dᵢ = (eᵢ² / (p * MSE)) · (hᵢᵢ / (1 - hᵢᵢ)²)
        Menaing:
            eᵢ = residual of observation i
            hᵢᵢ = leverage of observation i
            p = number of estimated model parameters, including intercept
            MSE = mean squared error of the regression model 
        Threshold: threshold=4/n
        Interpretation:
            D_i < 4/n = usually not strongly influential
            D_i > 4/n = invertigate the observation
            D_i > 1  = potentially highly influential


Variance inflation factor (VIF)
    Mearues: how much variance of a regression coefficients is increased beause the feature is linearly related to the other predictor variables.
    In Simple: VIF checks whether a feature contains enough unique information, or most of it's information is already contained in others
    VIF is diagnostic measure used to detect multicollinearity among the predictors in a regression model
        Formula:
                VIF = 1 / (1 - R²)
                VIF = 1 / (1 - (1 - R²))
                R² = residuals ** 2
        Interpretation 
            VIF ≈ 1 -> No multicollinearity problem
            VIF 1-5 -> Usually acceptable
            VIF 5-10 -> Moderate / concerning multicollinearity
            VIF > 10 -> Strong multicollinearity problem      
        Implementation steps:
            1. Choose a target feature
            2. Train a model
            3. Calculate R² (residuals ** 2)
            4. Calculate Tolerance (1 - R²)
            5. Calculate VIF  (1 / tolerance)
            6. Repeat this process for each feature    
    NOTE: The acutal target is not included.        
"""

# Univariate Feature Selection
"""
Univariate Feature Selection 
    Feature Selection is the process that Choosing the most useful features for a model and 
    exluding irrelevant, redundant, leaking or excessively problematic features

    | Feature     | Target      | Appropriate method                                 | 
    | ----------- | ----------- | ---------------------------------------------------| 
    | Categorical | Categorical | Chi-square, mutual information                     |
    | Categorical | Continuous  | ANOVA F-test, mutual information                   | 
    | Continuous  | Categorical | ANOVA F-test through f_classif, mutual information | 
    | Continuous  | Continuous  | Correlation, F-test, mutual information            |

    Adavatages:
        1. Improve Model interpretability
        2. Reduce overfitting
        3. Improve statistical reliability
        4. Reduce computation
""" 

# F-test
"""
F-test
        IT mearures how much variation in target can be explained by the feature, compared with how much can't be explained 
        Formula: 
            F-score = target variation explained by the feature / target variation still unexplained
        F-score -> Shows how large the explained variation is compared with the unexplained variation
        P-value -> Shows whether the evidence is statistically significant

        Example:
        Predicting without feature:     | Actual price | Prediction | 
        Intercept-only model            |      100,000 |    192,500 |
                                        |      150,000 |    192,500 |
                                        |      220,000 |    192,500 |
                                        |      300,000 |    192,500 |

        Adding one Feature: | Area | Actual price | Predicted price |
                            |   40 |      100,000 |         105,000 |
                            |   60 |      150,000 |         155,000 |
                            |   80 |      220,000 |         210,000 |
                            |  110 |      300,000 |         300,000 |

        Variation epxlained -> How much better after adding feature (area)
        Variation Unexplained -> Huch error still remains after adding feature (area)

        If the feature (area) explaines a lot of price variation and only a small amount remaining then
            F-score = larger explained variation / small unexplained variation
        
        If the feature (area) explaines a small part of price variation and a big amounnt remaining then
            F-score = small explained variation / larger unexplained variation

        Implementation steps:
            1-step: Choose feature and target     | example: area_m2-feature, arartment_price-target
            2-step: Build a Linear model          | example: OLS model
            3-step: Make predictions              | example: y_pred = coefficients * X + intercept
            4-step: Only Intercept model          | example: target_mean = np.mean(y_mean)
            5-step: Total Variation (SST)         | example: SST = np.sum((y-y_mean)**2)
            6-step: Explained Variation (SSR)     | example: SSR = np.sum((predictions - y_mean)**2)
            7-step: Unexplained Variatioon (SSE)  | example: SSE = np.sum((predictions - y_actual)**2)
            8-step: Decomposition SST = SSR + SSE | example: SST = SSR + SSE
            9-step: Degrees of freedom:           | example: degrees_of_freedom = 1, because model has one independent feature 'area_m2'
                Example:
                    Consider 3 numbers whose average must eqaul 10
                    Their total must be 3*10 = 30
                    You may freely choose first and second numbers. example: 5, 12
                    But third number is no longer free. 30 - 5 - 12 = 13
                    So: Num observations:3, One restriction:mean fixed, Degrees of freedom:3-1=2
            10-step: Error degrees of freedom df_error = n - parameters | example: data has 100 observations, 
                     5 parameters (1 intercept + 4 coeff) df_error = 100-5
            11-step: MSR repsentes tThe model's average explained variation per regression degree of freedom.
                    example: MSR = SST / Degree_of_freedom 
                    Formula: MSR = SST / degrees_of_freedom
            12-step: MSE repsentes the average unexplained variation, per error degree of freedom. 
                     Formula: MSE = SSE / error_degrees_of freedom
            13-step: F_statistic = MSR / MSE 
                    Interpretation:
                        Large F_statistic value means, the coefficient(s) explains much more variation in target than remaining average error.
                        Small F_statistic value means, the coefficient(s) explains little variation in target compared with unexplained variation.
            14-step: P-value represents how surpricing F_statistic would be, if the feature actually had no relationship with target. 
"""
  
# Mutual Information
"""
Mutual information measures how much information one feaure gives about another variable(target)
    It asks: How does knowing this feature reduces uncertainty about another variable(target)
    Written as I(X;Y) 

    Basic Intuition:
        Y = house price
        X = house area
        Befor knowing the area of the house, we are uncertain about the price.
        After knowing the area, we can make a better guess about the price.
        Therefore, hourse_area gives information about price I(area;price)
        X = ID
        knowing the ID usually does not help to understand anything about price
        So, I(ID;price) ≈ 0

    Mutual Information and independence
        IF X and Y are completely independent: P(X, Y) = P(X) * P(Y)
        Knowing X doesn't change what we know about Y
        So I(X; Y) = 0

    Formula: MI(X; Y) = Σₓ Σᵧ P(x, y) * log( P(x, y) / (P(x) * P(y)) )
        Important part:
            P(x, y) / (P(x)P(y))
        THis compares:
            the observed joint probability 
            the joint probability expected if the variables were independent
        When the radio equals 1
            1 = P(x, y) / (P(x)P(y))
            log(1) = 0
            this comnination contributes no information
        When radio is greater than 1
            The comnination occurs more frequently than expected under independence
        When radion is less than 1
            the combination occurs less frequently than expected under independence
        
        Example:
            Suppose we study whether having an elevator gives information about whether a property is expensive.
            | Has elevator | Cheap | Expensive | Total |
            | ------------ | ----: | --------: | ----: |
            | No           |    40 |        10 |    50 |
            | Yes          |    10 |        40 |    50 |
            | Total        |    50 |        50 |   100 |
        Define:
            X = has elevator
            Y = price category
        Consider:
            P(X = yes; Y = expensive) = 40 / 100 = 0.40
        margin probabilities: 
            P(X = yes) = 50 / 100 = 0.50
            P(Y = Expensive) = 50 / 100 = 0.50
        If the variables were independent, we would expect:
            P(X = yes) P(Y = expensive) = 0.50 * 0.50 = 0.25
        But observed probability is 0.40 
        The combination “elevator and expensive” appears much more frequently than the independence expectation: 0.40 > 0.25
        
    Mutual information in feature selection
        | Feature         | Mutual Information |
        | --------------- | -----------------: |
        | `area_m2`       |               0.74 |
        | `neighborhood`  |               0.48 |
        | `building_age`  |               0.21 |
        | `random_number` |               0.01 |
        here, Mutual information doesn't automatically tell us where to set the remobal threshold.
        We should combine it with domain kwowledge.

    Mutual information detects both linear and non-linear relationships
        but Mutual information does't show direction of the relationship.

    Mutual information is symmetric
        X(;Y) = I(Y;X)
        The information X provides about Y equals the information Y provides about X.

    Advantages:     
        detect nonlinear dependencies
        works with categorical and continuous data

    Disadvantages:
        No direction 
        No universal scale (a score 0.4 is not automatically good or bad)
        Sensitive to enstimation (value can be changed by sample size, num of negihbors, noise, treatement of categorical features)

    Interpretation:
        Mutual information is always non-negative
        I(X;Y) = 0 means X and Y are independent
        I(X;Y) > 0 means X and Y are dependent
        how strong MI is can be measured by comparing one feature's MI with other features' MIs. 
"""

# Chi-Square
"""
Chi-square test can be applied only for Categorical feature and categorical target.
    It asks: are these two categorical variables(one faature and target) dependent , or are they independent ?
    Chi-square measures how far the actual relationship between two categorical variables is from what we would see if they were independet.
"""

# Stepwise Feature Selection
"""
Stepwise Feature Selectio is an iterative method for choosing which idependent variables X1, X2, X3 should remain in a regression model. 
    Instead of every feature separately, we repeatedly:
        1. fit a regression model
        2. add or remove a feature
        3. evaluate whether the model improved.
        4. repeat until no useful change can be made.

    Advantages:
        Univariate feature selection might find two features important. For example: area_m2 and rooms. They are correlated.
        Since Univariate feature selection tests them seperately, it finds both useful. 
        But Stepwise feature selection detects this problem.
    
    Three main forms:
        Forward Selection  - add features one by one 
        Backward selection - Remove features one by one
        Stepwise Selection - Both add or remove features 
"""

# Forward Feature Selection
"""
Forward Feature Selection starts training model with only intercepts or no feature. And add features one by one until model doesn't change.

    Implementation:
        1. Train only intercept model.
        2. Try every feature and evaluate each candidate model using chosen measurement criteria.
        3. Try every remaining feature again and evaluate each candiate model using chosen measurement criteria.
        4. Repeat until none of the remaining features improves model based on the selected measurement criteria.
"""

# Backward Elimination
"""
Backward Elimination starts with the full regression model containing all condidate features, then removes the least useful feture one at a time

    Implementation:
        1. Train a model with all features and calculate chosen measurement criteria
        2. Temporarily remove each feature one at a time and calculate chose mearuement criteria
        3. Choose the model with best performance after removing a feature and remove the feature permanetly
        4. Repeat this process 
        5. Stop when Model performance decreases after removing any remaining features
    
    Example:
        Suppose: all features = ['area_m2','rooms','bedrooms','bathrooms','school_rating']
        Chosen Measurement criteria: Adjusted R2 score
        Full model gives R2=0.700
        1-step:
            | Removed feature | Adjusted (R^2) after removal |
            | `area_m2`       |                        0.510 |
            | `rooms`         |                        0.701 |
            | `bedrooms`      |                        0.699 |
            | `bathrooms`     |                        0.695 |
            | `school_rating` |                        0.680 |
            after removing rooms features, model performance is slightly better
            Selected features = ['area_m2','bedrooms','bathrooms','school_rating']
        2-step:
            | Removed feature | Adjusted (R^2) |
            | `area_m2`       |          0.520 |
            | `bedrooms`      |          0.700 |
            | `bathrooms`     |          0.703 |
            | `school_rating` |          0.681 |
            after removing bathrooms features, model gets better performance
            Selected features = ['area_m2','bedrooms','school_rating']
        3-step:
            Remove area_m2       → 0.520
            Remove bedrooms      → 0.699
            Remove school_rating → 0.681
            We stop because removing any features does't make model better
"""

# Dimensionality Reduction
"""
Dimensionality Reduction means: 
    Reducing a dataset from many features to fewer dimensions while trying to preserve as much as useful information as possible.
    Dimensionality Reduction:
        1. Creates new features/dimensions
        2. Combines information from features
    
    Dimensionality Reduction
    │
    ├── 1. Feature Selection - Keep some original features   
    │ 
    └── 2. Feature Extraction - Create fewer new features from the original features
    
    The most common Feature Extraction methods: 
        1. Principal Component Ananlyis - PCA 
        2. SVD 

    PCA (Principal Component Ananlyis)
        It takes several possibly correlated features and transform them into a smaller set of new variables called Principal components.
        Example:
            we features: area_m2, rooms, bedrooms -> strongly correlated features
            PCA tries to compress that shared infromation 
            SO: X1, X2, X3 → PC1, PC2, PC3
            The number of components can be the same number of original features, the dimensionality reduction happens when 
            we decide to keep only the most informative components
            Suppose:
                PC1 → 78% of variance
                PC2 → 17% of variance
                PC3 →  5% of variance
            PC1 + PC2 = 95%  so we may keep only PC1 and PC2

            v = eigenvector → direction of a possible principal component
            λ = eigenvalue → amount of variance captured in that direction
    
    SVD(Singular Value Decomposition)
        SVD decomposes a data matrix into three simpler matrices that describe its main directions, strengths, and coordinates.
        X = UΣVᵀ
        U = directions/patterns across the observations
        Σ = singular value, telling how important each direction is
        Vᵀ = directions/weights across the features
        Example:
            we have 5 features:
                area_m2
                rooms
                bedrooms
                bathrooms
                floor    
            SVD looks and says: can I describe most of this 5-dimensional data using only a few important underlying directions?
            then it decomposes: X = UΣVᵀ
            Original data X
                ↓
            ---------------------------------
            U      Σ      Vᵀ
            │      │       │
            │      │       └─ feature directions / weights
            │      │
            │      └─ importance of each direction
            │
            └─ coordinates/patterns of observations
        
            What is Vᵀ
                this roows of Vᵀ contain weights for the original features.
                For example one direction may be 
                    area_m2       0.54
                    rooms         0.52
                    bedrooms      0.54
                    bathrooms     0.38
                    floor         0.01
                It is similar to the eigenvector weights you saw in PCA

            Σ (Sigma) contains the singular values
                For example:
                    Σ = [   [125, 0,  0, 0, 0],
                            [0,  70, 0, 0, 0],
                            [0,  0, 25, 0, 0],
                            [0,  0,  0, 5, 0],
                            [0,  0,  0, 0, 1]]
                Direction 1 → singular value 125 → very important
                Direction 2 → singular value 70  → important
                Direction 3 → singular value 25
                Direction 4 → singular value 5   → little information
                Direction 5 → singular value 1   → very little information
            
            U describes how each observations relates to those new directions

        How does SVD reduce dimensions ?
            Dimensinality reduction happens when we keep only the strongest k singular values/directions.
            This is called: Truncated SVD
            Suppose the singular values indices that the 3 directions contain almost all useful information
            So 5 directions --> 3 directions

    PCA = dimensionality-reduction method / statistical technique
    SVD = mathematical matrix factorization method that can be used to implement PCA
""" 

# Model Interpretation
"""
Model interpretation means understanding what a trained model is telling us about the relationship between the input features and the target Y.
    Linear Regression equation:
        Ŷ = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ
    Training gives us the numbers(parameters)
    Model interpretation gives those numbers(parameters) meaning
    Example:
        price_hat = 50,000 + 3,000(area) - 1,500(age)
            Intercept = 50,000
            area coefficient = 3,000
            age coefficient = -1,500
        Model intepretation asks:
            1. What does the 3000 coefficient actually mean ?
            2. Why is the age coefficient negative ?
            3. Which feature has the strongest relationship with price ? 
            4. is a coefficient statistically sifnificant, or could it just be random noise ?
            5. How well does the whole model explain variation in the target ?
            5. is the model overffiting ?
            6. Would model performance remain stable on unseen data ?
    
    Interpret indivintual features
        What does each feature tell us about the target ?
        This includes:
            Interpreting coefficients
            Significance of coefficients
            Magnitude and direction of coefficients

    Intepreting the whole model
        How good is the entire regression model ?
        This includes:
            R² score
            Adjusted R² score
            RMSE, MAE
            F-statistic
            AIC, BIC
            Overfitting, underfitting
            Bias-Variance tradeoff
"""

# Interpreting Coefficients
"""
Interpreting coefficients
    What is a Coefficient ?
        Multiple Linear Regression: Ŷ = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ
        Each feature has a coefficient: price_hat = 50,000 + 3,000(area_m2)- 1,200(building_age) + 15,000(has_elevator)
            β₀ = 50,000
            β_area = 3,000
            β_age = -1,200
            β_elevator = 15,000
            How much does the predicted target change when this feature changes, while the other features stay constant?
        what if the coefficient is zero ?
            THe feature has no linear contribution to the predicted target after accounting for the other features.
            In real models, coefficients are rarely exactly zero unless regularization(L1, L2) sets them zero.'
        Interpreting the intercept
            price_hat = 50000 + 3000(area) - 1200(age) + 15000(elevator)
            The intercept - β₀ = 50000
            it is the predicted pirce, when every numerical feature equals zero and every dummy varianble is at its reference category.
            SO if: area = 0 | age = 0 | has_elevator = 0 --> price = 50000
            but an apartment with area=0m2 is unrealistic.
            So, The intercept has a mathematical meaning, but sometimes no useful real-world interpretation

Assessing the significance of coefficients
    is this estimated relationship statictically reliable, or could we have obtained it just because of random sampling variaton ?
    Example:
        All aparttments price in Poland. β_area 
            First sample of apartments - β_area=3000
            Second sample of apartments - β_area=2800
            Third sample of apartments - β_area=2950
        So estimated coefficient is not equal to the true population coefficient.
        All samples' coefficients are close to 3000
        This gives: The area coefficient is quite stable. The relationship probably is not just random noise.

    Another example:
        All aparttments price in Poland. β_area 
            First sample of apartments - β_area = -1500
            Second sample of apartments - β_area = 800
            Third sample of apartments - β_area = 3050
            Fourth sample of apartment - β_area = 6000
            Fifth sample of apartment - β_area = -500
        THis gives: The area coefficient is very uncertain. Maybe this apparent relationship is not reliable.
    SE(uncertainty) asks: How spread out are all the possible coefficient estimates?
        SE(β)=standard deviation of the coefficient estimates across repeated samples

    Methods to check the Significance of coefficients
        1. t-test
        2. p-value
        3. confidence interval
""" 

# Evaluating the magnitude and direction of coefficients
"""
Evaluating the magnitude and direction of coefficients
    Direction: Does the feature increase or decrease the predicted target ? 
        The sign of the coefficient gives it's direction
        Positive coefficient β_area = 3000 | β_area > 0 
            So area has a positive relationship with predicted price: area↑ ⇒ predicted price↑
            As apartment area increases, predicted price increases, holding other variables constant.
        Negative coefficient β_age = -1200 | β_age < 0
            So age has a negative reolationship with predicted oruce: age↑ ⇒ predicted price↓
            Older buildings are associated with lower predicted apartment prices, holding other variables constant.

    Magnitude: How large is that change?
        How large is the predicted change in Y for a one-unit change in X ?
        β_area = 3000  means A 1 m² change in area corresponds to about a $3,000 change in predicted price.
        β_age = -1200 means one years change in age corresonds to about a $1,200 change in predicted price

    Coefficient = -1200
        - sign = direction
        1200 = magnitude

    Comparing magnitudes are wrong
        area_m2             3000
        building_age       -1200
        distance_center    -5000
        Distance is the most important feature because 5000 is the largest coefficient. this wrong conclusion
        Because the features are different units:
            area             → square meters
            age              → years
            distance         → kilometers
"""
 
# Assessing the model fit
"""
Assesing the model fit asks: How well does the whole regression model fit the data ?
    How much of the variantion in Y does the model explain ?
    How large are the prediction errors ?
    Does the collection of predictors provide useful explanatory power ?
    Is one model better than another model ?

    Metrics for assessing model fit:
        R-squared
        Adjusted R-squared
        RMSE
        F-statistic
        AIC / BIC
    
    R-squared: How much of the variation in the target does the model explain ?
    Adjusted R-squared: Asks the same question, but it cosiders the number of predictors. 
                        It helps with the problem that ordinary R² usually increase when new feature is added even useless one
    RMSE: How far are predictions from actual values ? 
    F-statistic: How much variation in Target does the model explain compared to how much it doesn't explain ?
    AIC / BIC : Comparing models

"""

# R2-score 
"""
R2-score 
    It answers that how much variation in target does the model explain ?
    Formula:
        R² = 1 - (Σ(y_true - y_pred)² / Σ(y_true - mean(y_true))²)
    Simlely:
        R² = 1 - (SSR / SST)
        SSR = explained variation by model
        SST = total variation in target
    How to Interpret R²:
            R² = 1.0     → perfect model
            R² = 0.8     → model explains 80% of variation (How much the real target values are spread out or different from their average.)
            R² = 0.5     → model explains 50% of variation
            R² = 0       → model is not better than predicting the mean
            R² < 0       → model is worse than predicting the mean
"""

# Adjusted R2-score
"""
Adjusted R2-score 
    Ordinary R2-score has a problem that it will always increase even a new useless feature is added.
    Adjusted R2-score fixes this by penalizing the model for adding more predictors.
    The idea: did the new feature improve the model enough to justify increasing model complexity ?
    Formula:
        Adj R² = 1 - (1 - R²) * ((n - 1) / (n - p - 1))
        n = number of observations
        p = number of predictors
        R² = Ordinary R² 
"""

# Akaike information criterion (AIC)
"""
Akaike information criterion (AIC) 
    It is used to compare regression models.
    It answers: Which model gives a good fit without being unnecessarily complex ?
    It balances two things: Goot fit vs Model complexity
    The formula:
        AIC = 2k - 2ln(L)
        k = number of estimated parameters in the model
        L = maximum likelhood of the model
        ln(L) = measures how well the model fits the observed data 
    Intuition:
        AIC = fit penalty + complexity penalty
    The key rule:
        Lower AIC is better
    Example:
        | Model   | Features                                                  |  AIC |
        | Model A | area                                                      | 1250 |
        | Model B | area + age                                                | 1180 |
        | Model C | area + age + rooms + floor + elevator + 10 other features | 1195 |
        Model B is the best model
        Because the extra features may improve the fit only slightly, while increasing model complexity.
        Adding features is worth it only if they improve the fit enough to justify the extra complexity.
      
"""

# Bayesian information criterion (BIC)
"""
Bayesian information criterion (BIC)
    It is used to compare regression models.
    It balances model fit vs model complexity
    The formula:
        BIC = kln(n) - 2ln(L)
        k = number of estimated parameters
        n = number of observations
        L = likelihood of the fitted model
    Example:
        | Model   | Features                       |  BIC |
        | Model A | area                           | 1300 |
        | Model B | area + age                     | 1220 |
        | Model C | area + age + 12 other features | 1250 |
        BIC prefers Model B

    AIC vs BIC
        AIC -> AIC = 2k - 2ln(L)
        BIC -> BIC = kln(n) - 2ln(L)

        Both have -2ln(L) which represents model fit

        Complexity penalty is different:
            AIC: 2k
            BIC: kln(n)
            So BIC penalizes additional parameters more strongly than AIC.
        BIC usualy favors simpler models than more stronyly than AIC.
"""

# Overfitting
"""
Overfitting:
    The model fits the training data very well, including random noise and acidental patterns, but performs poorly on new unseen data.
    Why does verfitting happens:
        1. Too many festures
        2. Unnecessary predictors
        3. Very complex polynomial terms
        4. a samll training dataset
        5. feature selection performed using all the data
        6. noisy feautres
        7. multicollinearity and unstable coefficients 
    
    Detection:
        Comparing model perforamnce on training data | validation data/test data 
        Example:
            | Metric |  Train |   Test |
            | (R^2)  |   0.94 |   0.61 |
            | RMSE   | 10,000 | 32,000 |
            this large gap suggests overfitting

            | Metric |  Train |   Test |
            | (R^2)  |   0.78 |   0.75 |
            | RMSE   | 21,000 | 23,000 |
            this looks much healthier

    Treatment methods
        remove unnecessary features,
        use feature selection,
        reduce polynomial degree,
        collect more data,
        use cross-validation,
        use regularization such as Ridge or Lasso,
        reduce model complexity,
        avoid tuning decisions based directly on the test set.
"""
 
# Bias Vairance tradeoff
"""
Bias 
    The systematic error caused by a model being too simple or making assumptions that prevent it from capturing the tre pattern in the data.
    Example:
        The relationship: Y = X²
        Trained model: Y_hat = β₀ + β₁X₁ | it is a just straight , it can properly represent the curve.
        collecting a lots of data will not imporve model, it continues making similar mistakes, because structure is wrong
        this is high bias
    
    Another example:
        Apartment price prediction
        Price depends on: [area, neighborhood, age ...]
        Trained model: price_hat = β₀ + β₁(area)
        THis models can not capture many complex and required patterns, so it consistenly underestimares apartments' prices
            Actual     Prediction
            $200k      $170k
            $250k      $210k
            $300k      $245k
            $350k      $280k
        This is Bias
    
    High Bias
        a model has high bias when it is too restrictive to capture the underlying relationship
        Signs:
            model is too simple
            important features are missing
            nonlinear relationships are represented as linear
            both training and test perforamnce are poor.
        example:
            R²test = 0.35
            R²train = 0.33
        THis model can capture well training data itself.
        High Bias = underfitting

    Low Bias 
        The model is flexible enough to capture the underlying pattern fairly well.
        Suppose the true relationship is nonlinear, and istead of a stringt line you use an appropriate polynomial model.
        Extremely low bias can come from making a model so flexible that it starts fitting noise.
        Extremely low bias leads to high variance.

    Example:
        you are tring to hit the center of a target with arrows
        High Bias
            your arrows consistently land to left.
        Low Bias 
            The average location of the arrows is near the center.
    
    Simple model -> Higher bias
    More flexible model -> Lower bias

Variance 
    How much the trained model change if we would train it on different samples from the same population

    Low Variance:
        Sample 1 → β_area = 3000
        Sample 2 → β_area = 2950
        Sample 3 → β_area = 3050
        Sample 4 → β_area = 2980
        Low Variance = Stable model

    High Variance 
        Sample 1 → β_area = 500
        Sample 2 → β_area = 4200
        Sample 3 → β_area = -1000
        Sample 4 → β_area = 6500
        High Variance = Unstable model

    Why does High Variance happen ?
        THe mode is too flexible and starts learning details specific to the training sample, including noise.
        a very complicated model:  Ŷ = β₀ + β₁X + β₂X² + ... + β₁₅X¹⁵
        It fits one training data extremely well, but slightly chane the observations can couse a lot of effect.
        THis is High Variance, High Variance - Overfitting

    High Bias and Low Bias can happen at the same time in a model
    High Variance and Low Bias can happen at the same time in a model

    | Situation         | Training performance                 | Validation/Test performance        | Train-test gap               |
    | **High Bias**     | Poor                                 | Poor                               | Usually small                |
    | **Low Bias**      | Good                                 | Usually good or very good on train | Not determined by bias alone |
    | **High Variance** | Very good                            | Much worse                         | Large                        |
    | **Low Variance**  | Similar across train/test and splits | Similar                            | Small                        |

    example:
        High Bias
            R²train = 0.40 
            R²test = 0.37

        Low Bias
            R² = 0.92 
            checking only training performance is enough 
        
        High Variance
            R²train = 0.90
            R²test = 0.65

        Low Variance 
            R²train = 0.82
            R²test = 0.80 
        
        High Bias and Low Variance 
            R²train = 0.35
            R²test = 0.34
        
        Low Bias and High Variance 
            R²train = 0.90
            R²test = 0.60
        
        Low Bias and Low Variance 
            R²train = 0.95
            R²test = 0.93

Bias Variance Tradeoff
    Bias - Variance Tradeoff = finding the balance that generalizes best to unseen data

"""
