import requests

url = 'https://raw.githubusercontent.com/odaykhovskaya/obscene_words_ru/master/obscene_corpus.txt'
r = requests.get(url)
obscene_words = r.text.lower().split('\n')[:-1]


def vulgar_holder(text):
    tokens = text.split(' ')
    for i, v in enumerate(tokens):
        if 'ё' in v:
            tokens[i] = 'vulgar'
        elif v in obscene_words:
            tokens[i] = 'vulgar'
    return ' '.join(tokens)
