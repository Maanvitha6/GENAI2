
1. Probability :- Probability is the chance of something happening.

   Real-time Example:- 

   Out of 100 customers, 60 paid using Credit Card.Then, the probability that a new customer pays by Credit Card is:

   60 out of 100 = 60% = 0.6

   Python Code:-

   df['Payment Method'].value_counts(normalize=True).

   This shows the chance of each payment method (like Cash, Card, Digital Wallet).

2. Estimate :- Estimate means guessing something using data. (can happen anything).

   Why we need to do Estimation?

   Estimation is when we don't know the full data, so we use sample data to guess something important.

   We can’t always ask or track every customer, so we estimate things like:

     1. Average order total.

     2. Average items bought.

     3. Average tips given.

   This helps restaurants make decisions without needing 100% data.

   Real-time Example :-

      |       Customer          |      Order Total (\$)      |

      |       --------          |      ----------------      |

      |         1               |           25               |

      |         2               |           30               |

      |         3               |           20               |

      |         4               |           40               |

      |         5               |           35               |

      |         6               |           45               |

      |         7               |           50               |

      |         8               |           38               |

      |         9               |           28               |

      |         10              |           31               |

   add up all orders:

   25 + 30 + 20 + ... + 31 = $342

   Then you divide by number of customers (10):

   342 / 10 = $34.2

   So, the estimated average order total is $34.20.

   You now use this estimate to:

   1. Predict how much money you will make next month.

   2. Decide pricing or discount strategies.

   3. Manage kitchen resources and staff.

3. Inference :- We use what we already know to guess something else.

   It helps answer:

   “If I know A, what is the chance of B?”

4. Bayes theorem :- Update our belief about something, based on new information.

   Real-time example :-

      Total customers = 100

      Customers who ordered Main Dishes = 40

      Among those 40, 24 paid using Credit Card.

      Now we ask:

      If we already know a customer ordered a Main Dish , what’s the chance they paid with Credit Card?

      Answer:

      Out of 40 Main Dish orders, 24 used Credit Card.

      → 24 / 40 = 0.6 = 60%

      That’s Bayesian Inference:

      We’re using existing data to predict future behavior.

5. Density :- Density shows how values are spread — whether they are clustered in one area or spread out widely.

   Real-time Example :-

     You analyze food prices:

     If most items are around $10, the density is high there.

     If prices range from $5 to $50, they are widely spread, showing low density.

     Density helps you understand where most values lie.

6. Probability Mass Function(PMF) :- PMF is used for discrete data (countable values like categories).

   It gives the exact probability of each value.

   Real-time Example :-

   You check 100 customer payments:

   50 used Credit Card → P(Credit Card) = 0.5

   30 used Cash → P(Cash) = 0.3

   20 used Online → P(Online) = 0.2

   PMF helps answer:

   What’s the chance a customer pays using Credit Card?

7. Probability Density Function :-

   PDF is used for continuous data (like price, time, weight).

   It doesn’t give exact probability but shows how likely values are around a range.

   Real-time Example :-
   
   Meal prices range from $5.50 to $49.90.

   Most meals are between $9 and $12, so PDF is highest there.

   PDF is low near $50 because few items are that expensive.

   PDF helps answer:

   How likely is a price to be in a specific range (e.g., around $10)?

8. Normal Distribution :- Normal distribution is a bell-shaped curve.Most values are near the average, and very few are extremely

   high or low.

   Real-time Example :- (Delivery Times)

   You record delivery times:

   Most deliveries take 30 minutes.

   Some take 25 or 35, very few take 15 or 45.

   This pattern is symmetrical around the mean → normal distribution.

   It helps you understand:

   What’s typical vs what’s rare in a dataset.

9. Point Estimation :- One best guess (number) for something.

   Real-time Example :-

   You want to know:

   "How many items does a customer usually order?"

    You take data from the last 100 orders:

    Some customers ordered 1 item, some 2, some 3...

    You calculate the average number of items ordered.

    Let’s say the result is 2.4.

    That’s your point estimate for average quantity per customer.

    This 2.4 is not always correct, but it’s your best guess based on data.

       1. Why it matters?

          Helps us make decisions or predictions.

10. Confidence Margin :-

    Confidence Margin is a safe range that tells you where the true average value is likely to fall.

    In very easy words:

    Instead of saying “the average is exactly $50,” we say “we are 95% sure it’s between $47 and $53.”

    Real-time Example :-

    You check 100 recent customer bills:

    Average bill = $50

    Using statistics, you calculate a confidence margin:

    “We are 95% confident the true average bill is between $47 and $53.”

    So:

    You’re not saying the average is exactly $50.

    You’re saying it’s most likely between $47 and $53.

11. Hypothesis Testing :-

    Hypothesis testing helps you decide:

    Are two things truly different?

    Or is the difference just by random chance?

    It’s like a scientific test to check if what you’re seeing in data is real — or just luck.

    Real-time Example :-

    You observe:

    "I think people who pay with Credit Card spend more than those who pay with Cash."

     You collect bill amounts from:

     50 Credit Card users

     50 Cash users

     You see:

     Average Credit Card bill = $22.10

     Average Cash bill = $19.90

     This looks different, but is it significantly different?

     This is where Hypothesis Testing helps:

     We check:

     Is this difference real?

     Or did it happen by chance in the sample?

         1. How hypothesis testing works ?

         Step 1:- State Hypotheses

         | Type                      | Statement                                                        |

         | ------------------------- | ---------------------------------------------------------------- |

         | Null Hypothesis (H₀)      | There is **no difference** between Credit Card and Cash spending |

         | Alternate Hypothesis (H₁) | Credit Card users **spend more** than Cash users                 |

         Step 2:- Run the Test

         Use a t-test to compare the two groups.

         This gives a p-value.

         Step 3:- Interpret the P - value

         If p-value < 0.05 → Reject the null → Groups are truly different.

         If p-value > 0.05 → Cannot reject null → Difference might be by chance.

         Final Conclusion:-

         Let’s say:

         p-value = 0.02

         That means:

         There’s only a 2% chance the difference is random.

         So, you can confidently say Credit Card users spend more.





>>>>>>> f570649 (Added Probability.md with all probability concepts)

