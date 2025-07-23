

1. Text Analytics : Text analytics is the process of analyzing text data to discover useful patterns, trends, or insights.

   It's used to:

   . Find out what people are talking about.

   . Detect emotions/sentiment in text.

   . Summarize large documents.

   . Classify topics or detect spam.

  *  What kind of data does it handle?

     Text Analytics deals with text data, which is usually unstructured (not in rows & columns) . 

  *  To do Text Analytics, what do we need?

     We need 3 major things:

     | Component            | Description                                                                 |
     | -------------------- | --------------------------------------------------------------------------- |
     | **Text Data**        | Unstructured data (e.g., reviews, emails, messages)                         |
     | **Tools/Techniques** | Methods to process and analyze the text (like TF-IDF, sentiment analysis)   |
     | **Goals**            | What we want to find (e.g., detect positive reviews, classify topics, etc.) |

  * Steps to perform Text Analytics :

    Collect Text Data
    
    → From websites, reviews, chat logs, etc.

    Clean & Preprocess the Text.

    → Remove noise (punctuation, stopwords), tokenize, lowercase, etc.

    Convert Text to Numbers.

    → Use Bag of Words, TF-IDF, or word embeddings

    Analyze

    → Apply machine learning or statistical techniques

    Visualize/Report

    → Show results using graphs, dashboards, or alerts


2. Text Data : Text data is unstructured data made up of words, sentences, and paragraphs — it comes in human language (English,

   Hindi, etc.), not structured rows and columns like Excel.

   Examples of Text Data and their Sources :

   | Source Type        | Platform/Example       | Sample Text                              |
   |--------------------|------------------------|-------------------------------------------|
   | Social Media       | Twitter, Instagram     | "Loving the weather today! ☀️"           |
   | Product Reviews    | Amazon, Flipkart       | "Battery dies fast. Not worth the price." |
   | Emails             | Gmail, Outlook         | "Please send me the invoice."             |
   | Chat Messages      | WhatsApp, Messenger    | "Can I reschedule my appointment?"        |
   | News Articles      | CNN, BBC               | "Stocks drop due to market uncertainty."  |
   | Support Tickets    | Zendesk, Jira          | "Unable to reset my password."            |

   * How data is extracted ?

    | Source       | Extraction Method | Tool/Library                 |
    | ------------ | ----------------- | ---------------------------- |
    | Website      | Web Scraping      | BeautifulSoup, Selenium      |
    | PDFs/Docs    | File Reading      | PyPDF2, docx                 |
    | Social Media | APIs              | Tweepy, Reddit API           |
    | Databases    | SQL Queries       | pymysql, psycopg2            |
    | Emails       | IMAP              | imaplib, email               |
    | Audio Files  | Speech to Text    | speech\_recognition, Whisper |

3. Text Mining :

   Text Mining is the process of extracting useful and structured information from unstructured text data.

   | Industry     | Use Case               | What It Does                        |
   |--------------|------------------------|-------------------------------------|
   | E-commerce   | Product reviews        | Finds complaints & top features     |
   | Healthcare   | Doctor notes           | Extracts symptoms, diagnoses        |
   | Travel       | Feedback analysis      | Detects issues like delays          |
   | Call Center  | Chat transcripts       | Classifies complaints, sentiment    |
   | HR           | Resume screening       | Extracts skills, job matching       |

Summary :-

| **Text Mining**                              | **Text Analytics**                            |
| -------------------------------------------- | --------------------------------------------- |
| Focuses on **processing** and **extraction** | Focuses on **interpretation** and **insight** |
| Converts unstructured text → structured      | Uses structured data to **analyze trends**    |
| Foundation step in Text Analytics            | Next step after Text Mining                   |

