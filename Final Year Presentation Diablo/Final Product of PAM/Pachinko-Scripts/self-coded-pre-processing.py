import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import tomotopy as tp

stop_words = list()
strpun = list()
pun = string.punctuation
dataframe = pd.read_excel('dataset.xlsx')
abstracts = dataframe['ABSTRACT']

# Punctuations
for i in pun:
    strpun.append(i)
mdl = tp.PAModel(tw=tp.TermWeight.ONE, min_cf=10,
                 min_df=15, rm_top=1, k1=7, k2=270)
# Stop words
with open('words.txt', encoding='utf-8') as wf:
    for i in wf.readlines():
        # print(i)
        stop_words.append(i.replace('\n', ''))

# Reading text, tokenizing, filtering, length checking
for index in range(0, 2000):
    # print(index)
    #print('Inside Add index')

    # Reading Paragraph
    pargraph = abstracts[index].strip().replace('\n', ' ')

    if len(pargraph) > 600:
        # Tokeinzing
        word_tokens = word_tokenize(pargraph)  # Tokeinzing the paragraph
        filter_sentence = list()

        # Stopwords removal
        for w in word_tokens:
            if w.lower() not in stop_words:
                #      if w in words.words():
                #if w.lower not in filter_sentence:
                filter_sentence.append(w.lower())
        #filter_sentence = [w.lower() for w in word_tokens if not w.lower() in stop_words]
        filtered_sentence = list()
        for filteration in filter_sentence:
            try:
                temp = int(filteration)
            except:

                # Cleaning Punctuation
                for stri in strpun:
                    if not filteration.__contains__(stri):
                        # Filtered/Stop words removed text
                        filtered_sentence.append(filteration)
                    else:
                        break

        lementize = WordNetLemmatizer()
        lemetized_list = list()
        for word in filtered_sentence:
            lem_word = lementize.lemmatize(word)
            #if lem_word not in lemetized_list:
            lemetized_list.append(lem_word)

        empty_string = ""
        for filter in lemetized_list:
            empty_string += filter
        if len(empty_string) > 100:
            #print('Adding doc')

            mdl.add_doc(lemetized_list)  # Adding document
            mdl.burn_in = 1000  # Parameter optimization
