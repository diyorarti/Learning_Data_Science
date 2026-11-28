
# Coursera 
"""
Linear Regression Part 1 (1)
Linear Regression Part 2 (2)
    Linear Regression is a supervised learning algorithm usef for Regression tasks
        Regression means predicting a conituous numerical values
            - hourse price
            - salary
            - temperature

    The main idea of Linear Regression Algorithm:
        Find the best stright line that describes the relationship between input features and the target value

    For one Feature:
        f(x)=wx+b
            x = input feature
            w = weight / slope /coefccient
            b = bias / intercept
            f(x) = pridected value

Cost Function Formula (3)
Cost Function Intuition (4)
Visualizing Cost Function (5)
Visualization examples of Cost Function (6)
    THe model makes predictions, but thoses predictions are not always correct. So we need a way to measure: How wrong is the model ?
        This is called the "Cost Function " 
        For Linear Regression the most common used cost function is Mean Sqaured Error:
            J(w, b) = 1/(2m) * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)²
                m = number of training examples
                ŷ = predicted value
                y = actual value
                ŷ - y = error
                Squared for punishing or penalizing large mistakes strongly

Gradient Descent (7)
Implementing Gradient Descent (8)
Gradient Descent Intuition (9)
    Gradient Descent is an optimization algorithm. It's jobs is to find the best values of parameters (w and b)
    The idea:
        Start with random or zero values for w and b, then slowly update them to reduce the cost.
        Imagine you are standing on a mountain and want to go down to the lowest point. You look at the slope and take small steps downward.
        That is Gradient Descent 
        THe update rule:
            parameters = parameters - learning_rate * gradient 
        
        Gradient Descent Formula:
            w := w - α * ∂ / ∂w * J(w, b)
            b := b - α * ∂ / ∂b * J(w, b)
        Where: 
            α = learning rate
            ∂ / ∂w * J(w, B) = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾) * x⁽ⁱ⁾
            ∂ / ∂b * J(w, b) = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)
 
        Derivative:
            ∂J(w, b)/∂w = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)x⁽ⁱ⁾
            ∂J(w, b)/∂b = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)

Learning_rate(10)
    The Learning_rate constrols how big each step is during Gradient Descent
    it is usually writtent as -- α
    if learning_rate is too small --> Gradeint Descent becomes very slow
    if learning_rate is too large --> GRadient Descent may jump over the minimum and fail to converge

NOTE: To solve many local minimums problem, we use Squared error Cost Function, because it has bowl-shape, so it always has one global minimum

Gradient descent For Linear Regression (11)
    Linear Regression:
        ŷ = wx + b
    Cost Function:
        J(w, b) = 1/(2m) * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)²
    Gradient Descent:
        w := w - α * ∂ / ∂w * J(w, b)
        b := b - α * ∂ / ∂b * J(w, b)
    Derivative:
        ∂J(w, b)/∂w = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)x⁽ⁱ⁾
        ∂J(w, b)/∂b = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)

    Repeat this process for n_iterations time, to find values of w and b with min J(w,b)

Running Gradient Descent (12)
Multiple Features (13)

Vectorization part 1 (14)
Vectorization part 2 (15)
    Vectorization means replacing loops with matrix operations
        instead of writing: 
            for i in range(m):
                y_pred[i] = weights[0] * X[i][0] + weights[1] * X[i][1] + bias
        we write:
            y_pred = np.dot(X, weights) + bias
        Vectorization:
            - fast
            - clean code
            - easier to scale
            - use NumPy efficiently

Gradient Descent For Multiple Linear Regression (16)
    In real world, we usually have more than one feature
    example:
        House price prediction:
            - size
            - number of rooms
            - location score
            - age of house
        ŷ = Xw + b
            X = feature matrix
            w = weight vector
            b = bias
            ŷ = predictions

Feature Scaling (17)
Feature Scaling (18)
    Feature Scaling means putting features into a similar range
        for example without scaling:
            size: 50, 100, 200
            rooms: 1, 2, 3
            price: target
        The size feature has much larger numbers than rooms.
        THis can make gradient desceent slow becaue the cost function shape becomes stretech. 
        Feature scaling helps Gradient Descent converge faster
    Common Methods:
        1. Max Normalization:
            X_scaled = X / X_max

        2. Normalization (MinMax Normalization):
            X_scaled = (X- X_min) / (X_max - X_min)

        3. Mean Normalization:
            X_scaled = (X - Mean) / (X_max - X_min)

        4. Standardization(Z-score):
            X_scaled = (X- mean) / standard_deviation 
        
Checking Gradient Descent for Convergence (19)
    Convergence means:
        The cost function stops decreasing significantly
        During training , you should store the cost at every interion:
            Iteration 1: cost = 500
            Iteration 2: cost = 400
            Iteration 3: cost = 320
            Iteration 4: cost = 280
            ...
            Iteration 1000: cost = 12.3
        Cost decreases smoothly.

        Bad Signs:
            Cost increases.
            Cost becomes NaN.
            Cost jumps up and down. 
            Cost does not change at all.

Choosing Learning Rate (20):
    Choosing lthe learning rate is very important 
    Common value to try:
        0.1
        0.03
        0.01
        0.003
        0.001
        0.0003
        0.0001
    If cost decreases slowly, increase learning rate  0.0001 - 0.001 - 0.01 ...
    IF cost increases or becomes unstable, decrease learning rate  - 0.1 → 0.01

Feature Engineering (21)
    Feature Engineering means creating new better input features to help the model make better predictions
    For example:
        size
        number_of_rooms
    After Feature Engineering:
        price_per_room
        size_per_room
        house_age
        is_new_house
        distance_to_center

Polynomial Regression (22)
    Sometimes the relationship between X and y is not a stright line
    for example:
        Experience vs Salary
        maybe salary grows slowly at first, then faster later
        A simple linear model may not fit well
        Polynomial Regression solves this by creating polynomial features
            ŷ⁽ⁱ⁾ = w₁x⁽ⁱ⁾ + w₂(x⁽ⁱ⁾)² + w₃(x⁽ⁱ⁾)³ + ... + wₙ(x⁽ⁱ⁾)ⁿ + b
"""



