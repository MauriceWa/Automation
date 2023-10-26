import requests

API_KEY = 'f2488345765a4bccb86f03f6ca56c30a'

URL = ('https://newsapi.org/v2/top-headlines?')


def get_articles_by_category(category):
    query_parameters ={
        "category": category,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)



def _get_articles(params):
    print("TEMP")