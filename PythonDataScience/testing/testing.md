
* What is Testing ?
 
  It is like checking a claim or observation about data is true (or) not. Its like a "Is what i am seeing in the data really 
  
  true , or is it just happening by chance ?

1. Parametric Test :- It is a type of statistical  test . 

   * data follows a known distribution, usually Normal Distribution (bell curve shape).

   * Uses parameters like mean and standard deviation for calculations . 

   * we apply parametric test when data is numbers. 

   * Parametric Tests help compare numerical things (like sales) between two or more groups, but only if data follows a normal
   
     distribution."

   * Types of parametric tests :- 

     | Test         | When to Use                               | Restaurant Example                       |
     |--------------|-------------------------------------------|-----------------------------------------|
     | t-test       | Compare means of 2 groups                | Weekday vs Weekend Sales                |
     | Paired t-test| Compare before and after same group      | Sales before vs after discount          |
     | ANOVA        | Compare 3 or more groups                 | Breakfast vs Lunch vs Dinner Sales      |
     | Z-test       | Sample mean vs population mean (large sample) | This month’s sales vs Historical Average |


     Example :-

     Business Question:

     "Do customers spend more on weekends compared to weekdays in restaurant?"

     | Group         | Sales Data ($)               |
     |-------------- |-----------------------------|
     | Weekday Sales | 1000, 1100, 1200, 1050, 1150 |
     | Weekend Sales | 1500, 1600, 1550, 1520, 1580 |


     Here:

     Data is numerical (Sales amount in $).

     Data is assumed to follow normal distribution.

     We want to compare averages (means) between two groups.

     So, we use a t-test (a parametric test).

2. Non-parametric test :- 

   Non-Parametric Testing is a type of statistical testing that is used when:

   Your data is not normally distributed.

   Your data is categorical (like Payment Method: Cash/Card) or ordinal (like Customer Ratings: 1-5 stars)

   Sample size is small .

   You cannot calculate a mean and standard deviation reliably.

   * When we should use Non-parametric testing ?

     | Use Non-Parametric Tests When                     | Example                                     |
     |---------------------------------------------------|--------------------------------------------|
     | Data is Categorical (text or labels)              | Payment Method: Cash, Card, Online         |
     | Data is Ordinal (ranked, not numeric scale)       | Customer Rating: 1, 2, 3, 4, 5             |
     | Data is Non-Normally Distributed                  | Sales data with big outliers or skewed data|
     | Sample size is too small for parametric tests     | Less than 30 records                      |


   * Types of Non-parametric Testing :-

     | Test                | Used For                                       | Example                        |
     |---------------------|-----------------------------------------------|--------------------------------|
     | Chi-Square Test     | Relationship between 2 categories              | Day Type vs Payment Method     |
     | Mann-Whitney U Test | Compare 2 independent groups (non-normal data) | Ratings for 2 dishes           |
     | Kruskal-Wallis Test | Compare 3 or more groups (non-normal data)     | Wait times across 3 branches   |
     | Wilcoxon Test       | Before-After for same group (non-normal data)  | Sales before vs after discount |

3. Chi-square test :- 

   Chi-Square test tells us whether two categories are dependent on each other or not. 

   * When to use chi-square test ?

     | Condition                                          | Example (Restaurant)                                   |
     |----------------------------------------------------|--------------------------------------------------------|
     |  Both variables are categorical                 | Day Type (Weekday/Weekend), Payment Method (Cash/Card) |
     |  You want to check for dependency or association | Is Payment Method dependent on Day Type?               |

<<<<<<< HEAD
     | ----------------------------------------------------- | ------------------------------------------------------ |

     |  Both variables are categorical                     | Day Type (Weekday/Weekend), Payment Method (Cash/Card) |

     |  You want to check for dependency or association    | Is Payment Method dependent on Day Type?               |
=======
>>>>>>> cbcb0008da4da0488893b32736e5c1c92f0ee459

    Hypotheses :-

    | Hypothesis                  | Meaning                                                    |
    |-----------------------------|------------------------------------------------------------|
    | Null Hypothesis (H0)        | No relationship between variables (They are independent)  |
    | Alternative Hypothesis (H1) | There is a relationship between variables (They are dependent) |


    Decision Rule :-

    | Condition         | Meaning                                                     |
    |-------------------|-------------------------------------------------------------|
    | If p-value < 0.05 | Reject Null → There is a significant relationship           |
    | If p-value > 0.05 | Fail to reject Null → No relationship, variables are independent |