# Exponent
"""
Training Methods:
    1. Batch Gradient Descent
    2. Mini-batch Gradient Descent
    3. Stochastic Gradient Descent

Cost functions:
    1. Squared loss
    2. Absolute loss
    3. Huber loss 

Evaluation metrics:
    1. R2-score
    2. Adjusted R2-score
    3. Akaike Information Criterion (AIC)
    4. Bayesian Information Criterion (BIC)

Polynomical Features

Regularizations:
    1. L1 Regularization (Lasso Regression)
    2. L2 Regularization (Ridge Regression)
    3. L1+L2 Elastic Net

Requirements
    1. Linearity
    2. Normality of residuals
    3. Non-Collinearity
    4. Homoscedasticity
    5. Similar scales
    6. Independence

Limitions:

Common questions:
"""

# Training Methods
"""
Gradient Descent is an iterative optimization algorithm used to find the model parameters (β₀, β₁, ..., βₚ)
that minimize a loss function. Unlike solving OLS directly using matrix algebra, Gradient Descent starts 
with initial coefficients and repeatedly updates them.

Batch Gradient Descent:
    Batch Gradient Descent is an iterative optimzation algorithm that uses the entire training dataset to caculate the gradient 
    before updating the Linear regression model's coefficients.

    mathematically:
        Gradient Descent Formula:
            w := w - α * ∂ / ∂w * J(w, b)
            b := b - α * ∂ / ∂b * J(w, b)
        Where: 
            α = learning rate
            ∂ / ∂w * J(w, b): Derivative  for w
            ∂ / ∂b * J(w, b):  Derivative for b
    
        Derivative:            
            ∂ / ∂w * J(w, B) = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾) * x⁽ⁱ⁾
            ∂ / ∂b * J(w, b) = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)

        Const Function:
            J(w, b) = 1/(2m) * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)²: Cost function

    Advantages:
        1. Uses the exact full-dataset gradient rather than a sampled approximation
        2. stable and reproducible for fixed data, initialization, and learning rate
        3. easy to implement using vectorized NumPy operations
        4. For Linear Regression with MSE, optimizes a convex objective

    Disadvantages:
        1. Each update requires processing the entire dataset.
        2. Can be expensive when the dataset is extremely large.
        3. A poorly chosen learning rate can cause slow convergence or divergence.

Mini-batch Gradient Descent
    Mini-Batch Gradient Descent is an iterative optimization algorithm that divides the training dataset into 
    small batches and calculates the gradient using one batch at a time before updating the model's coefficients.

    How Mini-Batch Gradient Descent works:
        Training observations: m = 1000
        Batch size: B = 100
        Epochs: 10
        Updates per epoch: m / B = 1000 / 100 = 10 updates per epoch
        Total updates: 10 * 10 = 100 

        mathematical implemenation the same:
            Gradient Descent Formula:
                w := w - α * ∂ / ∂w * J(w, b)
                b := b - α * ∂ / ∂b * J(w, b)
            Where: 
                α = learning rate
                ∂ / ∂w * J(w, b): Derivative  for w
                ∂ / ∂b * J(w, b):  Derivative for b
        
            Derivative:            
                ∂ / ∂w * J(w, B) = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾) * x⁽ⁱ⁾
                ∂ / ∂b * J(w, b) = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)

            Const Function:
                J(w, b) = 1/(2m) * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)²: Cost function
    Advantages
        1. More frequent parameter updates than Batch Gradient Descent.
        2. Requires less memory per gradient calculation.
        3. Supports efficient vectorized and parallel computation.
        4. Often offers a good balance between training speed and gradient stability.
        5. Suitable for large-scale ML and deep learning.

    Disadvantages
        1. Gradients are noisier than full-batch gradients.
        2. Requires choosing a batch size.
        3. Loss can fluctuate between updates.
        4. Still requires tuning the learning rate.
        5. Very small batches may underutilize hardware, while very large batches can require substantial memory.

Stochastic Gradient Descent
    Stochastic Gradient Descent (SGD) is an iterative optimization algorithm that uses one training 
    observation at a time to calculate the gradient and update the Linear Regression model's coefficients.

    How Stochastic Gradient Descent works:
        Training observations: m = 1000
        Batch size: B = 1
        Epochs: 10 
        Updates per epoch: m = 1000 updates per epoch
        Total updates: 1000 * 10 = 10000 

    mathematical implemenation the same:
        Gradient Descent Formula:
            w := w - α * ∂ / ∂w * J(w, b)
            b := b - α * ∂ / ∂b * J(w, b)
        Where: 
            α = learning rate
            ∂ / ∂w * J(w, b): Derivative  for w
            ∂ / ∂b * J(w, b):  Derivative for b
    
        Derivative:            
            ∂ / ∂w * J(w, B) = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾) * x⁽ⁱ⁾
            ∂ / ∂b * J(w, b) = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)

        Const Function:
            J(w, b) = 1/(2m) * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)²: Cost function
    
    Advantages
        1. Frequent coefficient updates: Updates parameters after each observation.
        2. Low memory requirements: Processes only one observation per update.
        3. Suitable for large datasets: Does not require calculating a full-dataset gradient before updating.
        4. Online learning: Can update models as new observations arrive.
        5. Computationally cheap individual updates: Each update uses only one sample.

    Disadvantages
        1. Noisy gradients: Individual observations produce gradients that differ from the full-dataset gradient.
        2. Unstable convergence path: The cost may fluctuate between updates.
        3. Learning rate sensitivity: An inappropriate learning rate can cause divergence.
        4. May oscillate near the optimum: Especially with a constant learning rate.
        5. Limited vectorization per update: One-observation updates may be inefficient on modern parallel hardware.
"""

