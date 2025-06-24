GENAI CLASS 1 (May 29 2025)
BASIC PROBABILITY:-

* Probability - How likely the event is to occur. 
* random variable - we do something random - we get a result - we give it a number (just a number we use to describe the result)
* random experiment -  one of possible outcomes.(outcomes we can predict)
* basic outcome - possible outcome for the experiment.
* output - what we received based on our input.
* outcome - what we expecting we should achieve.
* population - whole dataset(superset)
* sample - subset of given population.
* sample space - set of all possible outcomes.(collecting the small amount of portion)
               tossing a coin - 2 outcomes - 2^n.
               rolling a dice - 6 outcomes - 6^n.
* event - subset of sample space. (collecting few of events where we are interested.)

Problem Statement:
A patient is randomly picked from a group of 5 patients to test for a disease. The group has 3 patients who tested positive and 2 who tested negative.

1.What is the random experiment?
  Picking one patient from the group.

2.If a patient is picked, what is the basic outcome?
 The selected patient.

3.If we assign positive = 1 and negative = 0, what is the random variable value if a patient with negative test is selected?
  0.

4.What is the output if one patient is selected?
  The patient selected in the random pick.

5.If the goal is to pick a patient who tested positive and the selected patient tested positive, what is the outcome?
  The outcome is achieved.

6.If the whole hospital has 1000 patients, what is the population?
  All 1000 patients in the hospital.

7.If we are selecting only 5 patients in the group, what is the sample?
  Only these 5 patients.

8.What is the sample space when picking one patient from 5?
  All 5 possible patients.

9. What is the event of picking a patient who tested positive?
   The subset of patients who have tested positive (3 patients).

* TYPES OF RANDOM VARIABLE:- 
    1.Discrete Random Variable - A variable that can take only specific separate values (complete value of any number)
       . Examples:- Number of patients diagnosed with a disease in a day (e.g., 1, 2, 3).
                    Number of symptoms a patient reports (e.g., 0, 1, 2).
                    Number of positive test results in a sample of patients (e.g., 4, 5, 6).
                    cricket score is 230 . score of soccer is 4 balls.
    2.Continuous Random Variable - A variable that can take any value within a range(number is finite with infinity values within the range.)
       . Examples:- Body temperature of a patient (e.g., 98.6°F, 99.3°F).
                    Time taken by a patient to recover from the disease (e.g., 5.25 days, 7.8 days).

* Distribution - rule that showing how often each outcome occurs.(how often each value occurs)
  . Example - How many patients have a fever of 100°F, 101°F, or 102°F?

* TYPES OF PROBABILITY DISTRIBUTION:- 
     1. Discrete Probability Distribution - outcomes are countable.
       . Example- If 1 patient is randomly picked from a group of 5 patients, the probability of picking each patient is:

          P(Patient 1) = 1/5
          P(Patient 2) = 1/5
          ...
          P(Patient 5) = 1/5
     2. Continuous Probability Distribution - takes values from a range.
       . Example- The probability distribution of the time (in days) it takes for patients to recover from the disease, e.g., 4.2 days, 5.5 days.

* FUNCTIONS:-
    ->function - specific input - specific output
  1. Probability Mass Function - (Pick one value and finding the probability)-set of probability value that assigns each of the value which taken by discrete random variable
     function which has probability and aggregating(sum). (applies to discrete random variable).
       * Thumbrule - pick one value and find the probability.
        . Example - Suppose 5 patients: A, B, C, D, E. Each has equal chance of being selected for a test.

                    Patient (X)	   P(X = patient)
                             A	        1/5
                             B	        1/5
                             C	        1/5
                             D	        1/5
                             E	        1/5

Sum of probabilities = 5 × 1/5 = 1
. What is the probability of selecting Patient C?
  P(X = C) = 1/5

2. Cumulative Distribution Function:- gives the probability that a random variable X is less than or equal to a certain value.
       * Thumbrule - putting one condition and adding all the outcomes.
        . Example- Patients: A, B, C, D, E
                   Each equally likely (1/5).
                   F(X) = P(X ≤ patient)
                   F(A) = 1/5
                   F(B) = P(A) + P(B) = 1/5 + 1/5 = 2/5
                   F(C) = P(A) + P(B) + P(C) = 3/5
                   F(D) = 4/5
                   F(E) = 5/5 = 1

. What is the probability of selecting patient A, B, or C?
  P(X ≤ C) = F(C) = 3/5 = 0.6

3. Probability Density Function:- calculating the probability function between two conditions.
    . Example- 





