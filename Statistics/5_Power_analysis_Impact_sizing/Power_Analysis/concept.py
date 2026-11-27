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
    Statistical Significance vs Practical Significance

Sample Size Determination  
    Required Sample Size (n)
        1. One sample mean
        2. Two independent means
        3. Two dependent/Paired means 
        4. One sample proportion
        5. Two independent proportions
        6. Three or more means (ANOVA)
        7. Categorical goodness-of-fit
        8. Categorical independence

    Relationships between MDE, Power, α, Variance, and n
    One-sided vs Two-sided Tests
    Power Analysis for Means
    Power Analysis for Proportions
    Unequal Group Allocation (e.g., 50/50 vs. 80/20)
    Sample Size Calculation Using Formulas
    Sensitivity Analysis:
        MDE sensitivity
        Variance sensitivity
        Power and α sensitivity
        Allocation sensitivity
        Scenario-based planning

C.Experiment Planning
    1. Sample Size → Experiment Duration
    2. Traffic / Data Collection Rate
    3. Traffic Allocation Between Groups 
    4. Seasonality and Business Cycles
    5. Budget and Time Constraints
    6. Practical Assumptions and Limitations
    7. Estimating Experiment Duration in Python
"""



# POWER ANALYSIS
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

    higher statistical power is generally desirable, but achieving it usually requires a larger sample size, 
    assuming everything else remains constant.
    For example, increasing desired power from 80% to 90% will generally increase the required sample size.

    Distinction between: Power vs Significance level
        Significance Level (α)                              Statistical Power 
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
    Formula:
        d = (μ₁ - μ₀) / σ
        μ₁ = hypothesized population mean
        μ₀ = Anticipated population mean
        σ = population standard deviation
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
                H₀: the new checkout design doesn't increase conversions
                Hₐ: the new checkout design increases conversion
                Sample Size = 1000 users per gourp
                True effect size = 2 percentage point
            Assume everything remains constant except α
            When we increase α, it becomes easier to reject H₀, which increases statistical power against the specified alternative:
                ↑α ⇒ ↓β ⇒ ↑Power 
                ↓α ⇒ ↑β ⇒ ↓Power 

    The relationship between Significance Level (α) and Sample Size (n)
        example:
            a company wants to maintain 80% statistical power.
            if it decreases α from 0.05 to 0.01, the experiment must generally collect more observations compensate for the stricter rejection.
                ↑ α ⇒ n ↓
                ↓ α ⇒ n ↑

    α = probability of Type I error when H₀ is True
    β = probability of Type II error under a specified alternative
    Power = probability of rejecting H₀ under that alternative
"""

# Variance and Standard Deviation
"""
How Var/Std affects Statistical Power, Type II error and Required Sample size n.
    Relationship between Var/Std and Statistical Power.
        we want to keep sample size n fixed.
        Suppose an e-commerce company wants to determine whether a new recommendation system increases average customer spending.
        Both experiments have the same true improvement: 
                                Experiment A	Experiment B
            True effect size	10 PLN	        10 PLN
            Standard deviation	10 PLN	        30 PLN
            Variance	        100	            900
            Sample size	        100 per group	100 per group
        but variablity of customer spending differs. 
        in experiment A, the spending values are relatively concentrated around their population means.
        in experiment B, the spending values are much more spread out. True improvement is 10pln, 
            but it is hard to distinguish from random variation.
        ↑Var/Std ⇒ ↓Power ⇒ ↑β
        In other words, higher variance increases the probability of missing a real effect when sample size is fixed

    Relationship between Variance and Required Sample Size.
        we want to maintain statistical power at 80%
        the approximate sample-size formula: n ≈ [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ²
        So, ↑Var/Std ⇒ ↑n
        n ∝ σ²
            Change	                    Required sample size
            Variance doubles	        2x
            Variance triples	        3x
            Standard deviation doubles	4x
            Standard deviation triples	9x
            Standard deviation halves	0.25x
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
    Practical Significance refers to whether the magnitude of an observed effect is large enough to be meaningful or valuable 
    in real-world context.
    Example:
        α = 0.05
        p = 0.01
        p < α = 0.01 < 0.05 -> Reject H₀
        the result is statistically signifiacnt.
        but whether this improvement is practically significanct depends on the business.
        for example, if implementation the new checkout design costs €100,000.
        but the expected additional profit is only €20,000, the change may not be worth implementing.
"""



