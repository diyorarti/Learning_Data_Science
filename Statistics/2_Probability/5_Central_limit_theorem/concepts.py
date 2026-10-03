"""
Central Limit Theorem
    Sampling Distribution
    Mathematical Structure of CLT 

Conditions and Assumptions of CLT
    Random Sampling
    Independence of observations
    Identically distributed observations
    Finite mean and finite Variance
    Sufficiently large sample size

CLT with different population distributions
Standardization Using CLT
CLT for Sums
"""
  
# Central Limit Theorem
"""
If we repeatedly take sufficiently large random samples from a population and calculate the sample mean of each sample,
the distribution of those sample means becomes aprroximately normal, even if the original population is not normally distributed
The point is that CLT is about the distribution of sample means, not original data

Suppose cusomers waiting times are strongly right-skewed. The population distribution may look like this
    Population data X   ********
                        *****
                        ***
                        ** 
                        *
                        ________________
    Now we repeatedly do this: 
        take n = 50 customers
    calculating their average x̄
        Sample 1 → mean = 9.8
        Sample 2 → mean = 10.4
        Sample 3 → mean = 9.6
        Sample 4 → mean = 10.1
        Sample 5 → mean = 9.9
        ...
    if we plot all those sample means, their distribution tends to look like:
            ***
          *********
       ***************
     *******************
       ***************
          *********
             ***
    Approximately normal
"""

# Sampling Distribution
"""
A Sampling distribution is the probability distribution of a statistic, such as the sample mean, calculated from many repeated random samples of the same size. 
THe word statistic is importan, a statisitc can be:
    sample mean x̄
    sample proportion p̂
    sample variance
    sample median ...

For, CLT we mainly care about the sampling distribution of the sample mean.
    Example:
        population = 2, 4, 6, 8, 10
        Samples: n = 2
            1-sample: 2, 4  | x̄ = (2 + 4) / 2 = 3
            2-sample: 6, 10 | x̄ = (6 + 10) / 2 = 8
            3-sample: 4, 8  | x̄ = (4 + 8) / 2 = 6
            after doing many times
            x̄1, x̄2, ...  = sampling distribution of x̄

Central Limit Theorem Core Idea
    IF we repeatedly take independent random samples of size n from a population and calculate the mean of each sample, 
    then as n becomes sufficiently large, the sampling distribution of those means becomes approximately normal.
    in simple words, how much n(sample size) increases, so much sampling distribution of the sample mean becomes normal or bell-shape.
"""

# Mathematical Structure of CLT
"""
Expected value:
    If we repeatedly take random samples and calculate the mean of each sample, the average of all those possible sample means is the population mean
    E[X̄] = μ
        E = expected value
        X̄ = sample mean, viewed as a random variable
        μ = population mean
    Example:
        Population has: μ = 100
        Repeatedly taking samples n=50
            sample 1 → X̄1 = 98
            sample 2 → X̄2 = 103
            sample 3 → X̄3 = 99
            sample 4 → X̄4 = 101 
            ...
        all these possible sample means is E[X̄] = 100

Variance:
    The variance of the sample mean across repeated samples equals the population variance divided by the sample size.
    Var(X̄) = σ² / n
        X̄ = sample mean
        σ² = population variance
        n = sample size
    Example:
        Population:
            μ = 100
            σ² = 400
            σ  = 20
        Sample:
            n = 25
            Var(X̄) = 400 / 25 = 16

Standard deviation:
    The standard deviation of the sample mean across repated samples equals the population variance divided square root of sample size
    Std(X̄) = σ / √n
        X̄ = sample mean
        σ = the population standard deviation 
        √n = the square root of sample size
    example:
        population:
            μ = 100
            σ² = 400
            σ  = 20
        Sample:
            n = 25 
            Std(X̄) = 20 / √25 = 20 / 5 = 4

Standard Error:
    Standard Error measures how much the sample mean is expected to vary from sample to sample
    SE(X̄) = σ / √n
        SE = standard error
        X̄ = sample mean
        σ = pilation standard deviation
        √n = the square root of sample size
    example:
        population:
            μ = 100
            σ² = 400
            σ  = 20
        Sample:
            n = 25
            SE(X̄) = 20 / √25 = 20 / 5 = 4
"""

