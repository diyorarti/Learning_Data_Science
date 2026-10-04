"""
1. What hypothesis testing actually does
2. Null hypothesis H₀ and alternative hypothesis Hₐ
3. One-tailed vs two-tailed hypotheses
4. Significance level α
5. Test statistic
6. Sampling distribution under H₀
7. Critical value and critical region
8. P-value
9. Reject vs fail to reject H₀
10. Type I and Type II errors
11. Choosing the correct statistical test
12. Z-test
13. T-tests
14. Chi-square tests
15. ANOVA
16. Full practical hypothesis-test design in Python
"""

# What is Hypothesis testing
"""
Hypothesis testing is a statistical methof used to make an inference about a population using sample data.
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

"""