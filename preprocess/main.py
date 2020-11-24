import re
import emoji
import pandas as pd

pos_emojis = ['😀', '😁', '😂', '🤣', '😃', '😄', '😆', '😊', '😋', '😎',
 '😍', '😘', '🥰', '😚', '☺️', '🙂', '🤗', '🤩', '😏', '😌', '😛', '😜',
 '😝', '🙃', '🤑', '🤠', '😇', '🥳', '🥺', '😅', '🤤', '🤧', '🥵', '😳',
  '😉', '😲', '😯', '🥳', '😈', '😺','😸', '😹', '😻', '😽', '😼', '👍', '✌️',
  '🤟', '🤘', '👌', ' 🤙', '🙌', '🙏', '👏', '🤞', ' 👀', '❤️', '🧡', '💛',
   '💚', '💙', '💜', '🤎', '🖤', '❣️', '💕', '💞', '💓', '💗', '💖', '💘',
   '💝', '💟', '♥️', '💔', '💌', '🎊', '🎉', '🔝', '🆒', '🆗',
   '💑', '👩‍❤️‍👩', '👨‍❤️‍👨', '💏', '👩‍❤️‍💋‍👩', '👨‍❤️‍💋‍👨', '👸', '🤴', '🙆‍♀️', '🙆‍♂️', '🕺', '💃', '🙈', '🐱', '🐶', '🔆', '🔅', '☀️','🎆', '🌅', '🌄', '🌠',
    '🎇', '🎆', '🌇', '🌌', '💡', '🏖', '🏝', '💯', '✅', '✔️', '☑️', '✓', '➕', '🎁', '💪', '👼',
     '🍀', '🌞', '🌸', '🌼', '🌻', '🌺', '🌹', '💐', '🌈', '🎈', '💥', '🔥', ':)',
      '👉👈', '🦋', '🐥', '🐾', '⭐', '🌟', '💫', '✨', '🐛', '💦', '👑',
      '🍑', '🍥', '🍺', '🍻', '🥂', '🍰', '🥇', '🎖', '🏅', '🧚‍♀️', '🧚', '🧚‍♂️', '🌤']


neg_emojis = ['🤨', '😐', '😑', '😶', '🙄', '😣', '😥', '🤐', '😫', '😓',
 '😔', '😕', '☹️', '🙁', '😖', '😞', '😟', '😤', '😢', '😭', '😦', '😧',
  '😨', '😩', '😬', '😰', '😡', '😠', '🤬', '🤥', '🤕', '🤢', '🤯', '🤮', '😪', '🤕', '👿', '😾',
   '😿', '🙀', '👎', '🤦‍♀️', '🤦‍♂️', '🙎‍♀️', '🙎‍♂️', '🙍‍♀️', '🙍‍♂️', '🙅‍♀️', '🙅‍♂️', '🥀', '🌥', '🌧',
    '⛈', '💔', '💢', '🔴', '🚨', '🧯', '⁉️', '🤡', '💩', '🆖', '☓', '❌', '☒']


neutral_emojis = ['😴', '🤒', '🤢', '😷', '😵', '🦠', '🥶', '🥴', '💤', '😱', '🤔']


def del_emoji(text_data):
    str_emo = emoji.demojize(text_data)
    text = re.sub(':.*?:', '', str_emo)
    return re.sub('\s+', ' ', text)


def replace_all_emoji(text_data):
    str_emo = emoji.demojize(text_data)
    text = re.sub(':.*?:', 'emoji', str_emo)
    return re.sub('\s+', ' ', text)


def replace_emoji_by_class(text_data):
    tokens = text_data.split()
    new_tokens = []
    for t in tokens:
        if t in pos_emojis:
            t = 'pos_emoji'
        elif t in neg_emojis:
            t = 'neg_emoji'
        else:
            t = re.sub(':.*?:', 'neutral_emoji', emoji.demojize(t))
        new_tokens.append(t)
    return " ".join(new_tokens)

from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()

def lemmatize(text_data: str):
  tokens = text_data.split()
  lemms = [morph.parse(t)[0].normal_form for t in tokens]
  return " ".join(lemms)


"""
usage:
lemms_string = lemmatize(text_string)
"""

import re
from urllib.request import urlretrieve
import os.path

from navec import Navec
from slovnet import NER

destination = 'navec_news_v1_1B_250K_300d_100q.tar'

if os.path.isfile(destination):
    pass
else:
    url = 'https://storage.yandexcloud.net/natasha-navec/packs/navec_news_v1_1B_250K_300d_100q.tar'
    urlretrieve(url, destination)

navec = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')
ner = NER.load('slovnet_ner_news_v1.tar')
ner.navec(navec)


def delete_ner(text):
    try:
        ner_spans = ner(text).spans
        for span in ner_spans:
            span_value = text[span.start:span.stop]
            text = re.sub(span_value, ' ', text)
        text = " ".join(text.split())
    except Exception:
        pass
    return text


