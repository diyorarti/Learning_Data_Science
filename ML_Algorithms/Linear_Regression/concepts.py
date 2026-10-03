# Exponent
"""
Training Methods:
    1. Batch Gradient Descent
    2. Stochastic Gradient Descent
    3. Mini-batch Gradient Descent

Cost functions:
    1. Squared loss
    2. Absolute loss
    3. Huber loss
    4. R2-score

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

# Cost functions
"""
R2-score 
    R2-score = Explained variation / total variation
"""

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
        Start with random or zero values for w and b, then slowly update them ro reduce the cost.
        Imagine you are standing on a mountain and want to go down to the lowest point. You look at the slope and take small steps downward.
        That is Gradient Descent 
        THe update rule:
            parameters = parameters - learning_rate * gradient 
        
        Gradient Descent Formula:
            w := w - α * ∂ / ∂w * J(w, b)
            b := b - α * ∂ / ∂b * J(w, b)
        Where: 
                α = learning rate
                ∂ / ∂w * J(w, b) = Derivative  for w
                ∂ / ∂b * J(w, b) = Derivative for b
 
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

Running GRadient Descent (12)
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

 