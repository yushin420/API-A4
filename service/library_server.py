from concurrent import futures
from google.protobuf.descriptor import EnumDescriptor

import logging

import grpc
import library_pb2
import library_pb2_grpc


# book database
database = {}
book_1 = library_pb2.Book()
book_1.isbn = "9780060935467"
book_1.title = "To Kill a Mockingbird"
book_1.author = "Harper Lee"
book_1.year = 1960
book_1.genre = library_pb2.Book.FICTION
database["9780060935467"] = book_1

book_2 = library_pb2.Book()
book_2.isbn = "9781946963444"
book_2.title = "Animal Farm"
book_2.author = "George Orwell"
book_2.year = 1945
book_2.genre = library_pb2.Book.FICTION
database["9781946963444"] = book_2
print(database)

class InventoryService(library_pb2_grpc.InventoryServiceServicer):

    def createBook(self, request, context):
        # if the book with that ISBN already exists, send a message that it exists in the database
        if request.isbn in database:
            return library_pb2.Message(message='A book with this ISBN (%s) already exists in the database!' % request.isbn)

        # if not add the new book to the database
        else:
            book = library_pb2.Book()
            book.isbn = request.isbn
            book.title = request.title
            book.author = request.author
            book.year = request.year

            # check the genre of the book
            if (request.genre == 1):
                book.genre = library_pb2.Book.FICTION
            elif (request.genre == 2):
                book.genre = library_pb2.Book.SCIENCEFICTION
            elif (request.genre == 3):
                book.genre = library_pb2.Book.NONFICTION
            elif (request.genre == 4):
                book.genre = library_pb2.Book.MYSTERY

            database[request.isbn] = book

            # return a successful message
            return library_pb2.Message(message='%s is added to the database!' % request.title)
    
    def getBook(self, request, context):
        # retrieve the book from the database
        book = database.get(request.isbn)
        return library_pb2.Book(isbn = book.isbn, title = book.title, author = book.author, genre = book.genre, year = book.year)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    print("gRPC starting")
    serve()