# SAMPLE SIZE DETERMINATION
# Required Sample Size (n)
"""
Required Sample Size (n)
    Required Sample Size(n) is the minimum number of observations needed in an experiment to detect a specified effect size with 
    a desired statistical power and significance level, under the assumed statistical model.

    The four key inputs required sample depends on.
        Input	                     Meaning	                                                Example
        1. Effect Size / MDE	     Smallest effect we want to detect	                        +2 percentage points
        2. Statistical Power(1-β)	 Desired probability of detecting the specified effect	    80%
        3. Significance Level(α)	 Allowed Type I error probability	                        0.05
        4. Variance(σ²)	             Variability of the outcome metric	                        Estimated from historical data
            
Statistical cases and Power Analysis:
    Case	                     Sample Size method                             Example
    One sample mean	             One-sample mean power calculation              Is average customer spending different from 100 PLN?
    Two independent sample means Two-independent-means power calculation        Is average spending different between users of website A and B?
    Two dependent sample means	 Paired-mean power calculation                  Does average spending change for the same customers before and after an intervention?
    Three or more sample means	 ANOVA power calculation                        Does average spending differ among three recommendation algorithms?
    One sample proportion	     One-proportion power calculation               Is the conversion rate different from 10%?
    Two independent proportions	 Two-proportion power calculation               Is conversion rate different between checkout designs A and B?
    Categorical goodness-of-fit	 Chi-square goodness-of-fit power calculation   Do customers choose four payment methods in the expected proportions?
    Categorical independence	 Chi-square independence power calculation      Is payment method associated with device type?

Factors affect to calculate Power analysis:
    1. Statistical scenarios:              One mean, two-means, paired means, proportions,  ANOVA,  chi-square
    2. Alterbative hypothesis:             One sided, Two sided
    3. Population variance:                known, unknown
    4. Variance assumptions:               equal or unequal group variances
    5. Group allocation:                   50/50, 80/20 etc.
 
Implemenation steps:  
    1. approximate sample size by Z-based formula
    2. calculate power for the approximated sample size
    3. increase sample size until to reach desired power
"""

# One-Sample Mean Power Analysis
"""
One-Sample Mean Power Analysis:
    Assumptions:
        1. Alterbative Hypothesis One-tailed and two-tailed: affacts calculation
        2. Population variances Known or unknown:            affects only power calculation   
        3. Population variances equal or unequal:            there is only one sample 
        4. Group allocation equal or unequal:                there is only one sample

    Sample size approximation formula(two-tailed): 
        Alternative hypothesis: two-sided:Z_(1-α/2) | left-sided:Z_(1-α) | right-sided:Z_(1-α)
        n ≈ ((Z_(1-α/2) + Z_(1-β))² * σ²) / δ²

    Power Calculation:
        Alternative hypothesis: two-sided:Z_(1-α/2) | left-sided:Z_(α) | right-sided:Z_(1-α)
        Z-based two-tailed:
            Power = Φ(-z_(1-α/2) - λ) + 1 - Φ(z_(1-α/2) - λ)
            λ = ((μ₁ - μ₀) * √n) / σ

        Alternative hypothesis: two-sided:t_(1-α/2) | left-sided:t_(α) | right-sided:t_(1-α)
        t-based right-tailed: 
            Power = P(T_(v,λ) > t_(1-α,v))
            λ = δ * √n /  σ
            v = n - 1
""" 

