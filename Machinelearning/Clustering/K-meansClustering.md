
 ***Clustering Techniques*** :-

   1. K-means Clustering :-

      K-Means Clustering is an unsupervised machine learning algorithm used to partition a dataset into 'K' distinct groups
      
      (clusters).

      * Steps involved in K-means clustering :-

      | Step                                     | Description                                                                   |
      | ---------------------------------------- | ----------------------------------------------------------------------------- |
      | **1. Choose the number of clusters (K)** | You decide how many groups you want the data to be divided into               |
      | **2. Initialize Centroids**              | Randomly select K data points as the initial centroids (center of clusters)   |
      | **3. Assign Data Points to Clusters**    | Assign each point to the **nearest centroid** using a **distance formula**    |
      | **4. Recalculate Centroids**             | Calculate the new centroid (mean) of the data points assigned to each cluster |
      | **5. Repeat Steps 3–4**                  | Continue until centroids do not change (this is called **convergence**)       |

      * Key-terms in K-means :-

      | Term            | Meaning                                                                     |
      | --------------- | --------------------------------------------------------------------------- |
      | **K**           | Number of clusters                                                          |
      | **Cluster**     | A group of similar data points                                              |
      | **Centroid**    | The center (average position) of all points in a cluster                    |
      | **Distance**    | Measure used to assign points to centroids (usually **Euclidean Distance**) |
      | **Inertia**     | Total squared distance of points from their respective centroid             |
      | **Convergence** | The point where centroids stop changing (loop ends)                         |

    *Example:-

    Suppose you have the following 2D points:

    | Point | x | y |
    | ----- | - | - |
    | A     | 1 | 2 |
    | B     | 2 | 3 |
    | C     | 6 | 8 |
    | D     | 7 | 9 |

    You choose **K = 2**, and pick A and C as initial centroids:

    * Centroid 1: (1, 2)

    * Centroid 2: (6, 8)

    Now, compute distance of each point to both centroids:

    | Point | Distance to C1 (1,2) | Distance to C2 (6,8) | Cluster |
    | ----- | -------------------- | -------------------- | ------- |
    | A     | 0                    | \~7.81               | C1      |
    | B     | \~1.41               | \~6.40               | C1      |
    | C     | \~7.81               | 0                    | C2      |
    | D     | \~9.22               | \~1.41               | C2      |

    So:

    * Cluster 1 → A, B

    * Cluster 2 → C, D

    Now, calculate new centroids:

    * New Centroid 1 = Mean of A and B = $\left( \frac{1+2}{2}, \frac{2+3}{2} \right) = (1.5, 2.5)$

    * New Centroid 2 = Mean of C and D = $\left( \frac{6+7}{2}, \frac{8+9}{2} \right) = (6.5, 8.5)$

    These new centroids are used in the next iteration.

    Repeat Until Convergence

    Repeat:

    * Assign each data point to the nearest new centroid.

    * Recalculate centroids again.

    Do this until:

    * The centroids do not change significantly, or

    * You reach a maximum number of iterations.

    *** Techniques to select K-value number of clusters :- There are 4 techniques, They are :***

      1. Elbow Method :-

          Idea:

          Run K-Means with different values of K (e.g., from 1 to 10)

          For each K, calculate the inertia (sum of squared distances between points and their centroid)

          Plot K vs Inertia

         .  What to look for:

            The point where the inertia starts decreasing slowly (forms an elbow shape)

            That’s your optimal K.

      2. Silhouette Score :-

         Idea:

         Measures how well each point fits in its cluster vs other clusters.

         Score ranges from -1 to 1.

         (1 = well matched, 0 = overlapping, -1 = wrong cluster)

         .  What to do:

            Run K-Means for different K values.

            Choose the K with the highest silhouette score.

      3. Gap Statistic :-

         Idea:

         Compares clustering performance on your data vs. random data.

         Choose K that maximizes the gap between actual and random clustering.

         More complex, but great for high-dimensional data.

      4. Domain Knowledge :-

         Sometimes, you already know how many segments exist.

         Examples:

         Zomato: Regular, Occasional, First-time customers → K = 3

         Education levels: Beginner, Intermediate, Advanced → K = 3

    ***Common ways to initialize centroids***

    ### 1. **Random Initialization** (Basic, but Risky)

    * Randomly pick **K points from the dataset as initial centroids.

    Example in Python:

    ```python

    initial_centroids = data.sample(n=K, random_state=42)

    ```

