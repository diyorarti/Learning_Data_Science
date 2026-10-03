"""
Data Transformation
│
├── Distribution transformations
│   ├── Logarithmic transformation
│   ├── Square-root transformation
│   └── Box-Cox transformation
│
└── Feature scaling
    ├── Z-score standardization
    └── Min-Max normalization

    Encoding Categorical variables:
        Ordinal
        Nominal
            Label Encoding
            One-Hot Encoding
            Dummy Encoding
"""

# Transformation
"""
Data Transformation
│
└── Distribution transformations
        ├── Logarithmic transformation
        ├── Square-root transformation 
        └── Box-Cox transformation

Distribution Transformation: 
    it is the process of applying a mathematical function to every value of a numerical variable to change how it's values are distributed.
    It changes an unsuitable distribution shape or relationship into a form that is easir for statistical methods or models to analyze. 
    it solves problems like: Skewness, Kurtosis (heavy tails)
    example: income = [ 1200, 1500, 1700, 2000, 2300, 2500, 50000]
        most observations are between 1200 and 2500, but one value is 50,000, this creates strongly right skewed
        A transformation can compress the high value and preduce a more balanced distribution (normal distribution is not guaranteed)
    Advantages:
        Stabilize variance
        Make relationships more linear
        Improve Residual behavior
        Improve Model Performance
    When do not apply Distribution Transformation:
        1. The distribution is already reasonably symmetric
        2. Relationship with the target is already linear
        3. Residuals is reasonably constant
        4. The model isn't affected by skewness
        5. using a tree-based model and already performing well.

    Logarithmic Transformation
            it is the processing of replacing each original value with it's logarithm
                Formula: X_log = log(x)
                it is mainly used for positive (right) skewed data

            Advantages:
                1. Reduce skewness
                2. Reduce influnce of large values
                3. Stabilize variance
                4. Make curved linearshio more linear
                5. Convert ratios into differences
            
            Types: 
                1. Natural Logarithm np.log(x) e≈2.718
                2. Base-10 Logarithm np.log10(x)
                3. Base-3 Logarithm np.log2(x)               
            
            Requirements to apply
                1. Positive values X>0 
                2. Stong postive(right) skewed
                2. Not symmetric feaure
                2. np.log1p(x) for 0 containing features, it calculates log(1+x)

    Square Root Transformation 
            Replacing every original value with it's square root
            Formula: x_sqrt = √x

            Advatages:
                1. Reduce skewness
                2. Stabilize variance
                3. Reduce influence of large values
                4. Improve linearity

            Requirements to apply:
                1. Non-negative values x≥0 
                2. Moderately or  Stong posistive skewed data

    Box Cox Transformation 
            Box-Cox is a family of power transformations that automatically estimates the lambda value for a strictly positive numerical feature. 
            Lambda determines the form and strength of the transformation.

            Formula:x^(λ) = {
                            (x^λ - 1) / λ,   λ ≠ 0
                            log(x),          λ = 0
                        }

            Meaning of Lambda:
                λ ≈ 1.0 → little or no shape transformation
                λ ≈ 0.5 → square-root-like transformation
                λ ≈ 0.0 → logarithmic transformation
                λ < 0.0 → reciprocal-like, stronger compression
                λ > 1.0 → power transformation that may reduce left skewness

            Advantages:
                1. Reduce skewness
                2. Make a distribution more symmetric
                3. Srabilize variance
                4. Reduce heteroscedasiticity
                5. Make data more suitable for statistical modeling
            
            Requirement:
                1. X > 0 All values must be strictly positive.
""" 

# Feature Scaling
"""
└── Feature scaling
    ├── Z-score standardization
    └── Min-Max normalization
    Scaling is the process of changing numerical variables so they have comparable numerical ranges or scales
    
    Types:
        Standardization (Z-score scaling): it is a feature-scaling method that transforms numerical values so that resulting feature has mean ≈ 0 std ≈ 1
            Formula: z = (x - μ) / std
                0	Exactly at the mean
                1	One standard deviation above the mean
                -1	One standard deviation below the mean
        
        Normalization: it is feature-scaling method that transforms numerical values into a fixed range (usualy between 0 and 1)
            Formula:  x = (x - x_min) / (x_max - x_min)
"""

# Encoding Categorical Variables
"""
Encoding 
    Encoding is the processing of converting categorical string values into numerical values
    So statistical methods and machine-learning models can use them

    Ordinal ecoding     
        Ordinal encoding converts ordered caregorical values into numerical codes while preserving their natural ranking.
            example: Low < Medium < High ---> 1 < 2 < 3
        
        When to use:
            1. The feature is categorical
            2. Its categories have a real natural order. Like: High school, Bachelor, Master, PHD
    
    Nominal encoding
        Nominal encoding is the process of converting unordered categorical values into a numerical values.
        example: cities = [Warsaw, Krakow, Gdansk, Katowice] -> unordered
        
        Label encoding:
            converting each category into a unique integer
            No -> 0 / Yes -> 1
            Rejected -> 0 / Pending -> 1 / Approaved -> 2
        
            When to use Label Encoding
                Binary features which only has two categories: Yes/No, True/False, Active/Inactive
                Any type of Target column ordered and unordered

        One-Hot encoding
            converting each category of nominal feature into a separate binary column 
            Example:
                | preferred_device | Mobile | Desktop | Tablet |
                | ---------------- | -----: | ------: | -----: |
                | Mobile           |      1 |       0 |      0 |
                | Desktop          |      0 |       1 |      0 |
                | Tablet           |      0 |       0 |      1 |

            When to use:
                The feature is categorical
                it is used as input feature X
                no natural order
                number of categories is relatively small
            there is a problem of multicollinerity
        
        Dummy Encoding
            converting a nominal categorical feature into binary colummns, but remove one category and treats it as the reference category.
            This solves the problem of multicollinearity that happens with One-Hot encoding.

            example: Mobile is the referece category.
                | preferred_device | Desktop | Tablet |
                | ---------------- | ------: | -----: |
                | Mobile           |       0 |      0 |
                | Desktop          |       1 |      0 |
                | Tablet           |       0 |      1 |
"""