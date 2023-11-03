import requests

# voer je eigen API in

API_KEY = 'f2488345765a4bccb86f03f6ca56c30a'

URL = 'https://newsapi.org/v2/top-headlines?'


def get_articles_by_category(category, country, number_of_pages):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": country,
        "pageSize": number_of_pages,
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)


def _get_articles(params):
    response = requests.get(URL, params=params)
    print(response)
    articles = response.json().get('articles', [])

    results = []

    for article in articles:
        results.append({'title': article['title'], 'url': article['url']})

    articles_to_print = min(len(results), 5)

    for i in range(articles_to_print):
        print(results[i]['title'])
        print(results[i]['url'])
        print('')


def menu_category():
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


def menu_country():
    categories = {
        1: "gb",
        2: "nl",
        3: "us"
    }
    print("Hello Mark Bin, here are the options available for you to choose from:")
    print("1. Great Britain\n2. The Netherlands\n3. The United States of America")

    while True:
        try:
            category_num = int(input('Which would you like to choose?\nInput a number please: '))
            if category_num in categories:
                country = categories[category_num]
                return country
            else:
                print("Invalid option. Please enter a number between 1 and 7.")
        except ValueError:
            print("Please input a number.")


def menu_pages():
    while True:
        try:
            pages = int(input('How many articles would you like to see?\nInput a number please: '))
            return pages
        except ValueError:
            print("Please input a number.")


def main():
    category = menu_category()
    country = menu_country()
    number_of_pages = menu_pages()
    print(get_articles_by_category(category, country, number_of_pages))


if __name__ == '__main__':
    main()
