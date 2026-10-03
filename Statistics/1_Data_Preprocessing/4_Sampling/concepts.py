"""
Sampling
    Simple Random Sampling
    Systematic Sampling
    Stratified Sampling
    Cluster Sampling

Evaluating the sample data
"""

"""
Sampling
    Sampling is the process of selecting a smaller group of observations from a larger group so that we can study the smaller group and 
    draw conclusions about the larger group
    example:
        an university has 10,000 students, and I want to estimate their average study time. 
        Population: 10,000
        Sample: 500 selected students
        Variable being measured: study hours
        Goal: use the 500 stundets to estimate the average study gours for all 10,000 studets

Simple Random Sampling
    Simple Random Sampling is a probability sampling method in which every member of the population has an equal chance of being selected.
    Formula: P(selected) = n / N
        N = population size
        n = sample size
    if population size = 10,000, sample size = 500
        P(selected) = 500/10,000 = 0.05
        each population has 0.05% to get selected
    Methods to perfrom Simple Random sampling:
        1. Lottery Method: it is the process like You write every number on a separate piece of paper, mix them, and randomly draw three numbers.
            sample_df = df.sample(n=500, random_state=42)
        2. Sampling by Percentage: , seleting a proportion of the popuplation by parameter frac, example frac=0.10, 10% of population
            sample_df = df.sample(frac=0.10, random_state=42)
        3. Sampling without Replacement: after a member is selected, the same member cannot be selected again.
            sample_df = df.sample(n=500, replace=False, random_state=42)
        4. Sampling with Replacement: after an observation is selected, it is returned to the population and may be selected again.
            sample_df = df.sample(n=500, replace=Truem random_state=42)
    
    Advantages:
        1. No conscious selection bias
        2. easy to understand
        3. Statistical formulas work well
        4. every memeber has a known probability
    
    Disadvantages:
        1. requires complete population list
        2. small groupds may be underrepresented

    
Systematic Sampling  
    Systematic sampling is a probability sampling method where you select observations from an ordered population list at a fixed interval.
    implemenation steps:
        1. Choose a random starting point among (1 - k)
        2. Select every k-th observation after that.

        k = N / n
        where: 
            k = sampling interval
            N = population size
            n = sampling size
    When to use:
        1. Ordered population list
        2. the population is large
        3. Simple Random Sampling would be inconvenient
        4. there is no dangerous repeating pattern in th list.
    
    Advantages:
        1. Easy to perform 
        2. Faster than Simple Random Sampling
        3. Sample is spread across the population 
    Disadvantages:
        1. periodicity

Stratified Sampling
    Stratified Sampling is a probability sampling method in which the population is first devided into important 
    subgroups called strata, and then a sample is selected from each stratum. 
    Formula:
        nₕ = (Nₕ / N) * n
    Where:
        nₕ = Sample size from Stratum h
        Nₕ = population size of stratum h
        N = total population size
        n = total sample size

Cluster Smapling 
    The population is divided into natural groups called clusters and then only some clusters are randomly selected
    Example:
        Population: students from 100 schools
        Randomly select 10 schools
        Study students in those 10 schools
    Here: 
        Population: all students in the city
        Clusters: schools
        Seleted clusters: randomly selected 10 schools
"""

""" 
1. Verify sampling design
2. Validate the selected records
3. Check sample size and coverage
4. Check missing data and nonresponse
5. Evaluate categorical representation
6. Evaluate numerical representation
7. Compare distributions
8. Check subgroup adequacy
9. Measure sampling uncertainty
10. Check design-specific problems
11. Evaluate fitness for purpose
12. Accept, accept with limitations, or resample
"""