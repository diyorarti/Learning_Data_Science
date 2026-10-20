"""
Motivation (1)
Logistic Regresion (2)
    Logistic Regression
        Logistic Regression is a classification algorithm. 
        It is used when the taget is categorical, especially Binary.
        Exampls:
            1. Is this email spam ? ---> No - Yes
            2. Is this transaction fradulent ? ---> No - Yes
            3. Is this tumer maligant ---> No - Yes

    The main idea:
        Linear Regression gives continuous numerical values: -10, 0.5, 7, 100 ...
        Logistic Regression converts that number into a probability between 0 and 1
        it does it using _sigmoid function:
            g(z) = 1 / (1 + e^(-z))
    
    Logistic Regression Formula:
        z = w * x + b
        g(z) = 1 / (1 + e^(-z))
        threshold = 0.5
        Output: 
            if g(z) >=0.5 then --> 1
            if g(z) < 0.5 then --> 0
    
Decisition Boundary (3)
    A Decision Boundary is the line, curve, or surface that seperates different classes

    For Binary(2 classes) classification:
        at first we calculate Linear relation:
            z = w * x + b
        Then pass the value z to _sigmoid:
            g(z) = 1 / (1 + e^(-z))
        After this, We use a threshold, usually 0.5:
            if g(z) >= 0.5:
                return 1
            else:
                return 0
        So the Decision Boundary happens when:
            w * x + b = 0

_cost Function for Logistic Regression (4)
Simplified Loss function (5)
    Mean Squared Error _cost Function:
        J(w, b) = 1/(2m) * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)²
        When MSE _cost function is applied for Logistic Regression, the optimization will result non-convex function 
            J(w, b)
            |
            |                      
            |                          
            |    /\     /\
            |   /  \   /  \   /\    /\
            |  /    \_/    \_/  \  /  \
            | /   non-Convex     \/    \__
            |/____________________________________________
        many Local Minimums 
    
    Binary Cross Entropy Loss Function is used for Logistic Regression, Becuase it is convex _cost function
        L(ŷ, y) = 1/(m) * Σᵢ₌₁ᵐ - [ y log(ŷ) + (1 - y) log(1 - ŷ) ]

        J(w, b)
        |\                /
        | \              /
        |  \            /
        |   \  Convex  /
        |    \        /
        |     \      /
        |      \____/
        |____________________________________________
    
Gradient Descent Implementation (6):

    Gradient Descent Formula:
        w := w - α * ∂ / ∂w * J(w, b)
        b := b - α * ∂ / ∂b * J(w, b)
    Derivatives
        ∂J(w, b) / ∂wⱼ = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾) * xⱼ⁽ⁱ⁾
        ∂J(w, b) / ∂b = 1/m * Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ - y⁽ⁱ⁾)

Overfitting (7):
    Overfitting happens when a model learns the traning data too well, including noise, random patterns, and 
    small details that not generalize to new data

    Underfitting:
        The model is too simple and cannot capture the real pattern.
        Model: almost flat/simple line
        Result: bad on training data and bad on test data

    Good fit:
        The model captures the general pattern.
        Model: smooth reasonable boundary
        Result: good on training data and good on test data

    Overfitting:
        The model becomes too complex and follows noise.
        Model: very complex curve
        Result: very good on training data, bad on test data

Addressing Overfitting (8):
    1. Collectiong more training data
    2. Feature Engineering / Feature Selection
    3. Regularization

_cost function with Regularization (9):
    Regularization means adding a penalty to the const function to stop weights from becoming too large
    Regularized Logistic Regression _cost function:
        J(w, b) = -1/m * Σᵢ₌₁ᵐ [y⁽ⁱ⁾log(ŷ⁽ⁱ⁾) + (1-y⁽ⁱ⁾)log(1-ŷ⁽ⁱ⁾)] + λ/(2m) * Σⱼ₌₁ⁿ wⱼ²

    where:
        λ = regularization parameter
        m = number of training examples
        n = number of features
        wⱼ = weight for feature j

        
"""

import numpy as np

