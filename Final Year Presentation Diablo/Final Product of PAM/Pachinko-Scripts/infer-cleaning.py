from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import pandas as pd
import tomotopy as tp
import os

topics_dict = dict()
labels_dict = dict()
labels_list = list()
stemmer = PorterStemmer()
stops = set(stopwords.words('english'))
stops.update(['many', 'also', 'would', 'often', 'could', '\it'])

stop_words_raw = list()
stop_words = list()

dataframe = pd.read_csv('file_name')
abstracts = dataframe['column_name']


base_dir = os.path.dirname(os.path.abspath(__file__))
mdl = tp.PAModel.load(
    f'{base_dir}{os.sep}bio_chem_cs_math_part_2.model.bin')
test_corpus = tp.utils.Corpus(
    tokenizer=tp.utils.SimpleTokenizer(stemmer=stemmer.stem), stopwords=lambda x: len(x) <= 2 or x in stops)
test_corpus.process(abstracts)

for k in range(mdl.k):
    
    for word, prob in mdl.get_topic_words(k, top_n=10):
        print(word)

