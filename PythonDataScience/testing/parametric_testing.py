import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, ttest_rel, f_oneway, norm, shapiro

# Step 1: Load the dataset
df = pd.read_csv("sample_restuarant_data.csv")

print("Dataset Loaded Successfully!")

# 1. Independent t-test (Weekday vs Weekend Sales)

print("\n 1. Independent t-test: Weekday vs Weekend Sales")

# Create groups
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekdays_sales = df[df['Day'].isin(weekdays)]['Sales']
weekend_sales = df[df['Day'].isin(['Saturday', 'Sunday'])]['Sales']

# Run t-test
t_stat, p_value = ttest_ind(weekdays_sales, weekend_sales, equal_var=False)
print(f"T-Statistic: {t_stat:.2f}, P-Value: {p_value:.4f}")

if p_value < 0.05:
    print(" Significant difference between Weekday and Weekend sales.")
else:
    print(" No significant difference.")


# 2. Paired t-test (Before vs After Discount)

print("\n 2. Paired t-test: Sales with and without Discount")

# Example - Take sales with Discount vs No Discount (Dummy pairing for demo purpose)
discount_yes = df[df['Discount_Applied'] == 'Yes']['Sales'][:30]  # Take first 30 for pairing
discount_no = df[df['Discount_Applied'] == 'No']['Sales'][:30]

# Run Paired t-test (make sure lengths are equal)
if len(discount_yes) == len(discount_no):
    t_stat, p_value = ttest_rel(discount_yes, discount_no)
    print(f"T-Statistic: {t_stat:.2f}, P-Value: {p_value:.4f}")

    if p_value < 0.05:
        print(" Sales after discount are significantly different.")
    else:
        print(" No significant difference after discount.")
else:
    print("Not enough paired samples for paired t-test.")


# 3. ANOVA (Breakfast vs Lunch vs Dinner Sales)

print("\n 3. ANOVA: Compare Sales across Meal Types")

breakfast_sales = df[df['Meal'] == 'Breakfast']['Sales']
lunch_sales = df[df['Meal'] == 'Lunch']['Sales']
dinner_sales = df[df['Meal'] == 'Dinner']['Sales']

f_stat, p_value = f_oneway(breakfast_sales, lunch_sales, dinner_sales)
print(f"F-Statistic: {f_stat:.2f}, P-Value: {p_value:.4f}")

if p_value < 0.05:
    print(" At least one meal type has significantly different sales.")
else:
    print(" No significant difference between meal types.")


#  4. Z-test (Current Sample Mean vs Historical Mean)

print("\n 4. Z-test: Current Sales vs Historical Average (Assumed)")

# Assume historical average sales = 1200, population std dev = 300
sample_sales = df['Sales']
sample_mean = np.mean(sample_sales)
population_mean = 1200
population_std = 300
n = len(sample_sales)

z_score = (sample_mean - population_mean) / (population_std / np.sqrt(n))
p_value = 2 * (1 - norm.cdf(abs(z_score)))

print(f"Z-Score: {z_score:.2f}, P-Value: {p_value:.4f}")

if p_value < 0.05:
    print(" Current sample sales are significantly different from historical average.")
else:
    print(" No significant difference compared to historical average.")

