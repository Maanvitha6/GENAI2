#                                Business Requirement Document (BRD)

# Project Title
  
  RESTUARANT SALES DATA CLEANING AND ANALYSIS

  # 1. Problem Statement (Executive Summary) :-

    The restaurant has accumulated large volumes of sales data, but it's unorganized and contains missing values,inconsistencies,

    and duplicates. This makes it difficult to extract actionable insights such as identifying top products, peak months, and 
    
    preferred payment methods. Cleaning and analyzing the dataset is essential for understanding customer behavior and improving

    Strategic planning.

  # 2. Goal :-

    To clean, process, and analyze the restaurant sales data to generate insights on top-selling items, category performance, and
    
    monthly revenue trends. The ultimate goal is to support better business decisions using data.

  # 3. Data Source :-

    File Name: restaurant_sales_data.csv ()

    Source: Downloaded from Kaggle

    Size: 17,500 rows (approx.)

    Format: CSV

    Upload Destination: MySQL Database (restaurant_db)

 # 4. Understanding the Data :-

   | Column Name    | Data Type | Description                     |

   | -------------- | --------- | ------------------------------- |

   | Order ID       | object    | Unique identifier for the order |

   | Customer ID    | object    | Unique ID for the customer      |

   | Order Date     | object    | Date the order was placed       |

   | Category       | object    | Food category (e.g., Beverages) |

   | Item           | object    | Item name                       |

   | Quantity       | int       | Quantity ordered                |

   | Unit Price     | float     | Price per item                  |

   | Order Total    | float     | Total cost for the order        |

   | Payment Method | object    | Mode of payment                 |

   | Location       | object    | Store location                  |

 # 5. Data Cleaning Steps :-

   | Step | Description                                                                                                        |

   | ---- | ------------------------------------------------------------------------------------------------------------------ |

   | 1️.   | Dropped duplicate rows.                                                                                            |

   | 2️.   | Removed rows with missing values in key fields: `Order Date`, `Category`, `Item`, `Order Total`, `Payment Method`. |

   | 3️.   | Dropped unnecessary columns: `Customer ID`, `Order ID`.                                                            |

   | 4️.   | Filled missing numeric values in `Quantity`, `Unit Price` with **mean**.                                           |

   | 5️.   | Filled missing `Location` using **mode**.                                                                          |

   | 6️.   | Standardized text fields like `Category` and `Payment Method`.                                                     |

   | 7️.   | Converted `Order Date` to datetime format and extracted `Month` column.                                            |

   | 8️.   | Final cleaned data saved to **CSV** and **MySQL database** (`restaurant_sales_cleaned`).                           |

 # 6. Functional Requirements :-

   | Requirement ID | Requirement Description                              |

   | -------------- | ---------------------------------------------------- |

   | FR1            | Load raw data into MySQL from CSV.                   |

   | FR2            | Drop duplicates and handle nulls strategically.      |

   | FR3            | Visualize top categories, items, and monthly trends. |

   | FR4            | Save cleaned data locally and in the database.       |

 # 7. Data Analysis Performed :-

   | Analysis Task             | Description                                               |

   | ------------------------- | --------------------------------------------------------- |

   |  Top-Selling Categories | Summed `Order Total` grouped by `Category`.               |

   |  Top 10 Selling Items   | Summed `Quantity` grouped by `Item` (excluding unknowns). |

   |  Monthly Sales Trend    | Summed monthly revenue from `Order Date` → `Month`.       |

   |  Statistical Summary    | Mean, Median, Mode, Std. Dev for numeric columns.         |

 # 8. Visuazilations :-

   Bar Chart               –     Total Sales by Category

   Horizontal Bar Chart    –     Top 10 Selling Items

   Monthly Trend Chart     –     Revenue per Month


Total sales by category :-

<img src = "https://github.com/Maanvitha6/GENAI/blob/main/Assets/figure%201(total%20sales%20by%20category).png">

Top 10 Selling Items :-

<img src = "https://github.com/Maanvitha6/GENAI/blob/main/Assets/figure%202(Top%2010%20selling%20items).png">

Revenue Per Month :-

<img src = "https://github.com/Maanvitha6/GENAI/blob/main/Assets/figure%203(Monthly%20sales%20trend).png">



