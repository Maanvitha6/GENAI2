import pandas as pd
from scipy.stats import ttest_rel, ttest_ind

# Step 1: Load the dataset
df = pd.read_csv("restaurant_non_parametric.csv")
print("Dataset Loaded Successfully!")


# Example 1: Paired t-test (Before vs After Discount Sales)

print("Example 1: Paired t-test → Before vs After Discount Sales (Same Group Customers)")

before = df['Before_Discount_Sales']
after = df['After_Discount_Sales']

t_stat, p_value = ttest_rel(before, after)

print(f"T-Statistic: {t_stat:.2f}, p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Significant difference: Discount had an impact on sales.")
else:
    print("No significant difference in sales after discount.")


# Example 2: Independent t-test (Weekday vs Weekend Sales)

print(" Example 2: Independent t-test → Weekday vs Weekend Sales (Two Independent Groups)")

weekday_sales = df[df['Day_Type'] == 'Weekday']['Before_Discount_Sales']
weekend_sales = df[df['Day_Type'] == 'Weekend']['Before_Discount_Sales']

t_stat, p_value = ttest_ind(weekday_sales, weekend_sales, equal_var=False)

print(f"T-Statistic: {t_stat:.2f}, p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Significant difference: Sales between Weekday and Weekend are different.")
else:
    print("No significant difference between Weekday and Weekend sales.")

