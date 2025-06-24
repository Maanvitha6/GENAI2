# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Read the dataset
df = pd.read_csv("instagram_users_1000.csv")

# Step 3: Print the rows
print(df.head())           # First 5 rows
print(df.tail())           # Last 5 rows
print(df.head(30))         # First 30 rows
print(df.tail(30))         # Last 30 rows

# Step 4: Display first 10 rows and 10 columns using different ways
print(df.iloc[:10, :10])
print(df.loc[:9, df.columns[:10]])
print(df[:10][df.columns[:10]])

# Step 5: Show specific range (350–355 rows, 10 columns)
print(df.iloc[350:355, :10])

# Step 6: Sort by Followers and reset index
df.sort_values(by='Followers', inplace=True)
print(df.head())
print(df.tail())
print(df.index)

df.reset_index(drop=True, inplace=True)
print(df.head())
print(df.tail())
print(df.index)

# Step 7: Add random Account_Created_Time column to simulate time
import random
df['Account_Created_Time'] = [f"{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}" for _ in range(len(df))]

# Convert to datetime and extract hour, minute, second
df['Time'] = pd.to_datetime(df['Account_Created_Time'], format='%H:%M:%S')
df['Hour'] = df['Time'].dt.hour
df['Minute'] = df['Time'].dt.minute
df['Second'] = df['Time'].dt.second

# Step 8: Drop Hour, Minute, Second
df.drop(columns=['Hour', 'Minute', 'Second'], inplace=True)
print(df.columns)
print(df.shape)

# Step 9: Save updated version
df.to_csv("instagram_users_1000_updated.csv", index=False)

# Step 10: Load and continue
df1 = pd.read_csv("instagram_users_1000_updated.csv")
print(df1.head())
print(df1.shape)

# Step 11: Check for missing data
print(df1.isnull().sum())

# Step 12: Add a fake Account_Created_Date for demo purposes
import numpy as np
df1['Account_Created_Date'] = pd.to_datetime(
    np.random.choice(pd.date_range("2023-01-01", "2023-12-31"), size=len(df1))
)

# Step 13: Convert date column and extract year, month, day
df1['Year'] = df1['Account_Created_Date'].dt.year
df1['Month'] = df1['Account_Created_Date'].dt.month
df1['Day'] = df1['Account_Created_Date'].dt.day
print(df1.shape)

# Step 14: Drop original date and time columns
df1.drop(columns=["Account_Created_Date", "Account_Created_Time", "Time"], inplace=True)
print("After dropping date and time columns:")
print(df1.shape)
print(df1.columns)

# Step 15: Save final version
df1.to_csv("instagram_users_1000_final.csv", index=False)

# Step 16: Load final version
df3 = pd.read_csv("instagram_users_1000_final.csv")
print(df3.head())
print(df3.shape)
print(df3.tail())
print(df3.columns)

# Step 17: Visualization 1 – Account Type distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df3, x='Account_Type', palette='Set2')
plt.title("📌 Account Type Distribution", fontsize=14)
plt.xlabel("Account Type")
plt.ylabel("Number of Users")
plt.grid(axis='y')
plt.tight_layout()
plt.show() 

# Visualization 2: Top 10 Users by Followers
top10 = df3.sort_values(by="Followers", ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top10['Followers'], y=top10['Username'], palette='coolwarm')
plt.title("🔥 Top 10 Most Followed Users", fontsize=14)
plt.xlabel("Followers")
plt.ylabel("Username")
plt.tight_layout()
plt.show()
