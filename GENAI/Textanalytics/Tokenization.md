
1. Tokenization : Tokenization is the process of breaking text into smaller pieces, called tokens.

   These tokens can be:

   Words (most common)

   Subwords

   Sentences

   Characters

   * Tokenization splits raw text into individual units like words, which can be used for further processing . 

   Example :- 

   Input - "I love eating pizza!"
 
   After Tokenization output - ['I', 'love', 'eating', 'pizza', '!']

2. why is Tokenization important ?

   | Purpose                      | How it helps                                  |
   | ---------------------------- | --------------------------------------------- |
   |  Preprocessing               | It’s the **first step** after cleaning text   |
   |  Converts to machine form    | Breaks natural language into structured parts |
   |  Foundation for NLP models   | Used in Bag of Words, TF-IDF, and even LLMs   |
   |  Pattern recognition         | Lets models learn meaning from word patterns  |

3. Types of Tokenization :

   | Type                    | What it Does                          | Example                                            |
   | ----------------------- | ------------------------------------- | -------------------------------------------------- |
   | **Word Tokenizer**      | Splits by words                       | `"I love pizza"` → `['I', 'love', 'pizza']`        |
   | **Character Tokenizer** | Splits each letter                    | `"Hi"` → `['H', 'i']`                              |
   | **Sentence Tokenizer**  | Splits by sentence                    | `"I ate. She slept."` → `['I ate.', 'She slept.']` |
   | **Subword Tokenizer**   | Splits into smaller meaningful chunks | `"unhappy"` → `['un', 'happy']` (used in LLMs)     |

   * where tokenization is used ?

     “Tokenization is used anywhere a machine needs to understand or generate text — from chatbots and search engines to LLMs 
     
      like ChatGPT — it’s the first and most essential step.”

      | Area                     | Why Tokenization is Used                    |
      |--------------------------|---------------------------------------------|
      | NLP & Text Mining        | Breaks text into analyzable pieces          |
      | Chatbots/Assistants      | Understands user queries                    |
      | Search Engines           | Matches queries with documents              |
      | Translation Apps         | Translates token-by-token                   |
      | LLMs (ChatGPT, GPT-4)    | Processes tokens, not raw text              |
      | Text Classification      | Input for models like Naive Bayes, SVM, etc |

4. What is Bag of words ? 

   Bag of Words (BoW) is a method to convert text into numbers by:

   1. Breaking the text into words (tokens).

   2. Ignoring grammar and word order.

   3. Counting how often each word appears.

   4. Representing that as a numeric vector.

   Simple Definition:

   "Bag of Words turns text into numbers by counting how many times each word appears."

    Real-Life Analogy:

    - Dish 1 = ["cheese", "tomato", "cheese"]

    - Dish 2 = ["cheese", "pasta"]

    We ignore order and just count:

    - cheese = 2 in dish 1, 1 in dish 2

    - tomato = 1

    - pasta = 1

    Example : 

    Text Documents:

    Doc1: "I love pizza"

    Doc2: "I love pasta"

    * Step 1: Tokenize Words:

      Doc1 → ['I', 'love', 'pizza']

      Doc2 → ['I', 'love', 'pasta']

    * Step 2: Build Vocabulary

      Vocabulary = ['I', 'love', 'pizza', 'pasta']

    * Step 3: Count Word Frequency

    | Word   | Doc1 | Doc2 |
    |--------|------|------|
    | I      |  1   |  1   |
    | love   |  1   |  1   |
    | pizza  |  1   |  0   |
    | pasta  |  0   |  1   |

* Why is it called “Bag of Words”?

  Because it treats text like a bag full of words — it doesn’t care about order or grammar, just the word counts . 

* Where is BoW Used?

| Use Case             | How BoW Helps                        |
|----------------------|--------------------------------------|
| Sentiment Analysis   | Counts words like “bad”, “love”      |
| Spam Detection       | Detects spam words like “win”, “free”|
| Topic Classification | Identifies topic-specific words      |
| Search Engines       | Matches keyword frequencies          |
| NLP Chatbots         | Converts input to model-friendly form|

5. Corpus : It is just a collection of text documents.

   Think of it like a library of text that you use to train, analyze, or feed into NLP models.

   Examples of Corpus :

   | Corpus Name                | What It Contains                     | Real-Life Usage                                    |
   | -------------------------- | ------------------------------------ | -------------------------------------------------- |
   |  **Twitter Corpus**        | Millions of tweets                   | Analyze public opinion, detect trends or fake news |
   | **IMDB Reviews**           | Movie reviews (positive/negative)    | Build sentiment analysis models                    |
   |  **Enron Email Corpus**    | Real company emails (spam & normal)  | Spam detection, email classification               |
   |  **Wikipedia Corpus**      | Articles from Wikipedia              | Train LLMs like ChatGPT, BERT                      |
   |  **News Article Corpus**   | News from BBC, CNN, etc.             | Topic classification (sports, politics, etc.)      |
   |  **Amazon Reviews**        | Product reviews from Amazon          | Product feedback analysis, recommendation systems  |
   |  **Legal Corpus**          | Case laws, contracts, legal opinions | Automate clause detection, legal document analysis |


   * Why is corpus important ? 

     | Reason                      | Explanation                                                          |
     | --------------------------- | -------------------------------------------------------------------- |
     | 📊 Provides Text Data       | Without text, we cannot analyze or train NLP models                  |
     | 🧠 Trains AI & LLMs         | ChatGPT, Google Translate, Siri — all are trained on large corpora   |
     | 🔍 Extracts Patterns        | Helps discover insights, frequent phrases, sentiment, topics         |
     | 📚 Builds Vocabulary        | Used to build word lists for BoW, TF-IDF, Word2Vec                   |
     | 🧪 Enables Testing/Research | Used in academia and industry to test NLP algorithms                 |
     | 🧩 Helps Generalization     | Bigger and diverse corpus = better machine understanding of language |
     
   * What does a corpus do in real-life ?

     A corpus is the foundation for many modern AI and text applications:

     | Real-Life Scenario                       | How Corpus Helps                                                        |
     | ---------------------------------------- | ----------------------------------------------------------------------- |
     | ✅ Chatbots (e.g., Zomato Assistant)      | Learns to reply from past chat corpus                                   |
     | ✅ Translate Languages (Google Translate) | Uses bilingual corpus to learn how phrases translate                    |
     | ✅ Sentiment Detection in Reviews         | Learns from review corpus which words are positive or negative          |
     | ✅ News Categorization                    | Uses article corpus to label topics like Sports, Politics               |
     | ✅ Spam Email Filtering                   | Uses email corpus to recognize spam vs normal emails                    |
     | ✅ Resume Matching in HR Systems          | Uses job/resume corpus to match skills to job descriptions              |
     | ✅ Training Large Language Models (LLMs)  | LLMs like ChatGPT are trained on large corpora of books, code, articles |
