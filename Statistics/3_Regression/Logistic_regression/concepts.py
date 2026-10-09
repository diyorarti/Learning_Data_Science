# Logistic Regression
"""
1.Logistic Regression Model Overview

2.Relationship to the Sigmoid Function

3.Assumptions of Logistic Regression
   3.1 Linearity of independent variables and log-odds
   3.2 Independence of observations
   3.3 Absence of multicollinearity
   3.4 Large sample size

4.Evaluating Model Performance
   4.1 True Positive (TP) 
   4.2 False Positive (FP)
   4.3 True Negative (TN)
   4.4 False Negative (FN)

   4.5 Metrics for Model Evaluation
       - Accuracy 
       - Balanced Accuracy  
       - Precision 
       - Recall
       - F1-score
  
5.Common Pitfalls & How to Avoid Them
   5.1 Overfitting 
   5.2 Misinterpreting coefficients
   5.3 Imbalanced dataset
"""

# Logistic Regression Model Overview
"""
The main purpose of Logistic Regression is to model a binary target variable
    Binary means target has two possible values: Y ∈ {0,1}
    For example:
        | Problem             | (Y=1  )  | (Y=0)            |
        | Customer conversion | Converts | Does not convert |
        | Spam detection      | Spam     | Not spam         |
        | Fraud detection     | Fraud    | Not fraud        |
        | Disease diagnosis   | Disease  | No disease       |

    Logistic Regression Model Formula:
        p = 1 / (1 + np.exp(-(β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ))
        Here:
            X₁ X₂ ... Xₙ = features
            β₀ = intercept
            β₁, β₂ ... βₙ = coefficients 
            p = probability 

        Convertion:
            odds = p / (1 - p)
            Log-odds = np.log(p / (1 - p))

    What is p ?
        p means: p = P(Y = 1 | X) -> the probability that Y=1, given the customer's features X.
        Example:
            p = 0.8 means: the model estimates 80% probability that this customer belongs to class 1.

    What is odds ?
        odds is p / (1 - p)
        example:
            p = 0.8  
            odds = 0.8 / (1 - 0.8) = 0.8 / 0.2 = 4
            odds=4/1 means the event is 4 times as likely to happen as not happen
        another example:
            p = 0.5
            odds = 0.5 / (1 - 0.5) = 0.5 / 0.5 = 1
            odds=1/1 means the event and non-event are equally likely
        another example:
            p = 0.2
            odds = 0.2 / (1 - 0.2) = 0.2 / 0.8 = 0.25
            odds=1/4 means the event is much less likely than the non-event

    What is log-odds (or logit)?
        Log-odds is the output of the linear part of the logistic regression model.
        log(odds) log(p / (1 - p)) is log-odds
        example:
            p = 0.8
            odds = p / (1 - 0.8) = 0.8 / 0.2 = 4
            log-odds = log(odds) = 1.386
        
        another example:
            p = 0.5
            odds = 1
            log-odds = 0
        
        another example:
            p = 0.2
            odds = 0.25
            log-odds = -1.386
        
    Very Important Pattern
        p < 0.5 -> log-odds < 0
        p = 0.5 -> log-odds = 0
        p > 0.5 -> log-odds > 0 
    
    Complete example:
        x = 5
        β₀ = -3 
        β₁ = 0.8
        log-odds = β₀ + β₁X₁ = -3 + 0.8 * 5 = 1
        odds = np.exp(log-odds) = 2.718
        p = odds / (1 + odds) = 0.731
        There is about a 73.1% estimated probability that the event happens.
""" 

