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
