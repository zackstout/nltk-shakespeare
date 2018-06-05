
import nltk # Interesting, if you run this with python instead of python3, it can't find nltk.
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
from csvs import allCsvs

# Bringing in a Shakespeare play to play with:
# csv = 'Macbeth'
# filename = 'csvs/' + csv + '.csv'
# df = pd.read_csv(filename, index_col=0)
# print(df.head())

# raw_text = ''
# for line in df['Lines']:
#     raw_text += line + '\n'

# print(raw_text)


# tokens = word_tokenize(raw_text)
# text = nltk.Text(tokens)



# text.concordance('strange')

# text.collocations()

# text.similar('strange')

# text.dispersion_plot(['strange', 'hate', 'blood'])
#
# richness = len(set(text)) / len(text)
# print(richness)
#
# print(text.count('strange'))
#
# fdist = FreqDist(text)
# print(fdist.most_common(50))
# print(fdist['strange'])
#
# print(fdist.hapaxes())




# Question: are `sorted` and `set` python things, or nltk things?

# Find words that are unique across all the plays:
def getUniqueWords():
    raw_text_all = ''

    for csv in allCsvs:
        filename = 'csvs/' + csv + '.csv'
        df = pd.read_csv(filename, index_col=0)
        for line in df['Lines']:
            raw_text_all += line + '\n'

    tokens = word_tokenize(raw_text_all)
    text = nltk.Text(tokens)
    # text.collocations()

    fdist = FreqDist(text)
    unique = fdist.hapaxes()
    sort_unique = sorted(unique)
    print(sort_unique)

# getUniqueWords()




# chillin
