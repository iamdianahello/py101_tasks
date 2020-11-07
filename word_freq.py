from nltk import FreqDist
import string
import re
import nltk
from nltk.corpus import stopwords
"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""


def no_trash(data):
    punctuation_symbols = string.punctuation
    no_trash_data = data
    for punct in punctuation_symbols:
        no_trash_data = no_trash_data.replace(punct, ' ')
    no_trash_data = no_trash_data.replace('\n', ' ')
    no_trash_data = re.sub(' +', ' ', no_trash_data)
    no_trash_data = no_trash_data.lower()
    return no_trash_data


def no_stopwords(data):
    nltk.download('stopwords')
    english_stopwords = stopwords.words('english')
    no_stopwords_data = data
    for stopword in english_stopwords:
        no_stopwords_data = no_stopwords_data.replace(' ' + stopword + ' ', ' ')
    return no_stopwords_data


def top_words_finder(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        raw_data = file.read()
        data_no_trash = no_trash(raw_data)
        clean_data = no_stopwords(data_no_trash)
    clean_words_list = clean_data.split(' ')
    fdist = FreqDist(clean_words_list)
    print(fdist.most_common(100))


if __name__ == '__main__':
    top_words_finder('/home/di/eng_text.txt')
