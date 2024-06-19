import networkx as nx
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def preprocess_text(text):
  """
  This function cleans and prepares the text for summarization.
  """
  sentences = sent_tokenize(text.lower()) # Split text into sentences
  stop_words = stopwords.words('english') # Load stopwords
  words = [word for sentence in sentences for word in sentence.split() if word not in stop_words] # Remove stopwords
  return words

def textrank(words, window=5):
  """
  This function implements the TextRank algorithm using networkx.
  """
  graph = nx.Graph()
  for i, word in enumerate(words):
    for j in range(i+1, min(i+window+1, len(words))):
      graph.add_edge(word, words[j])
  scores = nx.pagerank(graph)
  return scores

def summarize(text, num_sentences=5):
  """
  This function summarizes the text by selecting the top scoring sentences.
  """
  words = preprocess_text(text)
  sentence_scores = textrank(words)
  ranked_sentences = sorted(zip(sentence_scores.values(), sent_tokenize(text)), reverse=True)
  summary = ' '.join(sentence[1] for sentence in ranked_sentences[:num_sentences])
  return summary

# Example Usage
text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents" which are systems that can reason, learn, and act autonomously.

AI research has been highly successful in developing effective techniques for solving a wide range of problems, from game playing to medical diagnosis.

Some of the most successful AI applications are in the field of machine learning. Machine learning algorithms are trained on a large amount of data and are able to learn and improve their performance on a specific task. For example, machine learning algorithms are used to recommend products to customers on online shopping websites.
"""

summary = summarize(text)
print(summary)
