
# Step 1: Import required libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 2: Load your cleaned and engineered dataset
df = pd.read_csv("feature_engineered.csv")

# (Re-run your feature engineering steps here if needed)
# For simplicity, we’ll just select relevant numeric columns now

# Step 3: Select final features for clustering
features = [
    'Price', 'Quantity', 'Order Total', 'Avg_Price_Per_Item',
    'High_Value_Order', 'Is_Weekend', 'Year', 'Month_Num'
]
X = df[features]

# Step 4: Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Use Elbow Method to find best number of clusters
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Step 6: Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method - Optimal K')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.grid(True)
plt.show()

# Step 7: Apply K-Means with optimal k (e.g., choose k=3 or k=4 based on elbow)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Step 8: Show clustered sample
print("\nClustered Data Sample:")
print(df[['Price', 'Quantity', 'Order Total', 'Cluster']].head())

# step 9 : Save the clustered data to a new CSV file
df.to_csv("restaurant_sales_clustered.csv", index=False)
print("Clustered data saved to 'restaurant_sales_clustered.csv")
