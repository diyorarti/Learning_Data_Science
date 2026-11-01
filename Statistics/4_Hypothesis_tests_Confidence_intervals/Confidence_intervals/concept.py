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

# Confidence Intervals
"""
Confidence Interval (CI) is a range of values calculated from sample data that expresses uncertainty about an 
   unknown population parameter, such as the population mean or populatio proportion p.
   example: A company has 10,000 employees, and we want to estimate their average salary.
      instead of colllecting salary information from all 10,000 employees, we randomly select 200 employees.
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
         CI = Point Estimate ± Margin of Error
         in out example: CI = 600 ± 400 = [5,600, 6,400]
   Why do Data scientist use CI?
      Suppose, we conduct an A/B test and discover that a new website design increases conversion rate by 2% percentage points.
      without CI, we only know the observed difference.
      with CI, we mau report:
         Estimated improvement: 2 percentage points
         95% CI: [0.5, 3.5] percentage points
      this allows stakeholders to evaluate not only the estimated improvement but also its uncertainty and possible business impact.
"""

