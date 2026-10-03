"""
Expected Value
    Expected value of a Random Variable
        Discrete
        Continuous
    Expected value of a transformation
    Properties of expected value
    Variance
    Standard Deviation
    Covariance
"""  
# Expected value of a Random Variable 
"""
Expected value
    The expexted value of a random variable is the average value we expect to get in the long run if the random experiment is repeated many times
    It is written as: E[X], also called mean of the random variable
    Expected value = probability - weighted average of all possible values of the random variable
    Formula:
        E[X] = Σₓ xP(X = x)
    
    Example: Rolling a die
        X = number obtained when rolling a fair die
        Possible values: X ∈ {1, 2, 3, 4, 5, 6}
        Each value has prob: P(X = x) = 1 / 6 = 0.16
        Expected value = multiplied each possible value bu it's probability and add everything
            E[X] = 1 * (1 / 6) + 2 * (1 / 6) + 3 * (1 / 6) + 4 * (1 / 6) + 5 * (1 / 6) + 6 * (1 / 6) = 3.5
        What does E[X] = 3.5 means:
            It means that suppose rolling a die 100,000 times and calculating: sum of all results / 100,000 = result should be close to 3.5
            It doesn't mean rolling a die results becomes 3.5

    Why do we multiply by probabilities ?
        Example: X = 
            | (x) | Probability |
            |   0 |         0.1 |
            |   1 |         0.2 |
            |   2 |         0.6 |
            |   3 |         0.1 |
        The simple calculating normal average of possible values:
            (0+1+2+3)/4=1.5, this is misleading because these values are not equally likely.
            X = 2 occurs much more frequently than the others.
        So we need to give weighted based on its probability:
            0(0.1)+1(0.2)+2(0.6)+3(0.1)=0+0.2+1.2+0.3=1.7
        
    Expected value of a discrete random variable
        E[X] = Σₓ xP(X = x) means for each possible value x, calculate value*porb, then add everythin together.
        Example:
            X = {0,1,2,3}
            P(X) = {0.1,0.2,0.6,0.1}
            E[X] = 0(0.1)+1(0.2)+2(0.6)+3(0.1) 

    Expected value is not equal to the most likely value (mode)

    Expected value of a continuous random variable
        E[X] = ∫₋∞^∞ x f(x) dx means Conceptually, nothing changes: Expected value is still the probability-weighted average.
""" 

# Expected value of a transformation
"""
Expected value of a transformation 
    If we transform X into Y = g(X), what is expected value of Y ?
    X is random variable Y = g(X)
    we want: E[Y]
    So: E[Y] = E[g(X)] is the same with E[g(X)] = E[X²]

    Example:
        X = result of a fair die roll
        X ∈ {1, 2, 3, 4, 5, 6}
        P(X = x) = 1 / 6 
        Y = X² 

        | (X) | (Y=X^2) | Probability |
        |   1 |       1 |       (1/6) |
        |   2 |       4 |       (1/6) |
        |   3 |       9 |       (1/6) |
        |   4 |      16 |       (1/6) |
        |   5 |      25 |       (1/6) |
        |   6 |      36 |       (1/6) |

        E[X] = 1*(1/6)+2*(1/6)+3*(1/6)+4*(1/6)+5*(1/6)+6*(1/6) = 3.5
        E[Y] = 1*(1/6)+4*(1/6)+9*(1/6)+16*(1/6)+25*(1/6)+36*(1/6) = 15.17
"""

