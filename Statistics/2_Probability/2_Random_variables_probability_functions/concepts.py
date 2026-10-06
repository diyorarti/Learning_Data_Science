# Content table
"""
Random Variables and Probability Functions
│
├── Random variable
│   ├── Discrete
│   └── Continuous
│
├── Probability functions
│   ├── PMF(Probability Mass Function) → discrete
│   ├── PDF(Proabability Dinsity Function) → continuous
│   └── CDF(Cumculative Distribution Function) → discrete and continuous
│
├── Multiple random variables
│   ├── Joint
│   ├── Marginal
│   ├── Conditional
│   └── Independent
│
└── Transformations
    └── Y = g(X)
"""
 
# Random Variable
"""
A Variable is something that can take different values.Example: Age column with values [30, 21, 33, 23, 24]
                                                                Here Age is a variale. [30, 21, 33, 23, 24] - values
    Random variable is a variable whose value is determined by the outcome of a random experiment.
    Example: Rolling a six sided die.
            Possible outcomes: {1, 2, 3, 4, 5, 6}
            X = numbers shown on the die.
            Here: X - a random variable with die outcome values
    
    Discrete random variable:
        Discrete random variable is a random variable that can take a finite or countably infinite set of seperate numerical values.
    
    Continuous random variable:
        Continuous random variable is random variable that can take any numerical value within an interval or range.     
"""

# Probability Functions
"""
What values can A Random Variable take ? 
How is probability distributed accross those possible values ?
    A Probability function is a mathematical rule that describes how probabolities are associated with the possible values of a random variable.
        example: X = numbers of heads when tossing a coin twice.
                Possible values: {0, 1, 2}
            here we also want to know:
                How liekly is X = 0
                How likely is X = 1
                How likely is X = 2
                | X = number of heads | Probability |
                | ------------------: | ----------: |
                |                   0 |        0.25 | 
                |                   1 |        0.50 |
                |                   2 |        0.25 |
        So: 
            Random vaiable tells us: What values can occur ?
            Probability functoion tells us: How likely are those values ?

    Why are there different probability functions ?
        Because discrete and continuous random variables behave differently.
        Discrete variable:
            X = number of purchase 
            we can ask directly P(X = 2)
            there can be a positibe probability of exactly 2
            So PMF - Probabilit Mass Function
        Continuous variable:
            X = human height
            we normally don't assign probability to one exact value such as 170.1
            instead we calculate probability over a range: P(170 ≤ X ≤ 180)
            So PDF - Probability Density Function
"""

# Probability Mass Function
"""
PMF(Probability Mass Function) → discrete
    PMF tells us the probability that a discrete random variable takes each possible value.
    Formula: P(X = x) = p(x) = number of observations where X=x / total number of observations
    example: 
        tossing a coin twice
        Sample:space: {HH, TH, HT, TT}
        X = number of heads
        outcome - X 
        HH      - 2
        TH      - 1
        HT      - 1
        TT      - 0
        X ∈ {0, 1, 2}
        X = 0 -> Only TT gives, 1 TT in 4 possible outcomes  P(X = 0) = 1 / 4 = 0.25
        X = 1 -> TH, HT gives, 2 HT, HT in 4 possible outcomes P(X = 1) = 2 / 4 = 0.50
        X = 2 -> Only HH gives, 1 HH in 4 possible outcomes P(X = 2) = 1 / 4 = 0.25
    Two important properties of PMF 
        1. every probability must be between 0 and 1
        2. all probabilities must sum to 1 
"""

