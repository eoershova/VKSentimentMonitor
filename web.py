import pandas as pd

from scraper import scraper
from preprocess.main import preprocess
from ml import model_predict, metrics
from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def index():
    if request.args:
        link = request.args['link']
        n_posts = int(request.args['n_posts'])
        print(f'i got the args they are {link, n_posts}')

        # тут начинается получаение результата
        raw_comments_df = scraper(link, n_posts)
        print('raw comments shape', raw_comments_df.shape)
        # print(raw_comments_df)
        preprocessed_comments_df = pd.DataFrame({'text': raw_comments_df['text'].tolist()})
        preprocessed_comments_df['text'] = preprocessed_comments_df.text.apply(lambda x: str(preprocess(x)))
        preprocessed_comments_df = preprocessed_comments_df[preprocessed_comments_df['text'] != 'None']
        print('preproc comments shape', preprocessed_comments_df.shape)
        # print(preprocessed_comments_df)
        prediction = model_predict(preprocessed_comments_df)
        result = metrics(prediction)

        positive_n = result['positive_n']
        negative_n = result['negative_n']
        neutral_n = result['neutral_n']
        positive_index = result['positive_index']
        neutral_index = result['neutral_index']

        return render_template('result.html', positive=positive_n, negative=negative_n, neutral=neutral_n,
                               positive_index=positive_index, neutral_index=neutral_index)
    return render_template('index.html', links=[])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
