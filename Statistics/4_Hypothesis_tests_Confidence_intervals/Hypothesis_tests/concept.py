"""
1.What hypothesis testing actually does
2.Null hypothesis H₀ and alternative hypothesis Hₐ
3.One-tailed vs two-tailed hypotheses
4.Significance level α
5.Test statistic
6.Sampling distribution under H₀
7.Critical value and critical region
8.P-value
9.Type I and Type II errors
10.Choosing the correct statistical test:
        Z-test
            one-sample Z-test
            two-sample Z-test
            one-proportion Z-test
            two-proportion Z-test
        T-tests
            one-sample t-test
            independent two-sample t-test
            paired t-test
        Chi-square tests
            goodness-of-fit 
            test of independence
        ANOVA
            start with one-way ANOVA
12.Full practical hypothesis-test design in Python
"""  

# What is Hypothesis testing
"""
Hypothesis testing is a statistical method used to make an inference about a population using sample data.
    We observe soemthing in a sample and ask whether that result is strong enough to conclude that something is happening in the population.
    Example:
        A company claims that the average delivery time μ=30 minutes
        We can't measure every delivery that has ever happened, so we take a sample of 100 deliveries and get X̄₁₀₀ = 27 minutes
        Now important questions:
            1. is 27 minutes different enough from 30 minutes that we should believe that the population mean is not 30 ?
            2. could this difference simply be caused by random sampling variation ?
        Here: Hypothesis testing helps to determine.
    Process:
        1. Population claims a statistic
        2. Take a sample
        3. Observe a sample result 
        4. Ask: would this result be unusual if the original claim were true?
        5. Make a statistical decision

    Two competing statements:
        H₀ = null hypothesis
        Hₐ = alternative hypothesis 
        example:
            H₀: μ = 30
            Hₐ: μ ≠ 30
        The important logic:
            if H₀ were true, how likely would it be to observe a sample result like the one we got, or something even more extreme?
        example: 
            if the true mean is really 30:
            sample mean = 29.8 → not very surprising 
            sample mean = 29.2 → maybe still reasonable 
            sample mean = 20.7 → much more surprising
            the more unusual the sample result is under H₀, the stronger the evidence against H₀.
    Hypothesis testing eventually uses things like: 
        test statistic, p-value, α, critical region

    Hypothesis testing doesn't prove that a hypothesis is true or false.
        Reject H₀ → it doesn't mean "proved H₀ is false"
        Fail to rehect H₀ → it doesn't mean "proved H₀ is true"
    
    Example:
        A website currently has a conversion rate of 10%. A new design is tested.
            Old version: p=0.10
            New version sample: p=0.12
        Hypothesis asks:
            Is this increase from 10% to 12% large enough that it is unlikely to be explained by random variation alone?

"""

# Null hypothesis H₀ and alternative hypothesis Hₐ
"""
H₀ = null hypothesis
    Null hypothesis is the default assumption. It usually means no effect, no difference, no change, no relationship.
    example:
        A new  website design doesn't change the average purchase amount.
        H₀: μ_new = μ_old 
        H₀: μ_new - μ_old = 0

Hₐ = alternative hypothesis 
    Alternative hypothesis represents the effect or difference we are interested in detecting.
    example:
        A new  website design has different purchase amount than old one.
        Hₐ = μ_new ≠ μ_old
    
A example:
    A coffee machine company claims: The machine fills cups with an average of 250 ml.
    Thypothesis could be one of them:
        H₀: μ = 250 the true average amount is 250 
        Hₐ: μ ≠ 250 the true average amount is not 250
    take a sample:
        x̄ = 244
    if the true population mean really were 250 ml, would a sample mean of 244 ml be unusally faw away ? 
    This where test statistics and p-values come in.

Three forms of alternative hypothesis:
    1.Different    Hₐ: μ_new ≠ μ_old , example Hₐ: μ ≠ 250  
    2.Greater than Hₐ: μ_new > μ_old , example Hₐ: μ > 250
    3.Less than    Hₐ: μ_new < μ_old , example Hₐ: μ < 250
    Different(≠) form of alternative hypothesis leads a two-tailed test
    Greater(>) or less(<) forms of alternative hypothesis lead a one-tailed test
"""

