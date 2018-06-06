
import nltk # Interesting, if you run this with python instead of python3, it can't find nltk.
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
from csvs import allCsvs
from nltk.corpus import wordnet as wn

# Bringing in a Shakespeare play to play with:
def onePlay(play):
    filename = 'csvs/' + play + '.csv'
    df = pd.read_csv(filename, index_col=0)
    # print(df.head())

    raw_text = ''
    for line in df['Lines']:
        raw_text += line + '\n'

    # print(raw_text)


    tokens = word_tokenize(raw_text)
    text = nltk.Text(tokens)
    # text.concordance('strange')
    text.similar('strange')
    # text.collocations()
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



# onePlay('Macbeth')



def playWithWordNet(word):
    syn = wn.synsets(word)
    print(syn)

    syns = wn.synset('strange.a.01').lemma_names()
    syns2 = wn.synset('strange.s.02').lemma_names()
    defn = wn.synset('strange.s.02').definition()
    ex = wn.synset('strange.s.02').examples()
    lems = wn.synset('strange.s.02').lemmas()
    # name = wn.lemma('strange.s.02').name()
    print(syns, defn, ex)

    for synset in syn:
        print(synset.lemma_names())

    stranges = wn.lemmas('strange')
    print(stranges)

    synset1 = wn.synset('strange.s.02')
    types_of_strange = synset1.hyponyms()
    supersets_of_strange = synset1.hypernyms()
    root_hypernyms = synset1.root_hypernyms()
    paths = synset1.hypernym_paths()
    path1 = [synset.name() for synset in paths[0]]
    print(types_of_strange, supersets_of_strange, root_hypernyms, paths, path1)

    tree = wn.synset('human.n.01')
    parts = tree.part_meronyms()
    subst_parts = tree.substance_meronyms()
    wholes = tree.member_holonyms()
    print(tree, parts, subst_parts, wholes)

    entails = wn.synset('walk.v.01').entailments()

    antys = wn.lemma('rush.v.01.rush').antonyms()

    specificity = wn.synset('baleen_whale.n.01').min_depth()



playWithWordNet('strange')




def tagTester():
    raw_text = "hello there my young and fiendish friend, let us go for a wondrous walk through the woods, amiably."
    text = word_tokenize(raw_text)
    tagged_text = nltk.pos_tag(text)
    print(tagged_text)




# tagTester()



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
