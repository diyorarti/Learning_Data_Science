# Power Analysis 
"""
Power Analysis
    What is Power Analysis?
    Statistical Power (1-β)
    Effect Size and Minimum Detectable Effect (MDE)
        Absolute vs. relative MDE
        Standardized effect size (Cohen's d)
    Significance Level (α)
    Variance and Standard Deviation
    Statistical Significance vs. Practical Significance

Sample Size Determination
    Required Sample Size (n)
    Relationships between MDE, Power, α, Variance, and n
    One-sided vs Two-sided Tests
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
        How much data do we need to have a suffuciently high probability of detecting a real effect, if that effect exists ?
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
    It is the method used to express two different scale experiment outcomes:
    example:
        Experiment_A measures the difference in monthly spending (PLN)
        Experiment_B measures the difference in session duraction (minuted)
    Cohens'd is a standardized effect size that expresses the difference between two group means in units of standard deviation.
"""

# Significance Level (α)
"""
Assuming other relevant factors remain constant:
    Higher α → Higher statistical power
    Lower α  → Lower statistical power
    Lower α  → Larger required sample size (at fixed power)
    Higher α → Smaller required sample size (at fixed power)
    Trade-off: Lowering α reduces the Type I error rate, but achieving the same statistical power requires more observations.
"""

# Variance and Standard Deviation
"""
Higher Var/Std means more noise, which makes it harder to distinguish a real effect from sampling variation.
    example:
        A/B test to determine whether a new recommendation algorithm increases customer spending
        μ_A = 100  | μ_B = 110 -> δ = μ_B - μ_A = 10
        σ_A = 10   | σ_B = 30 
        Here, Experiment_B needs a larger sample size to detect the same 10pln customer spending improvement with the same statistical power.
    
    Relationship Var/Std and Power
        ↑σ²/σ ⇒ ↓Power
        ↓σ²/σ ⇒ ↑Power
    
    Relationship Var/Std and Sample Size
        ↑σ²/σ ⇒ ↑n(sample-size)
        ↓σ²/σ ⇒ ↓n(sample-size)
"""

# Statistical Significance vs Practical Significance
"""
Statistical significance
    Statistical Significance means that the observed result is sufficiently inconsistent with the null hypotheis H₀ 
    to reject it at the chosen significance level(α)
    Decision rule:
        p < α  ⇒ Reject H₀
        p > α  ⇒ Fail to Reject H₀
    example:
        an e-commerce company runs an A/B test comparing two checkout designs.
        α = 0.05
        p = 0.01
        0.01 < 0.05 ⇒ reject H₀
        there is statistically significant evidence that the conversion rates differ.
        However, statistical significance doesn't tell us whether the difference is large enough to matter to the business.
        That is where practical significance comes in.
    
Practical Significance
    Practical Significance refers to whether the magnitude of an ebserved effect is large enough to be meaningful or valuable in real-world context.
    Example:
        α = 0.05
        p = 0.01
        p < α = 0.01 < 0.05 -> Reject H₀
        the result is statistically signifiacnt.
        but whether this improvement is practically significanct depends on the business.
        for example, if implementation the new checkout design costs €100,000 annually 
        but the expected additional profit is only €20,000, the change may not be worth implementing.

Connection with Power Analysis and MDE
    When planning an experiment, Data scienctists should identify an effect that would be partically meaningful to the business.
    That effect can guide the selection of the Minimum Detectable Effect (MDE)
"""

# Required Sample Size (n)
"""
Required Sample Size (n)
    Required Sample Size(n) is the minimum number of observations needed in an experiment to detect a specified effect size with 
    a desired statistical power and significance level, under the assumed statistical model.

    The four key inputs required sample depends on.
        Input	                 Meaning	                                                Example
        Effect Size / MDE	     Smallest effect we want to detect	                        +2 percentage points
        Statistical Power(1-β)	 Desired probability of detecting the specified effect	    80%
        Significance Level(α)	 Allowed Type I error probability	                        0.05
        Variance(σ²)	         Variability of the outcome metric	                        Estimated from historical data
    
    Required sample size per group formula when comparing two independent population means.
        n ≈ [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ²
        n = required sample size per group
        Z_(1-α/2 = Standard normal quantile for significance
        Z_(1-β) = Standard normal quantile for desired power
        σ² = common population variance
        δ = minimum detectable difference between means
        used when:
            1. two independent groups are being compared 
            2. the outcome is continuous 
            3. two groups have equal population variance
            4. equal sample sizes are planned for both groups
            5. observations are independent, and a normal approximation is appropriate.
"""

# Relationships between MDE, Power, α, Variance, and n
"""
Relationship between MDE and n
    Smaller MDE → Larger required sample size.
    Why? Detecting a very small improvement is more difficult because it can be hidden by random sampling variation.
    n ∝ 1 / MDE²

Realtionship between Power and n
    Higher desired statistical power → Larger required sample size.
    Power is the probability of rejecting H₀ when a specified alternative is true.
    Increasing power from 80% to 90% means you want a higher chance of detecting the same true effect.
    To achaive this while keeping MDE, α, variance and design constant, you generally need more observations

Relationship between α and n 
    Lower significance level → Larger required sample size.
    a smaller α means stricter evidence is required to reject H₀.
    Suppose the company changes α = 0.05 → 0.01. This decreases the allowed Type I error probability from 5% to 1%.
    But mainintaing the same statistical power now requires a larger sample. 

Relationship between Variance and n
    Higher variance → larger required samole size

Relationship Table:
    Parameter changes          Required n      Reason
    -----------------------------------------------------------------------------
    MDE increases              ↓ Decreases     Larger effects are easier to detect
    MDE decreases              ↑ Increases     Smaller effects are harder to detect
    Desired power increases    ↑ Increases     Greater detection probability is required
    Desired power decreases    ↓ Decreases     Lower detection probability is accepted
    α increases                ↓ Decreases     Less stringent rejection threshold
    α decreases                ↑ Increases     More stringent rejection threshold
    Variance increases         ↑ Increases     More noise
    Variance decreases         ↓ Decreases     Less noise
"""

# One-sided vs. Two-sided Tests
"""

"""