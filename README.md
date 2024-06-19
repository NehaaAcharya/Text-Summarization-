# Text-Summarization-
I am excited to begin my learning and coding journey in the field of Machine Learning and NLP.As a beginner exploring the field of Machine Learning and NLP, this is my first project to train a model to take a lengthy piece of text and automatically generate a shorter summary that captures the main points.

The provided code utilizes a combination of NLP and Machine Learning concepts:

**NLP Concepts:**

Text Preprocessing: This is a fundamental NLP step that involves cleaning the text by removing stopwords (common words like "the", "a", "is") and converting it to lowercase. This prepares the text for further analysis.
Sentence Tokenization: The code splits the text into individual sentences using nltk.tokenize.sent_tokenize. This allows us to analyze each sentence independently.

**Machine Learning Concepts:**

TextRank Algorithm: This algorithm, while not a deep learning technique, utilizes a graph-based approach inspired by PageRank (used by search engines). TextRank builds a graph where words are nodes and co-occurrence within a window size defines edges. By analyzing the connections between words, TextRank assigns a score to each sentence reflecting its importance within the document's network of word relationships. 



