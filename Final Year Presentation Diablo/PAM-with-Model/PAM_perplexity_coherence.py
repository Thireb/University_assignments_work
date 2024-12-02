#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Imports
import json
import nltk
#nltk.download('wordnet')
#nltk.download('omw-1.4')
from pydoc_data.topics import topics
import tomotopy as tp
from nltk.corpus import words
import string
from nltk.tokenize import word_tokenize
import time
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer

# Read Dataset
dataframe = pd.read_excel('dataset.xlsx')
abstracts = dataframe['ABSTRACT']

# PAM Model
mdl = tp.PAModel(tw=tp.TermWeight.ONE, min_cf=10,
                 min_df=10, rm_top=5, k1=10, k2=270)
print('Term Weight ONE, Minimum Count: 10, Minimum Document count: 10, Super nodes: 10, Sub Nodes: 270, 700 abstracts')


#---------------------Data Pre-processing----------------
stop_words = list()
strpun = list()
pun = string.punctuation

# Punctuations
for i in pun:
    strpun.append(i)

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
                    
        # lementize = WordNetLemmatizer()
        # lemetized_list = list()
        # for word in filtered_sentence:
        #     lem_word = lementize.lemmatize(word)
        #     if lem_word not in lemetized_list:
        #         lemetized_list.append(lem_word)
        empty_string = ""
        for filter in filtered_sentence:
            empty_string += filter
        if len(empty_string) > 100:
            #print('Adding doc')

            mdl.add_doc(filtered_sentence)  # Adding document
            mdl.burn_in = 1000  # Parameter optimization

mdl.train(0)
loglikeli = None

# Start time of training
start = time.time()

# Model Training
for i in range(0, 1000, 10):
    mdl.train(10)  # Training the model
    #loglikeli = mdl.ll_per_word

# End time of training
end = time.time()
print('Training time in seconds: '+str(end - start))
#print('Iteration: {}\tLog-likelihood: {}'.format(i, mdl.ll_per_word))

# Perplexity
print("Perplexity: "+str(mdl.perplexity))

# Model Saving
# mdl.save('pam.model.bin')

# Model Loading
#mdl_new = tp.PAModel.load('pam.model.bin')

# Coherence
for preset in ('u_mass', 'c_uci', 'c_npmi', 'c_v'):
    coh = tp.coherence.Coherence(mdl, coherence=preset)
    average_coherence = coh.get_score()
    print('Coherence with {}'.format(preset))
    print('Average:', average_coherence)
    print()


# ---------------------------------Rest is storing the results and tree walking for topic labeling
topics = {
    "perplexity": loglikeli
}
for k in range(mdl.k):
    print('Topic #{}'.format(k))
    topiclist = list()
    for word, prob in mdl.get_topic_words(k):
        print('\t', word, prob, sep='\t')
        topiclist.append((word, prob))

    topics[f"topic_{k}"] = topiclist

# pprint(topics)


def get_category(alldict):
    keylist = list()
    for item in list(alldict.keys()):
        if not item == 'perplexity':
            keylist.append(item)
    with open("model.json") as modelfile:
        modeldata = dict(json.loads(modelfile.read()))

    topics = list()
    for key in keylist:
        catcount = dict()
        for catkey in list(modeldata.keys()):
            count = 0
            for item in alldict[key]:
                if item[0] in modeldata[catkey]:
                    count += 1
            catcount[catkey] = count
        print(catcount)
        topics.append(catcount)
    topic_cat = dict()
    for i in range(0, len(topics)):
        highest = 0
        highest_key = ""
        for key in list(topics[i].keys()):
            if topics[i].get(key) > highest:
                highest = topics[i][key]
                highest_key = key
            topic_cat[f"topic_{i}"] = highest_key
    # pprint(topic_cat)
    return topic_cat


print(get_category(topics))