# One-tailed vs two-tailed hypothesis
"""
This is mainly about the direction of the alternative hypothesis Hₐ
    one-tailed hypothesis tests are used when the hypothesis specifies a direction.
    two-tailed tests are used when we only care whether there is any difference.

Two-tailed hypothesis:
    it asks that: is the population parameter different from the hypothesized value in either direction ?
    Symbol: ≠
    example: company claims that Coffee machine average filling: 250
        H₀: μ = 250
        Hₐ: μ ≠ 250
        here: we care about both possibilities: μ < 250 and μ > 250
        So the machone could be underfilling or overfilling cups.
        μ = 240 or μ = 260
        Visually:
            Reject H₀ | Fail to reject H₀ | Reject H₀
            left tail | Center            | right tail

One-tailed Hypothesis:
    a one-tailed hypothesis asks about only one direction.
    there are two possible versions:
    
    Right-tailed test
        We want to know whether the population parameter is greater than some value.
        Hₐ: μ > population_mean
        example:
            does a new calibration make the coffee machine dispense more than 250 ml on average ?
            H₀: μ ≤ 250
            Hₐ: μ > 250
            The important direction is the right side of the distribution.

    Left-tailed test
        We want to know whether the pupulation parameter is less than some value.
        Hₐ: μ < population_mean
        example:
            does the coffee machine underfilling cups ?
            H₀: μ ≥ 250
            Hₐ: μ < 250
            now we reject region is only left side

What happens to α ?
    suppose α = 0.5
    two-tailed test:
        α = 0.5 / 2 = 0.025
        left tail = 0.025
        right tail = 0.025
    One-tail:
        α = 0.5 if it is in right-tail -> right-tail α = 0.5
        α = 0.5 if it is in left-tail -> left-tail α = 0.5
"""

# Significance level α
"""
The significance level α  is the threshold we choose before the test for deciding 
    how strong the evidence must be before we reject the H₀ null hypothesis.
    α = 0.05. This means that we are accepting a 5% Type I error rate.
    If H₀ is actually True, we are willing to tolerate up to 5% change of incorrevtly rejecting it.

    α = P(reject H₀ | H₀ is True) -> this is the probability of a Type I error.

    example: Coffee machine 
        H₀: μ = 250
        Hₐ: μ ≠ 250
        α = 0.05
        I will only reject H₀, if sample result is sufficiently unusual under the assumption that μ = 250.
        The significance level defines how unusual the result must be:
            if the result falls into the most extreme 5% of outcomes expected under H₀, then I reject H₀. 
    
    Connection with the p-value
        p < α → reject H₀
        p ≥ α → fail to reject H₀
        example:
            H₀: μ = 250
            α = 0.05
            Case-1: p = 0.02 → 0.02 < 0.05 → reject H₀          
                there is enough statistical evidence that the true average is different from 250
            Caas-2: p = 0.21 → 0.21 > 0.05 → fail to reject H₀
                there is no enough statictical evidence that the true average is different from 250

    one-tailed and two-tailed connection
        Suppose  α = 0.05
        
        one-tailed test
            the full 5% goes into one tail 
        
        two-tailed test 
            the 5% is spit: right tail 0.025 and left tail 0.025
"""

