


def menu_pages():
    while True:
        try:
            pages = int(input('Which would you like to choose?\nInput a number please: '))
            return pages
        except ValueError:
            print("Please input a number.")




menu_pages()