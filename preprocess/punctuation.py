import string

def del_punct(text_data):
    tokens = text_data.split()

    # delete punctuation symbols
    tokens = [i for i in tokens if ( i not in string.punctuation )]

    return " ".join( tokens )