# Two Independent Means Power Analysis
"""              
Two Independent Means Power Analysis:
    Assumptions:
        1. Alternative hypothesis: one-sided or two-sided
        2. Population variances:   known or unknown 
        3. Population variances:   equal or unequal
        4. Group allocation:       equal or unequal

    Sample size apprixmation: 
        known or unknown population variances don't affact
        Alternative hypothesis: two-sided:Z_(1-α/2) | left-sided:Z_(1-α) | right-sided:Z_(1-α)
            equal variances 
            equal allocation:
                n ≈ (2 * (Z_(1-α/2) + Z_(1-β))² * σ²) / δ²

            equal variances 
            unequal allocation:
                n_a ≈ ((Z_(1-α/2) + Z_(1-β))² * σ² * (1 + 1 / r))  / δ²
                n_b ≈ r * n_a

            unequal variances
            equal and unequal group allocation:
                n_A ≈ ((Z_(1-α/2) + Z_(1-β))² * (σ_A² + σ_B² / r)) / δ²
                n_B = r * n_A

    Power Calculation
        Z-based power analysis:
            population vrainces are known:
            Alternative hypothesis: two-sided:Z_(1-α/2) | left-sided:Z_(α) | right-sided:Z_(1-α)
                equal variances σ_A² = σ_B²: 
                    Power = Φ(-Z_(1-α/2) - λ) + 1 - Φ(Z_(1-α/2) - λ)
                    group allocation:
                        equal:    λ = δ / (σ√(2/n)) = (δ / σ)√(n/2)
                        unequal:  λ = δ / (σ√((1/n_A) + (1/n_B)))

                unequal variances σ_A² ≠ σ_B²:
                    Power = Φ(-Z_(1-α/2) - λ) + 1 - Φ(Z_(1-α/2) - λ)
                    group allocation:
                        equal:
                            SE = √((σ_A² + σ_B²) / n)
                            λ = ((μ_B - μ_A)√n) / √(σ_A² + σ_B²)
                        unequal:
                            SE = √((σ_A² / n_A) + (σ_B² / n_B))
                            λ = (μ_B - μ_A) / √((σ_A² / n_A) + (σ_B² / n_B))

        t-based power analysis 
            population standard deviations are unknown:
            Alternative hypothesis: two-sided:t_(1-α/2, df) | left-sided:t_(α, df) | right-sided:t_(1-α, df)
                equal variances Pooled t-test: σ_A² = σ_B²:
                    Power = P(T_(df,λ) < -t_critical) + P(T_(df,λ) > t_critical)
                    Group allocation:       
                        equal allocation:   SE = σ√(2/n)
                        unequal allocation: SE = σ√((1/n_A) + (1/n_B))
                    Noncentrality parameter:
                        λ = (μ_B - μ_A) / (σ√((1/n_A) + (1/n_B)))
                    Degrees of freedom:
                        equal allocation:   df = 2 * n - 2
                        unequal allocation: df = n_A + n_B - 2

                unequal variances Welch's t-test: σ_A² ≠ σ_B²:
                    Power ≈ P(T_(df,λ) < -t_critical) + P(T_(df,λ) > t_critical)
                    Standard error:  
                        equal group allocation:   SE = √((σ_A² + σ_B²) / n))
                        unequal group allocation: SE = √((σ_A² / n_A) + (σ_B² / n_B))
                    Noncentrality: 
                        equal group allocation:   λ = (μ_B - μ_A) / SE
                        unequal group allocation: λ = (μ_B - μ_A) / SE
                    Approximate degrees of freedom:
                        equal group allocation:
                            ν ≈ ((n - 1)(σ_A² + σ_B²)²) / (σ_A⁴ + σ_B⁴)
                        unequal group allocation:
                            df ≈ ((σ_A² / n_A) + (σ_B² / n_B))² / ((σ_A⁴ / (n_A²(n_A - 1))) +(σ_B⁴ / (n_B²(n_B - 1))))

"""

# Two dependent/Paired means Power Analysis
"""
Two dependent/Paired means Power Analysis:
    Assumptions:
        1. Alterbative hypothesis: One-sided or two-sided       affects 
        2. Population variance: known or unknown                affects on power calculation
        3. Population variance assumptions: equal or unequal    no effect
        4. Group allocation: equal or unequal                   no effect

    Sample size approximation(two-tailed): 
        Alternative hypothesis: two-sided:Z_(1-α/2) | left-sided:Z_(1-α) | right-sided:Z_(1-α)
        n ≈ ((Z_(1-α/2) + Z_(1-β))² * σ_D²) / δ_D²
            δ_D = anticipated absolute mean difference
            σ_D = planning standard deviation of the paired differences
    
    Power Calculation:
        Population variances are known:
        Z-based formula:
            Two-sided:   Hₐ: μ_D ≠ 0    Power = Φ(-Z_(1-α/2) - λ) + 1 - Φ(Z_(1-α/2) - λ)
            Right-sided: Hₐ: μ_D > 0    Power = 1 - Φ(Z_(1-α) - λ)
            Left-sided:  Hₐ: μ_D < 0    Power = Φ(Z_α - λ)
            paired difference:          D_i = after_i - before_i
            Noncentrality parameter     λ = (μ_D * √n) / σ_D
            
        Population variances are unknown:
        t-based formula:
            Two-sided:   Hₐ: μ_D ≠ 0    Power = P(T_(df,λ) < -t_c) + P(T_(df,λ) > t_c)
            Right-sided: Hₐ: μ_D > 0    Power = P(T_(df,λ) > t_(1-α,df))
            Left-sided:  Hₐ: μ_D < 0    Power = P(T_(df,λ) < t_(α,df))
            paired difference:          D_i = after_i - before_i
            Noncentrality parameter:    λ = (μ_D * √n) / σ_D
            Defgrees of freedom:        df = n - 1
"""

