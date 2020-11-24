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
        ner_spans = ner(text).spans
        for span in ner_spans:
            span_value = text[span.start:span.stop]
            text = re.sub(span_value, ' ', text)
        text = " ".join(text.split())
        return text
    
def replace_ner(text):
        ner_spans = ner(text).spans
        for span in ner_spans:
            span_value = text[span.start:span.stop]
            text = re.sub(span_value, ' NER ', text)
        text = " ".join(text.split())
        return text