def replace_ner(text):
    try:
        ner_spans = ner(text).spans
        for span in ner_spans:
            span_value = text[span.start:span.stop]
            text = re.sub(span_value, ' NER ', text)
        text = " ".join(text.split())
    except Exception:
        pass
    return text

import string

def del_punct(text_data):
    tokens = text_data.split()

    # delete punctuation symbols
    tokens = [i for i in tokens if ( i not in string.punctuation )]

    return " ".join( tokens )


from nltk.corpus import stopwords

stop_words = set(stopwords.words('russian'))

badwords = [
    u'я', u'а', u'да', u'но', u'тебе', u'мне', u'ты', u'и', u'у', u'на', u'ща', u'ага',
    u'так', u'там', u'какие', u'который', u'какая', u'туда', u'давай', u'короче', u'кажется', u'вообще',
    u'ну', u'чет', u'неа', u'свои', u'наше', u'хотя', u'такое', u'например', u'кароч', u'как-то',
    u'нам', u'хм', u'всем', u'да', u'оно', u'своем', u'про', u'вы', u'м', u'тд',
    u'вся', u'кто-то', u'что-то', u'вам', u'это', u'эта', u'эти', u'этот', u'прям', u'либо', u'как', u'мы',
    u'просто', u'блин', u'очень', u'самые', u'твоем', u'ваша', u'кстати', u'вроде', u'типа', u'пока', u'ок'
]


def del_stop_words(text_data: str, add_stop=[]):
    tokens = text_data.split()
    words = [t for t in tokens if t not in stop_words and t not in add_stop]
    return " ".join(words)


"""
usage:
import del_stop_words from drop_stopwords
string_without_stop_words = del_stop_words(text_string)
"""

import re
from pymorphy2.tokenizers import simple_word_tokenize

def tokenize(text_data):
    text_data = str(text_data).lower() # к нижнему регистру
    text_data = re.sub('\s+', ' ', text_data) # нормализовать все переносы и табы к просто пробелу
    text_data = re.sub('\[id\d*\|\w*\]', 'username', text_data) # замена всех упоминаний пользователей
    text_data = re.sub('"', '', text_data) # удаление двойных кавычек
    text_data = re.sub("'", '', text_data) # удаление апострофов
    text_data = re.sub('ё', 'е', text_data) # замена Ё на Е
    text_data = re.sub(r'(?<=\w)\*', 'ё', text_data) # замена * на Ё, если перед ним буква
    tokens = simple_word_tokenize(text_data) # токенизация
    return ' '.join(tokens)


"""
usage:
from preprocess import tokenization
token_string = tokenization.tokenize(text_string)
"""

import requests

url = 'https://raw.githubusercontent.com/odaykhovskaya/obscene_words_ru/master/obscene_corpus.txt'
r = requests.get(url)
obscene_words = r.text.lower().split('\n')[:-1]


def replace_vulgar(text):
    tokens = text.split(' ')
    for i, v in enumerate(tokens):
        if 'ё' in v:
            tokens[i] = 'vulgar'
        elif v in obscene_words:
            tokens[i] = 'vulgar'
    return ' '.join(tokens)


def preprocess(text, params={'punctuation_deletion': 'yes',
                             'lemmatization': 'no',
                             'stopwords_deletion': 'no', 
                             'emojis_processing': 'no', 
                            'preprocess_ner': 'del',
                             'vulgar_processing': 'yes'}):

    print('preproc has started')
    # print('BP', text)

    text = tokenize(text)

    if params['punctuation_deletion'] == 'no':
        pass 
    elif params['punctuation_deletion'] == 'yes':
        text = del_punct(text)
    else:
        raise ValueError('такой опции нет')
        
        
    if params['preprocess_ner'] == 'no':
        pass 
    elif params['preprocess_ner'] == 'del':
        text = delete_ner(text)
    elif params['preprocess_ner'] == 'replace':
        text = replace_ner(text)
    else:
        raise ValueError('такой опции нет')
        
        
    if params['lemmatization'] == 'no':
        pass 
    elif params['lemmatization'] == 'yes':
        text = lemmatize(text)
    else:
        raise ValueError('такой опции нет')
        
    if params['stopwords_deletion'] == 'no':
        pass 
    elif params['stopwords_deletion'] == 'yes':
        text = del_stop_words(text, add_stop=badwords)
    else:
        raise ValueError('такой опции нет')
        
    
    if params['emojis_processing'] == 'no':
        pass 
    elif params['emojis_processing'] == 'del':
        text = del_emoji(text)
    elif params['emojis_processing'] == 'replace':
        text = replace_all_emoji(text)
    elif params['emojis_processing'] == 'label':
        text = replace_emoji_by_class(text)
    else:
        raise ValueError('такой опции нет')

    if params['vulgar_processing'] == 'no':
        pass
    elif params['vulgar_processing'] == 'yes':
        text = replace_vulgar(text)
    else:
        raise ValueError('такой опции нет')

    if re.search('[а-яА-ЯёЁ]', text) is None and len(text.split()) < 1:
        text = 'None'
    # print('AP', text)
    return text