# Test statistic
"""
Test Statistic is a number that tells us how far out sample result is from what H₀ expects, mearured relative to the amount of variability in the data.
    Test statistic = observed difference / expected random variance
    For one-sample mean: 
        test statistic = (sample mean - value assumped by H₀) / standard error
        example Z-test:
            Z = (x̄ - μ₀) / (σ / √n)
            x̄ = sample mean
            μ₀ = mean assumed by H₀
            σ / √n = standard error
        example:
            H₀: μ = 250
            x̄ = 245 
            SE = 2
            Z = (245 - 250) / 2 = -2.5 
            the sample mean is 2.5 standard errors below the value expected under H₀.
        The test statistic converts row difference: 245 - 250 = -5 into standardized difference: -2.5
        because the difference of -5 units may be larger in one data and tiny in another data
            examples:
                Case-1: x̄ =245, μ₀=250, SE=10 | x= -5/10 = -0.5
                Case-2: x̄ =245, μ₀=250, SE=1 | x= -5/1 = -5
    
    Larger test statistic -> stronger evidence against H₀
        Suppose: 
            z = -3.5 | it is far from 0
            Under H₀, the expected difference is usally: x̄ - μ₀ = 0 

    More extreme test statistic -> smaller p-value -> stronger evidence against H₀
"""

# Sampling distribution under H₀
"""
The sampling Distribution under H₀ is the distribution of a statisitc we would expect to see if the null hypothesis were ture
and we repeatedly took many random samples.
    Suppose: H₀: μ = 250
        The H₀(null hypothesis) says that the true population is 250.
        Now if we repeatedly take samples of the the same size: for example - n=100
        Then calculate each sample mean: x̄₁, x̄₂, x̄₃, ... -> for example: 249.2, 251.1, 250.4, 248.9, 250.8
        those sample means from a sampling distribution. 
        Under H₀, that sampling distribution will be centered around μ₀=250.
        Because: H₀(null hypothesis) is true.
    
Why do we need sampling distribution:
    Suppose: H₀: μ = 250
        x̄₁ = 249 -> here we can't say: 249 ≠ 250 there reject H₀.
        Because sample means naturally vary.
        So instead, we ask: if H₀: μ = 250 were true, how common would a sample mean like 249 be ?
        The sampling distribution tells us that: 
            if 249 is very common under H₀, there is little evidence againt H₀.
            if we observe x̄ = 230 and the values near 230 are extremely rare under the sampling distribution μ = 250,
            the we have strong evidence against H₀.

Sampling distribution vs Population distribution
    The population distribution describes indivindual observations. For example: X = amount of coffee in an individual cup.
    THe sampling distribution deescribes a statistic across many hypotherical samples: X̄ = average amount from a sample cups.
"""

# Critical value and critical region
"""
The critical value and critical region are the boundaries we use to decide whether a test statistic is extreme enough to reject H₀ null hypothesis.

Critical Value: this is a cutoff. 
    two-tailed Z-test with α = 0.05
        the critial values are approximately -1.96 and 1.96 (these values are calculated from α=0.05)
        it means:
            if -1.96 ≤ z ≤ 1.96 -> Fail to reject H₀
            if z < -1.96 or z > 1.96 -> Reject H₀

Critical region: this is the are beyond the critical value.
    two-tailed Z-test with α = 0.05
        total rejecton area: 0.05
        we split between both tails: 0.025 + 0.025
        SO visually:
            Reject H₀     |    Fail to Reject H₀       |    Reject H₀
                        -1.96                         1.96
            to outside areas are the critical regions.

Right-tailed test:
    Hₐ: μ > 250   
    α = 0.05
    the z critical value is approximately: 1.645
    z > 1.645 -> reject H₀
    z ≤ 1.645 -> Fail to Reject H₀


Left-tailed test:
    Hₐ: μ < 250 
    α = 0.05
    the z critical value is approximately: -1.645
    z < -1.645 -> reject H₀
    z ≥ -1.645 -> Fail to Reject H₀

Critical(α) Value Formula (Conveting significance level α scale to observed value scale):
    Right-tailed:  z_c = Φ⁻¹(1 - α)
    Left-tailed:   z_c = Φ⁻¹(α)
    Two-tailed:    z_c = ±Φ⁻¹(1 - α/2)

    Python imlementation:
        from scipy.stats import norm

        alpha = 0.6
        two-tailed test:  critical_value = norm.ppf(1 - alpha / 2) -> -0.524 and +0.524
        righ-tailed test: critical_value = norm.ppf(1 - alpha) -> -0.253
        left-tailed test: critical_value = norm.ppf(alpha) -> 0.253

"""