# Properties of expected value
"""
1.Multiplying a random variable by a constant
    E[cX] = cE[X]
    If we multiply every possible value of a random variable X by a constant c, its expected value is also multiplied by c.
    example:
        E[X] = 4
        Y = 3X
        E[Y] = E[3X] = 3E[X] = 3(4) = 12
        every value of X becomes three times largers, its average also becomes three times larger
    Another example:
        | (X) | (Y=3X) | Probability |
        |   1 |      3 |         0.2 |
        |   2 |      6 |         0.5 |
        |   3 |      9 |         0.3 |
        E[X] = 1 * 0.2 + 2 * 0.5 + 3 * 0.3 = 2.1
        E[Y=3X] = 3 * 0.2 + 6 * 0.5 + 9 * 0.3 = 6.3
        E[Y=3X] = E[X] * 3 = 6.3

2.Adding a constant
    E[X + c] = E[X] + c
    if we add the same constant c to every possible value of a random variable X, expected value also increase by C
    Example:
        E[X] = 4
        Y = 10 + X
        E[Y] = E[X] + 10 = 14


3.General Linear Transformation
    E[Y] = E[aX + b] = aE[X] + b
    This combines previus two properties:
        Multiplying: E[cX] = cE[X]
        Adding: E[X + c] = E[X] + c
    Example:
        E[X] = 4
        a = 2
        b = 5
        E[Y] = E[aX + b] = 2 * 4 + 5 = 13

    
4.Expected value of s sum
    E[X + Y] = E[X] + E[Y]
    The expected value of the total of the two random variables equals the sum of their indivintial expected values.
    Example:
        X = number of morning visits: E[X] = 5
        Y = number of evening visits: E[Y] = 8
        Z = total visits 
        E[Z] = E[X] + E[Y]
        E[Z] = 5 + 8

    THen:
        E[X + Y] = 5 + 8 = 13
    This is callen linearity of expectation.

5.General linearity of expectation
    E[aX + bY + c] = aE[X] + bE[Y] + c 
    This combies all dicessed so above:
        X and Y are random variables
        a and b are constants multiplying 
        c is a constant being added
    Example:
        X = number of morning visits: E[X] = 5
        Y = number of evening visits: E[Y] = 8
        Z = a * E[X] + b * E[Y] + c
        E[X] = 3
        E[Y] = 5
        a = 2
        b = 4
        c = 10

        E[Z] = 2 * 3 + 4 * 5 + 10 = 36


6. Multiplication
    If X and Y are independent 
        E[XY] = E[X] * E[Y]
        example:
            X = result of die 1
            Y = result of die 2
            E[X] = 3.5
            E[Y] = 3.5
            E[XY] = E[X] * E[Y] = 3.5 * 3.5 = 12.25

    if X and Y are dependent 
        E[XY] ≠ E[X] * E[Y]
        example:
            So for every observation, multiplying the value of X by the value of Y
            | (X) | (Y) | (XY) | 
            |   1 |   2 |    2 |
            |   2 |   3 |    6 |
            |   3 |   4 |   12 |
            E[X] = 2
            E[Y] = 3
            E[XY] = ? 
            assuming all observations have equal probabilities
            E[XY] = (2 + 6 + 12) / 3 = 6.67
            E[XY] = E[X] * E[Y] = 2 * 3 = 6 

""" 

# Vairance
"""
Variance tells us:
    How spread out the possible values of X are around its expected value. 
    Example:
        X = {4, 5, 6}
        Y = {0, 5, 10}
        Both have the same mean:
            E[X] = 5, values are very close to 5
            E[Y] = 5, values are very far from 5
        So: Var(Y) > Var(X)
    Formual:
        Var(X) = E[(X - E[X])²]
        1-step: E[X] = 5. this is the expected value or mean
        2-step: X - E[X]. this tells, how far each possible value is from the mean
        Example:
            X = {4, 5, 6}
            E[X] = 5
            So:
                4 - 5 = -1
                5 - 5 = 0
                6 - 5 = 1
            sqaure of the dbiations: -1² + 0² + 1² = 2
            Var(X) = 1 * (1 / 3) + 0 * (1 / 3) + 1 * (1 / 3) = 2 / 3 = 0.667

        Another example:
            X = {1, 2, 3}
            | (X) | Probability |
            |   1 |        0.25 |
            |   2 |        0.50 |
            |   3 |        0.25 |

            Caluclating Expected value:
                E[X] = 1 * (0.25) + 2 * (0.50) + 3 * (0.25) = 0.25 + 1 + 0.75 = E[X] = 2

            Calculating deviations
                | (X) | (X-E[X]) |
                |   1 |       -1 |
                |   2 |        0 |
                |   3 |        1 |

            Squaring them:
                | (X) | (X-E[X]) | ((X-E[X])²)  |
                |   1 |       -1 |            1 |
                |   2 |        0 |            0 |
                |   3 |        1 |            1 |

            Calcualating Variance
                Var(X) = 1 * (0.25) + 0 * (0.50) + 1 * (0.25) = 0.25 + 0 + 0.25 = 0.5

    Transformation and Variance
        Var(X) = E[X²] - (E[X])²
"""

