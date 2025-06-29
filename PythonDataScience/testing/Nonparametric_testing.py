import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu, kruskal, wilcoxon

# Step 1: Load the dataset
df = pd.read_csv("restaurant_non_parametric.csv")
print(" Dataset Loaded Successfully!")

# 1. Chi-Square Test Example 1: Day_Type vs Payment_Method

print("1. Chi-Square Test: Day_Type vs Payment_Method")

table1 = pd.crosstab(df['Day_Type'], df['Payment_Method'])
print("\nContingency Table (Day_Type vs Payment_Method):\n", table1)

chi2, p, dof, expected = chi2_contingency(table1)
print(f"Chi-Square Statistic: {chi2:.2f}, p-value: {p:.4f}")

if p < 0.05:
    print("Payment Method depends on Day Type (Significant relationship).")
else:
    print("No significant relationship between Day Type and Payment Method.")


# 2. Chi-Square Test: Branch vs Payment_Method

print("2. Chi-Square Test: Branch vs Payment_Method")

table2 = pd.crosstab(df['Branch'], df['Payment_Method'])
print("\nContingency Table (Branch vs Payment_Method):\n", table2)

chi2, p, dof, expected = chi2_contingency(table2)
print(f"Chi-Square Statistic: {chi2:.2f}, p-value: {p:.4f}")

if p < 0.05:
    print("Payment Method depends on Branch (Significant Relationship).")
else:
    print("No significant relationship between Branch and Payment Method.")

# 3. Mann-Whitney U Test: Ratings for Dish A vs Dish B

print("3. Mann-Whitney U Test: Ratings for Dish A vs Dish B")

dish_a = df[df['Dish'] == 'Dish A']['Customer_Rating']
dish_b = df[df['Dish'] == 'Dish B']['Customer_Rating']

if len(dish_a) > 0 and len(dish_b) > 0:
    stat, p = mannwhitneyu(dish_a, dish_b, alternative='two-sided')
    print(f"Mann-Whitney U Statistic: {stat:.2f}, p-value: {p:.4f}")
    if p < 0.05:
        print("Significant difference in ratings between Dish A and Dish B.")
    else:
        print("No significant difference between Dish A and Dish B.")
else:
    print("Not enough data for both dishes to run Mann-Whitney test.")

# 4. Kruskal-Wallis Test: Ratings across Dish A, B, C

print("4. Kruskal-Wallis Test: Ratings across Dish A, Dish B, Dish C")

dish_c = df[df['Dish'] == 'Dish C']['Customer_Rating']

if len(dish_a) > 0 and len(dish_b) > 0 and len(dish_c) > 0:
    stat, p = kruskal(dish_a, dish_b, dish_c)
    print(f"Kruskal-Wallis Statistic: {stat:.2f}, p-value: {p:.4f}")
    if p < 0.05:
        print("At least one dish has different average ratings.")
    else:
        print("No significant difference across dishes.")
else:
    print("Not enough data for all three dishes to run Kruskal-Wallis test.")


# 5. Wilcoxon Signed-Rank Test: Before vs After Discount Sales

print("5. Wilcoxon Signed-Rank Test: Before vs After Discount Sales")

before = df['Before_Discount_Sales']
after = df['After_Discount_Sales']

if len(before) == len(after):
    stat, p = wilcoxon(before, after)
    print(f"Wilcoxon Statistic: {stat:.2f}, p-value: {p:.4f}")
    if p < 0.05:
        print("Sales significantly changed after discount.")
    else:
        print("No significant change in sales after discount.")
else:
    print("Sample sizes for Before and After sales do not match for Wilcoxon Test.")

