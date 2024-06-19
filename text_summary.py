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
The Great Barrier Reef is the world's largest coral reef system composed of over 2,900 individual reefs and 900 islands stretching for over 2,300 kilometres (1,400 mi) over an area of approximately 344,400 square kilometres (133,000 sq mi). The reef is located in the Coral Sea, off the coast of Queensland, Australia. The Great Barrier Reef can be seen from outer space and is the world's biggest single structure made by living organisms. This reef structure is composed of and built by billions of tiny organisms, known as coral polyps. It supports a wide diversity of life and was selected as a World Heritage Site in 1981. CNN labelled it one of the seven natural wonders of the world.  Unfortunately, the Great Barrier Reef is facing numerous environmental threats such as pollution and climate change.
"""

summary = summarize(text)
print(summary)
