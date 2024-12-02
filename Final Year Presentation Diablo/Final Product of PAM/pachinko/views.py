from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import inputForm
from django.core.files.storage import FileSystemStorage
import nltk
import tomotopy as tp
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import os
from .embed import label_generator, label_sorter


def PAMrunner(file_to_get, column_name):

    topics_dict = dict()
    stemmer = PorterStemmer()
    stops = set(stopwords.words('english'))
    stops.update(['many', 'also', 'would', 'often', 'could', '\it',"'s"])
    dataframe = pd.read_csv(file_to_get)
    try:
        abstracts = dataframe[column_name]

    except:
        return "Column doesn't exists. Please check again."

    base_dir = os.path.dirname(os.path.abspath(__file__))

    mdl = tp.PAModel.load(
        f'{base_dir}{os.sep}phy_chem_cs_math_part_2.model.bin')

    test_corpus = tp.utils.Corpus(
        tokenizer=tp.utils.SimpleTokenizer(stemmer=stemmer.stem), stopwords=lambda x: len(x) <= 2 or x in stops)
    test_corpus.process(str(abstracts))

    labeler = label_generator(mdl)
    for k in range(mdl.k):
        word_list = list()

        labels = []

        for label, score in labeler.get_topic_labels(k, top_n=5):
            items = label.split(' ')
            for item in items:
                if item not in labels:
                    labels.append(item)
        label_chunk = labels[:3]
        final_labels = label_sorter(label_chunk)
        current_label = " ".join(label for label in final_labels)

        for word, prob in mdl.get_topic_words(k, top_n=10):
            word_list.append(word)

        topics_dict[current_label] = word_list

    return topics_dict


def homeView(request):
    context = {}
    context['form'] = inputForm()
    return render(request, 'home_1.html', context)


def displayView(request):
    column_name = request.POST['column_name']
    csv_file = request.FILES['csv-file']

    if not csv_file.name.endswith('.csv'):
        return HttpResponse('<h1>File Incorrect</h1>')

    fs = FileSystemStorage()

    filename = fs.save(csv_file.name, csv_file)

    all_topics = PAMrunner(filename, column_name)
    if type(all_topics) != dict:

        return render(request, 'error.html', context={'error': all_topics})
    return render(request, 'display_1.html', context={'topics': all_topics})
