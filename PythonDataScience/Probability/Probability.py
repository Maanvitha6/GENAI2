import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Step 1: Load the already cleaned dataset
df = pd.read_csv("restaurant_sales_data_cleaned.csv")

print("✅ Step 1: Dataset loaded.\n")

# 1. Probability: Chance of each payment method
print("📊 1. Probability of each Payment Method:")
print(df['Payment Method'].value_counts(normalize=True), "\n")

# 2. Estimate: Average Order Total
avg_order = df['Order Total'].mean()
print("📊 2. Estimated Average Order Total: $", round(avg_order, 2), "\n")

# 3. Inference (Bayes): P(Credit Card | Main Dishes)
main_dishes = df[df['Category'] == 'Main Dishes']
bayes_result = (main_dishes['Payment Method'] == 'Credit Card').mean()
print("📊 3. Inference (Bayes): P(Credit Card | Main Dish) =", round(bayes_result, 2), "\n")

# 4. Density Plot for Prices
print("📈 4. Density Plot of Item Prices (displaying graph)...")
df['Price'].plot(kind='density', title='Price Density')
plt.xlabel("Price ($)")
plt.grid(True)
plt.show()

# 5. PMF: Payment Method Frequency (same as probability)
print("📊 5. PMF - Payment Method Distribution:")
print(df['Payment Method'].value_counts(normalize=True), "\n")

# 6. PDF: Price Distribution already shown in density plot
print("📊 6. PDF - Shown in the density plot of prices above.\n")

# 7. Normal Distribution: Check for Order Totals
mean_order = df['Order Total'].mean()
std_order = df['Order Total'].std()
print("📊 7. Normal Distribution of Order Totals:")
print("Mean =", round(mean_order, 2), ", Std Dev =", round(std_order, 2), "\n")

# 8. Point Estimation: Avg Quantity
point_estimate_qty = df['Quantity'].mean()
print("📊 8. Point Estimate (Avg Quantity per Order):", round(point_estimate_qty, 2), "\n")

# 9. Confidence Margin: 95% CI for Order Total
conf_interval = stats.t.interval(0.95, len(df)-1, loc=mean_order, scale=stats.sem(df['Order Total']))
print("📊 9. 95% Confidence Margin for Order Total: $", round(conf_interval[0], 2), "to $", round(conf_interval[1], 2), "\n")

# 10. Hypothesis Testing: Credit Card vs Cash Spending
credit_orders = df[df['Payment Method'] == 'Credit Card']['Order Total']
cash_orders = df[df['Payment Method'] == 'Cash']['Order Total']
t_stat, p_value = stats.ttest_ind(credit_orders, cash_orders, equal_var=False)

print("📊 10. Hypothesis Testing:")
print("T-Statistic =", round(t_stat, 2), "| P-Value =", round(p_value, 4))
if p_value < 0.05:
    print("✅ Result: Significant difference in spending between Credit Card and Cash users.\n")
else:
    print("❌ Result: No significant difference in spending between the groups.\n")

# 11. Save Final Output Dataset (only useful columns)
final_df = df[['Category', 'Item', 'Price', 'Quantity', 'Order Total', 'Payment Method']]
final_df.to_csv("cleaned_restaurant_output.csv", index=False)
print("✅ 11. Final output saved to: 'cleaned_restaurant_output.csv'")