# Three or more independent means (ANOVA) Power Analysis
"""
Three or more independent means (ANOVA) Power Analysis:
    Assumptions: 
        1. Alternative hypothesis: Three or more indpendent means is always right tailed. 
        2. Classical ANOVA estimates variance from the sample.
        3. Population variances: equal or unequal
        4. Group allocation: equal or unequal
        5. Number of groups: 3 or more

    Sample size approximation: 
        Equal variances and balanced allocation:
            Conhen's f: f = √(Σᵢ₌₁ᵏ (μᵢ - μ̄)² / (kσ²))
                        μ̄ = (Σᵢ₌₁ᵏ μᵢ) / k
            Noncentrality parameter: λ = knf²
            Degrees of freedom: df₁ = k - 1
                                df₂ = kn - k
            Minimum required sample size:
                n_min = min{n ≥ 2 : P(F_(k-1, kn-k, knf²) > F_critical) ≥ 1 - β}
                F_critical = F⁻¹(1 - α; k - 1, kn - k)
            Total sample size: N = kn
    
        Equal variances + unbalanced allocation:
            Specify allocation proportions: pᵢ = nᵢ / N,    Σᵢ₌₁ᵏ pᵢ = 1
            Calculate weighted mean:        μ_w = Σᵢ₌₁ᵏ pᵢμᵢ
            Calculate noncentrality:        λ = [N * Σᵢ₌₁ᵏ pᵢ(μᵢ - μ_w)²] / σ²
            Degrees of freedom: df₁ = k - 1
                                df₂ = N - k
            Find the required total sample size:
                N_min = min{N : P(F_(k-1, N-k, λ(N)) > F_critical) ≥ 1 - β}
            The candidate (N) must produce feasible integer group sizes under the chosen allocation proportions:
                nᵢ ≈ pᵢN

        Unequal variances and balanced allocation 
            variance-based weights:     wᵢ = n / σᵢ²
            weighted population mean:   μ_w = (Σᵢ₌₁ᵏ wᵢμᵢ) / (Σᵢ₌₁ᵏ wᵢ)
            noncentrality parameter:    λ = Σᵢ₌₁ᵏ wᵢ(μᵢ - μ_w)²
            Welch degrees of freedom:   W = Σᵢ₌₁ᵏ wᵢ
                                        df₁ = k - 1
                                        df₂ ≈ (k² - 1) / (3 * Σᵢ₌₁ᵏ ((1 - wᵢ/W)² / (n - 1)))
            required sample size:       n_min = min{n ≥ 2 : Power_Welch(n) ≥ 1 - β}
            Total sample size:          N = kn

        Unequal variances and unbalanced allocation:
            Weights:                    wᵢ = nᵢ / σᵢ²
            weighted population mean:   μ_w = (Σᵢ wᵢμᵢ) / (Σᵢ wᵢ)
            noncentrality parameter:    λ = Σᵢ wᵢ(μᵢ - μ_w)²
            welch degrees of freedom:   df₁ = k - 1
                                        df₂ ≈ (k² - 1) / (3 * Σᵢ₌₁ᵏ ((1 - wᵢ/W)² / (nᵢ - 1)))
            required sample size:       N_min = min{N : Power_Welch(n₁, ..., nₖ) ≥ 1 - β}
        
    Power Calculation:
        Equal variances and balanced allocation:
            Noncentrality parameter: λ = knf²
            Degrees of freedomL      df₁ = k - 1 | df₂ = kn - k
            Critical F-value:        F_critical = F⁻¹(1 - α; df₁, df₂)
            Statistical Power:       Power = P(F_(df₁, df₂, λ) > F_critical)

        Equal variances + unbalanced allocation
            Weighted grand mean:        μ_w = (Σᵢ₌₁ᵏ nᵢμᵢ) / N
            Noncentrality parameter:    λ = [Σᵢ₌₁ᵏ nᵢ(μᵢ - μ_w)²] / σ²
            Degrees of freedom:         df₁ = k - 1 | df₂ = N - k
            Statistical power:          Power = P(F_(df₁, df₂, λ) > F_critical)

        Unequal variances + balanced allocation
            Variance-based weights:     wᵢ = n / σᵢ²
                                        W = Σᵢ₌₁ᵏ wᵢ
            Weigheted population mean:  μ_w = (Σᵢ₌₁ᵏ wᵢμᵢ) / W
            Noncentrality:              λ = Σᵢ₌₁ᵏ wᵢ(μᵢ - μ_w)²
            Degrees of freedom:         df₁ = k - 1
                                        df₂ ≈ (k² - 1) / (3 * Σᵢ₌₁ᵏ ((1 - wᵢ/W)² / (n - 1)))
            statistical power:          Power_Welch ≈ P(F_(df₁, df₂, λ) > F_critical)

        Unequal variances + unbalanced allocation
            Weights:                    wᵢ = nᵢ / σᵢ²
            Weighted population mean:   μ_w = (Σᵢ wᵢμᵢ) / (Σᵢ wᵢ)
            noncentrality:              λ = Σᵢ wᵢ(μᵢ - μ_w)²
            Degrees of freedom:         df₁ = k - 1
                                        df₂ ≈ (k² - 1) / (3 * Σᵢ₌₁ᵏ ((1 - wᵢ/W)² / (nᵢ - 1)))
            statistical power           Power_Welch ≈ P(F_(df₁, df₂, λ) > F_critical)
"""

