import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')
import seaborn as sns
from sqlalchemy import create_engine
import urllib.parse

# Step 1: Load the CSV file
df = pd.read_csv("restaurant_sales_data.csv")

# Step 2: Upload raw data to MySQL
username = "root"
password = "Maanvitha@2002"
host = "localhost"
port = "3306"
database = "restaurant_db"

encoded_password = urllib.parse.quote_plus(password)
connection_string = f"mysql+mysqlconnector://{username}:{encoded_password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

df.to_sql(name='restaurant_sales', con=engine, if_exists='replace', index=False)
print("Raw data uploaded to MySQL")

# Step 3: Initial exploration
print(df.head())
print(df.columns)
print(df.info())
print(df.shape)

# Step 4: Drop duplicate rows
df = df.drop_duplicates()

# Step 5: Drop rows with critical missing values
critical_cols = ['Order Date', 'Category', 'Item', 'Order Total', 'Payment Method']
df = df.dropna(subset=critical_cols)
print(f"Rows after dropping missing in {critical_cols}: {df.shape[0]}")

# Step 6: Drop unimportant columns (if they exist)
for col in ['Customer ID', 'Order ID']:
    if col in df.columns:
        df.drop(columns=col, inplace=True)
        print(f"Dropped column: {col}")

# Step 7: Clean 'Category' and 'Payment Method'
df['Category'] = df['Category'].astype(str).str.strip().str.title()
df['Payment Method'] = df['Payment Method'].astype(str).str.strip().str.title()

# Step 8: Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Step 9: Fill only a few selected nulls using statistical analysis
numeric_cols = df.select_dtypes(include='number').columns
non_numeric_cols = df.select_dtypes(include='object').columns

# Fill a few important numeric columns
for col in ['Quantity', 'Unit Price']:
    if col in df.columns and df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mean())
        print(f"Filled missing values in {col} using MEAN")

# Fill a few important categorical columns
for col in ['Location']:
    if col in df.columns and df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])
        print(f"Filled missing values in {col} using MODE")

# Step 10: Final missing value check
print("Final Missing Value Summary:\n", df.isnull().sum())

# Step 11: Add 'Month' column for analysis
df['Month'] = df['Order Date'].dt.to_period('M')

# Step 12: Visualize Top Categories
category_sales = df.groupby('Category')['Order Total'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 4))
sns.barplot(x=category_sales.index, y=category_sales.values, palette="viridis")
plt.title("Total Sales by Category")
plt.ylabel("Total Sales ($)")
plt.xlabel("Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 13: Visualize Top Items
top_items = df[df['Item'] != 'Unknown Item'].groupby('Item')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(6, 4))
sns.barplot(x=top_items.values, y=top_items.index, palette="Blues_r")
plt.title("Top 10 Selling Items")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Item")
plt.tight_layout()
plt.show()

# Step 14: Monthly Sales Trend
monthly_sales = df.groupby('Month')['Order Total'].sum()
plt.figure(figsize=(8, 4))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 15: Save cleaned data
df.to_csv("restaurant_sales_data_cleaned.csv", index=False)
print("Cleaned data saved to CSV")

# Step 16: Upload cleaned data to MySQL
df['Month'] = df['Month'].astype(str)
df.to_sql(name='restaurant_sales_cleaned', con=engine, if_exists='replace', index=False)
print("Cleaned data uploaded to MySQL!")

# Step 17: Close connection
engine.dispose()
print("Database connection closed.")