# P-value
"""
The p-value tells us how unusual our observed test statistic would be if the null hypothesis H₀ were true.
    smaller p-value -> stronger evidence against H₀

    Case 1
        α = 0.05
        p = 0.02
        since 0.02 < 0.05 -> reject H₀
        there is enough statistical evidence against H₀

    Case 2
        α = 0.05
        p = 0.30
        since 0.30 > 0.05 -> fail to reject H₀
        there is not enough statistical evidence against H₀

Where does the p-value come from ?
    it comes from the sampling distribution under H₀
    suppose we have a Z-test and calculate: 
        z=2.0
        α = 0.05
        Two-tailed test:
            p = 2P(Z ≥ 2) 
            in Python:
                p_value = 2 * (1 - norm.cdf(abs(z))) output: 0.0456

        Right-tailed test: 
            p = P(Z ≥ 2.0) -> approximately: p=0.0228
            in Python: 
                from scipy.stats import norm
                p_value = 1 - norm.cdf(z) output:0.0228
                0.0228 < 0.05 -> reject H₀

        Left-tailed test:
            p = P(Z ≤ -2)
            in Python:
                p_value = norm.cdf(z) output:0.0228
                0.0228 < 0.05 -> reject H₀
"""

# Type I and Type II errors
"""
Type I and Type II errors are the two possible mistakes we can make when deciding whether to reject H₀
Table:
    | Reality  | Your decision     | Result       | 
    | H₀ true  | Fail to reject H₀ | Correct      | TP
    | H₀ true  | Reject H₀         | Type I error | FP
    | H₀ false | Reject H₀         | Correct      | TN
    | H₀ false | Fail to reject H₀ | Type II error| FN

"""

# Choosing the correct statistical test:
"""
Choosing the correct statistical test:
    Questions: 
        1.What am I comparing ?
        2.How many groups/samples ?
        3.Numerical or categorical ?
        4.Independent or paired ?

"""

# Z-test
"""

Z-test is a hypothesis test used when we want to compare an observed sample result with what H₀ claims, 
and test follows the standard normal distribution. 
Formula: Z = (observed result - value expected under H₀) / standard error
    in words: how many standard error awa is the observed result from what H₀ predicts ?
    Example:
        A company claims:  H₀:μ = 250
        Sample: x̄ = 246
        Suppose: σ = 20 | n = 100
        Standard Error: SE = σ / √n = 20 / √100 = 2
        Z-test: Z = (246 - 250) / 2 = -4 / 2 = -2
        The observed sample mean is 2 standard errors below the mean predicted by H₀ 

    One-Sample Z-test for a mean
        when to use:
            1.You have one sample
            2.outcome is numerical
            3.you compare the sample mean with a pypothesized population mean
            4.population standard deviation σ is known
        Example:
            company claims that the average bottle volume 500:
            H₀: μ = 500 
            Hₐ: μ ≠ 500 
        Formula:
            Z = (x̄ - μ) / (σ / √n)
    
    Two-sample Z-test for means
        When to use:
            1.you have two independet groups
            2.outcome is numerical
            3.you compare their population means
            4.population stadard deviations are known
        Example:
            is average salary different between Company A and Company B ?
            H₀: μ_A = μ_B
            Hₐ: μ_A ≠ μ_B
            the idea is: Observed difference = x̄_A - x̄_B 
        Formula:
            Z = ((X̄_A - X̄_B) - (μ_A - μ_B)₀) / √((σ_A² / n_A) + (σ_B² / n_B))

    One-proportion Z-test:
        Use when testing a proportion
        example:
            Suppose historically: p0 = 0.10
            Sample convertion rate: p̂ = 0.13
            is the true conversion rate different from 0.10(10%)?
                H₀: p = 0.10
                Hₐ: p ≠ 0.10

    Two-proportion Z-test:
        Use when comparing two proportions
        Example:
            Version_A and Version_B
            p̂_A = 0.10
            p̂_B = 0.13
            are the conversion rates different ?
                H₀: p_A = p_B
                Hₐ: p_A ≠ p_B

"""

