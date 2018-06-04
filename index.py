
import nltk # Interesting, if you run this with python instead of python3, it can't find nltk.
import pandas as pd


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

# NEW NOTES:
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
# set(text3)
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









# Bringing in a Shakespeare play to play with:
csv = 'Macbeth'
filename = 'csvs/' + csv + '.csv'
df = pd.read_csv(filename, index_col=0)
# print(df.head())

raw_text = ''
for line in df['Lines']:
    raw_text += line + '\n'

# print(raw_text)


tokens = word_tokenize(raw_text)
text = nltk.Text(tokens)



# text.concordance('mad')

# text.collocations()











#
