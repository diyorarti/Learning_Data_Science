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
    Power Analysis for Means
    Power Analysis for Proportions
    Unequal Group Allocation (e.g., 50/50 vs. 80/20)
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
        How much data do we need to have a suffuciently high probability of detecting a real effect, if that effect exists?
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
        --------------------------------------------------------
        H₀ is true	        Type I Error(α) 	Correct decision
        H₀ is false	        Power(1-β)	        Type II Error (β)

    higher statistical power is generally desirable, but achieving it usually requires a larger sample size, assuming everything else remains constant.
    For example, increasing desired power from 80% to 90% will generally increase the required sample size.

    Distinction between: Power vs Significance level
        Significance Level (α)                              Statistical Power (β)
        --------------------------------------------------------------------------
        Probability of rejecting (H₀) when it is true	    Probability of rejecting (H₀) when a specified alternative is true
        Controls Type I error	                            Measures ability to detect a real effect
        Common value: 5%	                                Common value: 80%
        Typically chosen before the test	                Typically targeted before the test
    
    Type II erorr β = 1 - Power 
        example:
            Power = 0.90 then Type II = 1 - 0.90 = 0.10
"""

# Effect Size and Minimum Detectable Effect (MDE)
"""
Effect Size is a quantitive measure of the magnitude of a difference between groups or the strength of a relationship between variables.
    Effect size tells us how big a difference or relationship is, rather than whether it is statistically significant.
    In A/B testing, it commonly refers to the difference between a treatment group and a control group
        Effect-size = μ_B - μ_A
            μ_A = 100 pln
            μ_B = 120 pln
            Effect-size = 120 - 100 = 20 pln
    For binary outcome such as conversion, we take the difference in proportions:
        Effect-size = p_B - p_A
        suppose an e-commerce company tests a new checkout design. 
            Group A (Control) = 10%
            Group B (Treatment) = 12%
            Effect-size = p_B - p_A = 0.12 - 0.10 = 0.02

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
How Significance Level (α) effects Statistical power and Sample Size (n)
    The relationship between Significance Level (α) and Statistical Power
        example:
            Suppose an e-commerce company conducts an A/B test:
                H₀ : the new checkout design doesn't increase conversions
                Hₐ : the new checkout design increases conversion
                Sample Size = 1000 users per gourp
                True effect size = 2 percentage point
            Assume everything remains constant except α
            When we increase α, it becomes easier to reject H₀ , which increases statistical power against the specified alternative:
                ↑ α ⇒ ↑ Power ⇒ β ↓
                ↓ α ⇒ ↓ Power ⇒ β ↑

    The relationship between Significance Level (α) and Sample Size (n)
        example:
            a company wants to maintain 80% statistical power.
            if it decreases α from 0.05 to 0.01, the experiment must generally collect more observationsto compensate for the stricker rejection.
                ↑ α ⇒ n ↓
                ↓ α ⇒ n ↑

    α = probability of Type I error when H₀ is True
    β = probability of Type II error under a specified alternative
    Power = probability of rejecting H₀ under that alternative
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

# One-sided vs Two-sided Tests
"""
A one-sided test generally requires a smaller sample size than a two-sided test when detecting an effect in its prespecified direction,
    assuming the same MDE, power, variance and significance level.
    A one-sided test concentrates its rejection region in one direction. A two-sided test must account for effects in both directions, 
    so its rejection thresholds are more stringent in either indivitual direction.

    Sample-size formulas:
        One-sided test: n ≈ [2 * (Z_(1-α) + Z_(1-β))² * σ²] / δ²
        Two-sided test: n ≈ [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ²

    example:
        Suppose a company wants to detect a 10pln improvement in average spending.
        Assumptions:
            Parameter	        Value
            MDE	                10 PLN
            Standard deviation	30 PLN
            Power	            80%
            α	                0.05
            Groups	            Two independent, equal-sized
        using the normal-approximation formulas:
            one-sided test requires 112 users per group
            two-sided test requires 142 users per group
            two-sided test requies 27% more observations then the one-sided test in this example.
"""

