# Power Analysis — Concept Revision Notebook

**Your original notes, organized for daily reading.** Topic order, explanations, examples, and source formulas are preserved. Mathematical notation is additionally typeset where possible.

> **Presentation only:** Existing mistakes or unfinished topics in the source have **not** been silently corrected or expanded. This notebook is a readable version, not a fact-checked revision.

## Contents

- [Original learning roadmap](#original-learning-roadmap)
- [Power Analysis](#power-analysis)
- [Statistical Power (1-β)](#statistical-power-1-β)
- [Effect Size and Minimum Detectable Effect (MDE)](#effect-size-and-minimum-detectable-effect-mde)
- [Significance Level (α)](#significance-level-α)
- [Variance and Standard Deviation](#variance-and-standard-deviation)
- [Statistical Significance vs Practical Significance](#statistical-significance-vs-practical-significance)
- [Required Sample Size (n)](#required-sample-size-n)
- [Relationships between MDE, Power, α, Variance, and n](#relationships-between-mde-power-α-variance-and-n)
- [One-sided vs Two-sided Tests](#one-sided-vs-two-sided-tests)
- [Power Analysis for Means](#power-analysis-for-means)
- [Power Analysis for Proportions](#power-analysis-for-proportions)
- [Unequal Group Allocation](#unequal-group-allocation)
- [Sample Size Calculation Using Formulas](#sample-size-calculation-using-formulas)
- [Sensitivity Analysis](#sensitivity-analysis)
- [TTestIndPower — Power analysis for comparing means](#ttestindpower--power-analysis-for-comparing-means)

## Original learning roadmap

Power Analysis  

**What is Power Analysis?**

&nbsp;&nbsp;Statistical Power (1-β)  
&nbsp;&nbsp;Effect Size and Minimum Detectable Effect (MDE)  
&nbsp;&nbsp;&nbsp;&nbsp;Absolute vs. relative MDE  
&nbsp;&nbsp;&nbsp;&nbsp;Standardized effect size (Cohen's d)  
&nbsp;&nbsp;Significance Level (α)  
&nbsp;&nbsp;Variance and Standard Deviation  
&nbsp;&nbsp;Statistical Significance vs Practical Significance  


### Sample Size Determination

&nbsp;&nbsp;Required Sample Size (n)  
&nbsp;&nbsp;&nbsp;&nbsp;1. One sample mean  
&nbsp;&nbsp;&nbsp;&nbsp;2. Two independent means  
&nbsp;&nbsp;&nbsp;&nbsp;3. Two dependent means  
&nbsp;&nbsp;&nbsp;&nbsp;4. One sample proportion  
&nbsp;&nbsp;&nbsp;&nbsp;5. Two independent proportions  
&nbsp;&nbsp;&nbsp;&nbsp;6. Three or more means (ANOVA)  
&nbsp;&nbsp;&nbsp;&nbsp;7. Categorical goodness-of-fit  
&nbsp;&nbsp;&nbsp;&nbsp;8. Categorical independence  

&nbsp;&nbsp;Relationships between MDE, Power, α, Variance, and n  
&nbsp;&nbsp;One-sided vs Two-sided Tests  
&nbsp;&nbsp;Power Analysis for Means  
&nbsp;&nbsp;Power Analysis for Proportions  
&nbsp;&nbsp;Unequal Group Allocation (e.g., 50/50 vs. 80/20)  
&nbsp;&nbsp;Sample Size Calculation Using Formulas  

**Sensitivity Analysis:**

&nbsp;&nbsp;&nbsp;&nbsp;MDE sensitivity  
&nbsp;&nbsp;&nbsp;&nbsp;Variance sensitivity  
&nbsp;&nbsp;&nbsp;&nbsp;Power and α sensitivity  
&nbsp;&nbsp;&nbsp;&nbsp;Allocation sensitivity  
&nbsp;&nbsp;&nbsp;&nbsp;Scenario-based planning  

&nbsp;&nbsp;C. Practical Power Analysis in Python  
&nbsp;&nbsp;&nbsp;&nbsp;1. TTestIndPower — Power analysis for comparing means  
&nbsp;&nbsp;&nbsp;&nbsp;2. NormalIndPower — Power analysis using normal approximations  
&nbsp;&nbsp;&nbsp;&nbsp;3. proportion_effectsize — Standardized effect size for proportions  
&nbsp;&nbsp;&nbsp;&nbsp;4. Calculate Required Sample Size  
&nbsp;&nbsp;&nbsp;&nbsp;5. Calculate Statistical Power for a Given Sample Size  
&nbsp;&nbsp;&nbsp;&nbsp;6. Visualize Relationships between Power, Effect Size, and Sample Size  
&nbsp;&nbsp;&nbsp;&nbsp;7. Interpret Results and Make Recommendations  

&nbsp;&nbsp;D. Experiment Planning  
&nbsp;&nbsp;&nbsp;&nbsp;1. Sample Size → Experiment Duration  
&nbsp;&nbsp;&nbsp;&nbsp;2. Traffic / Data Collection Rate  
&nbsp;&nbsp;&nbsp;&nbsp;3. Traffic Allocation Between Groups  
&nbsp;&nbsp;&nbsp;&nbsp;4. Seasonality and Business Cycles  
&nbsp;&nbsp;&nbsp;&nbsp;5. Budget and Time Constraints  
&nbsp;&nbsp;&nbsp;&nbsp;6. Practical Assumptions and Limitations  
&nbsp;&nbsp;&nbsp;&nbsp;7. Estimating Experiment Duration in Python

---

# Power Analysis

## Power Analysis

### What is Power Analysis?

&nbsp;&nbsp;Power Analysis is a statistical method used to determine how many observations(Sample Size) are needed  
&nbsp;&nbsp;to detect a meaningful effect with a specified level of statistical power.  

**IT answers this question:**

&nbsp;&nbsp;&nbsp;&nbsp;How much data do we need to have a suffuciently high probability of detecting a real effect, if that effect exists?  

**Example:**

&nbsp;&nbsp;&nbsp;&nbsp;An e-commerce company wants to test whether a new checkout design increases the purchase conversion rate.  
&nbsp;&nbsp;&nbsp;&nbsp;Question: How many users should particiate in each group to reliably detect this improvement ?  
&nbsp;&nbsp;&nbsp;&nbsp;Power Analysis answers this.  
&nbsp;&nbsp;&nbsp;&nbsp;Without Power Analysis, two major problems can occur.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Case-1: Sample size too small -&gt; fail to detect a real improvement.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Case-2: Sample size too large -&gt; waste of time, resources and money.

## Statistical Power (1-β)

Statistical Power is the probability of correctly rejecting the null hypothesis (H₀) when the null hypothesis is actually false.  

**Formula:**

&nbsp;&nbsp;&nbsp;&nbsp;Power = 1 - β  
&nbsp;&nbsp;&nbsp;&nbsp;β = probability of Type II error  
&nbsp;&nbsp;&nbsp;&nbsp;example: Power = 1 - 0.20 = 0.80  
&nbsp;&nbsp;&nbsp;&nbsp;Interpretation:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if a particular real effect exists, an experiment designed with 80% power has 80% probability of detecting  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;it as statistically significant, under the assumed effect size and other conditions.  

&nbsp;&nbsp;Relationship between Statistical power and Type II Error  

```text
Actual situation	Reject H₀	        Fail to reject H₀
H₀ is true	        Type I Error(α) 	Correct decision
H₀ is false	        Power(1-β)	        Type II Error (β)
```


&nbsp;&nbsp;higher statistical power is generally desirable, but achieving it usually requires a larger sample size, assuming everything else remains constant.  
&nbsp;&nbsp;For example, increasing desired power from 80% to 90% will generally increase the required sample size.  

&nbsp;&nbsp;Distinction between: Power vs Significance level  

```text
Significance Level (α)                              Statistical Power (β)
```

&nbsp;&nbsp;&nbsp;&nbsp;--------------------------------------------------------------------------  

```text
Probability of rejecting (H₀) when it is true	    Probability of rejecting (H₀) when a specified alternative is true
Controls Type I error	                            Measures ability to detect a real effect
Common value: 5%	                                Common value: 80%
Typically chosen before the test	                Typically targeted before the test
```


&nbsp;&nbsp;Type II erorr β = 1 - Power  
&nbsp;&nbsp;&nbsp;&nbsp;example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Power = 0.90 then Type II = 1 - 0.90 = 0.10

## Effect Size and Minimum Detectable Effect (MDE)

Effect Size is a quantitive measure of the magnitude of a difference between groups or the strength of a relationship between variables.  
&nbsp;&nbsp;Effect size tells us how big a difference or relationship is, rather than whether it is statistically significant.  
&nbsp;&nbsp;In A/B testing, it commonly refers to the difference between a treatment group and a control group  
&nbsp;&nbsp;&nbsp;&nbsp;Effect-size = μ_B - μ_A  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;μ_A = 100 pln  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;μ_B = 120 pln  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Effect-size = 120 - 100 = 20 pln  

**For binary outcome such as conversion, we take the difference in proportions:**

&nbsp;&nbsp;&nbsp;&nbsp;Effect-size = p_B - p_A  
&nbsp;&nbsp;&nbsp;&nbsp;suppose an e-commerce company tests a new checkout design.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group A (Control) = 10%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group B (Treatment) = 12%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Effect-size = p_B - p_A = 0.12 - 0.10 = 0.02  

Minimum Detectable Effect (MDE) is the smallest true effect size that an experiment is designed to detect with a specified  
&nbsp;&nbsp;statistical power and  significance level.  

**example:**

&nbsp;&nbsp;&nbsp;&nbsp;company's conversion rate is 10%  
&nbsp;&nbsp;&nbsp;&nbsp;the product team decides that an improvement of at least 1 percentage point would be meaningful.  
&nbsp;&nbsp;&nbsp;&nbsp;MDE = 0.01  
&nbsp;&nbsp;&nbsp;&nbsp;The experiment is designed to detect a change from 10% -&gt; 11%  


### Absolute and Relative MDE

&nbsp;&nbsp;Absolute MDE represents the difference between two values in their original units.  
&nbsp;&nbsp;&nbsp;&nbsp;For conversion rates:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MDE_absolute = p_B - p_A -&gt; 12% - 10% = 2 percentage points, not 2%  

&nbsp;&nbsp;Relative MDE represents the change relative to the baseline value.  
&nbsp;&nbsp;&nbsp;&nbsp;MSE_relative = (p_B - p_A) / p_A * 100% -&gt; (0.12 - 0.10) / 0.10 * 100% = 20%  


### Standardized Effect Size (Cohen's d)


**It is the method used to express two different scale experiment outcomes:**


**example:**

&nbsp;&nbsp;&nbsp;&nbsp;Experiment_A measures the difference in monthly spending (PLN)  
&nbsp;&nbsp;&nbsp;&nbsp;Experiment_B measures the difference in session duraction (minuted)  
&nbsp;&nbsp;Cohens'd is a standardized effect size that expresses the difference between two group means in units of standard deviation.

## Significance Level (α)

### How Significance Level (α) effects Statistical power and Sample Size (n)

&nbsp;&nbsp;The relationship between Significance Level (α) and Statistical Power  
&nbsp;&nbsp;&nbsp;&nbsp;example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppose an e-commerce company conducts an A/B test:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H₀: the new checkout design doesn't increase conversions  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hₐ: the new checkout design increases conversion  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sample Size = 1000 users per gourp  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;True effect size = 2 percentage point  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Assume everything remains constant except α  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When we increase α, it becomes easier to reject H₀, which increases statistical power against the specified alternative:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↑α ⇒ ↓β ⇒ ↑Power  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓α ⇒ ↑β ⇒ ↓Power  

&nbsp;&nbsp;The relationship between Significance Level (α) and Sample Size (n)  
&nbsp;&nbsp;&nbsp;&nbsp;example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a company wants to maintain 80% statistical power.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if it decreases α from 0.05 to 0.01, the experiment must generally collect more observations compensate for the stricter rejection.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↑ α ⇒ n ↓  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓ α ⇒ n ↑  

&nbsp;&nbsp;α = probability of Type I error when H₀ is True  
&nbsp;&nbsp;β = probability of Type II error under a specified alternative  
&nbsp;&nbsp;Power = probability of rejecting H₀ under that alternative

## Variance and Standard Deviation

### How Var/Std affects Statistical Power, Type II error and Required Sample size n.


&nbsp;&nbsp;Relationship between Var/Std and Statistical Power.  
&nbsp;&nbsp;&nbsp;&nbsp;we want to keep sample size n fixed.  
&nbsp;&nbsp;&nbsp;&nbsp;Suppose an e-commerce company wants to determine whether a new recommendation system increases average customer spending.  
&nbsp;&nbsp;&nbsp;&nbsp;Both experiments have the same true improvement:  

```text
Experiment A	Experiment B
True effect size	10 PLN	        10 PLN
Standard deviation	10 PLN	        30 PLN
Variance	        100	            900
Sample size	        100 per group	100 per group
```

&nbsp;&nbsp;&nbsp;&nbsp;but variablity of customer spending differs.  
&nbsp;&nbsp;&nbsp;&nbsp;in experiment A, the spending values are relatively concentrated around their population means.  
&nbsp;&nbsp;&nbsp;&nbsp;in experiment B, the spending values are much more spread out. True improvement is 10pln, but it is hard to distinguish from random variation.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↑Var/Std ⇒ ↓Power ⇒ ↑β  
&nbsp;&nbsp;&nbsp;&nbsp;In other words, higher variance increases the probability of missing a real effect when sample size is fixed  

&nbsp;&nbsp;Relationship between Variance and Required Sample Size.  
&nbsp;&nbsp;&nbsp;&nbsp;we want to maintain statistical power at 80%  
&nbsp;&nbsp;&nbsp;&nbsp;the approximate sample-size formula: n ≈ [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ²  

$$
n\approx\frac{2(z_{1-\alpha/2}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$

&nbsp;&nbsp;&nbsp;&nbsp;So, ↑Var/Std ⇒ ↑n  
&nbsp;&nbsp;&nbsp;&nbsp;n ∝ σ²  

```text
Change	                    Required sample size
Variance doubles	        2x
Variance triples	        3x
Standard deviation doubles	4x
Standard deviation triples	9x
Standard deviation halves	0.25x
```

## Statistical Significance vs Practical Significance

### Statistical significance

&nbsp;&nbsp;Statistical Significance means that the observed result is sufficiently inconsistent with the null hypotheis H₀  
&nbsp;&nbsp;to reject it at the chosen significance level(α)  

**Decision rule:**

&nbsp;&nbsp;&nbsp;&nbsp;p &lt; α  ⇒ Reject H₀  
&nbsp;&nbsp;&nbsp;&nbsp;p &gt; α  ⇒ Fail to Reject H₀  

**example:**

&nbsp;&nbsp;&nbsp;&nbsp;an e-commerce company runs an A/B test comparing two checkout designs.  
&nbsp;&nbsp;&nbsp;&nbsp;α = 0.05  
&nbsp;&nbsp;&nbsp;&nbsp;p = 0.01  
&nbsp;&nbsp;&nbsp;&nbsp;0.01 &lt; 0.05 ⇒ reject H₀  
&nbsp;&nbsp;&nbsp;&nbsp;there is statistically significant evidence that the conversion rates differ.  
&nbsp;&nbsp;&nbsp;&nbsp;However, statistical significance doesn't tell us whether the difference is large enough to matter to the business.  
&nbsp;&nbsp;&nbsp;&nbsp;That is where practical significance comes in.  


### Practical Significance

&nbsp;&nbsp;Practical Significance refers to whether the magnitude of an ebserved effect is large enough to be meaningful or valuable in real-world context.  

**Example:**

&nbsp;&nbsp;&nbsp;&nbsp;α = 0.05  
&nbsp;&nbsp;&nbsp;&nbsp;p = 0.01  
&nbsp;&nbsp;&nbsp;&nbsp;p &lt; α = 0.01 &lt; 0.05 -&gt; Reject H₀  
&nbsp;&nbsp;&nbsp;&nbsp;the result is statistically signifiacnt.  
&nbsp;&nbsp;&nbsp;&nbsp;but whether this improvement is practically significanct depends on the business.  
&nbsp;&nbsp;&nbsp;&nbsp;for example, if implementation the new checkout design costs €100,000.  
&nbsp;&nbsp;&nbsp;&nbsp;but the expected additional profit is only €20,000, the change may not be worth implementing.

---

# Sample Size Determination

## Required Sample Size (n)

### Required Sample Size (n)

&nbsp;&nbsp;Required Sample Size(n) is the minimum number of observations needed in an experiment to detect a specified effect size with  
&nbsp;&nbsp;a desired statistical power and significance level, under the assumed statistical model.  

&nbsp;&nbsp;The four key inputs required sample depends on.  

```text
Input	                 Meaning	                                                Example
Effect Size / MDE	     Smallest effect we want to detect	                        +2 percentage points
Statistical Power(1-β)	 Desired probability of detecting the specified effect	    80%
Significance Level(α)	 Allowed Type I error probability	                        0.05
Variance(σ²)	         Variability of the outcome metric	                        Estimated from historical data
```



### Statistical cases and Power Analysis:


```text
Case	                     Sample Size method                             Example
One sample mean	             One-sample mean power calculation              Is average customer spending different from 100 PLN?
Two independent sample means Two-independent-means power calculation        Is average spending different between users of website A and B?
One sample proportion	     One-proportion power calculation               Is the conversion rate different from 10%?
Two independent proportions	 Two-proportion power calculation               Is conversion rate different between checkout designs A and B?
Two dependent sample means	 Paired-mean power calculation                  Does average spending change for the same customers before and after an intervention?
Categorical goodness-of-fit	 Chi-square goodness-of-fit power calculation   Do customers choose four payment methods in the expected proportions?
Categorical independence	 Chi-square independence power calculation      Is payment method associated with device type?
Three or more sample means	 ANOVA power calculation                        Does average spending differ among three recommendation algorithms?
```



### One-Sample Mean Sample Size Formula:

&nbsp;&nbsp;one-tailed: n ≈ ((Z_(1-α) + Z_(1-β))² * σ²) / δ²  

$$
n\approx\frac{(z_{1-\alpha}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$

&nbsp;&nbsp;two-tailed: n ≈ ((Z_(1-α/2) + Z_(1-β))² * σ²) / δ²  

$$
n\approx\frac{(z_{1-\alpha/2}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$



### Two Independent Means Sample Size Formula

&nbsp;&nbsp;one-tailed: n ≈ (2 * (Z_(1-α) + Z_(1-β))² * σ²) / δ²  

$$
n\approx\frac{2(z_{1-\alpha}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$

&nbsp;&nbsp;two-tailed: n ≈ (2 * (Z_(1-α/2) + Z_(1-β))² * σ²) / δ²  

$$
n\approx\frac{2(z_{1-\alpha/2}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$



### One Sample Proportion Sample Size Formula

&nbsp;&nbsp;one-tailed: n ≈ [Z_(1-α) * √(p₀(1-p₀)) + Z_(1-β) * √(p₁(1-p₁))]² / (p₁ - p₀)²  

$$
n\approx\frac{\left[z_{1-\alpha}\sqrt{p_0(1-p_0)}+z_{1-\beta}\sqrt{p_1(1-p_1)}\right]^2}{(p_1-p_0)^2}
$$

&nbsp;&nbsp;two-tailed: n ≈ [Z_(1-α/2) * √(p₀(1-p₀)) + Z_(1-β) * √(p₁(1-p₁))]² / (p₁ - p₀)²  

$$
n\approx\frac{\left[z_{1-\alpha/2}\sqrt{p_0(1-p_0)}+z_{1-\beta}\sqrt{p_1(1-p_1)}\right]^2}{(p_1-p_0)^2}
$$



### Two Independent Proportions Sample Size Formula

&nbsp;&nbsp;one-tailed: n ≈ [Z_(1-α) * √(2p̄(1-p̄)) + Z_(1-β) * √(p_A(1-p_A) + p_B(1-p_B))]² / (p_B - p_A)²  

$$
n\approx\frac{\left[z_{1-\alpha}\sqrt{2\bar p(1-\bar p)}+z_{1-\beta}\sqrt{p_A(1-p_A)+p_B(1-p_B)}\right]^2}{(p_B-p_A)^2}
$$

&nbsp;&nbsp;two-tailed: n ≈ [Z_(1-α/2) * √(2p̄(1-p̄)) + Z_(1-β) * √(p_A(1-p_A) + p_B(1-p_B))]² / (p_B - p_A)²  

$$
n\approx\frac{\left[z_{1-\alpha/2}\sqrt{2\bar p(1-\bar p)}+z_{1-\beta}\sqrt{p_A(1-p_A)+p_B(1-p_B)}\right]^2}{(p_B-p_A)^2}
$$



### Two dependent means Sample Size Formula

&nbsp;&nbsp;one-tailed: n ≈ ((Z_(1-α) + Z_(1-β))² * σ_D²) / δ_D²  

$$
n\approx\frac{(z_{1-\alpha}+z_{1-\beta})^2\sigma_D^2}{\delta_D^2}
$$

&nbsp;&nbsp;two-tailed: n ≈ ((Z_(1-α/2) + Z_(1-β))² * σ_D²) / δ_D²  

$$
n\approx\frac{(z_{1-\alpha/2}+z_{1-\beta})^2\sigma_D^2}{\delta_D^2}
$$



### Categorical goodness-of-fit Sample Size Formula

&nbsp;&nbsp;w = √(Σᵢ₌₁ᵏ ((p₁ᵢ - p₀ᵢ)² / p₀ᵢ))  

$$
w=\sqrt{\sum_{i=1}^{k}\frac{(p_{1i}-p_{0i})^2}{p_{0i}}}
$$

&nbsp;&nbsp;λ = nw²  

$$
\lambda=nw^2
$$

&nbsp;&nbsp;df = k - 1  

$$
df=k-1
$$

&nbsp;&nbsp;Power = 1 - F_ncx²(χ²_critical; df, λ)  

$$
\mathrm{Power}=1-F_{\mathrm{nc}\chi^2}(\chi^2_{\mathrm{critical}};df,\lambda)
$$



### Categorical independence Sample Size Formula

&nbsp;&nbsp;w = √(Σᵢ Σⱼ ((pᵢⱼ - pᵢ₊p₊ⱼ)² / (pᵢ₊p₊ⱼ)))  

$$
w=\sqrt{\sum_i\sum_j\frac{(p_{ij}-p_{i+}p_{+j})^2}{p_{i+}p_{+j}}}
$$

&nbsp;&nbsp;λ = Nw²  

$$
\lambda=Nw^2
$$

&nbsp;&nbsp;df = (r - 1)(c - 1)  

$$
df=(r-1)(c-1)
$$

&nbsp;&nbsp;Power = 1 - F_ncx²(χ²_critical; df, λ)  

$$
\mathrm{Power}=1-F_{\mathrm{nc}\chi^2}(\chi^2_{\mathrm{critical}};df,\lambda)
$$



### Three or more independent means (ANOVA) Sample Size Formula

&nbsp;&nbsp;λ = Nf²  

$$
\lambda=Nf^2
$$

&nbsp;&nbsp;df₁ = k - 1  

$$
df_1=k-1
$$

&nbsp;&nbsp;df₂ = N - k  

$$
df_2=N-k
$$

&nbsp;&nbsp;Power = 1 - F_ncf(F_critical; df₁, df₂, λ)  

$$
\mathrm{Power}=1-F_{\mathrm{ncf}}(F_{\mathrm{critical}};df_1,df_2,\lambda)
$$

## Relationships between MDE, Power, α, Variance, and n

### Relationship between MDE and n

&nbsp;&nbsp;Smaller MDE → Larger required sample size.  
&nbsp;&nbsp;Why? Detecting a very small improvement is more difficult because it can be hidden by random sampling variation.  
&nbsp;&nbsp;n ∝ 1 / MDE²  


### Relationship between Power and n

&nbsp;&nbsp;Higher desired statistical power → Larger required sample size.  
&nbsp;&nbsp;Power is the probability of rejecting H₀ when a specified alternative is true.  
&nbsp;&nbsp;Increasing power from 80% to 90% means you want a higher chance of detecting the same true effect.  
&nbsp;&nbsp;To achieve this while keeping MDE, α, variance and design constant, you generally need more observations  


### Relationship between α and n

&nbsp;&nbsp;Lower significance level → Larger required sample size.  
&nbsp;&nbsp;a smaller α means stricter evidence is required to reject H₀.  
&nbsp;&nbsp;Suppose the company changes α = 0.05 → 0.01. This decreases the allowed Type I error probability from 5% to 1%.  
&nbsp;&nbsp;But maintaining the same statistical power now requires a larger sample.  


### Relationship between Variance and n

&nbsp;&nbsp;Higher variance → larger required sample size  


### Relationship Table:


```text
Parameter changes          Required n      Reason
```

&nbsp;&nbsp;-----------------------------------------------------------------------------  

```text
MDE increases              ↓ Decreases     Larger effects are easier to detect
MDE decreases              ↑ Increases     Smaller effects are harder to detect
power increases            ↑ Increases     Greater detection probability is required
power decreases            ↓ Decreases     Lower detection probability is accepted
α increases                ↓ Decreases     Less stringent rejection threshold
α decreases                ↑ Increases     More stringent rejection threshold
Variance increases         ↑ Increases     More noise
Variance decreases         ↓ Decreases     Less noise
```

## One-sided vs Two-sided Tests

A one-sided test generally requires a smaller sample size than a two-sided test when detecting an effect in its prespecified direction,  
&nbsp;&nbsp;assuming the same MDE, power, variance and significance level.  
&nbsp;&nbsp;A one-sided test concentrates its rejection region in one direction. A two-sided test must account for effects in both directions,  
&nbsp;&nbsp;so its rejection thresholds are more stringent in either indivitual direction.  


**Sample-size formulas:**

&nbsp;&nbsp;&nbsp;&nbsp;One-sided test: n ≈ [2 * (Z_(1-α) + Z_(1-β))² * σ²] / δ²  

$$
n\approx\frac{2(z_{1-\alpha}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$

&nbsp;&nbsp;&nbsp;&nbsp;Two-sided test: n ≈ [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ²  

$$
n\approx\frac{2(z_{1-\alpha/2}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$



**example:**

&nbsp;&nbsp;&nbsp;&nbsp;Suppose a company wants to detect a 10pln improvement in average spending.  
&nbsp;&nbsp;&nbsp;&nbsp;Assumptions:  

```text
Parameter	        Value
MDE	                10 PLN
Standard deviation	30 PLN
Power	            80%
α	                0.05
Groups	            Two independent, equal-sized
```

&nbsp;&nbsp;&nbsp;&nbsp;using the normal-approximation formulas:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;one-sided test requires 112 users per group  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;two-sided test requires 142 users per group  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;two-sided test requies 27% more observations then the one-sided test in this example.

## Power Analysis for Means

Power Analysis for Means is a statistical method used to determine the sample size required to detect a speficied difference  
&nbsp;&nbsp;in population means with a desired statistical power and significance level.  


**Example:**

&nbsp;&nbsp;&nbsp;&nbsp;an e-ecommerce company wants to evaluate whether a new recommendation algorithm increases average customer spending.  
&nbsp;&nbsp;&nbsp;&nbsp;Company wants to detect an increase of  δ = 110 - 100 = 10pln.  
&nbsp;&nbsp;&nbsp;&nbsp;We need to determine the sample size needed to detect this difference with 80% statistical power and α=0.05.  


**Types of Power Analysis For Means:**

&nbsp;&nbsp;&nbsp;&nbsp;1.One-sample-mean - Compare one population mean with a specified reference value - is average order value different from 100pln?  
&nbsp;&nbsp;&nbsp;&nbsp;2.Two independent means - Compare means from two indepenent groups - Do customers using design B spend more than customers using design A?  
&nbsp;&nbsp;&nbsp;&nbsp;3.Paired means - Compare related observations - Does spending change for the same customers before and after an intervetion ?  


**One-Sample Power Analysis For a Mean:**

&nbsp;&nbsp;&nbsp;&nbsp;Suppose the historical average order value is 100pln  
&nbsp;&nbsp;&nbsp;&nbsp;We want to detect whether the population mean differs from 100pln by at least 10pln  
&nbsp;&nbsp;&nbsp;&nbsp;Assume:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H₀: μ = 100  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hₐ: μ ≠ 100  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;δ = 10  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;σ = 30  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;α = 0.05  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Power = 80%  
&nbsp;&nbsp;&nbsp;&nbsp;For a Two-sided one-sample Z-test with known population standard deviation m the apporimate formula:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n = [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ² -&gt; n ≈ ((1.96 + 0.84)² × 30²) / 10² ≈ 70.6  

&nbsp;&nbsp;Two Independent Means  
&nbsp;&nbsp;&nbsp;&nbsp;Suppose customers are randomly assigned to two groups:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Group A receives the current recommendation algorithm  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Group B receives the new recommendation algorithm  
&nbsp;&nbsp;&nbsp;&nbsp;We want to detect a mean spending difference of 10pln  
&nbsp;&nbsp;&nbsp;&nbsp;Formula For two independent groups with equal sizes, equal population variance, and a two-sided test:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n = [2 * (Z_(1-α/2) + Z_(1-β))² * σ²] / δ²  

$$
n\approx\frac{2(z_{1-\alpha/2}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Var(X̄_B - X̄_A) = (σ_A² / n_A) + (σ_B² / n_B) = 2σ² / n  

$$
\operatorname{Var}(\bar X_B-\bar X_A)=\frac{\sigma_A^2}{n_A}+\frac{\sigma_B^2}{n_B}=\frac{2\sigma^2}{n}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n ≈ [2(1.96 + 0.84)² × 900] / 100 ≈ 141.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per group = 142, total samples 284  

&nbsp;&nbsp;Paired Means  
&nbsp;&nbsp;&nbsp;&nbsp;Now imagine measuring the same customers before and after a change.  
&nbsp;&nbsp;&nbsp;&nbsp;each customer contributes two measurements, producing a paired differences.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dᵢ = X_after_i - X_before_i  
&nbsp;&nbsp;&nbsp;&nbsp;instead of comparing independent means, we analyze the mean of these differences  
&nbsp;&nbsp;&nbsp;&nbsp;approximate two-sided sample-size formula:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n ≈ ((Z_(1-α/2) + Z_(1-β))² * σ_D²) / δ_D²  

$$
n\approx\frac{(z_{1-\alpha/2}+z_{1-\beta})^2\sigma_D^2}{\delta_D^2}
$$

&nbsp;&nbsp;&nbsp;&nbsp;Paired power analysis uses the standard deviation of the differences, not individual measurements.

## Power Analysis for Proportions

Power Analysis for Proportions is a statistical method used to determine the sample size required to detect a specified  
&nbsp;&nbsp;difference in population proportions with a desired statistical power and significance level.  
&nbsp;&nbsp;How many observations do we need to detect a meaningful difference in conversion rates, success rates, or other proportions ?  


**Two types of power analysis for proportions:**

&nbsp;&nbsp;&nbsp;&nbsp;One-proportion test - compare a population proportion against a reference.  
&nbsp;&nbsp;&nbsp;&nbsp;Two-proportion test - compare proportions from two independent groups.  

&nbsp;&nbsp;Two-Proportion Power Analysis  
&nbsp;&nbsp;&nbsp;&nbsp;Suppose an e-commerce company wants to test whether a new checkout design increase its conversion rate.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group A - 10% Control  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group B - 12% Treatment  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Company wnat to detect an improvement of: δ = p_B - p_A = 0.12 - 0.10 = 0.02  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Absolute MDE = 2 percentage points  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Relative MDE = 20%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Assuming: α = 0.05 \| power = 0.80  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goal is to determine the sample size needed per group  
&nbsp;&nbsp;&nbsp;&nbsp;For two indpendent proportions, equal group sizes and a two-sided Z-test:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n ≈ [Z_(1-α/2) * √(2p̄(1-p̄)) + Z_(1-β) * √(p_A(1-p_A) + p_B(1-p_B))]² / (p_B - p_A)²  

$$
n\approx\frac{\left[z_{1-\alpha/2}\sqrt{2\bar p(1-\bar p)}+z_{1-\beta}\sqrt{p_A(1-p_A)+p_B(1-p_B)}\right]^2}{(p_B-p_A)^2}
$$



&nbsp;&nbsp;One-Proportion Power Analysis  
&nbsp;&nbsp;&nbsp;&nbsp;Suppose the company has a historical conversion-rate benchmark of 10%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;it wants to determine whether the current conversion rate differs from 10% using only one sample.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hypothesis:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H₀: p = 10  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hₐ: p ≠ 10  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppose the smallest difference of interest is 2 percentage points, so we plan an alternative proportion of 12%.  
&nbsp;&nbsp;&nbsp;&nbsp;For two-sided one-sample proportion Z-test  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n ≈ [Z_(1-α/2) * √(p₀(1-p₀)) + Z_(1-β) * √(p₁(1-p₁))]² / (p₁ - p₀)²  

$$
n\approx\frac{\left[z_{1-\alpha/2}\sqrt{p_0(1-p_0)}+z_{1-\beta}\sqrt{p_1(1-p_1)}\right]^2}{(p_1-p_0)^2}
$$

## Unequal Group Allocation

### Group allocation

&nbsp;&nbsp;Group allocation describes how participants are distributed between the control and treatment groups.  

**example:**

&nbsp;&nbsp;&nbsp;&nbsp;an E-commerce company has 10,000 users available for an A/B test.  
&nbsp;&nbsp;&nbsp;&nbsp;50/50 allocation: 5,000 users in each group = equal group allocation  
&nbsp;&nbsp;&nbsp;&nbsp;80/20 allocation: 8,000 users in the control group and 2,000 users in the treatment group = unequal group allocation  

&nbsp;&nbsp;The main principle: with equal group allocation and a fixed total sample size, a 50/50 allocation usually provides greater  
&nbsp;&nbsp;statistical power than an unequal allocation.  


**Why does unequal group allocation affect statistical power ?**

&nbsp;&nbsp;&nbsp;&nbsp;Variance of the difference between sample means  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Var(X̄_B - X̄_A) = (σ_A² / n_A) + (σ_B² / n_B)  

$$
\operatorname{Var}(\bar X_B-\bar X_A)=\frac{\sigma_A^2}{n_A}+\frac{\sigma_B^2}{n_B}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this formula calculates how much the estimated difference between two independent sample means varies across repeated samples.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;example: A/B test  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;what we are interested in: X̄_B - X̄_A.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group A: average spending = 100pln  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Group B: average spending = 110pln  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the observed difference 110pln - 100pln = 10pln  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if we repeat the experiment many times, the observed difference will vary due to random sampling variation.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the variance is higer when sample sizes are smaller, assuming underlying population variance is unchanged.  

&nbsp;&nbsp;&nbsp;&nbsp;Standard Error  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SE = σ * √((1 / n_A) + (1 / n_B))  

$$
SE=\sigma\sqrt{\frac{1}{n_A}+\frac{1}{n_B}}
$$


&nbsp;&nbsp;&nbsp;&nbsp;example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;σ = 30, n=10,000  

```text
allocation             Standard Error
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;50/50 (5,000 / 5,000)  0.600  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;80/20 (8,000 / 2,000)  0.750  
&nbsp;&nbsp;&nbsp;&nbsp;the 80/20 allocation has a25% larher standard error, making it harder to dectect the same effect with the same sample size.  

&nbsp;&nbsp;Sample Size Formula for Unequal Group Allocation  
&nbsp;&nbsp;&nbsp;&nbsp;For unequal group allocation, introduce the allocation ratio: r = n_A / n_B  
&nbsp;&nbsp;&nbsp;&nbsp;For a two-sided test with common variance:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n_a = ((Z_(1-α/2) + Z_(1-β))² * σ² * (1 + 1/r)) / δ²  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n_b = r * n_a  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N = n_a + n_b  

&nbsp;&nbsp;&nbsp;&nbsp;For unequal variance the general normal approximation formula:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n_a = ((Z_(1-α/2) + Z_(1-β))² * (σ_A² + σ_B² / r)) / δ²  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n_b = r * n_a  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N = n_a + n_b  


**How much more sample size does 80/20 require ?**

&nbsp;&nbsp;&nbsp;&nbsp;For equal variance:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N_r / N_(50/50) = (1 + r)² / (4r)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r = 0.20 / 0.80 = 0.25  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N_(80/20) / N_(50/50) = (1.25)² / (4(0.25)) = 1.5625  
&nbsp;&nbsp;&nbsp;&nbsp;Therefore: 56.25% more total observations required for appromimately the same power, MDE, α.  


**Why should we use unequal group allocation ?**

&nbsp;&nbsp;&nbsp;&nbsp;1. Risk management: A new treatment may be experimental, so the company initially exposes fewer users to it.  
&nbsp;&nbsp;&nbsp;&nbsp;2. Business costs: One treatment might be more expensive to deliver.  
&nbsp;&nbsp;&nbsp;&nbsp;3. Ethical considerations: Researchers may want to limit exposure to a potentially harmful or burdensome treatment.  
&nbsp;&nbsp;&nbsp;&nbsp;4. Different group variances: When population variances differ, a 50/50 allocation is not always the most statistically efficient choice.

## Sample Size Calculation Using Formulas

### General Procedure:

&nbsp;&nbsp;1. Choose the statistical : Z-test, t-test, chi-square test, ANOAVA, etc.  
&nbsp;&nbsp;2. Specify the MDE: the smallest effect our experiment should be able to detect.  
&nbsp;&nbsp;3. Choose α and power: Common choices are α=0.05 and power=80%  
&nbsp;&nbsp;4. Estimate variablity: Standard deviation, proportion, or standardized effect size, depending on the test.  
&nbsp;&nbsp;5. Apply the appropriate formula: calculate and round the required sample size upward.  


**Example:**

&nbsp;&nbsp;&nbsp;&nbsp;an E-commerce company wants to test whether a new recommendation algorithm increase average customer spending.  

```text
Parameters                  Value
Control mean                100 PLN
```

&nbsp;&nbsp;&nbsp;&nbsp;Treatment mean to detect    110 PLN  

```text
MDE δ                       10 PLN
Population SD σ             30 PLN
Significance level α        0.05
Statistical power           80%
Allocation                  50/50
Test                        Two-sided, Two-independent means Z-test
```


&nbsp;&nbsp;&nbsp;&nbsp;1-step: The sample size foruma: n ≈ (2 * (Z_(1-α/2) + Z_(1-β))² * σ²) / δ²  

$$
n\approx\frac{2(z_{1-\alpha/2}+z_{1-\beta})^2\sigma^2}{\delta^2}
$$

&nbsp;&nbsp;&nbsp;&nbsp;2-step: Find the critical Z-values:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;α = 0.05 -&gt; Z_(1-α/2) = Z_0.975 = 1.96  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Power = 80% -&gt; Z_(1-β) = Z_0.80 = 0.8416  
&nbsp;&nbsp;&nbsp;&nbsp;3-step: n = (2 * (1.96 + 0.8416)² * 30²) / 10² = 141.28 -&gt; 142 customers per group 142 + 142 = 284 total.

## Sensitivity Analysis

Sensitivity Analysis is a technique used to examine how changes in input assumptions affect the result of a statistical analysis.  
&nbsp;&nbsp;In power analysis, it helps us understand how changes in parameters such as MDE, Var, α and power affect:  
&nbsp;&nbsp;&nbsp;&nbsp;required sample size  
&nbsp;&nbsp;&nbsp;&nbsp;achievanle statistical power  
&nbsp;&nbsp;&nbsp;&nbsp;minimum detectable effect  
&nbsp;&nbsp;&nbsp;&nbsp;feasibility of an experiment  
&nbsp;&nbsp;example: an e-commerce company wants to run A/B test to determine whether a new recommendation algorithm increases avera customer spending.  
&nbsp;&nbsp;&nbsp;&nbsp;initially, the company assumes:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MDE = 10 PLN  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Std = 30 PLN  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;α   = 0.05  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Power = 80%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allocation = 50/50  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;statistical test = two-sided indepdent-means test  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;using the normal approximation: n ≈ (2 * (Z_(1-α/2) + Z_(1-β))² * σ²) / δ²  -&gt; we obtain 142 customers per group, 284 in total.  
&nbsp;&nbsp;&nbsp;&nbsp;But what if our assumptions are wrong ?  
&nbsp;&nbsp;&nbsp;&nbsp;Std is 40 instead of 30 or MDE is 5 PLN or Power is 90%  
&nbsp;&nbsp;&nbsp;&nbsp;Sensitivity Analysis answers these questions.  


**Two main types of Sensitivity Analysis:**

&nbsp;&nbsp;&nbsp;&nbsp;1.Sample-size Sensitivity Analysis:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We fix the sedired power and examine how changes in the other parameters affect required sample size.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MDE decreases = Sample size increases  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Variance increases = Sample size increases  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Power increases = Sample size increases  

&nbsp;&nbsp;&nbsp;&nbsp;2.Statistical-power Sensitivity Analysis:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We fix the available sample size and examine how changes in the other parameters affect the achievable power.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for example:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if we have only 500 customers, will we achieve 80% power when the true effect is 5 PLN ?  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What about 10 PLN  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this second type is particulary useful when a company has limited traffic or budget.  

&nbsp;&nbsp;MDE Sensitivity  
&nbsp;&nbsp;&nbsp;&nbsp;MDE Sensitivity Analysis evaluates how different detectable-effect assumptions change required sample size or achievable statistical power.  
&nbsp;&nbsp;&nbsp;&nbsp;The central relationship is n ∝ 1 / MDE²  
&nbsp;&nbsp;&nbsp;&nbsp;Main types:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fixed desired power: change MDE and calculate required sample size  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fixed sample size: Change the assumed true effect and calculate achievable power  

&nbsp;&nbsp;Variance Sensitivity  
&nbsp;&nbsp;&nbsp;&nbsp;Variance Sensitivity Analysis examines how different assumptions about population variability affect the required sample size  
&nbsp;&nbsp;&nbsp;&nbsp;and achievable statistical power.  
&nbsp;&nbsp;&nbsp;&nbsp;The main relationship: n ∝ σ²  
&nbsp;&nbsp;&nbsp;&nbsp;For fixed desired power:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Variance ↑ ⇒ n ↑  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Variance ↓ ⇒ n ↓  
&nbsp;&nbsp;&nbsp;&nbsp;For fixed sample size:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Variance ↑ ⇒ Power ↓  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Variance ↓ ⇒ Power ↑  


**Power and α Sensitivity Analysis:**

&nbsp;&nbsp;&nbsp;&nbsp;Power and α Sensitivity Analysis evaluates how different combinations of desired statistical power and significance levels  
&nbsp;&nbsp;&nbsp;&nbsp;influence required sample size or achievable statistical power.  

```text
Change	                  Required n (power fixed)	    Achieved power (n fixed)
Desired power target ↑	    ↑	                        Target itself is a planning choice
Desired power target ↓	    ↓	                        Target itself is a planning choice
α↑	                        ↓	                        ↑
α↓	                        ↑	                        ↓
```



**Allocation sensitivity Analysis:**

---

# Practical Power Analysis In Python

## TTestIndPower — Power analysis for comparing means
