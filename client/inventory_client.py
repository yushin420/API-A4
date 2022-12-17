import grpc

from service import library_pb2_grpc
from service import library_pb2

class client(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = library_pb2_grpc.InventoryServiceStub(self.channel)
    
    def createBook(self, isbn: str, title: str, author: str, genre: str, year: int):
        request = library_pb2.Book(isbn=isbn, title=title, author=author, genre=genre, year=year)
        response = self.stub.createBook(request)
        return response
    
    def getBook(self, isbn):
        request = library_pb2.Book(isbn=isbn)
        response = self.stub.getBook(request)
        return response