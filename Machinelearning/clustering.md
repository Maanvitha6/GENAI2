
1. Recommendation Systems :-

   It is a smart tool that suggests items to users based on past behavior, preferences, or similar users.

   Example:

   Netflix recommends movies you might like.

   Amazon shows products based on your past purchases.

   Zomato suggests restaurants you might love.

     * Why do we need Recommendation systems ? 

       Helps users discover content without searching.

       Improves user experience.

       Increases sales or engagement for businesses.

2. Filtering :-

   Filtering out or selecting the most relevant items from a large set — based on some logic.

   There are two main filtering techniques. They are :

   1. Content-based Filtering :-

      Recommends items that are similar to what the user already liked or purchased, based on the features or attributes of those 
      
      items.

      Example :-

      If a user buys Nike Running Shoes, content-based filtering looks at the features:

      Brand: Nike

      Category: Running Shoes

      Color: Black

      Size: 8

      Then it recommends other shoes with similar attributes:

      Adidas Running Shoes (same category)

      Nike Sneakers (same brand)

      Puma Sports Shoes (similar style)

      Logic: Based on the item’s description, recommend similar items.

   2. Collaborative-based Filtering :-

      Recommends items based on what other users with similar tastes or behavior have liked — even if the current user has never 
      
      seen those items before.

      Example :-

      Let’s say User A buys:

      Phone Case

      Power Bank

      Bluetooth Earphones

      User B also buys:

      Phone Case

      Power Bank

      So the system recommends Bluetooth Earphones to User B.

      Even if User B hasn’t searched for earphones, the system sees a pattern among users and makes the suggestion.

  * which filtering technique is suitable for business-decision making and why ? 

    Collaborative filtering is suitable for decision-making because : It gives better business insights such as 

    . What users like together

    . What combinations drive more sales

    . How groups of users behave

    . What products or services are trending among certain user segments


3. Clustering :-  Grouping data points based on their similarity. 

  . It is technique in Unsupervised Learning, which has no labels finds patterns from the data. 

  Example :- Customer Shopping Behavior

  Imagine a supermarket has the following data about their customers:

  | Customer | Total Money Spent | Number of Visits |
  | -------- | ----------------- | ---------------- |
  | A        | $200              | 2                |
  | B        | $1500             | 15               |
  | C        | $300              | 3                |
  | D        | $1200             | 12               |
  | E        | $250              | 2                |
  
    1.  What clustering will do ? It will automatically group similar customers together. 

    | Cluster             | Who Belongs Here | 
    | ------------------- | ---------------- | 
    | Low Spending Group  | A, C, E          | 
    | High Spending Group | B, D             |

    * Why Clustering ? 

      . To understand hidden patterns in your data.

      . To create customer segments.

      . To make targeted marketing strategies.

      . To improve business decisions.

4. Clustering Techniques :-

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

    * Methods to select K-value number of clusters :- There are 4 methods, They are :

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
