
import nltk # Interesting, if you run this with python instead of python3, it can't find nltk.
import pandas as pd
from nltk import FreqDist

# nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize
#
# EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
#
# print(sent_tokenize(EXAMPLE_TEXT))
#
# # Stop words are filler words we want to weed out.
# from nltk.corpus import stopwords
#
# example_sent = "This is a sample sentence, showing off the stop words filtration."
#
# stop_words = set(stopwords.words('english'))
#
# word_tokens = word_tokenize(example_sent)
#
# # 2 ways of writing the same thing:
# filtered_sentence = [w for w in word_tokens if not w in stop_words]
#
# print(filtered_sentence)






# THANK YOU https://www.nltk.org/book/ch01.html

# ================= FROM CHAPTER 1 ===================

# IN THE SHELL:
# import nltk
# from nltk.book import *
# text1.concordance("madness") (shows occurences)
# text1.similar("madness") (shows words used in same context)
# >>> text2.common_contexts(["monstrous", "very"])
#
# >>> text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
# >>> text3.generate() (actually this is deprecated)
#
# set(text3) (will generate a set of unique words, or whatever, collapsing repeats)
# sorted(set(text3))
# len(set(text3)) (number of unique types, or groups of symbols)
# Lexical richness: len(set(text3)) / len(text3)
#
# text3.count('smote')
#
# fdist = FreqDist(text1)
# fdist.most_common(50)
# fdist['whale']
#
# fdist.hapaxes() (words that appear only once)
#
# V = set(text1)
# long_words = [w for w in V if len(w) > 15] (a "list comprehension", right?)
# sorted(long_words)
#
# (add condition that fdist5[w] > 7)
#
# text5.collocations() (gives us especially frequent bigrams, one's that are more frequent than individual frequencies would suggest)
#
#
# fdist = FreqDist(len(w) for w in text1) (gives freq distribution by word-length)
#
# fdist.max()
# fdist.tabulate()
# fdist.plot()
# fdist.plot(cumulative=True)
#
# w.startswith(t)
# w.endswith(t)
# w.istitle()
#
# len(set(word.lower() for word in text1 if word.isaplha()))







# ================= FROM CHAPTER 2 ===================
# Conditional Frequency Distributions...
#
# WordNet synsets
# - Check how general a word is by checking the depth of its synset
# - entailments, antonyms, ambiguous senses, holonyms and meronyms....







# ================= FROM CHAPTER 3 ===================

# import re
# >>> wsj = sorted(set(nltk.corpus.treebank.words()))
# >>> [w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]
# >>> [w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]
#
#
# >>> re.findall(r'[aeiou]', word)
#
#
# # Don't fully understand this...
#
# >>> wsj = sorted(set(nltk.corpus.treebank.words()))
# >>> fd = nltk.FreqDist(vs for word in wsj
# ...                       for vs in re.findall(r'[aeiou]{2,}', word))


# This page, https://www.nltk.org/book/ch03.html, is generally gold.


# Wow, wordnet has a ton of built-in info about types and instances...., synonyms and senses....
# and there is also Stemming....
# All of this is so great, one only needs a touch of imagination to build some interesting and useful queries.







# ================= FROM CHAPTER 4 ===================

# - "It is crucial to appreciate this difference between modifying an object via an object reference, and overwriting an object reference."
#
# - bar = foo[:]. This copies the object references inside the list. To copy a structure without copying any object references, use copy.deepcopy().
#
# - zip function
# - sequences (i.e. tuples), comma separated -- unlike lists, they are immutable
# - Generator expressions (more efficient for large lists, because they stream the data to find e.g. max value)
#
# - Procedural is closer to machine-level code -- declarative uses more high-level concepts
#
#
# >>> maxlen = max(len(word) for word in text)
# >>> [word for word in text if len(word) == maxlen]
#
# - Mutability example:
#
# >>> p = []
# >>> properties = p
# >>> properties.append('noun')
# >>> properties = 5
# >>> p
# ['noun']
#
# - add assertions to your code as a kind of defensive programming, or validation
#
# - divide your code into 10-line functions, each with a clear purpose, expressing one main idea
#
# - lambda functions are shortcuts for passing anonymous functions as arguments
#
# - yield is a way of making accumulative functions more efficient
#
# - NetworkX package for visualizing data-graphs !!!








#