# Cost functions
"""
Cost function measures how far the model's predictions are from the actual target values. 
During training, the model attempts to minimize this cost by adjusting it's coefficients w and b.

Squared Loss(L2 Loss)
    Squared Loss is a loss function that measures the squared difference between the actual value and the predicted value.
    It is commonly used to train Linear Regression models because it penalizes large prediction errors more heavily than small errors.

    Mathematically:
        Single observation squared loss:        L(y⁽ⁱ⁾, ŷ⁽ⁱ⁾) = (y⁽ⁱ⁾ - ŷ⁽ⁱ⁾)²
        Entire dataset mean squared error:      J(w, b) = (1 / m) * Σᵢ₌₁ᵐ (y⁽ⁱ⁾ - ŷ⁽ⁱ⁾)²
        Half-MSE used in Gradient Descent:      J(w, b) = (1 / (2 * m)) * Σᵢ₌₁ᵐ (y⁽ⁱ⁾ - ŷ⁽ⁱ⁾)²
    
    Root Mean Squared Error(RMSE): 
        RMSE = √MSE
    
    Advantages:
        1. Easy to understand and implement
        2. Differentiable everywhere
        3. Convex objective for Linear Regression
        4. Works naturally with Gradient Descent
        5. Strongly penalizes large errors
    
    Disadvantages:
        1. sensitive to outliers
        2. large errors can dominate the cost
        3. can be affected by noisy and incorrect target values
        4. MSE is expressed in squared target units
        5. May not be suitable when robustness is the priority

Absolute Loss(L1 Loss)
    Absolute Loss is a loss function that measures the absolute difference between the actual value and the predicted value.
    Unlike Squared Loss (L2) which squares prediction errors, Absolute Loss(L1) penalizes errors linearly.

    Mathematically:
        Single observation absolute loss:        L(y⁽ⁱ⁾, ŷ⁽ⁱ⁾) = (y⁽ⁱ⁾ - ŷ⁽ⁱ⁾)
        entire dataset mean abolute Error(MAE):  J(w, b) = (1 / m) * Σᵢ₌₁ᵐ (y⁽ⁱ⁾ - ŷ⁽ⁱ⁾)

    Advantages:
        1. Less sensitive to extreme prediction errors than Squared Loss
        2. Easy to interpret because MAE uses the same units as the target.
        3. Penalizes prediction errors proportionally to their magnitude
        4. Produces a convex objective for Linear Regression
        5. Useful for robust Regressiom when the dataset contains outliers

    Disadvantages:
        1. Not differentiable at zero error.
        2. Requires subgradient methods or other suitable optimization algorithms.
        3. Does not penalize large errors as strongly as Squared Loss.
        4. Gradient-based training can converge less smoothly.
        5. May be less suitable when large prediction errors are especially costly.

Huber loss 
    Huber loss is a loss function that combines the characteristics of Squared Loss(L2) and Absolute Loss(L1)
        For small prediction erros, it behaves like Squared Loss (L2)
        For large prediction erros, it behaves like Absolute Loss (L1)
    
    Mathematically: 
        single observation: eⁱ = ŷⁱ - yⁱ
        Huber loss Function: L_δ(e) = { (1/2)e²,         |e| ≤ δ
                                      { δ(|e| - (1/2)δ), |e| > δ 
            e = prediction error
            δ = hyperparameter controlling when the loss changes from quadratic to linear
            L_δ = Huber loss for one observation
        Cost function for entire dataset: J(w, b) = (1 / m) * Σᵢ₌₁ᵐ L_δ(ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)

    Advantages:
        1. Less sensitive to outliers than Squared Loss
        2. Differentiable everywhere
        3. Combines quadratic and linear error penalties.
        4. Convex for Linear Regression
        5. Useful for datasets containing occasional extreme target values
    
    Disadvantages:
        1. Requires choosing δ.
        2. Performance depends on the chosen threshold.
        3. More complex than MSE or MAE.
        4. Does not completely eliminate the influence of outliers, particularly high-leverage feature outliers.
        5. May not be appropriate when very large prediction errors must receive especially strong penalties.
"""

