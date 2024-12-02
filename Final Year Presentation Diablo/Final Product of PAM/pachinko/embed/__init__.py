from typing import Any, Dict, List
from gensim.models import Word2Vec
import gensim
import csv
import pandas as pd
import tomotopy as tp
import nltk


def vectorization(
    data: list,
    min_count: int = 1,
    vector_size: int = 2,
    window: int = 1,
    times: int = 3,
) -> List[List[Any]]:
    vector = [data]
    main_model = Word2Vec(
        vector,
        min_count=min_count,
        vector_size=vector_size,
        window=window,
    )
    datalist = list()
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            temp_list = []
            if data[i] == data[j]:
                continue
            temp_list.append(data[i])
            temp_list.append(data[j])
            temp_list.append(main_model.wv.similarity(data[i], data[j]))
            datalist.append(temp_list)
    return distancing(datalist, times=times)


def distancing(data: List[List[Any]], times: int) -> List[Any]:
    labels = list()
    first_item = None
    for i in range(0, times-1):
        temp_list = data
        if first_item:
            temp_list = []
            for item in data:
                if item[0] == second_item:
                    if item[1] in labels:
                        continue
                    temp_list.append(item)
        first_item, second_item = csv_ing(temp_list, first=first_item)
        if first_item not in labels:
            labels.append(first_item)
        if second_item not in labels:
            labels.append(second_item)
        first_item = second_item
    return(labels)


def csv_ing(data: List[Any], first: str = None):
    with open('datafile.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["data[i]", "data[j]", "distance"])
        for item in data:
            csvwriter.writerow(item)
    dataframe = pd.read_csv('datafile.csv')
    sorted = dataframe.sort_values(by='distance')
    if first == None:
        data_i = sorted['data[i]']
        data_i = list(data_i)[0]
        data_j = sorted['data[j]']
        data_j = list(data_j)[0]
    elif first != None:
        datad = sorted.loc[sorted["data[i]"] == f"{first}"]
        data_i, data_j = list(datad["data[i]"])[0], list(datad["data[j]"])[0]
    return data_i, data_j


def label_generator(mdl):
    extractor = tp.label.PMIExtractor(
        min_cf=7, min_df=5, min_len=1, max_len=5, max_cand=10000)  # , normalized=True)
    cands = extractor.extract(mdl)

    labeler = tp.label.FoRelevance(
        mdl, cands, min_df=5, smoothing=1e-6, mu=0.25, window_size=50)
    return labeler


def label_sorter(label):
    #Noun Pronoun Adverb Verb Adjective.
    tag_list = nltk.pos_tag(label)
    if len(tag_list) == 3:
        first, second, third = nltk.pos_tag(label)
        first = list(first)
        second = list(second)
        third = list(third)
        labels_list = [first, second, third]
    else:
        return label
    sorted_label_arrangement = []
    for label in labels_list:
        if label[1] in ['JJ', 'JJR', 'JJS']:
            label[1] = '4'
        elif label[1] in ['VBG', 'VB', 'VBD', 'VBN', 'VBP', 'VBZ']:
            label[1] = '3'
        elif label[1] in ['NN', 'NNS', 'NNP', 'NNPS']:
            label[1] = '1'
        elif label[1] in ['RB', 'RBR', 'RBS']:
            label[1] = '2'
        else:
            label[1] = '5'
    for index in range(1, 6):
        for label in labels_list:
            if label[1] == str(index):
                sorted_label_arrangement.append(label[0])

    return sorted_label_arrangement