# Relationship to the Sigmoid Function
"""
Sigmoid function
    Logistic Regression first creates a linear score (log-odds=β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ)
    log-odds can be any number −∞ < log-odds < ∞
    But probability must always be : 0 < p < 1
    This is the sigmoid function that converts linear score to probability
    Formula: 
        σ(z) = 1 / (1 + e⁻ᶻ)
    Important Pattern:
        | Log-odds (z)   | Sigmoid probability |
        |             -5 |               0.007 |
        |             -2 |               0.119 |
        |             -1 |               0.269 |
        |          **0** |           **0.500** |
        |              1 |               0.731 |
        |              2 |               0.881 |
        |              5 |               0.993 |
        z<0 ⇒ p<0.5
        z=0 ⇒ p=0.5 
        z>0 ⇒ p>0.5

    Midpoint behavior 
        The midpoint happens when log-odds = 0 
        p = 1 / (1 + np.exp(-log_odds)) = 0.5
        It means the model is exaclty in the middle
        The midpoint of the sigmoid function occurs when the log-odds equal zero, 
        which corresponds to a probability of 0.5. At this point, the model is essentially 
        uncertain about the outcome—it's equally likely to predict either class (0 or 1). 
        The curve around this point is steep, meaning that small changes in the log-odds lead 
        to rapid changes in predicted probability. 
        This steep transition ensures that cases near the decision boundary 
        (e.g., whether a user converts or not) are very sensitive to small shifts in input values.

    Closer to the extremes
        As the log-odds increase far above 0 or fall far below 0, the sigmoid function flattens out. 
        This means that for very high positive or negative log-odds, the predicted probabilities approach 1 or 0, 
        respectively, but they do so slowly. As the probability nears 0 or 1, the model becomes more confident in 
        its prediction, and additional changes in the predictors have diminishing effects on the probability.

"""
 