# One Sample Proportion Power Analysis
"""
One Sample Proportion Power Analysis
    Assumptions:
        1. Alternative Hypothesis:                  Left-Tailed, Righted-Tailed, Two-sided
        2. Population variance known or unknow:     not a separate choice
        3. Population variances equal or unequal:   Not applicable
        4. Group allocation equal or unequal:       Not applicable

    Sample size approximation:
        n ≈ [Z_critical * √(p₀(1 - p₀)) + Z_(1-β) * √(p₁(1 - p₁))]² / (p₁ - p₀)²
            p₀ = Population proportion under the null hypothesis
            p₁ = Anticapated population proportion under the alternative hypothesis
            δ = p₁ - p₀ = Minimum detectable effect MDE
            1 - β = Desired statistical power

    Power calculation:
        Standard Error:
            Under Null Hypothesis:        SE₀ = √(p₀(1 - p₀) / n)
            Under alternative hypothesis: SE₁ = √(p₁(1 - p₁) / n)
        Power calculation:
            Two-sided Hₐ: p ≠ p₀: 
                Power ≈ Φ((p₀ - Z_(1-α/2)SE₀ - p₁) / SE₁) + 1 - Φ((p₀ + Z_(1-α/2)SE₀ - p₁) / SE₁)
            Right-sided Hₐ: p > p₀
                Power ≈ 1 - Φ((p₀ + Z_(1-α)SE₀ - p₁) / SE₁)
            Left-sided Hₐ: p < p₀:
                Power ≈ Φ((p₀ + Z_α SE₀ - p₁) / SE₁)
"""

