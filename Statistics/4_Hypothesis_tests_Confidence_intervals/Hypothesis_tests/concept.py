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
        Here: Hypothesis testing helps.
        

"""