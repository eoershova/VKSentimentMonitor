import pandas as pd


def scraper(link, n_posts, token='tokentoken'):
    print('i doing the scraping')
    dummy_df = pd.DataFrame({'text': ['я люблю Илью :)', 'ааа как я не ненавижу хрень'],
                             'context': ['post', 'вот хрень']})
    return dummy_df