# Two Independent Proportions power analysis
"""
Two independent Proportions power Analysis
    Assumptions:
        Alternative hypothesis:     one-tailed or two-tailed
        Group allocation:           Equal or Unequal
        population variances:       not a seperate method 
        equal or unequal variances: not a seperate method
    
    Sample size approximation:
        equal group allocation: 
            n ≈ [Z_(1-α/2) * √(2p̄(1 - p̄)) + Z_(1-β) * √(p_A(1 - p_A) + p_B(1 - p_B))]² / (p_B - p_A)²
            total sample size: N = 2n
        unequal group allocation: 
            n_A ≈ [Z_(1-α/2) * √(p̄(1 - p̄)(1 + 1/r)) + Z_(1-β) * √(p_A(1 - p_A) + p_B(1 - p_B)/r)]² / (p_B - p_A)²
            n_B ≈ r * n_A
            N = n_A + n_B

    Power Calculation:
        equal group allocation:
            Standard Error:
                Under the null hypothesis:        SE₀ = √((2p̄(1 - p̄)) / n)
                Under the alternative hypothesis: SE₁ = √((p_A(1 - p_A) + p_B(1 - p_B)) / n)
            expected difference: δ = p_B - p_A
            Power ≈ Φ((-Z_(1-α/2)SE₀ - δ) / SE₁) + 1 - Φ((Z_(1-α/2)SE₀ - δ) / SE₁)

        unequal group allocation:
            Standard Error:
                Under the null hypothesis:        SE₀ = √(p̄(1 - p̄) * ((1 / n_A) + (1 / n_B)))
                Under the alternative hypothesis: SE₁ = √((p_A(1 - p_A) / n_A) + (p_B(1 - p_B) / n_B))
            Expected difference: δ = p_B - p_A
            Power ≈ Φ((-Z_(1-α/2)SE₀ - δ) / SE₁) + 1 - Φ((Z_(1-α/2)SE₀ - δ) / SE₁)
"""

# Categorical goodness-of-fit power analysis
"""
Categorical goodness-of-fit power analysis
    Assumptions:
        alternative hypothesis:                         not a seperate choise 
        population variances known or unknown:          not a seperate choise
        equal vs unequal population variances:          not a seperate choise 
        group allocation equal or unequal:              not a seperate choise
        number of categories(k):                        affects, determines degrees of freedom
        expected and anticipated category proportions:  affects, determines effect size
    
    Implementation:
        Calculate Cohen's w:        w = √(Σᵢ₌₁ᵏ ((p₁ᵢ - p₀ᵢ)² / p₀ᵢ))
        noncentrality parameter:    λ = nw²
        degrees of freedom:         df = k - 1
        Statistical Power:          Power = P(χ²_(df, λ) > χ²_critical)
                                    χ²_critical = χ²_(1-α, df)
        Required sample size:       n_min = min{n : P(χ²_(k-1, nw²) > χ²_(1-α, k-1)) ≥ 1 - β}
"""

# Categorical independence Power analysis
"""
Categorical independence Power analysis
    Assumptions:
        Group allocation:           Category proportions affect effect size and sample size
        Number of categories:   	Determines degrees of freedom
        Strength of association: 	Determines Cohen's w
"""