---

   ### 2. **K-Means++ (Recommended for Real-World Use)**

   * Smarter initialization strategy that spreads out the initial centroids.

   * Process:

    1. Choose first centroid randomly.

    2. Choose next centroid with probability proportional to distance² from the closest existing centroid.

    3. Repeat until K centroids are selected.

    #### In sklearn (automatic):

    ```python

   from sklearn.cluster import KMeans

   model = KMeans(n_clusters=K, init='k-means++', random_state=42)


 *** 3. Hierarchical Clustering + K-Means Hybrid***

 * Use agglomerative clustering to form rough groupings first.

 * Then take the mean of those groups as initial centroids for K-Means.

 * Used when** prior structure is known or data is small enough to handle.

---

 ### 4. **Random Sampling + Mini-Batch K-Means** (For Huge Datasets)

 * For very large datasets, run K-Means on a random subset of the data first (e.g., 10,000 samples).

 * Use the centroids from that sample as initial centroids for full dataset K-Means.

  #### Use MiniBatchKMeans:

  ```python

  from sklearn.cluster import MiniBatchKMeans

  model = MiniBatchKMeans(n_clusters=K, init='k-means++', batch_size=10000)

  model.fit(large_dataset)
```

  5. **Domain Knowledge or Heuristic-based Initialization**

  * In some real-world problems, you might already know **logical groups** (e.g., regions, categories).

  * You can use **centroids of known categories** as initial points.


    1. How to decide the Centroid ?

       Average of all the data points in the cluster.

* Insights we can generate from clustering :-

  | Insight Type               | Example in Business                            |
  | -------------------------- | ---------------------------------------------- |
  | **Customer Segments**      | High spenders vs low spenders (Zomato, Amazon) |
  | **Product Groupings**      | Group similar products together                |
  | **User Behavior Patterns** | Cluster users by app usage frequency           |
  | **Target Marketing**       | Personalized ads to specific clusters          |
  | **Anomaly Detection**      | Identify outliers (unusual spending, fraud)    |

* Metrics used in K-means :-

  | Metric                      | Description                                                  |
  | --------------------------- | ------------------------------------------------------------ |
  | **WCSS (Inertia)**          | Measures compactness (lower is better)                       |
  | **Silhouette Score**        | Measures how well-separated the clusters are                 |
  | **Calinski-Harabasz Index** | Ratio of between-cluster variance to within-cluster variance |
  | **Davies-Bouldin Index**    | Lower values indicate better clustering                      |
 

5. Heirarichal Clustering :-

   Hierarchical Clustering is a clustering algorithm that builds a tree-like structure (called a dendrogram) to group data
   
   points. 

   * Two-types of Heirarichal Clustering :-
     
     | Type              | Description                                                                               |
     | ----------------- | ----------------------------------------------------------------------------------------- |
     | **Agglomerative** | Bottom-up: Start with each point as its own cluster, then **merge** step-by-step          |
     | **Divisive**      | Top-down: Start with all points in one cluster, then **split** step-by-step (less common) |

  * Steps in Agglomerative Clustering :-

    1. Start with N clusters (each point is its own cluster)

    2. Compute distances between every pair of clusters.

    3. Merge the two closest clusters.

    Repeat until:

    All points are in one cluster.

    Or, you reach a stopping condition (e.g., cut the tree)

    * Distance Between Clusters(Linkage Methods):-

      | Linkage Method       | Description                                         |
      | -------------------- | --------------------------------------------------- |
      | **Single Linkage**   | Distance between the closest points in two clusters |
      | **Complete Linkage** | Distance between the farthest points                |
      | **Average Linkage**  | Average distance between all points                 |
      | **Ward’s Method**    | Minimizes total variance (used in `scikit-learn`)   |

    Example:-

    Points: A, B, C, D

    Step-by-step merge:

      . Start: {A}, {B}, {C}, {D}

      . Find the two closest → merge A & B → {AB}, {C}, {D}

      . Merge closest again → {AB}, {CD}

      . Merge all → {ABCD}

    * Real-life Usecases:-

      | Use Case                 | Description                          |
      | ------------------------ | ------------------------------------ |
      | Customer segmentation    | Discover natural groups in customers |
      | Gene similarity analysis | Group genes by function              |
      | Document classification  | Cluster documents by content         |
