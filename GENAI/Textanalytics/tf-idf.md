
1. Unigram : A unigram is just one single word.

   Example:

   Sentence: "I love pizza"

   Unigrams = ['I', 'love', 'pizza']

   Each word is a unigram.

2. Bigram : A bigram is a pair of two consecutive words in a sentence.

   Example:

   Sentence: "I love pizza"

   Bigrams = ['I love', 'love pizza']

   We move 2 words at a time → that’s a bigram.

3. Trigram : A trigram is a group of three consecutive words.

   Example:

   Sentence: "I love spicy pizza"

   Trigrams = ['I love spicy', 'love spicy pizza']

4. N-gram : N-gram is a general term.

   If n = 1, it’s a unigram.

   If n = 2, it’s a bigram.

   If n = 3, it’s a trigram.

   So, n-gram means "n words grouped together" in order.

   * Real-life Examples of these :

   * Example 1: Chatbot / Voice Assistant

   You say: "Book a table for two".

   Bigram = ['Book a', 'a table', 'table for', 'for two'].

   The system can understand the action using these phrases.

   Chatbots learn phrases, not just words.

   * Example 2: Sentiment Analysis

   Review: "Not good".

   Unigram = ['Not', 'good'] → Doesn't capture meaning.

   Bigram = ['Not good'] → Detects negative phrase.

   Bigrams help detect real meaning.

   * Example 3: Search Engines (Google).

   You type: "Best pizza in".

   Google predicts: "Best pizza in New York".

   Google uses trigrams or 4-grams to predict next words.

   This helps in auto-complete.

   * Example 4: Spam Detection

   Spam emails often say: "Win money now".

   The system checks for bigrams like "win money", "money now".

   N-grams help in detecting repeated spam phrases.

5. Why Are Unigram, Bigram, Trigram Important?

   | Type    | Importance                                              |
   | ------- | ------------------------------------------------------- |
   | Unigram | Simple word-level analysis, like word frequency         |
   | Bigram  | Understands **short phrases** and **word combinations** |
   | Trigram | Understands **longer context**, like full expressions   |
   | N-gram  | You can choose `n` based on how much context you want   |

6. Term Frequency : Term Frequency (TF) tells us how often a word appears in a single document.

   It shows how important a word is within that document.

   Formula:

   TF(t)=  Number of times the word t appears in the document / Total number of words in the document
​
   Example:

   Document: "I love spicy pizza and I love coke"

   Word = "love"

   Appears = 2 times

   Total words = 8
   
   TF(t) = 8/2=4 . 

7. Inverse Document Frequency : IDF tells us how rare or unique a word is across all documents.

   Words that are common in many documents get low scores.

   Words that are rare (appear in fewer documents) get high scores.

   Formula:

   IDF(t)=log( Number of documents with word t / Total number of documents).

   If a word appears in every document → IDF = low

   If a word appears in few documents → IDF = high