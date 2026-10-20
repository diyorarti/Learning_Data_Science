"""
Decision Trees(1):

    Given data:
        ear_shape | face_shape | whiskers | cat
        ---------------------------------------
        pointy    | round      | present  | 1
        floppy    | not_round  | present  | 1
        floppy    | round      | absent   | 0
        pointy    | not_round  | present  | 0
        pointy    | round      | present  | 1
        pointy    | round      | absent   | 1
        floppy    | not_round  | absent   | 0
        pointy    | round      | absent   | 1
        floppy    | round      | absent   | 0
        floppy    | round      | absent   | 0

        ear_shape, face_shape and whiskers -> features
        cat -> Target (1 -> cat, 0 -> dog)

    Decision Tree :

                            (ear_shape) 
                            /             \
                           /               \
                    point /                 \ floppy
                         /                   \
                (face_shape)               (whiskers)
                  /       \                 /      \
            round/         \not         pre/        \absent
                /           \             /          \ 
            [1, 1, 1, 1]     [0]        [1]    [0, 0, 0, 0]


Learning Process(2):

    Decision 1: What feature to use to split data at each node ? -> Maximize Purity / Minizize impurity
                Choose the feature with the highest Information gain / impurity reduction

                To know the feature which has the higest information gain, we calculate information gain for all features

                Information Gain Formula:
                    Information Gain = Parent Entropy - Weighted Child Entropy
                        IG(S, A) = H(S) - Σ ( |Sv| / |S| ) * H(Sv)
                            Where:
                                S     = parent dataset
                                A     = feature used for splitting
                                Sv    = subset of data after splitting by value v of feature A
                                H(S)  = entropy of the parent node
                                H(Sv) = entropy of each child node
                
                Entropy Formula:
                    H(S) = - Σ p_i * log2(p_i)
                    For Binary Classification:
                        H(S) = -p1 * log2(p1) - p0 * log2(p0)
                            Where:
                                S  = dataset / node
                                p1 = probability of class 1
                                p0 = probability of class 0


                         (ear_shape)                  P1 = 5/10, H_root_p1 = -0.5 * log2(0.5) -0.5 * log2(0.5) = 1
                         /         \
                  pointy/           \Floppy
                       /             \   
         [1, 0, 1, 1, 1]           [1, 0, 0, 0, 0]    P1 = 1/5 = 0.2, H_right_p1 = -0.2 * log2(o.2) -0.8 * log2(0.8) = 0.72
        
                                                      p1 = 4/5 = 0.8 H_left_p1 = -0.8 * log2(0.8) -0.2 * log2(0.2) = 0.72
                                                      in_gain = H_root_p1 - (5/10 * H_left_p1 + 5/10 * H_right_p1) = 0.28 
                
        Decision 2: When to stop splitting ?
                      1. When a node is 100% one class
                      2. when splitting data in a node will exceed max depth
                      3. when information gain score is less than a threshold
             
Measuring Purity/Impurity(3)
        Entropy
        Gini

Information Gain (4)

Putting all together (5)

Using One-hot encoding for Categorical features (6):
    Given data:                                     new_features:
        ear_shape | face_shape | whiskers | cat        pointy | Oval | Flopy 
        ---------------------------------------        ---------------------
        pointy    | round      | present  | 1             1   |   0  |  0
        oval      | not_round  | present  | 1             0   |   1  |  0
        oval      | round      | absent   | 0             0   |   1  |  0
        pointy    | not_round  | present  | 0             1   |   0  |  0
        oval      | round      | present  | 1             0   |   1  |  0
        pointy    | round      | absent   | 1             1   |   0  |  0
        floppy    | not_round  | absent   | 0             0   |   0  |  1
        oval      | round      | absent   | 1             0   |   1  |  0
        floppy    | round      | absent   | 0             0   |   0  |  1
        floppy    | round      | absent   | 0             0   |   0  |  1 

        The ear_shape feature is now categorical , if we apply One-Hot Encoding, we will have three different features

Countinuous Value Features(6):
    Given data:
        ear_shape | face_shape | whiskers | weight | cat
        ------------------------------------------------
        pointy    | round      | present  | 7.2    | 1
        floppy    | not_round  | present  | 8.8    | 1
        floppy    | round      | absent   | 15.0   | 0
        pointy    | not_round  | present  | 9.2    | 0
        pointy    | round      | present  | 8.4    | 1
        pointy    | round      | absent   | 7.6    | 1
        floppy    | not_round  | absent   | 11.0   | 0
        pointy    | round      | absent   | 10.2   | 1
        floppy    | round      | absent   | 18.0   | 0
        floppy    | round      | absent   | 20.0   | 0
    
    weight is continuous valued feature, Decision Tree doesn't split data by exact categories.Instead, it tries different threshold.
    Then Algorithm chooses the the threshold with the higest information gain. 
    Decison Tree tries to take thresholds from midpoints between sorted feature values

Decision Tree Regression (7):
    Given data:
        ear_shape | face_shape | whiskers | weight 
        ------------------------------------------
        pointy    | round      | present  | 7.2   
        floppy    | not_round  | present  | 8.8   
        floppy    | round      | absent   | 15.0  
        pointy    | not_round  | present  | 9.2   
        pointy    | round      | present  | 8.4   
        pointy    | round      | absent   | 7.6   
        floppy    | not_round  | absent   | 11.0  
        pointy    | round      | absent   | 10.2  
        floppy    | round      | absent   | 18.0  
        floppy    | round      | absent   | 20.0  

        In Decision Tree Regressor Goal is variance reduction

        [7.2, 8.8, 15, 9.2, 8.4, 7.6, 11, 10.2, 18, 20] 
                          (ear_shape)   Variance_parent = 20.51
                         /            \
                        /              \
                pointy /                \ floppy
                      /                  \
        [7.2, 9.2, 8.4                  [8.8, 15.0, 11.0, 
         7.6, 10.2]                       18.0, 20.0]
        Varinace_left = 1.47            Variance_right = 21.87

        Information Gain = Variance_parent - (W_left * Variance_left + W_right * Variance_right) = 20.51 - 11.67 = 8.83

Tree Ensembles(8):
    Single Decisiont Tree is too sensitive, it is overfited to training data, changing sinle sample of training data may result total different tree.
    So solve this , multiple decision trees can be trained.

Sampling with Replacement (9):
    1. Pick one sample from the dataset
    2. Put it back into the dataset
    3. Pick again
    4. Because we put it back, the same sample can be selected again

Random Forest (10):
    Given Training set of size m:
        For b = 1 to B:
            Use sampling with replacement to create a new training set of size m
            Train a Decision tree on the new data


XGBoost (11):
    Given training set of size m:
        For b=1 to B:
            Use sampling with replacement to create a new training set of size m.
            XGBoost Algorithm does, instead of picking from all examples with equal probabilities (1/m) , 
                make it more likely to pick miscalssified examples from previously trained trees.
            Train a Decision Tree on the new dataset.
""" 

