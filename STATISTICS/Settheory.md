# set theory

1. set :- collection of well-defined objects.

   * (well-defined means there is no confusion about what belongs to the set.)
  
   example:- 
   Set A = {COVID, Dengue, Malaria}
   Set B = {Chickenpox, Dengue, ulcer}

   Each set contains diseases that are well-defined. So, they are valid sets.

2. Collection :- collection can be any group of items, not well-defined.

   example:- All common diseases (not well-defined that means it is not clear like what disease)

   * Union (A ∪ B)
     Combines all elements from both sets (no duplicates).

     Example:
     A = {COVID-19, Dengue}
     B = {Malaria, Dengue}
     A ∪ B = {COVID-19, Dengue, Malaria}

   * Intersection (A ∩ B)
     Includes only elements that are common to both sets.

     Example:
     A = {COVID-19, Dengue}
     B = {Malaria, Dengue}
     A ∩ B = {Dengue}

    * Difference (A – B or A \ B)
      Elements in A but not in B.

      Example:
      A = {COVID-19, Dengue}
      B = {Malaria, Dengue}
      A – B = {COVID-19} 

Example:-
 #Problem Statement

  Problem:
  In a hospital of 1000 patients:
  300 have a disease in Set A (viral diseases)
  250 have a disease in Set B (infected diseases)
  100 have diseases from both sets (A ∩ B)

  Find: Probability that a randomly selected patient has either a viral or infected disease.

  Solution:
  Given:
  P(A) = 300 / 1000 = 0.30
  P(B) = 250 / 1000 = 0.25
  P(A ∩ B) = 100 / 1000 = 0.10

  Using the formula:
  P(A ∪ B) = 0.30 + 0.25 – 0.10 = 0.45
  There is a 45% chance that a randomly selected patient has either a viral or infected disease.


3. Conditional Probability:-

Conditional probability is the probability of event A happening that event B has already occurred.

This is written as:

P(A|B) = P(A∩B)/ P(B)

A depends on B.
B is already happened.

Example:-
#Problem Statement:-
  In a population of 1000 patients:
  300 have viral diseases (Set A)
  250 have infected diseases (Set B)
  100 have both viral and infected diseases (A ∩ B)

  What is the probability that a patient has a viral disease, given that they already have a infected disease?

  Solution:-
  P(A) = 300 / 1000 = 0.30
  P(B) = 250 / 1000 = 0.25
  P(A ∩ B) = 100 / 1000 = 0.10

  Formula:
  P(A | B) = P(A ∩ B) / P(B)
  P(A | B) = 0.10 / 0.25 = 0.40

  There is a 40% chance that a patient has a viral disease, given that they already have a infected disease.

4. Expected value (mean): Average of the values.
5. Variance :  How much the values are different from the average.
6. Standard Deviation : The average distance from the mean.(Square root of the variance.)

Example :
#Problem Statement
In a hospital of 1000 patients:
300 have viral diseases
250 have infected diseases
100 have both viral and infected diseases
Find the mean, variance, and standard deviation of patient counts in these three groups.

Solution:- 

Step 1: Calculate Mean
Mean = (300 + 250 + 100) / 3 
     = 650 / 3 
     = 217

Step 2: Calculate Variance
Calculate differences from mean:
300 - 217 = 83
250 - 217 = 33
100 - 217 = -117

Square these differences:
83² = 6889, 33² = 1089, (-117)² = 13689

Average the squared differences:
Variance = (6889 + 1089 + 13689) / 3 = 7222.33

Step 3: Calculate Standard Deviation
Standard Deviation = squareroot(7222.33) = 85

7. Bernoulli Theorem:- 
 Only 2 outcomes: Success (1) or Failure (0).
 Probability of success = p, failure = 1-p

8. Binomial Distribution:-
  Perform n independent Bernoulli trials (same experiment repeated n times).
  Counts the total number of successes in those trials.

9. Normal Distribution:-
   When the mean, median, and mode of data are very close, the data is normally distributed.

   Example:-

   #Problem Statement
   In a hospital of 1000 patients:
   300 have viral diseases
   250 have infected diseases
   100 have both viral and infected diseases
   
   Questions:-

   1. Using Bernoulli theorem, what is the probability that a randomly selected patient has a viral disease?
   2. If 10 patients are selected randomly, what is the probability exactly 4 have viral disease? (Binomial distribution)
   3. Over time, the daily number of patients with viral disease tends to follow a normal distribution — explain what this means  in terms of mean, median, and mode.?

   Given:
Total patients = 1000
Viral diseases (Set A) = 300
infected diseases (Set B) = 250
Both viral & infected diseases = 100

1. Bernoulli Theorem
   Question: What is the probability that a randomly selected patient has a viral disease?
   Success: Patient has viral disease
   Failure: Patient does not have viral disease
   p = 300/1000 = 0.3

   Probability p = 0.3 . (There is a 30% chance that the patient has a viral disease)
