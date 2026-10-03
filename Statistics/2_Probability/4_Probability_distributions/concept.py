# Probability Distributions
"""
Probability Distributions
    Continuous values probability distributions:
        Normal (Gaussian)
        Exponential
        Uniform
    Discrete values probability distributions:
        Bernoulli 
        Binomial
        Poisson
"""

# Probability Distributions
"""
A probability distribution is the pattern that describes how probabilities are distributed across the possible values of random variable.
    Steps to detect the type of distribution:
        1. Understand whether the random variable is discrete or continuous
        2. checking possible values min, max, unuque .. ect.
        3. visualizing the distribution
        4. descriptive statistics
        5. checking the properties of the indetified distribution

""" 

# Normal (Gaussian) Distribution  
"""
A normal distribution is a continuous probability distribution where values tend to cluster a central value,
and values father away from the center become less likely.
its shape is the famous bell-shape(curve)
    Probability density
        ^
        |
        |                 /\  
        |               /    \
        |             /        \
        |           /            \
        |_________/________________\________> X
                          μ
        
    Example:
        X = height of adult men in a population
        μ = 175
        Observation:
            many people around 170-180
            fewer people around 160 
            fewer people around 190
            very few people around 145 or 205

    Parameters of Normal distribution
        μ = mean
        σ = standard deviation
        σ²= variance
    
    How to detect Normal Distribution:
        1. Histogram
        2. Comparing: Mean=Median=Mode
        3. Skewness skew≈0
        4. Kurotisis Pearson≈3 | Fisher/Excess≈0

    Normal Distribution properties:
        68-95-99.7 rule
            this rules means:
                68% of values ≈ μ ± 1σ
                95% of values ≈ μ ± 2σ
                99.7% of values ≈ μ ± 3σ
            example:
                μ = 100
                σ = 15
                1-standard deviation
                    100 - 15 = 85
                    100 + 15 = 115
                    so approximately 68% observations between 85 and 115
                2-standard deviation
                    100 - 2 * 15 = 70
                    100 + 2 * 15 = 130
                    so approximately 95% observations between 70 and 130
                3-standard deviation
                    100 - 3 * 15 = 55
                    100 + 3 * 15 = 145
                    so approximately 99.7% observations between 55 and 145

    Probability Density Function
        P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx
        Here:
            f(x) = 1 / (σ√(2π)) · e^(-((x - μ)² / (2σ²))
            x = the examining value
            μ = mean
            σ = standard deviation
            Numpy implementation:
                density_X = (1 / (std * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)))
            


"""
 
# Exponential Distribution
"""
THe Exponential Distrbution is a continuous probaility distribution used to model the amount of time, distance or other continuous quantity until 
the next random event occurs, when events happen independetly at a constant average rate.
    Shape:
        high    |
                |\
                | \
                |  \
                |   \
                |    \__
                +----------------
                0        x

    Characteristic of Exponential distribution:
        1. It only has non-negative values: X ≥ 0
        2. shape: right-skewed
        3. It has one parameter λ (lambda): λ = average event rate
        4. Mean and standard deviation are equal: E[X] = 1 / λ  equal SD(X) = 1 / λ
    
    Where Lambda come from ?
        Lambda λ means: How frequently events happen 
        λ = 1 / E[X]
            example:
                λ = 0.125 events/minute
                0.125 * 60 = 7.5 events/hour  
        
    E[X] = 1 / λ
        Expected value means: how long we wait for the next event to happen
        example
            λ = 0.125 events/minute
            E[X] = 1 / λ = 1 / 0.125 = 8 minutes

    Variance:
        Var(X) = 1 / λ²
        example:
            λ = 0.125 events/minute
            Var(X) = 1 / (0.125)² = 64 minutes²

    Standard Deviation:
        SD(X) = 1 / λ
        example:
            λ = 0.125 events/minute
            SD(X) = 1 / 0.125 = 8 minutes

    PDF:
        P(a ≤ X ≤ b) = ∫ₐᵇ λe^(-λx) dx
        Here:
            ∫ₐᵇ = integral from a to b
            λ = parameter of the exponential distribution
            e = mathematical constant 2.71828
            x = represents a possible value of the random variable

        Numpy implementation:
            P(10 ≤ X ≤ 20) = np.exp(-λ * 10) - np.exp(-λ * 20)
        
"""

# Uniform Distribution
"""
A uniform distribution is a continuous probability distribution where all values are within a specified range are equally likely.
    X ∼ U(a,b)
    a = minimum possible value
    b = maximum possible value
    every value between a and b has the same probability density.

    Example:
        X = waiting time for a bus
        bus arrive scheduled at every 0 and 10 minutes
        the distribution looks flat:
            density
            ^
            |      ┌───────────────┐
            |      │               │
            |      │               │
            |______│_______________│________> X
                    0              10
        Unlike the Normal distribution, there is no central peak
    
    Main characteristic:
        equal probability density across the interval
        example X ∼ U(0, 10)
            interval length = 2
            P(0 < X < 2)
            P(6 < X < 8)

    Characteristics:
        | Characteristic | Uniform distribution   |
        | -------------- | ---------------------- |
        | Type           | Continuous             |
        | Range          | a ≤ X ≤ b              |
        | Shape          | Flat / rectangular     |
        | Parameters     | a and b                |
        | PDF            | 1 / (b - a)            |
        | Mean           | (a + b) / 2            |
        | Variance       | (b - a)² / 12          |
        | Symmetric      | Yes                    |
        | Equal density  | Yes                    |
    
    Expected Value:
        E[X] = (a + b) / 2

    Variance:
        Var(X) = ((b - a) ** 2) / 12

    PDF (Probability Density Function)
        denstiy = 1 / (b - a)

"""
 
