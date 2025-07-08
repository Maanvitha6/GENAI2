
1. Datascience :- 

   Data Science is an interdisciplinary field that involves collecting, cleaning, analyzing, and interpreting data to extract
   
   useful insights and help in making smart business decisions .

      1. What is meant by Interdisciplinary :-

         Interdisciplinary means combining knowledge or skills from two or more different fields (subjects) to solve a problem or 
      
         understand something better . ( Simply using multiple fields.)

         Example - There is a restuarant , It becomes interdisciplinary when it uses technology, data, business skills together to
      
         make smarter business decisions. 

    * Datascience is interdisciplinary because it has two major parts of data :- 

            1. Web data - data from websites, apps . It is Unstructured. It has no format. It is  like a free form .

            Example - Text , images , audio , vedios etc..

            2. Relational database - organised data stored in table format rows and columns. It is sturctured. 

            Example - Restuarant sales table (orderid, customer, fooditem, quantity, price). 

2.  Journey of datascience :-

      1. **Problem Understanding**

      → Identify the business problem or question to solve.

      2. **Data Collection**

      → Gather data from sources like databases, APIs, files, or web.

      3. **Data Cleaning**

      → Fix missing values, remove duplicates, and standardize formats.

      4. **Exploratory Data Analysis (EDA)**

      → Explore data using statistics and visualizations to find patterns.

      5. **Feature Engineering**

      → Create new, meaningful variables to improve model performance.

      6. **Model Building**

      → Train machine learning or statistical models on the data.

      7. **Model Evaluation**

      → Test model accuracy using performance metrics.

      8. **Deployment**

      → Integrate the model into a system or app for real-world use.

      9. **Visualization & Communication**

      → Share insights with stakeholders using reports or dashboards.

      10. **Feedback & Improvement**

      → Monitor, refine, and retrain models with new data as needed.

    * Tools of Datascience :-

     | Purpose              | Tools/Languages                        |
     | -------------------- | -------------------------------------- |
     | **Programming**      | Python, R                              |
     | **Data Handling**    | SQL, Pandas, NumPy                     |
     | **Visualization**    | Matplotlib, Seaborn, Tableau, Power BI |
     | **Machine Learning** | Scikit-learn, TensorFlow, XGBoost      |
     | **Big Data**         | Hadoop, Spark                          |
     | **Deployment**       | Flask, Docker, Streamlit               |

3. Data Analysis Pipeline :- 

   The data analysis pipeline is a step-by-step process that transforms raw data into valuable insights for decision-making.

   | Step | Name                     | Description                                                         |
   | ---- | ------------------------ | ------------------------------------------------------------------- |
   | 1️⃣  | Data Collection          | Gather data from various sources like websites, databases, sensors. |
   | 2️⃣  | Data Extraction          | Pull only the relevant data you need for analysis.                  |
   | 3️⃣  | Data Wrangling           | Clean and prepare the data (fix errors, format properly).           |
   | 4️⃣  | Data Analysis (EDA)      | Understand patterns, trends, and relationships.                     |
   | 5️⃣  | Data Visualization       | Show findings through graphs and dashboards.                        |
   | 6️⃣  | Modeling (if needed)     | Use Machine Learning to predict or classify things.                 |
   | 7️⃣  | Insights & Decision      | Make final conclusions or business decisions.                       |

4. Data Extraction :- 

   The process of collecting data from different sources. (websites, databases)

   Data extraction techniques like - Scraping(beautifulsoup , selenium, API)

   * How can we extract data ?
     
     . We can extract data from different sources . 

     | **Source**         | **Tools**                  | **Use Case**                |
     | ------------------ | -------------------------- | --------------------------- |
     | Files (CSV, Excel) | pandas, Excel, Power Query | Local storage               |
     | SQL Databases      | SQLAlchemy, psycopg2, JDBC | Enterprise or app databases |
     | APIs               | requests, Postman          | Web services, real-time     |
     | Web Scraping       | BeautifulSoup, Selenium    | No API access               |
     | Cloud Platforms    | AWS/GCP SDKs, BI tools     | Big data, remote sources    |
     | Logs/Sensors       | Kafka, Spark, Python       | IoT or log monitoring       |


5. Data Wrangling :-

   Data Wrangling is the process of cleaning, correcting, and converting raw data into a usable format for analysis.

   1. Data Collection:

   * Import data from sources: CSV, databases, APIs, etc.

   2. Data Cleaning:

   * Handle missing values

   * Fix inconsistent formatting (e.g., date formats)

   * Remove duplicates or irrelevant entries.

   3. Data Transformation:

   * Convert data types (e.g., strings to dates)

   * Normalize or scale numerical values.

   * Extract or create new features (columns).

   4. Data Integration:

   * Merge data from multiple sources or tables.

   5. Data Validation:

   * Check for outliers, logic errors, or incorrect values.

   6. Data Structuring:

   * Reshape data into tidy format (e.g., pivot tables).

   * Ensure the structure matches modeling or analysis needs.

   . Data Cleaning vs Data Wrangling :-

     Think of It Like This:

     . Data Cleaning = Making sure the data is correct and consistent.

     . Data Wrangling = Making the data correct + usable + well-structured.

      Example Scenario:-

      You receive a messy dataset. Here’s how each process would help:

     🔹 Problems in the Dataset:

        Some rows have missing “Amount”.

        “Date” column is stored as text.

         Two tables: orders and products need to be combined.

     🔹 Data Cleaning Would:

        Fill or remove missing "Amount".

        Convert "Date" to proper date format.

        Remove duplicate rows.

     🔹 Data Wrangling Would:

        Do all of the cleaning tasks.

        Merge orders and products tables.

        Create new column: "Amount after Discount".

        Normalize product names (e.g., "Veg pizza", "veg Pizza" → "Veg Pizza").

        Reshape table to group by product category.

6. Types of Data :-

   | **Type**        | **What It Is**                 | **Examples**                         | **Tools**     |
   | --------------- | ------------------------------ | ------------------------------------ | ------------- |
   | Structured      | Table format (rows & columns)  | Sales data, employee list            | SQL, Excel    |
   | Unstructured    | No fixed format                | Emails, images, videos, social posts | NLP, CV tools |
   | Semi-Structured | Partial structure (tags, keys) | JSON, XML, API output, sensor logs   | NoSQL, Python |


  * Raw Data vs Processed Data :-

  | **Feature**        | **Raw Data**                                     | **Processed Data**                              |
  | ------------------ | ------------------------------------------------ | ----------------------------------------------- |
  | **Definition**     | Data directly from source, unmodified            | Cleaned, formatted, and ready for analysis      |
  | **Structure**      | Often messy and unorganized                      | Well-structured and consistent                  |
  | **Examples**       | Log files, sensor readings, raw survey responses | Cleaned CSVs, summary tables, formatted reports |
  | **Use Case**       | Initial capture or backup                        | Analysis, visualization, ML models              |
  | **Tools Required** | Needs parsing, scripts                           | Ready for Excel, SQL, or ML tools               |
  | **Quality**        | May include errors, duplicates, noise            | High-quality, cleaned, and validated            |

  * Labeled vs Unlabeled Data :-
 
  | **Type**  | **Meaning**                | **Example**                      |
  | --------- | -------------------------- | -------------------------------- |
  | Labeled   | Has input + correct output | Text: "Great!" → Label: Positive |
  | Unlabeled | Has input only, no label   | Text: "Great!" → No label        |

      

