
1. Feature Engineering :- 

   Feature Engineering means creating, modifying, or selecting the right data (features) that helps machine learning models 
   
   perform better.

   *  Why is Feature Engineering important?

     . Raw data is not always ready for modeling.

     . Bad features → bad results (like putting wrong ingredients in food).

     . Good features → better accuracy, less overfitting.

     Example :-

     You have restaurant sales data:

     Date, Category, Item, Price, Discount, Payment Type, Customer Visit Time

     From this, you can engineer new features like:

     Final Price = Price - Discount. 

     * Steps involved in Feature Engineering :

       | **Step**                   | **What It Means**                      | **Example (Restaurant)**                    |
       | -------------------------- | -------------------------------------- | ------------------------------------------- |
       | 1. Feature Creation        | Create new features from existing data | "Total Bill" = Food Cost + Tax              |
       | 2. Feature Extraction      | Extract useful parts from a column     | From "Date" → extract "Day", "Month"        |
       | 3. Transformation          | Change format or scale of data         | Convert "Cash/Card" to 0/1 (Encoding)       |
       | 4. Feature Selection       | Keep only the most important features  | Drop "Order ID", keep "Dish Type", "Amount" |
       | 5. Feature Scaling         | Normalize data values to same scale    | Scale "Price" between 0 and 1               |
       | 6. Handle Missing Data     | Fill or remove missing values          | Fill missing "Amount" with average value    |
   
      1. Feature Creation :-

         . What it means:

           Creating new columns (features) by combining or calculating values from existing ones.

         . Why it's useful:

           It adds meaningful insights that help the model learn better.

           . Example (Restaurant):

            You have Food Cost and Tax.

            Create a new column:

            → Total Bill = Food Cost + Tax

      2. Feature Extraction :

         Deriving new features from raw data.

         * Purpose: Extract useful signals or patterns from raw, unstructured, or semi-structured data.

         Examples : 

         * From a `date`, extract `year`, `month`, `weekday`.

         * From a `text`, extract number of words, sentiment score, or use TF-IDF.

         * From a `location`, extract distance from a known point.

      3. Feature Transformation :

         Modifying features to improve their scale, distribution, or format.

      . Purpose   : Make features more usable for models and improve performance.

      . Common Techniques:

      | Task                  | Purpose                                               |
      | --------------------- | ----------------------------------------------------- |
      | Imputation            | Fill missing values to avoid data loss                |
      | Outlier Handling      | Avoid skewing model with extreme values               |
      | Binning               | Convert numerical values into categorical bins        |
      | Log Transform         | Normalize skewed data                                 |
      | One-Hot Encoding      | Convert categorical to numerical                      |
      | Feature Splitting     | Extract parts from compound values                    |
      | Scaling               | Normalize feature values (standardization or min-max) |


2. What is Feature Selection :- 

   Feature Selection is the process of choosing a subset of relevant features (input variables) from the dataset. 

   1. Why is feature selection important ?

      |  Benefit              |  Description                                             |
      | --------------------- | ------------------------------------------------------   |
      | Improves Accuracy     | Removes irrelevant or noisy data                         |
      | Reduces Overfitting   | Fewer inputs = lower chance of learning wrong patterns   |
      | Speeds Up Training    | Smaller dataset = faster training and testing            |
      | Simplifies Models     | Easy to interpret and maintain                           |


      Example :-

      I already have these:

      Date , Category , Item , Price , Discount , Payment Type , Customer Visit Time , Final Price.
      
      After Feature Selection :- 
      
      | Feature        | Reason                                     |
      | -------------- | ------------------------------------------ |
      | `Final Price`  | Directly represents money spent            |
      | `Category`     | Helps group items (e.g., Food vs Drink)    |
      | `Payment Type` | May influence customer behavior or pattern |
      | `Date`         | For time-series trends (optional)          |


3. Feature Selection methods :- 

   1. Filter Methods (Statistical) :- Use statistical tests to rank features. 

      1. Correlation      - for numerical features

      2. Chi-squared test - for categorical features

   2.  Wrapper Methods (Model-Based) :-

       Try different combinations using a model.

       Slower but more accurate.

       Examples:

       Recursive Feature Elimination (RFE).
  
       Forward/Backward Selection.

   3. Embedded Methods (Built into Models):-

      Feature selection during training

      Examples:

      Lasso (L1 Regularization).

      Random Forest / XGBoost importance.

