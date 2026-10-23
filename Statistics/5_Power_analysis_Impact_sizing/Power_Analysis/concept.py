# Power Analysis 
"""
Power Analysis
    A. Fundamentals
        1. What is Power Analysis?
        2. Statistical Power (1-β)
        3. Type II Error (β)
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
        How much data do we need to have a suffuciently high probability of detecting a real effect, it that effect exists ?
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

"""