4. A/B Testing :- 

   A/B Testing is a statistical experiment where you compare two different versions of something (Version A and Version B) to
   
   find out which one performs better.

   Concept Flow :-

   | Step    | What Happens                                                                                           |
   |-------- |-------------------------------------------------------------------------------------------------------|
   | Step 1  | Select a business question (Ex: Does giving discount increase sales?)                                  |
   | Step 2  | Divide your audience into 2 groups: Group A and Group B                                                |
   | Step 3  | Apply two different treatments/versions: Group A → No Discount (Old), Group B → Discount (New)         |
   | Step 4  | Collect outcome data (Ex: Sales for both groups)                                                       |
   | Step 5  | Perform a statistical test (t-test or Mann-Whitney depending on data type)                             |
   | Step 6  | Make decision based on p-value: If p < 0.05 → Difference is significant                                 |


   Hypothesis in A/B testing :-

   | Term                        | Meaning                                 |
   |-----------------------------|-----------------------------------------|
   | Null Hypothesis (H0)        | There is no difference between A and B |
   | Alternative Hypothesis (H1) | There is a difference between A and B  |


   Statistical tests used in A/B testing :-

   | If Data is                          | Use This Test                       |
   |-------------------------------------|-------------------------------------|
   | Normally Distributed (Numeric Data) | t-test (Independent or Paired)      |
   | Not Normally Distributed            | Mann-Whitney U Test or Wilcoxon Test |
   | Categorical Outcomes                | Chi-Square Test                     |


   Example 1:- 

   | Group   | Data Source           | Explanation                  |
   |-------- |---------------------- |-----------------------------|
   | Group A | Before_Discount_Sales | Sales before giving discount |
   | Group B | After_Discount_Sales  | Sales after giving discount  |


    Test Type -  Paired t-test (Because same customers before and after).

    Example 2 :- 

    | Group   | Data Source   | Explanation              |
    |-------- |-------------- |-------------------------|
    | Group A | Weekday Sales | Sales on Monday-Friday  |
    | Group B | Weekend Sales | Sales on Saturday-Sunday |


    Test Type - Independent t-test (Two independent groups) .

5. Linear Regression :- 

   Linear Regression is a statistical method used to predict a continuous numeric value based on one or more input (independent)
   
   variables.

   Key points about Linear Regression :-

   | Feature         | Details                                                                   |
   |---------------- |--------------------------------------------------------------------------|
   | Purpose         | To predict a numeric (continuous) output                                 |
   | Output          | Any number (e.g., sales amount, price, number of customers)              |
   | Relationship    | Shows linear relationship between input (X) and output (Y)               |
   | Formula         | Y = mX + c (Straight Line Equation)                                      |
   | Input Variables | One or more independent variables (like day, number of customers)        |
   | Output Variable | A continuous numeric variable                                             |
   | Graph Type      | Straight line                                                            |


   Example :- 

   Business Question:

   "Can we predict today’s sales based on the number of customers and average order value?"

   | Input (X)                            | Output (Y)  |
   |--------------------------------------|-------------|
   | Number of customers, Avg order value | Total Sales |


6. Logistic Regression :- 

   Logistic Regression is a classification algorithm used to predict the probability of a categorical outcome, often binary (like
   
   Yes/No, 0/1).

   Key points about logistic regression :- 

   | Feature         | Details                                                            |
   |---------------- |--------------------------------------------------------------------|
   | Purpose         | To predict category/class (e.g., Yes/No, Pass/Fail, 0/1)           |
   | Output          | Probability between 0 and 1, usually converted to Yes/No           |
   | Formula         | Logistic function (S-shaped curve)                                 |
   | Input Variables | One or more independent variables (like order value, waiting time) |
   | Output Variable | Binary or multi-category                                            |
   | Graph Type      | Sigmoid / S-curve                                                  |

   Example :- 

   Business Question:

   "Can we predict whether a customer will give positive feedback (Yes/No) based on order total and waiting time?

   | Input (X)                  | Output (Y)       |
   |--------------------------- |----------------- |
   | Order amount, Waiting time | Feedback: Yes/No |


   












   