# Linearity of independent variables and log-odds
""" 
Assumptions are conditions we expect the data and the relationship between variables to satisfy so that the model's 
coefficients, probabilities and statistical conclusions are reliable.

General Workflow:
    1.Selecting quantitive predictors and plotting each of the features and empirical log-odds
    2.Interpreting the plots and decide what to do next.
        1.if Aprroximately straight line relationship. Keep the feature as it is.
        2.if the relationship is Simple U, inverted-U or simple curve. Apply Polynomial term
        3.if the relationship is more complicated smooth curve. Apply Spline/GAM
    3.When we can't decide that whether a features has linear relationship or not. Apply Box-Tidwell statistical method
        1.if the evidence is significant. Invistigate shape with Ploynomial/Spline/GAM
    4.Partial-Effect Plot is used to check what is the shape of fitted model assigning to this feature.

1.Linearity of Independent Variables and Log-Odds
    Independet variables have a linear relationship with the log-odds of the dependent variable.
    Logistic Regression deesn't assume that X has a linear relationship with the probability p.
    IT assumes that X has a linear relationship with the log-odds.
    
    X has a linear relationship with log-odds, not with probability:
        |     X | Log-odds | Probability |
        |     0 |     -3.0 |       0.047 |
        |     1 |     -2.2 |       0.100 |
        |     2 |     -1.4 |       0.198 |
        |     3 |     -0.6 |       0.354 |
        |     4 |      0.2 |       0.550 |
        |     5 |      1.0 |       0.731 | 
        a one-unit increase in X increases the log-odds by 0.8
        But the probability changes are not constant

    Why does LR require linearity ?
        log-odds = β₀ + β₁X₁ 
        this equation says: each one-unit increase in X changes the log-odds by the same amount β₁.
        If the true relationship is very curved, then one single coefficient β₁ may not describe it properly.
        For example:
            low X       → low risk
            medium X    → high risk
            very high X → low risk again
    
    Testing methods:
        1. empirical log-odds plots
            Implementation steps:
                1.Divide the quantitative feature into bins
                2.Within each bin, calculate:
                    a repsentative feature value, usually the mean of the feature
                    the mean of the binary target
                3.Convert that probability into empirical log-odds
                4.Plot representative feature value vs empirical log-odds

        2. Box-Tidwell tests       

        3. spline plots / GAM-style smooths:
            Ordinary Logistic Regression fits a straight-line 
                log-odds = β₀ + β₁X₁ 
                log-odds    |                  *
                            |              *
                            |          *
                            |      *
                            |  *
                            +------------------------> age
            But the reality relationship may be curved
                log-odds
                    |          *  *
                    |       *        *
                    |    *
                    |                  *
                    | *
                    +------------------------> age
            In this case, we need the relationship bended
            Spline and GAMs allows the fitting relationship to be curved.
                log-odds = β₀ + s(age)
            How does Spline create the curve ?
                Instead of fitting one stright line accross all data, Spline devides the data into several regions
                the feature: knots
                For example:
                    feature = age
                    knots = 4 
                    Spline may devide like this:
                        18-30   → increasing line
                        30-45   → increasing faster line
                        45-60   → almost flat line
                        60-75   → decreasing line
                        
            What is GAM ?
                GAM means Generalized Additive Model
                Ordinary Logistic Regression with multiple features: logit(p) = β₀ + β₁age + β₂income + β₃visits
                In Ordinary Logistic Regression, each feature is forced to have a stright-line on log-odds
                A GAM does: logit(p) = β₀ + s₁(age) + s₂(income) + s₃(visits)
                Now each feature can have its own smooth curve.
                For example:
                    age      → inverted U
                    income   → increasing then flattening
                    visits   → increasing
            Spline VS GAM:
                A Spline is the smooth mathematical function used to model a curved relatinship 
                A GAM is a model that can combine several smooth functions

        4. polynomial terms
            Polynomial term make the relationship between the feature and the log-odds nonlinear.
            For example:
                log-odds(p) = β₀ + β₁age -> fitts a straight-line relationship
                log-odds(p) = β₀ + β₁age + β₂age² -> the Polynomial term allows the relationship to be curved.
                When nonlinear shape is simple we use Polynomial term, when it is complexer we use Spline

        5. partial-effect plots:
            What relationship did the fitted model actually learn from each predictor ?
            This is not primarily used to discover the linearity assumption from scratch. They are more of a post-fit 
            diagnostic and interpretation tool.

            Partial-effect implementation is different in different predictors.
                1.Straigt line relationship
                2.Polynomial term applied predictor
                3.Spline applied predictor
                4.GAM applied predictor
                
            Suppose we have features: age, income, session_minutes
            logit(p) = β₀ + β₁age + β₂income + β₃session
            Now we specifically want to understand:
                What effect does age have on the model prediction, separately from income and session_minutes
            THis is the main idea of partial-effect plots

            A partial-effect plot isolates one feature
                Conseptually wo do something like this for age
                age     income     session
                20      5000       15
                25      5000       15
                30      5000       15
                35      5000       15
                40      5000       15
                ...
                70      5000       15
                age changes 
                income stays fixed 
                session stays fixed
                Then, making predictions with the new data(age original values and income, session with values fixed)
                according to this fitter model, what happens when age changes while the other predictors are controlled ?

        6. residual diagnostics 
            Residual means: How different was the observed restult from what the model expected ? 
            In Linear Regression: Residual = y - ŷ. example: e = 100 - 90 = 10
            Simplest Logistic Regression residual: e = y - p̂. Example: e = 1 - 0.8 = 0.2

            What does this have to do with linearity ?
                suppose we fit: logit(p) = β₀ + β₁age
                so model assumes that age has a straight-line relationship with log-odds
                But the real relationship is:
                    young age     → low purchase tendency
                    middle age    → high purchase tendency
                    older age     → low purchase tendency
                    So true relationship is an inverted U shape.
                So the model systematically makes mistakes
                    | Age region | What may happen     |
                    | Young      | model overpredicts  |
                    | Middle     | model underpredicts |
                    | Old        | model overpredicts  |
                Then, the residuals may show a pattern like this:
                Residual 
                            | *                         *
                            |   *                     *
                            0 |------*---------------*---------> Age
                            |        *           *
                            |           *  *  *
            How a good residual plot look like:
                Residual 
                            |   *      *       *
                            |      *       *
                            0 |-----------------------------> Age
                            | *       *        *
                            |      *      *
            Two common types of residuals in Logistic Regression:
                Pearson residuals:
                    rᵢ = (yᵢ - p̂ᵢ) / √(p̂ᵢ(1 - p̂ᵢ))
                Deviance residuals:
"""