# Power Analysis for Means
"""
Power Analysis for Means is a statistical method used to determine the sample size required to detect a speficied difference 
    in population means with a desired statistical power and significance level.

    Example:
        an e-ecommerce company wants to evaluate whether a new recommendation algorithm increases average customer spending.
        Company wants to detect an increase of  δ = 110 - 100 = 10pln.
        We need to determine the sample size needed to detect this difference with 80% statistical power and α=0.05.
    
    Types of Power Analysis For Means:
        1.One-sample-mean - Compare one population mean with a specified reference value - is average order value different from 100pln?
        2.Two independent means - Compare means from two indepenent groups - Do customers using design B spend more than customers using design A?
        3.Paired means - Compare related observations - Does spending change for the same customers before and after an intervetion ?

    One-Sample Power Analysis For a Mean:
        Suppose the historical average order value is 100pln
        We want to detect whether the population mean differs from 100pln by at least 10pln
        Assume:
            H₀: μ = 100
            Hₐ: μ ≠ 100
            δ = 10
            σ = 30
            α = 0.05
            Power = 80%
        For a Two-sided one-sample Z-test with known population standard deviation m the apporimate formula:
            n = [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ² -> n ≈ ((1.96 + 0.84)² × 30²) / 10² ≈ 70.6

    Two Independent Means 
        Suppose customers are randomly assigned to two groups:
            - Group A receives the current recommendation algorithm
            - Group B receives the new recommendation algorithm
        We want to detect a mean spending difference of 10pln
        Formula For two independent groups with equal sizes, equal population variance, and a two-sided test:
            n = [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ² 
            Var(X̄_B - X̄_A) = (σ_A² / n_A) + (σ_B² / n_B) = 2σ² / n
            n ≈ [2(1.96 + 0.84)² × 900] / 100 ≈ 141.1
            per group = 142, total samples 284

    Paired Means
        Now imagine measuring the same customers before and after a change.
        each customer contributes two measurements, producing a paired differences.
            Dᵢ = X_after_i - X_before_i
        instead of comparing independent means, we analyze the mean of these differences
        approximate two-sided sample-size formula:
            n ≈ ((Z_(1-α/2) + Z_(1-β))² * σ_D²) / δ_D²
        Paired power analysis uses the standard deviation of the differences, not individual measurements.
"""

# Power Analysis for Proportions
"""
Power Analysis for Proportions is a statistical method used to determine the sample size required to detect a specified
    difference in population proportions with a desired statistical power and significance level.
    How many observations do we need to detect a meaningful difference in conversion rates, success rates, or other proportions ?

    Two types of power analysis for proportions:
        One-proportion test - compare a population proportion against a reference.
        Two-proportion test - compare proportions from two independent groups.

    Two-Proportion Power Analysis
        Suppose an e-commerce company wants to test whether a new checkout design increase its conversion rate.
            Group A - 10% Control  
            Group B - 12% Treatment 
            Company wnat to detect an improvement of: δ = p_B - p_A = 0.12 - 0.10 = 0.02
            Absolute MDE = 2 percentage points
            Relative MDE = 20%
            Assuming: α = 0.05 | power = 0.80
            Goal is to determine the sample size needed per group
        For two indpendent proportions, equal group sizes and a two-sided Z-test:
            n ≈ [Z_(1-α/2) * √(2p̄(1-p̄)) + Z_(1-β) * √(p_A(1-p_A) + p_B(1-p_B))]² / (p_B - p_A)²


    One-Proportion Power Analysis
        Suppose the company has a historical conversion-rate benchmark of 10%
            it wants to determine whether the current conversion rate differs from 10% using only one sample.
            Hypothesis:
                H₀: p = 10
                Hₐ: p ≠ 10

            Suppose the smallest difference of interest is 2 percentage points, so we plan an alternative proportion of 12%.
        For two-sided one-sample proportion Z-test 
            n ≈ [Z_(1-α/2) * √(p₀(1-p₀)) + Z_(1-β) * √(p₁(1-p₁))]² / (p₁ - p₀)²
"""

# Unequal Group Allocation (e.g., 50/50 vs. 80/20)
"""

"""