# Bernoulli Distribution
"""
A Bernoulli Distribution describes a random variable that has exactly two possible outcomes
If a feature has exactly two possible values, it can be treated as a Bernoulli variable.
A binary variable follows a Bernoulli distribution.
    Examples:
        Customer purchase: Yes/No
        Load defaults: Yes/No
        Eamil clicked: 1/0
        Machine works: True/False
        Coin toss: Head/Tail
    
    Bernoulli Distribution has only one parameter: p = probablity
        Example:
            P(X = Yes) = 0.7
            P(X = No) = 1 - 0.7 = 0.3
    
    Expected value
        E[X] = p
        Because: E[X] = 0 * P(X = 0) + 1 * P(X = 1) = p 
        Suppose: 
            P(X = 1) = 0.7
            P(X = 0) = 1 - 0.7 = 0.3
        THen: E[X] = 0 * 0.3 + 1 * 0.7 = 0.7

    Variance:
        Var(X) = p(1 - p)
        example:
            p = 0.7
            Var(X) = 0.7 * (1 - 0.7) = 0.7 * 0.3 = 0.21
    
    Standard Deviation: 
        SD(X) = √p * (1 - p)
        example:
            p = 0.2
            SD(X) = √0.2 * (1 - 0.2) = √0.2 * 0.8 = √0.16 = 0.46

    PMF(Probability Mass Function):
        P(X = x) = pˣ(1 - p)¹⁻ˣ,   x ∈ {0, 1}

    | Characteristic     | Bernoulli         |
    | Type               | Discrete          |
    | Possible values    | (0,1)             |
    | Number of outcomes | 2                 |
    | Parameter          | (p)               |
    | P(X=1)             | (p)               |
    | P(X=0)             | (1-p)             |
    | Mean               | (p )              |
    | Variance           | (p(1-p))          |
    | Standard deviation | (sqrt{p(1-p)}   ) |

"""

# Binomial Distribution
"""
A Binomial distribution describes the number of successes in a fixed number of independent Bernoulli trails.
    The key idea: Binomial = counting successes across many Bernoulli trainls
    Exmaple:
        10 customers visit a website:
            Purchase = 1
            No purchase = 0
        Each customer is Bernoulli trail.
            X = number of customers who purchase out of 10
        this X can follow a Binomial distribution

    Bernoulli = one trail -> 0/1 probability
    Binomial = many trails -> number successes

    Parameters of Binomial:
        n = number of trails
        p = probability of success on each trail
        X ∼ Binomial(10,0.7)
        This means: 
            10 trainls
            each train has 70% probability of success

        Suppose 70% of customers usually purchase:
            p = 70%
            n = 10
            means exactly 7 of the 10 customers purchase.
        
    Conditions for a Binomial Distributiuon:
        1. Fixed number of trains n
        2. Each trail has exactly two outcomes.
        3. Trails are independent
        4. THe success probability p is the same for every trail
        5. We count number of successes
        Example:
            1. Fixed trail: n=20
            2. two outcomes: Head/Tail
            3. Independent trails
            4. the same probs: p = 0.5
            5. count heads

    Estimate p
        p = E[X] / n 

    Expected value E[X]:
        E[X] = p * n

    Variance:
        Var(X) = n*p*(1 - p)
        example:
            n = 10
            p = 0.7
            Var(X) = 10 * 0.7 * (1 - 0.7) = 2.1

    Binomial PMF
        P(X = k) = (n, k) · pᵏ · (1 - p)ⁿ⁻ᵏ
        k = number of success
        Example:
            X ∼ Binomial(10,0.7)
            P(X = 7) = (10 choose 7) · (0.7)⁷ · (0.3)³
"""

# Poisson Distribution
"""
A Poisson Distribution describes the number of times an event occurs within a fixed interval of time, space, area, legth, etc.
    Poisson Distribution = couting events in a fixed interval
    Example:
        number of customers in 1 hour
        number of calls in 10 minutes
        number of websire visits in 1 second
    
    Parameter λ
        Lambda λ respresents the average number of events in the specified interval.
        λ = 5 means on average 5 events occur per interval

    Poisson doesn't predict the exact count, it shows the average number events in many different intervals

    The difference from Binomial:
        In Binomial Distribution, we have a fixed number of opportunities for success.
            example: n = 10 customers
            each trail can produce only one success
            so success will be maximum 10, not more than 10
        In Poisson Distribution, we have a fixed amount of exposure such as time or space.
            example: 1 hour
            we want to count the number of calls.
            We may receive 10, 20, 100 ... not fixed 
       
    Mean 
        E[X] = λ
        Example:
            λ = 5
            E[X] = 5
    
    Variance 
        Var(X) = λ
        Example:
            λ = 5
            Var(X) = 5

    Standard Deviation 
        SD = √Var(X) 
        Example:
            λ = 5 
            ST(X) = √Var(5) = 2.32 

    Poisson PMF
            P(X = k) = (e⁻λ · λᵏ) / k!
            k = number of observed events
            λ = average number of events
            Formula answers : what is the probability of exactly k events ?
            Exanple:
                λ = 5
                What is P(X = 3) ?
                P(X = 3) = (e⁻⁵ · 5³) / 3! = np.exp(-5) * (5 ** 3) / math.factorial(3) = 0.14
""" 