# Relationships between MDE, Power, α, Variance, and n
"""
Relationship between MDE and n
    Smaller MDE → Larger required sample size.
    Why? Detecting a very small improvement is more difficult because it can be hidden by random sampling variation.
    n ∝ 1 / MDE²

Relationship between Power and n
    Higher desired statistical power → Larger required sample size.
    Power is the probability of rejecting H₀ when a specified alternative is true.
    Increasing power from 80% to 90% means you want a higher chance of detecting the same true effect.
    To achieve this while keeping MDE, α, variance and design constant, you generally need more observations

Relationship between α and n 
    Lower significance level → Larger required sample size.
    a smaller α means stricter evidence is required to reject H₀.
    Suppose the company changes α = 0.05 → 0.01. This decreases the allowed Type I error probability from 5% to 1%.
    But maintaining the same statistical power now requires a larger sample. 

Relationship between Variance and n
    Higher variance → larger required sample size

Relationship Table:
    Parameter changes          Required n      Reason
    -----------------------------------------------------------------------------
    MDE increases              ↓ Decreases     Larger effects are easier to detect
    MDE decreases              ↑ Increases     Smaller effects are harder to detect
    power increases            ↑ Increases     Greater detection probability is required
    power decreases            ↓ Decreases     Lower detection probability is accepted
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

# Unequal Group Allocation
"""
Group allocation
    Group allocation describes how participants are distributed between the control and treatment groups.
    example:
        an E-commerce company has 10,000 users available for an A/B test.
        50/50 allocation: 5,000 users in each group = equal group allocation
        80/20 allocation: 8,000 users in the control group and 2,000 users in the treatment group = unequal group allocation

    The main principle: with equal group allocation and a fixed total sample size, a 50/50 allocation usually provides greater 
    statistical power than an unequal allocation.
    Why:
        the main reason is that unequal group allocation increases the standard error of the estimated difference between groups,
        assuming the sample the same total sample size and equal population variances.

    Why does unequal group allocation affect statistical power ?
        Vairance of two independent groups:         Var(X̄_B - X̄_A) = (σ_A² / n_A) + (σ_B² / n_B)
            σ_A² = 1225
            σ_b² = 1225
            50%/50% group-allocation: Var(X̄_B - X̄_A) = (1225 / 500) + (1225 / 500) = 4.9
            80%/20% group-allocation: Var(X̄_B - X̄_A) = (1225 / 800) + (1225 / 200) = 7.65625
            Interpretation: Across repeated experiments with 800 control customers and 200 treatment customers, 
            the estimated difference between sample means has a sampling variance of 7.65625 PLN², under the assumptions.

        Standard Error of two independent grups:    SE(X̄_B - X̄_A) = √((σ_A² / n_A) + (σ_B² / n_B))
        example:
            σ_A = 35
            σ_b = 35
            50%/50% group-allocation: SE =  √(35 ** 2 / 500) + (35 ** 2 / 500) = 2.214
            80%/20% group-allocation: SE =  √(35 ** 2 / 800) + (35 ** 2 / 200) = 2.767
            interpretation: 2.767 / 2.214 = 1.25 This means unequal allocation produces a 25% larger standard error in this example, 
            even though both experiments have 1,000 participants.
        Conclusion:
            SE ↑ ⇒ Power ↓
    
        How many additional observations ?
            for equal population variances: N_unequal / N_50/50 = (1 + r)² / (4r)
            r = n_B / n_A
            example: For 80/20 allocation
                r = 20 / 80 = 0.25
                N_80_20 / N_50_50 = (1 + 0.25)** / (4 * 0.25) = 1.5625
                This means 80/20 allocation requires approximately 56.25% more total observations than 
                50/50 allocation to maintain the same statistical power, under the stated assumptions.
    When to use unequal Group allocation:
        Case 1 is a statistical reason. Unequal allocation can actually improve statistical efficiency 
            when the groups have different population variances.
        Cases 2 and 3 are business reasons. Unequal allocation may reduce risks or costs, even though it can require more total observations.
        
        Decision rule:
            Equal variances:         similar costs, low risk: Usually start with 50/50.
            Different variances:     Consider allocating more observations to the higher-variance group.
            Risky treatment:         Consider limiting treatment exposure.
            Expensive treatment:     Consider allocating fewer observations to the costly treatment.
    
    Calculate Power Analysis for Unequal Group Allocation:
        step-1: Calculate the ratio
            r = n_B(treatment) / n_A(Control)  for 80(control)/20(treatment) allocation: r = 0.20 / 0.80 = 0.25
                this means the treatment group must contain one-quater as many observations as the control group.
        step-2: Sample-size Formual
            n_a = ((Z_(1-α/2) + Z_(1-β))² * σ² * (1 + 1/r)) / δ²
            n_b = r * n_a
            N = n_a + n_b
        
        example:
            Parameter	            Value
            α	                    0.05
            Power               	0.80
            β	                	0.20
            Standard deviation σ    35 PLN
            MDE δ               	8 PLN
            Control allocation	    80%
            Treatment allocation	20%
            Alternative	            Two-sided

            r = 0.20 / 0.80 = 0.25
            z_1-α/2 = 1.9600
            z_b-β = 0.8416
            n_a = (1.9600 + 0.8416)² * 35² * (1 + 1 / 0.25) + 8² = 751.16 = 752
            n_b = 0.25 * 752 = 188
            N = 752 + 188 = 940


    
    Sample Size Formula for Unequal Group Allocation
        For unequal group allocation, introduce the allocation ratio: r = n_A / n_B
        For a two-sided test with common variance:
            N = n_a + n_b 

        For unequal variance the general normal approximation formula:
            n_a = ((Z_(1-α/2) + Z_(1-β))² * (σ_A² + σ_B² / r)) / δ²
            n_b = r * n_a
            N = n_a + n_b
