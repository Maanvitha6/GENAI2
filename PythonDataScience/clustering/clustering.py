import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("restaurant_sales_data_cleaned.csv")

print(" Dataset Loaded with shape:", df.shape)

# ------------------------------- 1. Clustering (K-Means) -----------------------------------
print(" Clustering Customers Based on Order Total and Quantity...")

clustering_data = df[['Order Total', 'Quantity']].dropna()
scaler = StandardScaler()
scaled_data = scaler.fit_transform(clustering_data)

kmeans = KMeans(n_clusters=2, random_state=0)
df['Cluster'] = kmeans.fit_predict(scaled_data)

print(df[['Order Total', 'Quantity', 'Cluster']].head())

# ------------------------------- 2. Association Example ------------------------------------
print(" Association Example: Checking if higher Quantity is associated with higher Order Total...")

correlation, _ = pearsonr(df['Quantity'].fillna(0), df['Order Total'].fillna(0))
print("Correlation between Quantity and Order Total:", correlation)

# ------------------------------- 3. Dependence Example -------------------------------------
print(" Dependence Example: Total Order depends on Quantity (Logical Check)...")

df['Estimated Total'] = df['Quantity'] * df['Price']
print(df[['Quantity', 'Price', 'Order Total', 'Estimated Total']].head())

# ------------------------------- 4. Causation Example --------------------------------------
print(" Causation Example: Effect of Month on Sales Count (Chi-Square Test)...")

sales_per_month = pd.crosstab(df['Month'], df['Category'])
chi2, p, dof, expected = chi2_contingency(sales_per_month)
print(f"Chi-Square Statistic: {chi2}, p-value: {p}")

# ------------------------------- 5. Correlation Example -------------------------------------
print(" Correlation: Quantity vs Order Total...")

corr, _ = pearsonr(df['Quantity'].fillna(0), df['Order Total'].fillna(0))
print("Correlation Coefficient (Quantity vs Order Total):", corr)

# ------------------------------- 6. Variance Example ---------------------------------------
print(" Variance in Daily Sales Amount...")

variance = df['Order Total'].var()
print("Variance in Order Total:", variance)

# ------------------------------- 7. Covariance Example -------------------------------------
print(" Covariance between Quantity and Order Total...")

covariance = df[['Quantity', 'Order Total']].cov()
print(covariance)

# ------------------------------- 8. Simpson's Paradox Example ------------------------------
print(" Simpson's Paradox: Check Dine-in vs Takeaway reviews by Month...")

branch_data = df[['Payment Method', 'Order Total', 'Month']].dropna()
takeaway_sales = branch_data[branch_data['Payment Method'] == 'Takeaway'].groupby('Month').count()['Order Total']
dinein_sales = branch_data[branch_data['Payment Method'] == 'Dine-in'].groupby('Month').count()['Order Total']

summary = pd.DataFrame({'Dine-in': dinein_sales, 'Takeaway': takeaway_sales}).fillna(0)
print(summary)


# ------------------------------- Visualization Example (K-Means) ---------------------------
plt.scatter(df['Order Total'], df['Quantity'], c=df['Cluster'], cmap='viridis')
plt.title('K-Means Clustering: Order Total vs Quantity')
plt.xlabel('Order Total')
plt.ylabel('Quantity')
plt.show()
