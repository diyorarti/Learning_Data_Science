"""
K-Means Clustering:
    1. Intuition
        K-Means is an unsupervised learning algorithm used to group similar data points into clusters.
        Main idea:
            - X1 and X2 are initial cluster centroids.
            - • represents data points.
            - Each data point is assigned to the nearest centroid.
            - Then, the centroid is moved to the center of its assigned points.
            - This process repeats until the centroids stop changing much.

        Steps:
            Step 1: Choose initial centroids         Step 2: Assign each data                  Step 3: Recalculate the centroids
                X1, X2 = cluster centroids                   point to the nearest centroid     The centroid moves to the average position of the points assigned to it.
                •      = data points
                |      X1    •    • •   •    •       |      X1    •    • •   •    •            |         •  •   •    •
                |      • • •  • •                    |      • • •  • •                         |      • • •  X1 • •
                |      •     •  X2                   |      •     •  X2                        |      •     •
                |    •   •                           |    •   •                                |    • X2  •
                | •  • •                             | •  • •                                  | •  • •
                |______________________________      |______________________________           |_____________________________
            Step 4: Repeat Step 2 and Step 3 until the centroids become stable.

    2. K-Means Algorithm
        1. Step Randomly initialize K cluster centroids μ1, μ2, ..., μk  In examble above K=2(X1, X2)
        2. Repeat two steps:{
                1. Assign points to cluster centroids
                    For i = 1 to m:
                        c_i = index(from 1 to K) of cluster centroid closest to X_i
                        minₖ || x⁽ⁱ⁾ - μₖ ||²
                2. Move The cluster centroids
                    For k=1 to K:
                        μK := average(Mean) of points assigned to cluster k

    3. Optimization Objective of K-Means:
            c_i = index of cluster (1, 2, ...K) to which example X_i is currently assigned
            μK = cluster centroid K (the location of cluster centroid)
            μ_C_i = cluster centroid of cluster tow which example x_i has been assigned
        Cost Function
        J(c⁽¹⁾, ..., c⁽ᵐ⁾, μ₁, ..., μₖ) = 1/m ∑ᵢ₌₁ᵐ || x⁽ⁱ⁾ - μ_c⁽ⁱ⁾ ||²
        Meaning:
            J = cost function
            m = number of training examples / data points
            i = index of one data point    Example: i = 1, 2, 3, ..., m
            x^(i) = one data point Example: x^(1) is the first data point.
            c^(i) = cluster number assigned to x^(i) Example: if x^(i) belongs to cluster 2, then c^(i) = 2.
            μ_k = centroid of cluster k Example: μ_1 is centroid of cluster 1.
            μ_c^(i) = centroid of the cluster assigned to x^(i) Example: if c^(i) = 2, then μ_c^(i) = μ_2.
            || x^(i) - μ_c^(i) ||² = squared distance between data point x^(i) and its assigned cluster centroid.
            ∑ from i=1 to m = add this distance for all data points.
            1/m = take the average
    
    4. Initializing K-Means
       Random initialization:  
                     Choose K < m
       

"""
