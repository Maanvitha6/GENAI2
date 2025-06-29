import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix
import numpy as np

# Step 1: Load the dataset
df = pd.read_csv("restaurant_non_parametric.csv")
print("Dataset Loaded Successfully!")

#Example 1: Linear Regression → Predict Sales Amount from Customer Rating

print(" Example 1: Linear Regression → Predict After Discount Sales based on Customer Rating")

# Select Feature (X) and Target (y)
X_linear = df[['Customer_Rating']]  # Independent variable
y_linear = df['After_Discount_Sales']  # Target variable (continuous)

# Create and train Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_linear, y_linear)

# Make predictions
y_pred_linear = linear_model.predict(X_linear)

# Evaluate Linear Regression
print("Coefficient (Slope):", linear_model.coef_[0])
print("Intercept:", linear_model.intercept_)
print("R² Score:", r2_score(y_linear, y_pred_linear))
print("Root Mean Squared Error (RMSE):", np.sqrt(mean_squared_error(y_linear, y_pred_linear)))


# Example 2: Logistic Regression → Predict High Rating (Yes/No) from Before Discount Sales

print(" Example 2: Logistic Regression → Predict High Customer Rating based on Before Discount Sales")

# Step 1: Create binary target column for High Rating (1 if rating >= 4, else 0)
df['High_Rating'] = df['Customer_Rating'].apply(lambda x: 1 if x >= 4 else 0)

# Select Feature (X) and Target (y)
X_logistic = df[['Before_Discount_Sales']]  # Feature (numeric)
y_logistic = df['High_Rating']  # Target (binary 0/1)

# Create and train Logistic Regression model
logistic_model = LogisticRegression()
logistic_model.fit(X_logistic, y_logistic)

# Make predictions
y_pred_logistic = logistic_model.predict(X_logistic)

# Evaluate Logistic Regression
print("Model Coefficient (Weight for Sales):", logistic_model.coef_[0][0])
print("Intercept:", logistic_model.intercept_[0])
print("Accuracy:", accuracy_score(y_logistic, y_pred_logistic))
print("Confusion Matrix:\n", confusion_matrix(y_logistic, y_pred_logistic))