# Conditions and Assumptions of the CLT
"""
Random sampling
    The observations in the sample should be selected from the population in a way that gives population 
    members a fair chance of being included and avoids systematic selection bias.
    Example:
        A good sampling might be:
        Population = 100,000
        n = 500
        μ = 100
        x̄1 = 98
        x̄2 = 103
        x̄3 = 101
        x̄4 = 99
        they fluctuate around μ = 100 
    
    A bad example might be:
        population = 100,000
        n = 10,000
        μ = 2000
        x̄1 = 8000
        Sample mean is far away from population mean.
        This is selection bias

Independence of observations
    The value of one observation should not determine or strongly affect the value of another observation
    For example:
        if we select 100 unrelated customers from a very large population. This may be reasonably independent.
        But if we select:
            the same customer many times
            members of the same household
            employees from the same team
            measurements from the same machine every minute.
        They may be dependent.
    
Identically Distributed Observations
    Population: scores=[80, 88, 89, 79, 59, 60, 67, 76, 88, 99, 100, 57, 59, 85, 81, 82, 79, 78, 95, 93]
        mean=79.7
        std=13.027
        Var=169.7

    Samples
        n = 5
        sample-1 -> X1 = [95, 82, 59, 78, 88] 
            here: x1=95, x2=82, x3=59, x4=78, x5=88 these value come indentiaclly distributed.
            every xi is selected using the same random process from the same population.
            all of them have the same underlying distribution.
            the same is true for every sample

        sample-2 -> X2 = [93, 89, 100, 95, 85] 
        sample-3 -> X3 = [89, 85, 59, 79, 100] 
        sample-4 -> X4 = [88, 82, 59, 79, 88] 
        sample-5 -> X5 = [78, 60, 88, 59, 67]

         So: 
            E[X1] = E[X2] = E[X3] = E[X4] = E[X5] = population mean 79.7
            Std(X1) = Std(X2) = Std(X3) = Std(X4) = Std(X5) = population std 13.0.27
            Var(X1) = Var(X2) = Var(X3) = Var(X4) = Var(X5) = population var 169.7

Finite mean and finite Variance
    E[X] = μ < ∞
    Var(X) = σ² < ∞
    It means that The population needs to have a meaningful center μ and a meaningful finite amount of spread σ².
    Example:Population
        scores=[80, 88, 89, 79, 59, 60, 67, 76, 88, 99, 100, 57, 59, 85, 81, 82, 79, 78, 95, 93]
        μ = 79.7 < ∞
        σ² = 169.71 < ∞
    finite means well defined number it may be mean, variance or expected value. 
    CLT requires that population should have well defined mean, Expected value and Variance.

Sufficiently large sample size
    The sample size n should be large enough for the sampling distribution of the sample mean X̄ to be approximately normal.
    If the original population strongly non-normal, then with a very small sample such as n=3, n=5 sampling distribution may be skewed.
    As n increases the sampling distribution of X̄ generally becomes more near normal.
    n =< 30 often more normal, it is not a strict approach,
"""
 
# CLT with differet population distributions
"""
Continuous value distrubutions:
    Normal Distribution
        This type of data is the easiest.

    Uniform Distribution
        X ∼ U(a,b)
        if we repeatedly take samples and calculate their means, the sampling distribution of X̄ becomes increasingly bell-shape.
    
    Exponential Distribution
        X ∼ Exponential(λ)
        At small n, distribution of X̄ may be right-skewed. As n increases, the skewness decreases.

Discreate value distributions
In binary value data X ∈ {0, 1}
Suppose: churn probability
    E[X] = p 
    Var(X) = p(1 - p)
    if we take n customers: x1, x2, ..., xn
    X̄ =( x1 + x2 + ... + xn) / n
    example:
        n = 10
        Customers_churn = [0,1,0,0,1,0,1,0,0,0] 
        X̄ = (0 + 1 + 0 + 0 + 1 + 0 + 1 + 0 + 0 + 0) / n = 0.30

"""

# Standardization Using CLT
"""
ordinary Z-score standardization formula is : Z = (X - μ) / σ 
But in sample:
    X̄ = sample mean
    E[X̄] = μ
    SD(X̄) = σ /√n
    Var(X̄) = σ² / n

Z-score Standardization:
    Z = (X̄ - μ) / (σ /√n)
    How many standard errors is the observed sample mean away from the population mean ?
"""

# CLT for Sums
"""
Sums means the sum of a sample:
    example:
    Population - customers spending
    Sample size = 5
    Sample-1 = {10, 20, 30, 40, 50} -> Sn = 10 + 20 + 30 + 40 + 50 = 150 -> S5 = 150
    Sample-2 = {5, 25, 30, 42, 39} -> Sn = 5 + 25 + 30 + 42 + 39 = 141 -> S5 = 141
    it continues like this with all samples may have different sums

Formulas of CLT for Sums:
    Expected value:
        E[Sn] = nμ
        Exanple:
            μ = 30
            n = 5
            E[Sn] = 5 * 30 = 150
    
    Standard Deviation:
        SD(Sn) = σ * √n
        example:
            σ = 10
            n = 25
            SD(S25) = 10 * √25 = 50
            
    Variance
        Var(Sn) = n * σ²
        example:
            σ² = 100
            n = 25
            Var(S25) = 25 * 100 = 2500
"""

 