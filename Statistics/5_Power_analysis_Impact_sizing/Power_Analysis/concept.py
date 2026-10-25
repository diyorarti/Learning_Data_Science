# Power Analysis 
"""
Power Analysis
    What is Power Analysis?
    Statistical Power (1-β)
        4. Effect Size and Minimum Detectable Effect (MDE)
            - Absolute vs. relative MDE
            - Standardized effect size (Cohen's d)
        5. Significance Level (α)
        6. Variance and Standard Deviation
        7. Statistical Significance vs. Practical Significance

    B. Sample Size Determination
        1. Required Sample Size (n)
        2. Relationships between MDE, Power, α, Variance, and n
        3. One-sided vs. Two-sided Tests
        4. Power Analysis for Means
        5. Power Analysis for Proportions
        6. Unequal Group Allocation (e.g., 50/50 vs. 80/20)
        7. Sample Size Calculation Using Formulas
        8. Sensitivity Analysis
    C. Practical Power Analysis in Python
        1. TTestIndPower — Power analysis for comparing means
        2. NormalIndPower — Power analysis using normal approximations
        3. proportion_effectsize — Standardized effect size for proportions
        4. Calculate Required Sample Size
        5. Calculate Statistical Power for a Given Sample Size
        6. Visualize Relationships between Power, Effect Size, and Sample Size
        7. Interpret Results and Make Recommendations
    D. Experiment Planning
        1. Sample Size → Experiment Duration
        2. Traffic / Data Collection Rate
        3. Traffic Allocation Between Groups
        4. Seasonality and Business Cycles
        5. Budget and Time Constraints
        6. Practical Assumptions and Limitations
        7. Estimating Experiment Duration in Python
"""

# Power Analysis 
"""
What is Power Analysis?
    Power Analysis is a statistical method used to determine how many observations(Sample Size) are needed
    to detect a meaningful effect with a specified level of statistical power.
    IT answers this question: 
        How much data do we need to have a suffuciently high probability of detecting a real effect, itf that effect exists ?
    Example:
        An e-commerce company wants to test whether a new checkout design increases the purchase conversion rate.
        Question: How many users should particiate in each group to reliably detect this improvement ?
        Power Analysis answers this.
        Without Power Analysis, two major problems can occur.
            Case-1: Sample size too small -> fail to detect a real improvement.
            Case-2: Sample size too large -> waste of time, resources and money.
""" 

# Statistical Power (1-β)
"""
Statistical Power is the probability of correctly rejecting the null hypothesis (H₀) when the null hypothesis is actually false.
    Formula:
        Power = 1 - β
        β = probability of Type II error
        example: Power = 1 - 0.20 = 0.80 
        Interpretation:
            if a particular real effect exists, an experiment designed with 80% power has 80% probability of detecting 
            it as statistically significant, under the assumed effect size and other conditions.
        
    Relationship between Statistical power and Type II Error
        Actual situation	Reject H₀	        Fail to reject H₀
        H₀ is true	        Type I Error(α) 	Correct decision
        H₀ is false	        Power(1-β)	        Type II Error (β)

    higher statistical power is generally desirable, but achieving it usually requires a larger sample size, assuming everything else remains constant.
    For example, increasing desired power from 80% to 90% will generally increase the required sample size.

    Distinction between: Power vs Significance level
        Significance Level (α)                              Statistical Power (β)
        Probability of rejecting (H₀) when it is true	    Probability of rejecting (H₀) when a specified alternative is true
        Controls Type I error	                            Measures ability to detect a real effect
        Common value: 5%	                                Common value: 80%
        Typically chosen before the test	                Typically targeted before the test
    
    Type II erorr = 1 - Power 
        example:
            Power = 0.90 then Type II = 1 - 0.90 = 0.10
"""

# Effect Size and Minimum Detectable Effect (MDE)
"""
Effect Size is a quantitive measure of the magnitude of a difference between groups or the strength of a relationship between variables.
    In A/B testing, it commonly refers to the difference between a treatment group and a control group
    Effect-size = μ_B - μ_A
    For binary outcome such as conversion, we take the difference in proportions:
    Effect-size = p_B - p_A

Minimum Detectable Effect (MDE) is the smallest true effect size that an experiment is designed to detect with a specified 
    statistical power and  significance level.
    example:
        company's conversion rate is 10%
        the product team decides that an improvement of at least 1 percentage point would be meaningful.
        MDE = 0.01
        The experiment is designed to detect a change from 10% -> 11%

Absolute and Relative MDE
    Absolute MDE represents the difference between two values in their original units.
        For conversion rates:
            MDE_absolute = p_B - p_A -> 12% - 10% = 2 percentage points, not 2%

    Relative MDE represents the change relative to the baseline value.
        MSE_relative = (p_B - p_A) / p_A * 100% -> (0.12 - 0.10) / 0.10 * 100% = 20%

Standardized Effect Size (Cohen's d)
    
"""

