
1. Stemming : Stemming is the process of reducing a word to its root or base form (stem) by removing suffixes or prefixes . 

   Example:

   Words: "running," "runner," "ran"

   Stem: "run"

   How It Works:

   Stemming algorithms (e.g., Porter Stemmer, Snowball Stemmer) apply rules to strip affixes. For instance, "playing" → "play," 
   
   "studies" → "studi."

   * Importance:

     . Simplifies Text: Stemming reduces variations of words to a common form, making it easier to analyze text by grouping 
     
       related terms.

     . Improves Search: In information retrieval (e.g., search engines), stemming ensures that queries like "run" match "running" 
       
       or "runner."

     . Reduces Vocabulary Size: Helps in reducing the dimensionality of text data for machine learning models, saving 
     
       computational resources.

   * Real-Life Application:

     . Search Engines: Google uses stemming to match user queries with relevant documents. If you search "cooking recipes," it 
       
       matches documents with "cook," "cooked," or "cooks."

     . Sentiment Analysis: In analyzing customer reviews, stemming groups "loved," "loving," and "loves" as "love," simplifying
      
       the process of counting positive sentiment words .

2. Lemmatization : Lemmatization reduces a word to its base or dictionary form (lemma) by considering its part of speech (POS) 
   
   and context.

   Example:

   Words: "running," "ran"

   Lemma (verb): "run"

   Words: "better," "best"

   Lemma (adjective): "good"

   * How It Works:

    . Lemmatization uses linguistic rules and dictionaries (e.g., WordNet) to map words to their canonical form, often requiring
    
      POS tagging (e.g., is "running" a verb or noun?).

    . Tools: NLTK, spaCy, Stanford NLP.

   * Importance:

    . Preserves Meaning: Unlike stemming, lemmatization ensures the base form is a valid word, maintaining semantic accuracy.

    . Context-Aware: By considering POS, it distinguishes between different uses of a word (e.g., "saw" as a verb → "see," as a 
      
      noun → "saw").

    . Improves Model Performance: In NLP tasks like sentiment analysis, lemmatization provides cleaner, more meaningful features
    
      for machine learning models.

    * Real-Life Application:

     . Chatbots: In customer service chatbots, lemmatization ensures that "I’m running late" and "I ran into an issue" are 
       
       correctly interpreted by mapping "running" and "ran" to "run."

     . Sentiment Analysis: For a product review like "The service was better than expected," lemmatizing "better" to "good" 
       
       ensures the model recognizes the positive sentiment accurately.

3. Differences between Stemming and Lemmatization :

   | Feature               | **Stemming**                                  | **Lemmatization**                                 |
   | --------------------- | --------------------------------------------- | ------------------------------------------------- |
   | **Definition**        | Removes suffixes to reduce word to root form  | Converts word to its base/dictionary form (lemma) |
   | **Method**            | Rule-based chopping                           | Dictionary + context-based analysis               |
   | **Output Example**    | "running" → "run" or "runn"                   | "running" → "run"                                 |
   | **Accuracy**          | Less accurate, may produce invalid words      | More accurate, produces valid words               |
   | **Speed**             | Faster                                        | Slower                                            |
   | **Complexity**        | Simple                                        | Complex                                           |
   | **Tool Example**      | `PorterStemmer`, `LancasterStemmer` (NLTK)    | `WordNetLemmatizer` (NLTK)                        |
   | **Grammar Awareness** | Not aware of grammar or context               | Considers POS (Part of Speech) and context        |
   | **Use Case**          | When speed is important and small errors okay | When accuracy is more important                   |