"""

# Sample Size Calculation Using Formulas
"""
General Procedure:
    1. Choose the statistical : Z-test, t-test, chi-square test, ANOAVA, etc.
    2. Specify the MDE: the smallest effect our experiment should be able to detect.
    3. Choose α and power: Common choices are α=0.05 and power=80%
    4. Estimate variablity: Standard deviation, proportion, or standardized effect size, depending on the test.
    5. Apply the appropriate formula: calculate and round the required sample size upward.

    Example:
        an E-commerce company wants to test whether a new recommendation algorithm increase average customer spending.
        Parameters                  Value
        Control mean                100 PLN
        Treatment mean to detect    110 PLN
        MDE δ                       10 PLN
        Population SD σ             30 PLN
        Significance level α        0.05
        Statistical power           80%
        Allocation                  50/50
        Test                        Two-sided, Two-independent means Z-test

        1-step: The sample size foruma: n ≈ (2 * (Z_(1-α/2) + Z_(1-β))² * σ²) / δ²
        2-step: Find the critical Z-values:
            α = 0.05 -> Z_(1-α/2) = Z_0.975 = 1.96
            Power = 80% -> Z_(1-β) = Z_0.80 = 0.8416
        3-step: n = (2 * (1.96 + 0.8416)² * 30²) / 10² = 141.28 -> 142 customers per group 142 + 142 = 284 total.
"""

# Sensitivity Analysis 
"""
Sensitivity Analysis is a technique used to examine how changes in input assumptions affect the result of a statistical analysis.
    In power analysis, it helps us understand how changes in parameters such as MDE, Var, α and power affect:
        required sample size
        achievable statistical power
        minimum detectable effect 
        feasibility of an experiment
    example: an e-commerce company wants to run A/B test to determine whether a new recommendation algorithm increases avera customer spending.
        initially, the company assumes:
            MDE = 10 PLN
            Std = 30 PLN
            α   = 0.05
            Power = 80%
            allocation = 50/50
            statistical test = two-sided indepdent-means test
            using the normal approximation: n ≈ (2 * (Z_(1-α/2) + Z_(1-β))² * σ²) / δ²  -> we obtain 142 customers per group, 284 in total.
        But what if our assumptions are wrong ?
        Std is 40 instead of 30 or MDE is 5 PLN or Power is 90% 
        Sensitivity Analysis answers these questions.

    Two main types of Sensitivity Analysis:
        1.Sample-size Sensitivity Analysis:
            We fix the sedired power and examine how changes in the other parameters affect required sample size.
            for example:
                MDE decreases = Sample size increases
                Variance increases = Sample size increases
                Power increases = Sample size increases 

        2.Statistical-power Sensitivity Analysis:
            We fix the available sample size and examine how changes in the other parameters affect the achievable power.
            for example:
                if we have only 500 customers, will we achieve 80% power when the true effect is 5 PLN ?
                What about 10 PLN
            this second type is particulary useful when a company has limited traffic or budget.

    MDE Sensitivity
        MDE Sensitivity Analysis evaluates how different detectable-effect assumptions change required sample size or achievable statistical power.
        The central relationship is n ∝ 1 / MDE²
        Main types:
            Fixed desired power: change MDE and calculate required sample size
            Fixed sample size: Change the assumed true effect and calculate achievable power
    
    Variance Sensitivity
        Variance Sensitivity Analysis examines how different assumptions about population variability affect the required sample size 
        and achievable statistical power.
        The main relationship: n ∝ σ²
        For fixed desired power:
            Variance ↑ ⇒ n ↑
            Variance ↓ ⇒ n ↓
        For fixed sample size:
            Variance ↑ ⇒ Power ↓
            Variance ↓ ⇒ Power ↑

    Power and α Sensitivity Analysis:
        Power and α Sensitivity Analysis evaluates how different combinations of desired statistical power and significance levels 
        influence required sample size or achievable statistical power.
            Change	                  Required n (power fixed)	    Achieved power (n fixed)
            Desired power target ↑	    ↑	                        Target itself is a planning choice
            Desired power target ↓	    ↓	                        Target itself is a planning choice
            α↑	                        ↓	                        ↑
            α↓	                        ↑	                        ↓

    Allocation sensitivity Analysis:
"""

