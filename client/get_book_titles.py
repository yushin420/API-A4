from client import inventory_client

def get_book_titles(client, isbn):
    book_titles = []
    for i in isbn:
        # retrieve Book object
        book = client.getBook(i)
        # add title to the list
        book_titles.append(book.title)
    return book_titles

if __name__ == "__main__":
    client = inventory_client.client()
    titles = get_book_titles(client, ["9780060935467", "9781946963444"])
    print(titles)