#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Imports
from datetime import datetime
import json
import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from pydoc_data.topics import topics
import tomotopy as tp
from nltk.corpus import words
import string
from nltk.tokenize import word_tokenize
import time
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
import csv
# Read Dataset

#dataframe = pd.read_csv('datasets/bio_chem_cs_math.xlsx')


dataframe = pd.read_excel('20News.xlsx')
abstracts = dataframe['text']
print(len(abstracts))
print(datetime.now())
super_nodes = 1
sub_nodes = 700
number_of_docs = 2000
perplexity = 0
coherence = 0
train_iterations = 2000
article_name = '20_news_part_3'

# PAM Model

mdl = tp.PAModel(tw=tp.TermWeight.ONE, min_cf=7,
                 min_df=7, rm_top=1, k1=super_nodes, k2=sub_nodes)
#print('Term Weight ONE, Minimum Count: 5, Minimum Document count: 10, Super nodes: 5, Sub Nodes: 17, 300 abstracts')


# Data Pre-processing
stop_words = list()
strpun = list()
pun = string.punctuation
topics_dict = dict()
labels_dict = dict()
labels_list = list()
# Punctuations
for i in pun:
    strpun.append(i)

# Stop words
with open('words.txt', encoding='utf-8') as wf:
    for i in wf.readlines():
        # print(i)
        stop_words.append(i.replace('\n', ''))

# Reading text, tokenizing, filtering, length checking
for index in range(0, number_of_docs):
    # print(index)
    #print('Inside Add index')

    # Reading Paragraph
    pargraph = str(abstracts[index]).strip().replace('\n', ' ')

    if len(pargraph) > 600:
        # Tokeinzing
        word_tokens = word_tokenize(pargraph)  # Tokeinzing the paragraph
        filter_sentence = list()

        # Stopwords removal
        for w in word_tokens:
            if w.lower() not in stop_words:
                #      if w in words.words():
                # if w.lower not in filter_sentence:
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
            # if lem_word not in lemetized_list:
            lemetized_list.append(lem_word)

        empty_string = ""
        for filter in lemetized_list:
            empty_string += filter
        if len(empty_string) > 100:
            #print('Adding doc')

            mdl.add_doc(lemetized_list)  # Adding document
            mdl.burn_in = 1000  # Parameter optimization

mdl.train(0)
loglikeli = None

# Start time of training
start = time.time()
# Model Training
for i in range(0, train_iterations, 10):
    mdl.train(10)  # Training the model
    #loglikeli = mdl.ll_per_word

# End time of training
end = time.time()
total_time = end - start
print('Training time in seconds: '+str(end - start))
#print('Iteration: {}\tLog-likelihood: {}'.format(i, mdl.ll_per_word))

# Perplexity
perplexity = mdl.perplexity
print("Perplexity: "+str(perplexity))

# Model Saving
mdl.save('news_model/'+article_name+'.model.bin')

# Model Loading
#mdl_new = tp.PAModel.load('pam.model.bin')

# Coherence
# for preset in ('u_mass',):
coh = tp.coherence.Coherence(mdl, coherence='u_mass')
average_coherence = coh.get_score()
coherence = average_coherence
print('Coherence with u_mass')
print('Average:', average_coherence)
print()


with open('news_model_results/news_record.csv', 'a') as csvFile:
    reader = csv.writer(csvFile)
    reader.writerow([article_name, number_of_docs,
                     super_nodes, sub_nodes, perplexity, coherence, train_iterations, total_time])
# ---------------------------------Rest is storing the results and tree walking for topic labeling
# topics = {
#     "perplexity": loglikeli
# }
for k in range(mdl.k):
    print('Topic #{}'.format(k))
    topiclist = list()
    for word, prob in mdl.get_topic_words(k):
        print('\t', word, prob, sep='\t')
        topiclist.append((word, prob))
    # for word2 in mdl.get_sub_topics(k):
        #print('topic words sub ed:----- '+ str(word2) )
    #topics[f"topic_{k}"] = topiclist


# #pprint(topics)
# test_corpus = tp.utils.Corpus(
#     tokenizer=tp.utils.SimpleTokenizer(), stopwords=['.'])
# test_corpus.process(abstracts[300:310])
# inferred_corpus, ll = mdl.infer(test_corpus)
# #for doc in inferred_corpus:
# #    print(list(doc))
#     #print(doc.get_topic_dist())

#data_store = dict()
# extractor = tp.label.PMIExtractor(
    # min_cf=10, min_df=15, max_len=10, max_cand=20000, normalized=True)
#cands = extractor.extract(mdl)

# labeler = tp.label.FoRelevance(
    # mdl, cands, min_df=10, smoothing=1e-2, mu=0.25)
# for k in range(mdl.k):
    #word_list = list()
    #label_cands = list()

    #labels = []

    # for label, score in labeler.get_topic_labels(k, top_n=5):
        #items = label.split(' ')
        # for item in items:
        # if item not in labels:
        # labels.append(item)

        #current_label = " ".join(label for label in labels[:3])

        #labels_dict['label_'+str(k)] = current_label
        # labels_list.append(current_label)

        # for word, prob in mdl.get_topic_words(k, top_n=10):
        # word_list.append(word)

        #topics_dict[current_label] = word_list
#df = pd.DataFrame(data=topics_dict)
# df.to_csv('general_results.csv')
# for k in range(mdl.k):
#     print("== Topic #{} ==".format(k))
#     print("Labels:", ', '.join(label for label,
#         score in labeler.get_topic_labels(k, top_n=1)))
#     for word, prob in mdl.get_topic_words(k, top_n=10):
#         print(word, prob, sep='\t')
#     print()


# def get_category(alldict):
#     keylist = list()
#     for item in list(alldict.keys()):
#         if not item == 'perplexity':
#             keylist.append(item)
#     with open("model.json") as modelfile:
#         modeldata = dict(json.loads(modelfile.read()))

#     topics = list()
#     for key in keylist:
#         catcount = dict()
#         for catkey in list(modeldata.keys()):
#             count = 0
#             for item in alldict[key]:
#                 if item[0] in modeldata[catkey]:
#                     count += 1
#             catcount[catkey] = count
#         print(catcount)
#         topics.append(catcount)
#     topic_cat = dict()
#     for i in range(0, len(topics)):
#         highest = 0
#         highest_key = ""
#         for key in list(topics[i].keys()):
#             if topics[i].get(key) > highest:
#                 highest = topics[i][key]
#                 highest_key = key
#             topic_cat[f"topic_{i}"] = highest_key
#     # pprint(topic_cat)
#     return topic_cat


# print(get_category(topics))
