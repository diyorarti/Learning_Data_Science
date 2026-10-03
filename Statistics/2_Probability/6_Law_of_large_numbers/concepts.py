"""
Law of Large Numbers
│
├── 1. Core idea
│   └── X̄ₙ → μ as n increases -> Convergence
|
├── 2. Weak Law of Large Numbers
│   └── Convergence in probability
│
├── 3. Strong Law of Large Numbers
│   └── Almost sure convergence
│
├── 4. Practical LLN simulation
│   ├── Running/cumulative mean
│   ├── Increasing n
│   └── Plot X̄ₙ against μ 
|
└── 5. Data Science applications
    ├── Estimation
    ├── Monte Carlo simulation
    ├── Model metrics
    └── Experimentation
"""


# Law Of Large Numer Core Idea:
"""
LLN is about convergence of the sample mean toward the population mean.
Large samples make sample-based estimates increasingly close to their corresponding population quantities.
    As sample size n increases:
        sample mean      → population mean
        sample variance  → population variance
        sample std       → population std
    under appropriate assumptions.

    example:
        population : Customer spending μ = 50
        sample-1: n=5 -> X̄=48
        sample-2: n=20 -> X̄=51.1
        sample-3: n=100 -> X̄=50.3
        sample-2: n=1000 -> X̄=51.02


    THe dinstinction between CLT and LLN
        CLT(Distribution): n↑ increases and sampling distribution of X̄  becomes approximately Normal
        LLN(Convergence): n↑ increases and sample mean X̄ₙ gets closer to population mean μ    

    Convergence  X̄ₙ → μ
    As the sample size n becomes larger, the sample mean X̄ tends to get closer to the population μ.
    Suppose:
        Population: μ=50
        X̄₅ = 42
        X̄₂₀ = 55
        X̄₁₀₀ = 51.8
        X̄₁₀₀₀ = 50.4
        X̄₁₀₀₀₀ = 50.05
        42 → 55 → 51.8 → 50.4 → 50.05. it is converging.

    Convergance doesn't mean every step gets closer. may be like: 50.8 → 50.3 → 50.6 → 50.1 → 50.2 → 50.02
"""

# Weak Law of Large Numbers
"""
The Weak Law of Large Numbers that the sample mean converges to the population mean in probability
    X̄ₙ ⟶ᵖ μ
    ⟶ᵖ this symbol means convergence in probability.
    Convergence in probability means that considering the sample mean if it is close enough
    Suppose if it is within 1 unit. 
    Example:
        Population mean μ = 50
        Convergence in probability 49 ≤ X̄ₙ ≤ 51

    The Formula: P(|X̄ₙ - μ| ≥ ε) → 0 
    Probaility that the sample mean is far from the population mean goes to zero as sample size increases.
    Weak LLN = large sample means are very likely to be close to the population mean.

"""

#  Strong Law of Large Numbers
"""
Strong LLN means that the running sample mean converges to μ almost surely.
    X̄ₙ ⟶ᵃ·ˢ· μ
    
    example:
        Population mean μ = 50
        n = 1        X̄₁      = 70
        n = 10       X̄₁₀     = 53.2
        n = 100      X̄₁₀₀    = 49.4
        n = 1,000    X̄₁₀₀₀   = 50.2
        n = 10,000   X̄₁₀₀₀₀  = 49.98
        ...

    the difference between Weak LLN and Strong LLN 
        Weak LLN: look at one sample size at a time
        Strong LLN: follow one entire sequence
"""