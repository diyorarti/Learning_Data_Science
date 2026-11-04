# Confidence Intervals 
"""
Confidence Intervals

I. Fundamentals
   1. Point estimate vs interval estimate
   2. Confidence interval
   3. Confidence level
   4. Standard error
   5. Margin of error
   6. Critical values
   7. CI width and precision

II. Confidence Intervals for Means
   1. One-sample Z confidence interval
   2. One-sample t confidence interval
   3. Two independent means
   4. Paired means

III. Confidence Intervals for Proportions
   1. One-proportion CI
   2. Difference between two proportions
   3. Wald vs Wilson CI

IV. Interpretation
   1. Correct interpretation of 95% CI
   2. CI containing zero
   3. CI not containing zero
   4. Narrow vs wide intervals
   5. Statistical vs practical significance

V. CI and Hypothesis Testing
   1. α and confidence level
   2. Null value inside/outside CI
   3. Two-sided tests and CIs

VI. Bootstrap Confidence Intervals
   1. Bootstrap resampling
   2. Bootstrap distribution
   3. Percentile CI
   4. Mean CI
   5. Median CI
   6. Group-difference CI

VII. Regression Confidence Intervals
   1. Linear regression coefficient CI
   2. Logistic regression coefficient CI
   3. Odds-ratio CI
   4. Confidence interval vs prediction interval

VIII. Practical Applications
   1. A/B test treatment effects
   2. Conversion rates
   3. Mean differences
   4. Reporting effect + CI
"""

# Fundamentals
# Point estimate vs Interval estimate
"""
Point Estimate 
   a point estimate is a single numerical value calculated from sample data to estimate an unknown population paramter.
   example:
      a company has 10,000 employees, and we want to estimate average salary, but collecting salary information from everyone would be expensive.
      So instead, we randomly select n sample and calculate their average monthly salary.
         suppose we obtain: x̄ = 6000
         here:
            Population μ = unknown
            Sample x̄ = 6000
            Sample size n = 100
   Formula:
      x̄ = (Σᵢ₌₁ⁿ xᵢ) / n
   Common point estimators
      Population Paramter                    Point estimator
      Population μ                           Sample mean  x̄
      Population proportion p                Sample proportion p̂
      population Variance σ²                 Sample variance s²
      population std σ                       Sample std s
      Population regression coefficient β    Estimated coefficient β
      Estimator: The rule of statistic used to estimate the parameter, such as x̄
      Estimte: The numerical result obtained from the sample such as 6,000 PLN

   Limitation of point estimates:
      A point estimate doesn't tell us how uncertain out estimate is.

Interval Estimate
   An interval estimate is a range of values calculated from sample data to estimate an unknown population paramter.
   example:
      a company has 10,000 employees, and we want to estimate average salary, but collecting salary information from everyone would be expensive.
      suppose, we calculate 95% CI = [5600, 6400] PLN
   Formula:
      CI = x̄ ± z* · (σ / √n)
"""

# Confidence Intervals
"""
Confidence Interval (CI) is a range of values calculated from sample data that expresses uncertainty about an 
   unknown population parameter, such as the population mean or population proportion p.
   example: A company has 10,000 employees, and we want to estimate their average salary.
      instead of collecting salary information from all 10,000 employees, we randomly select 200 employees.
      then we calculate:
         Sample mean x̄ = 6,000 PLN
         95% CI = [5,600 PLN, 6,400 PLN]
      this CI tells us that values between 5,600 and 6,400 are plausible for the true population mean, according to this esimation method.
      95% CI doesn't mean that there is a 95% probability that the fixed true population mean lies inside the interval.
   What does a 95% CI mean?
      Suppose repeatig the same experiment above 1,000 times:
         1.randomly select 200 employees
         2.calculate the sample mean
         3.construct a 95% CI
         4.repeat the entire process 1,000 times
      if statistical assumptions hold, approximately 950 of the 1,000 intervals would contain the true population mean.
      this is the meaning of a 95% confidence: the method produces intervals that capture the true parameter in 95% of repeated samples in the long run.
      General Formula:
         CI = Point Estimate ± Margin of Error or CI = θ̂ ± E
         θ̂  = Point estimate of the population paramter
         E = Margin of error
         CI = Confidence Interval
         in out example: CI = 600 ± 400 = [5,600, 6,400]
   Why do Data scientist use CI?
      Suppose, we conduct an A/B test and discover that a new website design increases conversion rate by 2% percentage points.
      without CI, we only know the observed difference.
      with CI, we mau report:
         Estimated improvement: 2 percentage points
         95% CI: [0.5, 3.5] percentage points
      this allows stakeholders to evaluate not only the estimated improvement but also its uncertainty and possible business impact.
"""

# Confidence level
"""
A Confidence Level is the long-run percentage of confidence intervals expected to contain the true population paramter when 
   we repeatedly collect samples and construct intervals using the same statistical procedure.
   Mathematically:
      Confidence Level = 1 - α
   For example:
      Confidence Level  α         Interpretation
      90%               0.10      About 90 out of 100 intervals contain the parameter
      95%               0.05      About 95 out of 100 intervals contain the parameter
      99%               0.01      About 99 out of 100 intervals contain the parameter 

      90 out 100 intervals contain the parameter means that:
         Suppose: the paramter μ = 6000
         Sample      90% Confidence interval    Contains μ=6000 parameter
         Samole-1    [5,800 - 6,200]            Yes
         Samole-1    [5,900 - 6,300]            Yes
         Samole-1    [5,700 - 6,100]            Yes
         Samole-1    [6,100 - 6,500]            No
         ...  
         So, 90 out of 100 intervals contain the true parameter.

   The relationship between Confidence level and Significance level
      CL = 1 -  α
      α = 1 - CL 

   Confidence level vs Confidence Interval width
      When Confidence level increases the confidence interval becomes wider, assuming the same sample and estimation method.
      The general Formula:
         Confidence Level:
            CI = x̄ ± z* · (σ / √n)
            x̄ = sample mena
            z* = critical z-value
            n = sample size
         Two-sided test critical value formual:
            z* = ±Φ⁻¹(1 - α/2)
         Alpha α:
            α = 1 - Confidence Level
         x̄, σ and n remain fixed, increasing the confidence level increases the critical value z*.
         Consequently, the margin of error becomes larger, producing a wider interval.
      example:
         Case-1: Suppose Confidence Level = 90%
            x̄ = 100
            σ = 20
            n = 100
            CL = 90%
            α = 1 - 0.90 = 0.10
            z* = ±Φ⁻¹(1 - α/2) = ±1.64
            CI = x̄ ± z* · (σ / √n) = 100 ± 1.64 · (20 / √100) = 100 ± 3.28 = CI = [96.72 - 103.28]
            Range = 6.56
         Case-2: Suppose Confidence Level = 95%
            x̄ = 100
            σ = 20
            n = 100
            CL = 95%
            α = 1 - 0.95 = 0.05
            z* = ±Φ⁻¹(1 - α/2) = ±1.96
            CI = x̄ ± z* · (σ / √n) = 100 ± 1.96 · (20 / √100) = 100 ± 3.92 = CI = [96.08 - 103.92]
            Range = 7.84
         SO:
            CL ↑ ⇒ z* ↑ ⇒ E ↑ ⇒ CI wider
            CL ↓ ⇒ z* ↓ ⇒ E ↓ ⇒ CI narrower  
"""

# Standard error
"""

"""