# Evaluation Metrics
"""    
R2-score
    R² is a regression evaluation metric that measures how well a model explains the variation in the target 
    compared  with a baseline model that always predicts the mean target value.

    Mathematically:
        R² = 1 - (SS_res / SS_tot)
            SS_res = Residual Sum of Squares(SSE or RSS):   SS_res = Σᵢ₌₁ᵐ (y⁽ⁱ⁾ - ŷ⁽ⁱ⁾)²
            SS_total = Total Sum of Squares (SST):          SS_tot = Σᵢ₌₁ᵐ (y⁽ⁱ⁾ - ȳ)²

    The problem in R²:
        The mean problem with R² is that it doesn't penalize adding unncecassary features(predictors) to Linear Regression Model.
        an example:
            Model-1: - Features: house_size                                         R²=0.80         Adjusted-R²=0.79
            Model-2: - Features: house_size, bedrooms                               R²=0.85         Adjusted-R²=0.84
            Model-1: - Features: house_size, bedrooms, +10 inrrelevant features     R²=0.87         Adjusted-R²=0.85
        adding a new feature to model always increase R² or leaves R² unchanged on the training dataset.
        it never decreases.

Adjusted R²
    It is a regression evaluation metric that measures how well a model explains variantion in the target variable 
    while accounting for the number of predictors(independent variables) used in the model.
    Unlike regular R², which cannot decrease when additional predictors are added to an ordinary least-squares model 
    fitted with an intercept, Adjusted R² penalizes unnecessary predictors.

    mathematical formula:
        R²_adj = 1 - (1 - R²) * ((m - 1) / (m - p - 1))


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


# Requirements on data to apply Linear Regression:
"""
Requirements on data to apply Linear Regression:
    1. Linearity.
        THe linearity between input features and Target labels

    2. Normality of Residuals.
        What is the shape/distribution of residuals 
        checking methods:
            1. Visualizations : Histogram, Q-Q plot
            2.  Summary statistics methods: Skewness, Kurtosis
            3. Statistical test methods: Jarque-Bera test or Shapiro-Wilk test
        
    3. Non-collinearity
        Linearity = Feature ↔ Target
        Collinearity = Feature ↔ Feature
        Collinearity means two predictor features are strongly linearly related each other
            example:    area_m2    rooms
                        50         2
                        70         3 
                        90         4
                        110        5
        Collinearity: refers to a strong linear relationship between two predictos
            Detection methods:
                1. scatter plots 
                2. correlation / correlation heatmap
            Treatment methods:
                1. Remove one of the redundant features
                2. Combine strongly related features
                3. Use Ridge Regression / Lasso Regression / Elastic Net
                4. PCA - Principal Component Analysis 

        Multicollinearity: occurs when one predictor is strongly explained by several other predictors together   
            Detection methods:
                1. VIF (Variance Inflation Factor)
                    VIF answers the question : can one feature be predicted well using the other feature columns?
                    Formula:             1
                              VIF_j = ──────────
                                       1 - R_j²
                        VIF_j = VIF value for Xj 
                        R_j²  = R-squared from predicting feature Xj using all other features
                    Interpretation 
                        VIF ≈ 1 -> No multicollinearity problem
                        VIF 1-5 -> Usually acceptable
                        VIF 5-10 -> Moderate / concerning multicollinearity
                        VIF > 10 -> Strong multicollinearity problem
                2. Tolerance 
                3. Condition number
                4. Eigenvalue analysis
                5. Auxiliary  Regression R   
            Treatment methods:
                1. Remove one of the redundant features
                2. Combine strongly related features
                3. Use Ridge Regression / Lasso Regression / Elastic Net
                4. PCA - Principal Component Analysis 

        NOTE: one serous problem with collinearity is interpretation the model
    4. Heteroscedasticity/Homoscedasticity ---> measures how Residuals have approximately constant variance/spread
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
                                 
    
    5. Similar Scales
        Features should be on a comparable numeric scale.
"""

 