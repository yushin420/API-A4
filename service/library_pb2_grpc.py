# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service.library_pb2 as library__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createBook = channel.unary_unary(
                '/InventoryService/createBook',
                request_serializer=library__pb2.Book.SerializeToString,
                response_deserializer=library__pb2.Message.FromString,
                )
        self.getBook = channel.unary_unary(
                '/InventoryService/getBook',
                request_serializer=library__pb2.Book.SerializeToString,
                response_deserializer=library__pb2.Book.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createBook(self, request, context):
        """return a string message indicating whether book was successfully added
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBook(self, request, context):
        """return Book to give detail of the specific book
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createBook': grpc.unary_unary_rpc_method_handler(
                    servicer.createBook,
                    request_deserializer=library__pb2.Book.FromString,
                    response_serializer=library__pb2.Message.SerializeToString,
            ),
            'getBook': grpc.unary_unary_rpc_method_handler(
                    servicer.getBook,
                    request_deserializer=library__pb2.Book.FromString,
                    response_serializer=library__pb2.Book.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/createBook',
            library__pb2.Book.SerializeToString,
            library__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/getBook',
            library__pb2.Book.SerializeToString,
            library__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
