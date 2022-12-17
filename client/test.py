import grpc
from unittest.mock import MagicMock

from client import inventory_client
from client.get_book_titles import get_book_titles
from service.library_pb2 import Book

def test_get_book_titles():
    book_1 = Book()
    book_1.isbn = "9780060935467"
    book_1.title = "To Kill a Mockingbird"
    book_1.author = "Harper Lee"
    book_1.year = 1960
    book_1.genre = Book.FICTION

    book_2 = Book()
    book_2.isbn = "9781946963444"
    book_2.title = "Animal Farm"
    book_2.author = "George Orwell"
    book_2.year = 1945
    book_2.genre = Book.FICTION

    client = inventory_client.client()
    client.getBook = MagicMock(side_effect=[book_1,book_2])
    titles = get_book_titles(client, ["9780060935467", "9781946963444"])
    # check actual == expected
    assert titles == ["To Kill a Mockingbird", "Animal Farm"]
    print("First test passed")
    print(titles)

def test_integration():
    # check grpc service is running
    try:
        grpc.channel_ready_future(
            grpc.insecure_channel("localhost:50051")
        ).result(timeout=10)
    except grpc.FutureTimeoutError:
        print("gRPC service is not running")
        return

    client = inventory_client.client()
    titles = get_book_titles(client, ["9780060935467", "9781946963444"])
    # check actual == expected
    assert titles == ["To Kill a Mockingbird", "Animal Farm"]
    print("Second test passed")
    print(titles)

if __name__ == "__main__":
    #comment out necessary functions to run the unit test
    # without server
    test_get_book_titles()
    # with server
    test_integration()
