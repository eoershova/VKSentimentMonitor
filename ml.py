import pickle

import numpy as np
import pandas as pd



# импортирует натренированный векторайзер и модель
vectorizer = pickle.load(open('/home/VKSentimentMonitor/VKSentimentMonitor/models/vectorizer.pickle', 'rb'))
model = pickle.load(open('/home/VKSentimentMonitor/VKSentimentMonitor/models/classifier.pickle', 'rb'))

# vectorizer = pickle.load(open('models/vectorizer.pickle', 'rb'))
# model = pickle.load(open('models/classifier.pickle', 'rb'))


def metrics(predicted):
    positive_n = predicted[predicted['prediction'] == 1].shape[0]
    negative_n = predicted[predicted['prediction'] == -1].shape[0]
    neutral_n = predicted[predicted['prediction'] == 0].shape[0]

    try:
        positive_index = positive_n / (negative_n + neutral_n + positive_n)
    except Exception:
        positive_index = 'не удалось рассчитать'

    try:
        neutral_index = neutral_n / (negative_n + neutral_n + positive_n)
    except Exception:
        neutral_index = 'не удалось рассчитать'

    result = {
        'positive_n': positive_n,
        'negative_n': negative_n,
        'neutral_n': neutral_n,
        'positive_index': positive_index,
        'neutral_index': neutral_index
    }

    return result


def model_predict(comments):
    print('prediction going on')
    texts = comments.text
    X = vectorizer.transform(texts)
    y_pred = model.predict(X)
    comments['prediction'] = y_pred
    return comments







