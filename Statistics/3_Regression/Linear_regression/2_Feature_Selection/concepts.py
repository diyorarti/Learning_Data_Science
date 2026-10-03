# Content table
"""
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