# Proabability Density Function
"""
PDF(Proabability Density Function) → continuous
    PDF describes how probability is distributed over the possible values of continuous random variable.
    General PDF formula: 
        P(a ≤ X ≤ b) = ∫ₐᵇ f_X(x) dx

    Density changes in different distributions:
        Uniform:     f_X(x) = 1 / (b - a) 
        Exponential: f_X(x) = λe^(-λx)
        Normal:      f_X(x) = 1 / (σ√(2π)) · e^(-((x - μ)² / (2σ²)))


Uniform Distribution PDF
    example: X = waiting time, the time can be anywhere between 0 and 10 minutes.
        Suppose: f_X(x) = 0.1
        We want: P(3 ≤ X ≤ 5) = ?
        P(a ≤ X ≤ b) = ∫ₐᵇ f_X(x) dx = ∫₃⁵ * 0.1 = (5-3) * 0.1 = 0.2 
        Converting to % 0.2 * 100 = 20
        there is 20% proability x can be a value between 3 and 5

    What about One exact value:
        Suppose we want: P(X = 5)
        for truly continuous variable: P(X = 5) = 0
        It doesn't mean X = 5 is impossible
        Why is the P(X = 5) = 0:
            Interval width: 5 - 5 = 0
            density = 0.1
            area = 5 * 0.1 = 0 
            so: P(X = 5) = 0 

    Property of PDF 
        Density can not be negative fx(x) ≥ 0
        Total area equals 1

    Surprizing fact:
        Density can be greater than 1
        area(area = density * interval width) is always between 0 and 1

        Example:
            X = waiting time in minutes
            X can be only between 0 and 0.25
            f(x) = 4 , density 4
            X = ( 0 ≤ x ≤ 0.25) 
            
            we want: P(0.05 ≤ X ≤ 0.15) = ?
            interval width = 0.15 - 0.05 = 0.10
            area = density * interval width = 4 * 0.10 = 0.40
            So: There is a 40% probability that the waiting time is between 0.05 and 0.15 minutes.


Exponetial Distribution PDF
    Formula: P(a ≤ X ≤ b) = ∫ₐᵇ f_X(x) dx
        f_X(x) = λe^(-λx)
        Here:
            ∫ₐᵇ = integral from a to b
            λ = parameter of the exponential distribution
            e = mathematical constant 2.71828
            x = represents a possible value of the random variable
    example:
            λ = 0.2 customers per minute
            E[X] = 1 / λ = 5 munutes
            P(3 ≤ X ≤ 8) = ?
            P(3 ≤ X ≤ 8) = ∫₃⁸ 0.2e^(-0.2x) dx
            P(3 ≤ X ≤ 8) = 0.5488 - 0.2019 = 0.347
            There is about a 34.7% probability that the waiting time until the next customer is between 3 and 8 minutes.
    Numpy implementation:
        P(3 ≤ X ≤ 8) = np.exp(-0.2 * 3) - np.exp(-0.2 * 8)
        P(3 ≤ X ≤ 8) = 0.5488 - 0.2019 = 0.347
        There is about a 34.7% probability that the waiting time until the next customer is between 3 and 8 minutes.

        
Normal Distribution PDF
    Probability Formula: P(a ≤ X ≤ b) = ∫ₐᵇ f_X(x) dx

    Density Formula: f_X(x) = 1 / (σ√(2π)) · e^(-((x - μ)² / (2σ²)))
    example:
        X ~ N(100, 15²)
        μ = 100
        σ = 15
        f_X(x) = 1 / (15 * √(2π)) · e^(-((x - 100)² / (2(15)²)))

        Suppose we want density at: x = 100
            f_X(100) = 1 / (15√(2π)) · e^(- (100 - 100)² / 2(15)²) = 1 / (15√(2π)) = 0.0266
            0.0266 is density at 100, not probability

"""

