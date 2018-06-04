
import nltk # Interesting, if you run this with python instead of python3, it can't find nltk.
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize


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



text.concordance('strange')

# text.collocations()