import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, max_depth=10, min_samples_split=2, task='regression', criterian='entropy'):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.task = task
        self.criterian = criterian
        self.root = None
    
    def fit(self, X, y):
        self.root = self._grow_tree(X, y)
    
    def _grow_tree(self, X, y, depth=0):
        n_samples, n_feautures = X.shape
        n_labels = len(np.unique(y))

        if self.max_depth <= depth or self.min_samples_split > n_samples or n_labels == 1:
            leaf_value = self._leaf_value(y)
            return Node(value=leaf_value)
        
        best_feature, best_threshold = self._best_split(X, y, n_feautures)

        left_indices, right_indices = self._split(X[:, best_feature], best_threshold)

        left_child = self._grow_tree(
            X[left_indices],
            y[left_indices],
            depth + 1
        )

        right_child = self._grow_tree(
            X[right_indices], 
            y[right_indices],
            depth + 1   
        )

        return Node(
            feature=best_feature,   
            threshold=best_threshold,
            left=left_child,
            right=right_child
        )

    def _best_split(self, X, y, n_features):
        best_gain = 0
        best_feature = None
        best_threshold = None

        for feature in range(n_features):
            X_column = X[:, feature]
            thresholds = np.unique(X_column)

            for threshold in thresholds:
                gain = self._information_gain(X_column, y, threshold)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold
        return best_feature, best_threshold

    def _information_gain(self, X_column, y, threshold):
        parent_impurity = self._impurity(y)

        left_indices, right_indices = self._split(X_column, threshold)

        n = len(y)
        n_left = len(left_indices)
        n_right = len(right_indices)

        if n_left == 0 or n_right == 0:
            return 0
        
        left_impurity = self._impurity(y[left_indices])
        right_impurity = self._impurity(y[right_indices])

        return parent_impurity - (n_left / n * left_impurity + n_right / n * right_impurity)


    def _split(self, X_column, threshold):
        left_indices = np.argwhere(X_column >= threshold).flatten()
        right_indices = np.argwhere(X_column < threshold).flatten()
        return left_indices, right_indices

    def _impurity(self, y):
        if self.task == 'regression':
            return np.var(y)
        elif self.task == 'classification':
            if self.criterian == 'entropy':
                return self._entropy(y)
            elif self.criterian == 'gini':
                return self._gini(y)
            else:
                raise ValueError("criterian must be either 'gini' or 'entropy'")
        else:
            raise ValueError("task must be either 'regression' or 'classification'")

    
    def _entropy(self, y):
        count = np.bincount(y)
        prob = count / len(y)
        return - np.sum(prob * np.log2(prob))
    
    def _gini(self, y):
        count = np.bincount(y)
        prob = count / len(y)
        return 1 - np.sum(prob ** 2)
    
    def _leaf_value(self, y):
        if self.task == 'regression':
            return np.mean(y)
        elif self.task == 'classification':
            count = Counter(y)
            return count.most_common(1)[0][0]
        else:
            raise ValueError("task must be either 'regression' or 'classification'")
    