# Independence of observations
""" 
Each observation(row) in the dataset should provide independent information, one observation shouldn't be direcly dependent on another one.
    For example:
        | Customer | Month | Purchased |
        | A        | Jan   |         1 |
        | A        | Feb   |         1 |
        | A        | Mar   |         0 |
        These three rows are not fully independent because they all belong to the same customer.

    Why is this problem ?
        SLG assumes each row contributes independent evidence to the likelihood.
        THis cause to:
            underestimated standard errors
            overly small p-values
            confidence intervals that are too narrow
            misleading coefficient significance
    
    Detection methods
        1.Check for repeated entities / duplicated IDs
            Example:
                customer_id   month   visits   spend   churn
                C1042         Jan       5       300      0
                C1042         Apr       1        50      1
                C1042         May       0         0      1
                this is not a mistake in the data. The reason for duplication is repeated measurement over time
            so duplication doesn't mean duplicated ids, it is about duplicated rows, 
            all values of a row is the same with one ore more than one other rows

            Cases of duplications:
                1. Exact duplicated rows
                    customer_id   age   income   churn
                    C001          30    5000      0
                    C001          30    5000      0
                    Treatment: Droping duplicated rows

                2. Some duplicated columns:
                    customer_id   month   income   churn
                    C001          Jan     5000      0
                    C001          Jan     5200      0
                
                3. Repeated entity, but legitimate different observations - same ID, different observations
                    customer_id   month   income   churn
                    C001          Jan     5000      0
                    C001          Feb     5100      0
                    C001          Mar     5200      1

            Treamtent:
                Aggregation 
                When to use?
                    Aggregation is useful when multiple rows are legitimate observations at a lower level, 
                    but model needs one observation at a higher level. For example, we want to predict monthly customer churn.
                    Desired unit: 1 row = 1 customer in 1 month
                    but data may look like this:
                    customer_id   month   purchase_amount   visits   churn
                    C001          Jan          100             1       0
                    C001          Jan          250             2       0
                    C001          Jan           50             1       0
                    C002          Jan          400             3       1

        2.Check for natural groups or clusters
            Natural cluster or Natural groups: different people belong to the same group
            customer_id   branch_id   age   churn
            C001          B01         25      0
            C002          B01         44      1
            C003          B01         32      0
            C004          B02         51      1
            C005          B02         39      1
            here all customers are unique, but customers belong to the same branches.
            B01 → C001, C002, C003
            B02 → C004, C005
            customers from one group/brach/team/ share several the same information. For example:
                same local management
                same promotions
                same service quality
                sam geographic area
            For treating understanding the data is very important.
            Methods:
                1. Cluster-robutest standard errors
                2. Mixed-effect Logistic Regression
                3. GEE
                4. Group-aware training/test splitting

        3.Check time dependence / autocorrelation
            This method is relevent when observations have a meaningful time order.
            Suppose we are predicting customer churn every month.
            customer_id   month   churn:
            C001          Jan       0
            C001          Feb       0
            C001          Mar       1
            C001          Apr       1
            These rows may not be independent because February comes after January, March comes after February.
            The main idea: an observation at time t may be related to an observation at t-1.
            This relationship is called autocorrelation or serial correlation.
            Mathematically, lag-1 autocrrelation asks about 
                Corr(rt, rt-1)
                rt = residual at the current time
                rt-1 = residual from the previous time
 
        4.Inspect residual dependence 
            Here the main idea: After fitting Logistic Regression, are the remaining errors related across observations ? 


        5.Check for spatial dependence
"""
  