# Standard Deviation
"""
Standard Deviation: SD = √Var(X)
    SD measures how far the values of random variable typically spread awawy from its expected value (mean).
        E[X] = center / mean
        Var(X) = spread around the center, squared
        SD(X) = spread around the center in the original unit
    Formula:
        SD(X) = √E[(X - E[X])²]

    Example:
        X = {4, 5, 6}
        all values are equally likely: 
            P(X = 4) = 1/3
            P(X = 5) = 1/3
            P(X = 6) = 1/3
        Expected value: 4 * (1 / 3) + 5 * (1 /3) + 6 * (1 / 3) = 5
        Deviations: 
            4 - 5 = -1
            5 - 5 = 0
            6 - 5 = 1
        Squared deviations: 1, 0, 1
        Variance: 1 * (1 / 3) + 0 * (1 / 3) +  1 * (1 / 3) = 0.667
        Standard Deviation: √Var(0.667) = 0.816
"""

# Covariance
"""
Covariance 
    how two ranodma varianles change together
    example:
        Positive Covariance
            X = hours studied
            Y = Exam score
        Negative Covariance
            X = product price
            Y = quantity demanded
    
    Formula:
        Cov(X, Y) = E[(X - E[X]) * (Y - E[Y])]

    Example:
        X = {1, 2, 3}
        Y = g(X) = X*2
        Transformation:
            | (X) | (Y) |
            |   1 |   2 |
            |   2 |   4 |
            |   3 |   6 |
        Expected values:
            E[X] = 2
            E[Y] = 4
        calculations:
            | (X) | (Y) | (X-E[X]) | (Y-E[Y]) | (X-E[X])*(Y-E[Y])  |
            |   1 |   2 |       -1 |       -2 |                  2 |
            |   2 |   4 |        0 |        0 |                  0 |
            |   3 |   6 |        1 |        2 |                  2 |
        Covariance:
            Cov(X, Y) = 2 * (1 / 3) + 0 * (1 / 3) + 2 * (1 / 3) = 1.33
        Positive covariance makes sense because X and Y increase together
    
Coveriance and Independence 
    X and Y independent ⇒ Cov(X,Y) = 0
    BUT Cov(X,Y) = 0 ⇏ X and Y independent
""" 
 
# Variance of a sum of random variables 
"""
Formula:
    Var(X + Y) = Var(X) + Var(Y) + 2 * Cov(X, Y)
    The variability of X + Y depends not only on the variability of X and Y, but also on how they move together.

    Positive Coveriance example:
        Var(X) = 4
        Var(Y) = 9
        Cov(X, Y) = 2
        Var(X + Y) = 4 + 9 + 2 * 2 = 17
        without coveriance, we would have only: Var(X + Y) = 4 + 9 = 13

    Negative coveriance example
        Var(X) = 4
        Var(Y) = 9
        Cov(X, Y) = -2 
        Var(X + Y) = 4 + 9 + 2 * (-2) = 13 - 4 = 9
    
    X and Y are independet:
        Var(X + Y) = Var(X) + Var(Y)
        because: indepent X and Y have Cov(X, Y) = 0
        So: Var(X + Y) = Var(X) + Var(Y) + 2 * 0
"""