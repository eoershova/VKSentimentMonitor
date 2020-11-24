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


def del_stop_words(text_data: str, add_stop = []):
  tokens = text_data.split()
  words = [t for t in tokens if t not in stop_words and t not in add_stop]
  return " ".join(words)
 
  
"""
usage:
import del_stop_words from drop_stopwords
string_without_stop_words = del_stop_words(text_string)
"""