# Absence of multicollinearity
"""
The independent varianles should not be too strongly linearly related to each other.
    log-odds = β₀ + β₁X₁ + β₂X₂ + β₃X₃ 
        X₁ = monthly income                                                              
        X₂ = annual income
        X₃ = number of website visits
    here: monthly income and annual income contain the same information.
    THis is multcollinearity.
    Logistic Regression model tries to estimate indivindual effect of each predictor features.
    But if two features have the same information, the model has difficulty how effect should I assign to first and how much to second ?

    A pairwise correlation alone doesn't detect every type of multicollinearity. A variable can be strongly explained by a combination of 
    several other predictors even no single pairwise correlation is extremely high.

    Detection Methods
        1.Correlation Heatmap plot
            Checking any pair of numeric predictor features has a very strong linear relationship.
            Correlation method is mainly a screening method. it tells " these prodictors may be causing a multicollinearity problem.
            It does't tell there is 100% multicollinearity probme and which treatment method should be applied

        2. Variance inflation factor (VIF)
            Mearues: how much variance of a regression coefficients is increased beause the feature is linearly related to the other predictor variables.
            In Simple: VIF checks whether a feature contains enough unique information, or most of it's information is already contained in others
            VIF is diagnostic measure used to detect multicollinearity among the predictors in a regression model.
            VIF can be used for both continuous and dicrease value features.
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

        4. Condition number and condition index
        5. Eigenvalues / singular values / matrix rank
        6. Coefficient instability

    Treatment Methods 
        1. Remove one of the redundant features
        2. Combine strongly related features
        3. Use Ridge Regression / Lasso Regression / Elastic Net
        4. PCA - Principal Component Analysis 
"""

# Large sample size
"""
Logistic Regression needs enough observations - especially enough observations of both classes - to estimate it's coefficients reliably.
    Example:
        A = dataset
        Total transactions = 100
            Fraud = 3
            Not Fraud = 97
            the Model has very little information about Y = 1 (Fraud)

        B = dataset
        Total transactions = 10,000
            Fraud = 800
            Not Fraud = 9,200
            Now the model has enough observations for both class to learn

    Number of predictors also matter
        Situation 1
            10,000 - observations
            3 - predictors
            usualy plenty of information
        Situation 2
            100 - observations
            40 - predictors
            much more problematic
        Conceptually:
            More predictors -> More data required

    Checking the data:
        1.Total number of observations: N
            more observations generally give the model more information. But there is no universal rule, such as 1000 records is enough.

        2.Number of observations in each outcome class:
            Total: 1000
            Class 1: 980
            Class 0: 20
            This can be problematic because the model has only 20 observations from the minority class to learn from.

        3.Number of estimated parameters relative to available events.
            100 observations with 40 model parameters is problematic. 
            Don't count as parameter:
                Dummy variables
                polynomial terms
                spline basis functions
                interaction terms
                categorical levels
"""

