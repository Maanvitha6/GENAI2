import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("restaurant_sales_feature_engineered.csv")

# Step 1: Select numerical features
features = [
    'Price', 'Quantity', 'Year', 'Month_Num', 'Day', 'Is_Weekend',
    'Avg_Price_Per_Item', 'High_Value_Order'
]
X = df[features]

# Step 2: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply PCA with 3 components
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# Step 4: Explained variance
explained_var = pca.explained_variance_ratio_.cumsum()
plt.figure(figsize=(6, 4))
plt.plot(range(1, 4), explained_var, marker='o')
plt.title('Explained Variance by Top 3 PCA Components')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 5: Show component loadings (feature contributions)
loadings = pd.DataFrame(
    pca.components_.T,
    columns=['PC1', 'PC2', 'PC3'],
    index=features
)
plt.figure(figsize=(8, 5))
sns.heatmap(loadings, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("PCA Loadings (Top 3 Components)")
plt.tight_layout()
plt.show()

# Step 6: Output transformed data
pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2', 'PC3'])
print(pca_df.head())
