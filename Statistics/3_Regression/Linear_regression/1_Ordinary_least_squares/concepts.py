"""
Ordinary Least Squares

Ordinary least squares Assumptions:
    Linearuty
    Independenc of errors
    Homoscedasticity
    Normality of errors
    Absence of severe multicollinearity

    Residual analysis
    Cook's distance
    Variance inflation factor (VIF)

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
            Means the relationship between the independet variables(target variables) and the dependent variable(feautes). 
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

        3. Homoscedasticity -> measures how Residuals have approximately constant spread
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
                        
        4. Normality of errors
            Measures the distribution of erros
            Detection methods:
                1. Histogram
                2. Q-Q plot
                3. Skewness
                4. Kurtosis
                5. Jarque-Bera test or Shapiro-Wilk test

        5. Absence of severe multicollinearity 
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
    NOTE: The acutal target is not included.        
"""
 