"""
I. NEURAL NETWORKS INTUITION
    Big picture of Neural network: Input data → Neurons → Layers → Prediction → Error → Weight update → Better prediction
    1. neural networks and brain:
        Neural Networks were inspired by human brain, but modern neural netoworks are not exact copies of the brain.
        In the human brain, we have biological neurons. They receive signals, process them, and send signals to other neurons.
        Artifical Neural Ntowkrs use a simplified idea:
            Input signals → Artificial neuron → Output signal
            For example:
                study hours | sleep hours | attendance
                                    ↓
                                neuron
                                    ↓
                            pass probability
                A neruron recieve information, gives inportance to each input using weights, adds bias and produces an output.
                Simple Formula:
                    z = w1 * x1 + w2 * x2 + ... wn * xn + b
                    a = activation(z)
                Here:
                    x = input
                    w = weight
                    n = num of input features
                    b = bias
                    z = linear calculation
                    a = output/activation
                
    2. Demand production:
        let's say we want to predict demant for a T-shirt
            Inputs: 
                price         → x1        |O| → affordibility     → a1|
                shipping cost → x2 → x̄ →  |O| → awerness          → a2| → ā1 → |O|  → a2 probability of a T-shirt to be high demand
                marketing     → x3        |O| → percieved quality → a2|     
                material      → x3      
            Outout:
                predicted demand
        Classical ML algorithms (Linear or Logistic Regression) mayn't learn complex patterns from data. 
        Neural Networks can learn moe complex patterns like affordability, customer awerness, percived quality. 

    3. Recognizing images
        Image recognations is one of the best applications of Neural networks.
        A computer sees an image as numbers, a black-and-white image is a grid of pixel values. For nueral network: image = many numbers
        If an image is 28x28 pixels, then it has 28x28=784 input values
        The Neural Network receives these pixel values as input featues and learns patterns:
            for example:
                Early layers may learn --> edges, corners, simple lines
                Middle layers may learn --> eyes, ears, fur patters
                Layer layers may learn --> cat face, full cat shape

II. Neural Network model.
   1. neural network layer:
        A layer is a group of neurons. 
            Example: Input layer → Hidden layer → Output layer
        Simple Full-Connacted Nerual Network Architecture: 3 input features, 1 Hidden layer with 3 Neurons , output layer 1 neuron: 
                      |X1|      w̄1_1 |O| b1_1 → a1_1 = g(w̄1_1 * x̄ + b1_1)     |a1|
              Input_x̄-|X2|→ x̄ → w̄1_2 |O| b1_2 → a1_2 = g(w̄1_2 * x̄ + b1_2) → ā1|a2| →  w̄2_1 |O| b2_1 → a2 = g(w̄2_1 * ā1 + b2_1) → ā2 probabilities
                      |X3|      w̄1_2 |O| b1_3 → a1_3 = g(w̄1_3 * x̄ + b1_3)     |a3|

   2. More complex neural networks:
        Input → Hidden layer 1 → Hidden layer 2 → Hidden layer 3 → Output
                             |O|       
                 |O|         |O|       
                 |O|         |O|          |O|
         x̄  →    |O| → ā1  → |O| → ā2 →   |O| → ā3 → |O| → ā4
                 |O|         |O|          |O| 
                 |O|         |O|       
                             |O|       
        General Structure of Forward propagation: a[l]_[j] = g(w̄[l]_[j] *ā[l-1] + b[l]_[j])


    3. Inference Making Predictions (forward Propagation):

    |255||255||255||255||255||255||255||255|       |O|                
    |255||255||255|| 0 ||255||255||255||255|       |O|           |O|      
    |255||255|| 0 || 0 ||255||255||255||255|       |O|           |O|      
    |255||255||255|| 0 ||255||255||255||255| → x̄ → |O|   → ā1 →  |O| →  ā2 →  |O| ā3  →  if  ā3 >= Thresholds → ŷ = 1 else ŷ = 0
    |255||255||255|| 0 ||255||255||255||255|       |O|           |O|           1Neurons
    |255||255||255|| 0 ||255||255||255||255|       |O|           |O|      
    |255||255|| 0 || 0 || 0 ||255||255||255|       |O|           |O|      
    |255||255||255||255||255||255||255||255|       |O|           15Neurons     
                                                   25Neurons

III. Tensorflow Implementation
   1. Inference in Code:
            |O|  
        x̄ → |O| → ā1 → |O| → ā2
            |O|  
        
        layer_1 = Dense(units=3, activation='sigmoid')
        ā1 = layer1(x̄)
        layer_2 = Dende(units=1, activation='sigmoid')
        ā2 = layer_2(ā1)

    2.Data in Tensorflow
        scalar  → one number
        vector  → one-dimensional list
        matrix  → two-dimensional table
        tensor  → general name for these number structures

        tf.Tensor([[0.2, 0.7, 0.3]], shape=(1, 3), dtype='float')

    3. Building a Nerural Network
            |O|  
        x̄ → |O| → ā1 → |O| → ā2
            |O|  
        
        model = Sequential( Dense(units=3, activation='sigmoid),
                            Dense(units=1, activation='sigmoid'))
        model.compile(...)
        model.fit(X, y)
        model.predict(X_text)

            |O|         
            |O|         |O|  
        x̄ → |O| → ā1 →  |O| → ā2 → |O| → ā3
            |O|         |O|        1N
            |O|         15N
            25N
        
        model = Sequential( Dense(units=25, activation='sigmoid),
                            Dense(units=15, activation='sigmoid'),
                            Dense(units=1, activation='sigmoid'))
        model.compile(...)
        model.fit(X, y)
        model.predict(X_test)


IV. Neural Network implementation in Python. 
   1. Forward propagation in single layer:
             w̄1_1 |O| b1_1 → a1_1 = g(w̄1_1 * x̄ + b1_1) → w̄1_1 = np.array(...)| b1_1 = np.array(...) | z1_1 = np.dot(w̄1_1, x̄) + b1_1 | a1_1 = sigmoid(z1_1)
        x̄ →  w̄1_2 |O| b1_2 → a1_2 = g(w̄1_2 * x̄ + b1_2) → w̄1_2 = np.array(...)| b1_2 = np.array(...) | z1_2 = np.dot(w̄1_2, x̄) + b1_2 | a1_2 = sigmoid(z1_2)
             w̄1_3 |O| b1_3 → a1_3 = g(w̄1_3 * x̄ + b1_3) → w̄1_3 = np.array(...)| b1_3 = np.array(...) | z1_3 = np.dot(w̄1_3, x̄) + b1_3 | a1_3 = sigmoid(z1_3)
   
V. Neural Network training, 
  1. TensorFlow implementation:
            |O|         
            |O|         |O|  
        x̄ → |O| → ā1 →  |O| → ā2 → |O| → ā3
            |O|         |O|        1N
            |O|         15N
            25N
    model = Sequential([
                        Dense(units=25, activation='sigmoid),
                        Dense(units=15, activation='sigmoid),
                        Dense(units=1, activation='sigmoid)
                    ])
    model.compile(
                 Loss=BinaryCrossEntropy() → For classification
                 MeanSquaredError() → For Regression
                )
    model.fit(X, y)
    model.predict(X_test)


VI. Activation functions. 
     1. Alternatives to sigmoid activation:

            Linear Activation                    ReLU                         Sigmoid                       Tanh
                  |   /                           |   /                          |                                |      
                  |  /                            |  /                           |      _/                        |    _/
                  | /                             | /                            |  __/                           |  _/
        __________|/___________         __________|/___________                  __/                    __________|_/___________
                 /|                              |                            _/ |                              _/|
                / |                              |                          _/   |                           _/   |
               /  |                              |                       __/_____|___________            __/      |

        f(X) = X                         f(X) = max(0, X)              f(X) = 1/ (1 + e(-X))          f(x) = (e^x - e^(-x)) / (e^x + e^(-x))


    2. Choosing the right activation function:
        For Output Layer it dependes on the problem:
            If Binary Classification                   → Sigmoid
            If Regression(output only positive number) → ReLU
            If Regression(Output positive and Negative)→ Linear

        For Hidden Layers:
            ReLU is the most common chose
                Sigmoid →  slower
                ReLU    →  faster



    3. Why we need activation function:
        Without activation functions, Neural Network would only behave like a Linear mode.
        Even many hidden layers can't learn non-linear patterns without activation function

    ReLU activation function. 

VII. Multiclass classification. 
   1. Multiclass classification
     ŷ can be a small discreate categories, not any number

     |X X X  | ◼ ◼ ◼
     |X X X X|◼ ◼ ◼ ◼
     |  X X  |  ◼ ◼
     |-------+----------
     |O O O  | ▲ ▲ ▲ ▲
     |O O O  |   ▲  ▲
     |O O    | ▲  ▲ ▲
     |_______|__________   

   2. Softmax
        X  → Z1 = w̄1 * x̄ + b1   a1 = eᶻ¹ / ( eᶻ¹ + eᶻ² + eᶻ³ + eᶻ⁴) 
        O  → Z2 = w̄2 * x̄ + b2   a2 = eᶻ² / ( eᶻ¹ + eᶻ² + eᶻ³ + eᶻ⁴) 
        ◼ → Z3 = w̄3 * x̄ + b3   a3 = eᶻ³ / ( eᶻ¹ + eᶻ² + eᶻ³ + eᶻ⁴) 
        ▲  → Z4 = w̄4 * x̄ + b4   a1 = eᶻ⁴ / ( eᶻ¹ + eᶻ² + eᶻ³ + eᶻ⁴) 

        Softmax Regression For N possible outputs:
            Z_j = w̄j * x̄ + bj 
            j = 1, 2, 3, ..., N
            Parameters: w̄1, w̄2, ..., w̄N | b1, b2, ..., bN
            aj = eᶻʲ / (Σ # eᶻᵏ)
        
        Cost Function for Softmax Regression:
                                | -log(a1) if y=1
                                | -log(a2) if y=2
        Loss(a1, a2, ..., aN) → | -log(a3) if y=3
                                |       :
                                | -log(aN) if y=N



   3. Neural networks with softmax:

        Neural Network with Softmax Regression (10 possible outputs)
                |O|
                |O|         |O|        |O|          Z3_1 = w̄3_1 * ā2 + b3_1  a3_1 = eᶻ³₁ / ( eᶻ³₁ + ... + eᶻ³₁₀)
                |O|         |O|        |O|                               :
            x̄ → |O| → ā1 →  |O| → ā2 → |O| → ā3                          :
                |O|         |O|        |O|          Z3_10 = w̄3_10 * ā2 + b3_10  a3_10 = eᶻ³₁₀ / ( eᶻ³₁ + ... + eᶻ³₁₀)
                |O|         |O|        10N
                |O|         15N        
                25N

        Neural Netwok with Softmax Regression Tensorflow implementation

            model = Sequential([
                                Dense(units=25, activation='ReLU')
                                Dense(units=15, activation='ReLU')
                                Dense(units=20, activation='softmax')
                            ])
            model.comile(loss=SparseCategoricalCrossentropy())
            model.fit(X, y, epochs=1000)
            model.predict(X_text)
    4. Impreved Version of Softmax Regression:
        Numerical RoundOff Errors: SparseCategoricalCrossentropy(from_logits=True)

    5. Multilabel Classification:
         ____________                                img1   img2   img3
        |            |   1. is there a car ?         1       0       1
        |   image    |   2. is there a bus ?         0       0       1
        |            |   3. is there a padestrain ?  1       1       0
        |____________|

        Two approaches to train Neural Network for Multilabel classifcation:
            1. Training one Nerual Network for each class
            2. Training one Neural Network with N neurons in output layer
   
VIII. Additional neural network concepts. 
    1. Advanced Optimization

        In gradient descent, the parameter updates do not always move efficiently toward convergence.

        Sometimes, the updates move consistently in one direction but with very small steps. In this case, 
        convergence becomes slow because the model takes too many small steps.

        Other times, the updates oscillate from one side to another and take very large steps. 
        In this case, the model may struggle to converge because the learning rate is too high.

        To solve this problem manually, we could increase the learning rate when the updates move 
        smoothly in one direction, and decrease the learning rate when the updates start oscillating.

        The Adam optimization algorithm solves this problem automatically during training by adapting the learning rate for each parameter.

IX. Advice for applying machine learning

"""