class LogisticRegressionFromScratch:
    def __init__(self, learning_rate=0.001, n_iteration=1000, method='batch', batch_size=32, regularization=None, lamb_da=0.001):
        self.learning_rate = learning_rate
        self.n_iterations = n_iteration
        self.method = method
        self.batch_size = batch_size
        self.regularization = regularization
        self.lamb_da = lamb_da
        self.weights = None
        self.bias = None
        self.errors = []
    
    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):

            if self.regularization == None:
                if self.method == 'batch':
                    z = np.dot(X, self.weights) + self.bias
                    y_pred = self._sigmoid(z)
                    error = self._cost(y_pred, y)
                    self.errors.append(error)
                    dw = (1 / n_samples) * np.dot(X.T,error)
                    db = (1 / n_samples) * np.sum(error)
                    self.weights = self.weights - self.learning_rate * dw
                    self.bias = self.bias - self.learning_rate * db
                
                elif self.method == 'sgd':
                    indices = np.random.permutation(n_samples)

                    for i in indices:
                        X_i = X[i]
                        y_i = y[i]
                        z = np.dot(X_i, self.weights) + self.bias
                        y_pred = self._sigmoid(z)
                        error = self._cost(y_pred, y_i)
                        self.errors.append(error)
                        dw = np.dot(X_i * error)
                        db = error
                        self.weights = self.weights - self.learning_rate * dw
                        self.bias = self.bias - self.learning_rate * db

                elif self.method == 'mini_batch':
                    indices = np.random.permutation(n_samples)

                    X_shuffled = X[indices]
                    y_shuffled = y[indices]

                    for star in range(0, n_samples, self.batch_size):
                        end = star + self.batch_size
                        X_batch = X[star:end]
                        y_batch = y[star:end]
                        m = len(X_batch)

                        z = np.dot(X_batch, self.weights) + self.bias
                        y_pred = self._sigmoid(z)
                        error = self._cost(y_pred, y_batch)
                        self.errors.append(error)
                        dw = (1 / m) * np.dot(X_batch.T, self.weights)
                        db = (1 / m) * np.sum(error)
                        self.weights = self.weights - self.learning_rate * dw
                        self.bias = self.bias - self.learning_rate * db

                else:
                    raise ValueError("method must be 'batch' or 'sgd' or 'mini_batch'")
                
            elif self.regularization == 'L1':
                if self.method == 'batch':
                    z = np.dot(X, self.weights) + self.bias
                    y_pred = self._sigmoid(z)
                    error = self._cost(y_pred, y)
                    self.errors.append(error)
                    dw = (1 / n_samples) * np.dot(X.T,error) + self.lamb_da * np.sign(self.weights)
                    db = (1 / n_samples) * np.sum(error)
                    self.weights = self.weights - self.learning_rate * dw
                    self.bias = self.bias - self.learning_rate * db
                
                elif self.method == 'sgd':
                    indices = np.random.permutation(n_samples)

                    for i in indices:
                        X_i = X[i]
                        y_i = y[i]
                        z = np.dot(X_i, self.weights) + self.bias
                        y_pred = self._sigmoid(z)
                        error = self._cost(y_pred, y_i)
                        self.errors.append(error)
                        dw = np.dot(X_i * error) + self.lamb_da * np.sign(self.weights)
                        db = error
                        self.weights = self.weights - self.learning_rate * dw
                        self.bias = self.bias - self.learning_rate * db

                elif self.method == 'mini_batch':
                    indices = np.random.permutation(n_samples)

                    X_shuffled = X[indices]
                    y_shuffled = y[indices]

                    for star in range(0, n_samples, self.batch_size):
                        end = star + self.batch_size
                        X_batch = X[star:end]
                        y_batch = y[star:end]
                        m = len(X_batch)

                        z = np.dot(X_batch, self.weights) + self.bias
                        y_pred = self._sigmoid(z)
                        error = self._cost(y_pred, y_batch)
                        self.errors.append(error)
                        dw = (1 / m) * np.dot(X_batch.T, self.weights) + self.lamb_da * np.sign(self.weights)
                        db = (1 / m) * np.sum(error)
                        self.weights = self.weights - self.learning_rate * dw
                        self.bias = self.bias - self.learning_rate * db

                else:
                    raise ValueError("method must be 'batch' or 'sgd' or 'mini_batch'")
                
            elif self.regularization == 'L2':
                if self.method == 'batch':
                    z = np.dot(X, self.weights) + self.bias
                    y_pred = self._sigmoid(z)
                    error = self._cost(y_pred, y)
                    self.errors.append(error)
                    dw = (1 / n_samples) * np.dot(X.T,error) + 2 * self.lamb_da * self.weights
                    db = (1 / n_samples) * np.sum(error)
                    self.weights = self.weights - self.learning_rate * dw
                    self.bias = self.bias - self.learning_rate * db
                
                elif self.method == 'sgd':
                    indices = np.random.permutation(n_samples)

                    for i in indices:
                        X_i = X[i]
                        y_i = y[i]
                        z = np.dot(X_i, self.weights) + self.bias
                        y_pred = self._sigmoid(z)
                        error = self._cost(y_pred, y_i)
                        self.errors.append(error)
                        dw = np.dot(X_i * error) + 2 * self.lamb_da * self.weights
                        db = error
                        self.weights = self.weights - self.learning_rate * dw
                        self.bias = self.bias - self.learning_rate * db

                elif self.method == 'mini_batch':
                    indices = np.random.permutation(n_samples)

                    X_shuffled = X[indices]
                    y_shuffled = y[indices]

                    for star in range(0, n_samples, self.batch_size):
                        end = star + self.batch_size
                        X_batch = X[star:end]
                        y_batch = y[star:end]
                        m = len(X_batch)

                        z = np.dot(X_batch, self.weights) + self.bias
                        y_pred = self._sigmoid(z)
                        error = self._cost(y_pred, y_batch)
                        self.errors.append(error)
                        dw = (1 / m) * np.dot(X_batch.T, self.weights) + 2 * self.lamb_da * self.weights
                        db = (1 / m) * np.sum(error)
                        self.weights = self.weights - self.learning_rate * dw
                        self.bias = self.bias - self.learning_rate * db

                else:
                    raise ValueError("method must be 'batch' or 'sgd' or 'mini_batch'")
            else:
                raise ValueError("regularization must be None or 'L1' or 'L2'")
    
 
    def _cost(self, y_pred, y):
        error = -(1 / len(y)) * np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
        return error

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        predictions = self._sigmoid(z)

        return predictions





