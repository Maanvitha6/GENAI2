
# Step 1: Import pandas
import pandas as pd

# Step 2: Load the CSV file into a DataFrame
df = pd.read_csv("restaurant_sales_data_cleaned.csv")

# Step 3: Show first 5 rows of the dataset
print("Sample Data:")
print(df.head())

# Step 4: Show all column names
print("\nColumn Names:")
print(df.columns.tolist())

# Step 5: Show dataset information (rows, columns, data types, nulls)
print("\nDataset Info:")
print(df.info())
+++++++++
# Feature Engineering for Restaurant Sales Data

# Step 6: Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])  # Feature Transformation

# Step 7: Extract date-related features
df['Year'] = df['Order Date'].dt.year                # Feature Extraction
df['Month_Num'] = df['Order Date'].dt.month          # Feature Extraction
df['Day'] = df['Order Date'].dt.day                  # Feature Extraction
df['Weekday'] = df['Order Date'].dt.day_name()       # Feature Extraction
df['Is_Weekend'] = df['Weekday'].isin(['Saturday', 'Sunday']).astype(int)  # Feature Extraction

# Step 8: Create new numeric features
df['Avg_Price_Per_Item'] = df['Order Total'] / df['Quantity']   # Feature Creation
df['High_Value_Order'] = (df['Order Total'] > 100).astype(int)  # Feature Creation

# Step 9: Encode categorical columns using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Category', 'Payment Method'], drop_first=True)  # Feature Transformation

# Step 10: Show the final dataframe with new features
print("\nFeature-Engineered Data Sample:")
print(df_encoded.head())

# Show all column names
print("\nColumn Names:")
print(df.columns.tolist())

#save to new csv file
# Assuming df_encoded is your final feature-engineered DataFrame
df_encoded.to_csv("restaurant_sales_feature_engineered.csv", index=False)

print("Feature-engineered data saved to 'restaurant_sales_feature_engineered.csv'")
