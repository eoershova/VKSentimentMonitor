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