# Evaluating Model Performance
"""
True Positive TP: Model correcly predicts the positive class. Example, predicting a user will convert (1) | when they actually do convert (1)
True Negative TN: Model correcly predicts the negative class. Example, predicting a user willn't convert (0) | when they acutally don't convert (0)
False Positive FP: Model incorrectly predicts the positive class. Example, predicting a user will convert (1) | when they acutally don't convert (0)
False Negative FN: Model incorrectly predicts the negative class. Example, predicting a user willn't convert (0) | when they actually do convert (1)

Confusion Matrix:
    TP = sum( (y_pred == 1) & (y_test == 1) )
    TN = sum( (y_pred == 0) & (y_test == 0) )
    FP = sum( (y_pred == 1) & (y_test == 0) )
    FN = sum( (y_pred == 0) & (y_test == 1) )

Metrics for model evaluation:
    Accuracy = (TP + TN) / (TP + TN + FP + FN)
        Accuracy is useful when the classes are reasonably balanced and mistakes in both classes matter similarly.
            For example:
                Class 0 = 52%
                Class 1 = 48%
            Problematic Case:
                Not fraud = 990
                Farud = 10
                Suppose model predicts all transactions not fraud
                Accuracy = 990 / 1000 = 0.99 = 99% 
                This sounds excellent but the model detected 0 frauds

        Accuracy and Error Rate
            Error rate = 1 - accuracy 
            Example:    
                accuarcy = 0.78
                error = 1 - 0.78 = 0.22
                Accuarcy = 78%
                error = 22% 

    Balanced Accuracy = 1/2 * (TP / (TP + FN) + TN / (TN + FP))
        How well does the model correctly indentify both the positive class and the negative class, giving equal importance to each ?
        Example:
            Negative class = 990
            Positive class = 10
            Model predictions:
                TN = 990
                TP = 0
                FN = 10
                FP = 0
            Accuracy = (990 + 0) / (990 + 0 + 10 + 0) = 990 / 1000 = 99%
            Balanced arruracy = 1 / 2 * (TP / (TP + FN) + TN / (TN + FP)) = 1 / 2 * (0 / (0 + 10) + (990 / (990 / 0))) = 0.5 * (0 + 1) = 0.5 = 0.5

    Precision = TP / (TP + FP) 
        Out of all observations the model predicted as positive, how many were actually positive ?
        Precision focuses only on the cases where the model predicted y_hat = 1
        Example:
            the model predicts 50 transactions - Fraud
            40 are actually fraud -> TP = 40
            10 are actually not fraud -> FP = 10 
            Precision = TP / (TP + FP) = 40 / (10 + 40 ) = 0.8
            of all the transactions that the model labeled as fraud, 80% were actually fraudelent.
        Precision = When the model says Yes, how often is it correct ?

        another example:
            if the model says: "This patient has the disease" 
            Precision asks: "How often does the patient actually have the disease ? "

        Whent to use Precision ? 
            Precision is particularly important when False Positives are expensive or harmful ?
        
    Recall = TP / (TP + FN) 
        Out of all observations that were actually positive, how many did the model correctly indetify as positive.
        Recall focuses on on the actual positive class. 
        example:
            50 transactions are actually fraud
            the model:
                40 correctly are fraud = TP = 40
                10 incorrectly as not fraud = FN = 10
            Recal = 40 / (40 + 10) = 0.8
            THe model found 80% of all actual fraud cases.

        another example:
            Of all patients who actually have the disease, how many did the model identify?
        
        When is Recall important
            False negatives are costly or dangerous 

    F1-Score = 2 * ((Precision * Recall) / (Precision + Recall))
        F1-score answers that how well does the model balance Precision and Recall at the same time ?
        example:
            Precision = 0.80
            Recall = 0.60
            F1 = 2 * ((0.80 * 0.60 ) / (0.80 + 0.60)) = 2 * (0.48 / 1.4) = 2 * 0.34 ≈ 0.68
        
        Why not simply average Precision and Recall ?
            F1 uses the harmonic mean, not the ordinary arithmetic mean.
            F1 penalizes situations where one metric is much worse than the other
            example:
                Precision = 1.0
                Recall = 0.1
                Odirnary average = (1 + 0.1) / 2 = 0.55
                F1 = 2 * ((1 * 0.1) / (1 + 0.1)) = 0.18
""" 

# Common Pitfalls & How to Avoid Them
"""
Overfitting 
    Logistic Regression model learns the training data too closely, including noise and accidental pattern, 
    so it performs well on trainin data but worse on new unseen data

    How to detect overfitting ?
        the main way is to compare training and validation/test performance.

    How to avoid Overfitting:
        1. Feature Selection
        2. Regularization
        3. Reduce unnecessary model complexity
        4. Use cross-validation
        5. Collect more data
        6. Handle rare categories carefully

Misinterpreting coefficients
    log(1 / (1 - p)) = β₀ + β₁X₁
    β₁ = 0.8
    interpretation is :
        one-unit increase in X increases the log-odds of Y = 1 by 0.8, holding other variables constant
        β₁ -> changes in log-odds
        log-odds -> changes in probability
        example:
            X = number of website visits
            β₁ = 0.8
            For every additional website visit, the log-odds of purchase increase by 0.8
            e^0.8 ≈ 2.23 -> each additional visit multiplies the odds of purchase by about 2.23
        Positive Coefficient
            β > 0 -> e^β > 1
        Negative coefficient
            β < 0 -> e^β < 1

Imbalanced datasets
    an imbalanced dataset means two target classes are not represented in roughly similar proportions.
    For example:
        Y = 0 -> 9,500 customers -> 95% belong to class 0
        Y = 1 -> 500 customers  -> 5% belong to class 1

    Why is imbalanced a problem?
        Not fraud = 9,900
        Fraud = 100
        a completely useless model could predict: -> 10,000 transactions as not fraud
            Accuracy = 9,900 / 10,000 = 99%
            Recall = 0%

    Treatement methods:
        1. Class weight
        2. Oversampling the minority class
        3. Undersampling the majority class
        4. Change the classification threshold
        5. Collect more minority-class data
"""