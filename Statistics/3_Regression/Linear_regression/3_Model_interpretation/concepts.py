"""
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