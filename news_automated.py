import requests

API_KEY = 'f2488345765a4bccb86f03f6ca56c30a'

URL = 'https://newsapi.org/v2/top-headlines?'


def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "nl",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)


def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json().get('articles', [])

    results = []

    for article in articles:
        results.append({'title': article['title'], 'url': article['url']})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')
        break


def menu():
    categories = {
        1: "Business",
        2: "Entertainment",
        3: "General",
        4: "Health",
        5: "Science",
        6: "Sport",
        7: "Technology"
    }

    print("Hello Mark Bin, here are the options available for you to choose from:")
    for key, value in categories.items():
        print(f"{key}. {value}")

    while True:
        try:
            category_num = int(input('Which would you like to choose?\nInput a number please: '))
            if category_num in categories:
                category = categories[category_num]
                return category
            else:
                print("Invalid option. Please enter a number between 1 and 7.")
        except ValueError:
            print("Please input a number.")
def main():
    category = menu()

    get_articles_by_category(category)
    print(_get_articles('news'))


if __name__ == '__main__':
    main()