# Cumculative Distribution Function
"""
CDF(Cumculative Distribution Function) → discrete and continuous
    The probability that a random variable X is less than or equal to a particular value x.
    The formula: F_X(x) = P(X ≤ x) read as the CDF at x is the probability that X is less than or equal to x. 
    F_X(3) = P(X ≤ 3) means that What is the probability that X takes a value of 3 or less?

    Exaple:
        | (x) | (P(X=x)) |
        |   0 |     0.10 |
        |   1 |     0.20 |
        |   2 |     0.40 |
        |   3 |     0.20 |
        |   4 |     0.10 |
    we want: F_X(2) = P(X ≤ 2) 
        P(X = 0) + P(X = 1) + P(X = 2) = 0.10 + 0.20 + 0.40 = 0.70  F_X(2) = 0.70
        There is a 70% probability that X is 2 or less.

    CDF for → discrete random variable  
        X = number of heads from two coin tosses
            | (x) |  PMF |
            |   0 | 0.25 |
            |   1 | 0.50 |
            |   2 | 0.25 |
        at x = 0  f(0) = P(X ≤ 0) = 0.25
        at x = 1  f(1) = P(X ≤ 1) + P(X ≤ 0) = 0.50 + 0.25 = 0.75
        at x = 2  f(2) = P(X ≤ 2) + P(X ≤ 1) + P(X ≤ 0) = 0.25 + 0.50 + 0.25 = 1

    CDF for → continuous random variale
        X = waiting time , where waiting time is uniformly distributed between 0 and 10 munutes 
        f(x) = 0.1 (density)
        suppose we want F(4) = P(X ≤ 4)
        interval withd = 4 - 0 = 4
        area = 4 * 0.1 = 0.40 
        So: F(4) = 40%
        There is a 40% probability that the waiting time is 4 minutes or less.
"""

# Multiple random variables
"""
Multilple random variable means we define two or more random variables on the same random experiement or observation.
    example:
        X = number of purchases
        Y = total amount spent

    Joint (Intersection) probability/distribution
        Joint means looking at more than one random variables together at the same time.
        Suppose:
            X = num of purchases
            Y = coupon used
            Instead of:
                P(X = 2)
                or P(Y = Yes)
            Here: we ask P(X = 2, Y=Yes)

        Example:
            X = number of purchases
            Y = coupon used (0/1)
            total 100 customers
            | Purchases (X) | Coupon (Y) | Number of customers | Joint probability |
            |             0 |          0 |                  10 |     10/100 = 0.10 |
            |             0 |          1 |                   5 |      5/100 = 0.05 |
            |             1 |          0 |                  20 |     20/100 = 0.20 |
            |             1 |          1 |                  15 |     15/100 = 0.15 |
            |             2 |          0 |                  20 |     20/100 = 0.20 |
            |             2 |          1 |                  30 |     30/100 = 0.30 |
            We want to know P(X = 2, Y = 1) = 30 / 100 = 0.30
            There is a 30% probability that a randomly selected customer made exactly 2 purchases and used a coupon.

    Marginal (not the same as Union) probability/distribution
        Marginal means looking at one random variable by itself, ignoring the other random variables
        Example:
            X = num of purchases
            Y = coupon usage
            Assume 100 customers
            | Purchases (X) | Coupon No | Coupon Yes |   Total |
            |             0 |        10 |          5 |      15 |
            |             1 |        20 |         15 |      35 |
            |             2 |        20 |         30 |      50 |
            |     **Total** |    **50** |     **50** | **100** |
            What is the probability that a randomly selected customer made exactly 2 purchases?
            Customers with 2 purchases are:
                20 customers → no coupon
                30 customers → coupon
                Total = 50 customers
                P(X = 2) = 50 / 100 - 0.50
    
    Conditional(the same with Probability Laws CP) Porbability

    Independent (the same with Laws of proability indepdent events)

"""

# Transformation
"""
A transformation creates a new random variable Y by applying a mathematical function g to an existing random variable X.
    So: Y = g(X)
    Take whatever random value X produces, apply the function g, and the result becomes the value of Y.
    Example:
        X = number shown when rolling a die
        X ∈ {1, 2, 3, 4, 5, 6}
        Define: Y = 2X
        g(X) = 2X
        So:
            X = 1 → Y = 2
            X = 2 → Y = 4
            X = 3 → Y = 6
            X = 4 → Y = 8
            X = 5 → Y = 10
            X = 6 → Y = 12
        
"""