# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import prototype_pb2 as prototype__pb2


class PicturesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPicture = channel.unary_unary(
                '/prototype.Pictures/GetPicture',
                request_serializer=prototype__pb2.PictureRequest.SerializeToString,
                response_deserializer=prototype__pb2.PictureResponse.FromString,
                )
        self.AddPicture = channel.unary_unary(
                '/prototype.Pictures/AddPicture',
                request_serializer=prototype__pb2.AddPictureRequest.SerializeToString,
                response_deserializer=prototype__pb2.PictureResponse.FromString,
                )


class PicturesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPicture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPicture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PicturesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPicture': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPicture,
                    request_deserializer=prototype__pb2.PictureRequest.FromString,
                    response_serializer=prototype__pb2.PictureResponse.SerializeToString,
            ),
            'AddPicture': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPicture,
                    request_deserializer=prototype__pb2.AddPictureRequest.FromString,
                    response_serializer=prototype__pb2.PictureResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prototype.Pictures', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Pictures(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPicture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Pictures/GetPicture',
            prototype__pb2.PictureRequest.SerializeToString,
            prototype__pb2.PictureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPicture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Pictures/AddPicture',
            prototype__pb2.AddPictureRequest.SerializeToString,
            prototype__pb2.PictureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SpecsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListProducts = channel.unary_unary(
                '/prototype.Specs/ListProducts',
                request_serializer=prototype__pb2.SpecsRequest.SerializeToString,
                response_deserializer=prototype__pb2.SpecsResponse.FromString,
                )
        self.AddProduct = channel.unary_unary(
                '/prototype.Specs/AddProduct',
                request_serializer=prototype__pb2.SpecsRequest.SerializeToString,
                response_deserializer=prototype__pb2.SpecsResponse.FromString,
                )
        self.GetProduct = channel.unary_unary(
                '/prototype.Specs/GetProduct',
                request_serializer=prototype__pb2.SpecsRequest.SerializeToString,
                response_deserializer=prototype__pb2.SpecsResponse.FromString,
                )


class SpecsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpecsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProducts,
                    request_deserializer=prototype__pb2.SpecsRequest.FromString,
                    response_serializer=prototype__pb2.SpecsResponse.SerializeToString,
            ),
            'AddProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProduct,
                    request_deserializer=prototype__pb2.SpecsRequest.FromString,
                    response_serializer=prototype__pb2.SpecsResponse.SerializeToString,
            ),
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=prototype__pb2.SpecsRequest.FromString,
                    response_serializer=prototype__pb2.SpecsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prototype.Specs', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Specs(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Specs/ListProducts',
            prototype__pb2.SpecsRequest.SerializeToString,
            prototype__pb2.SpecsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Specs/AddProduct',
            prototype__pb2.SpecsRequest.SerializeToString,
            prototype__pb2.SpecsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Specs/GetProduct',
            prototype__pb2.SpecsRequest.SerializeToString,
            prototype__pb2.SpecsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CartStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddProduct = channel.unary_unary(
                '/prototype.Cart/AddProduct',
                request_serializer=prototype__pb2.CartRequest.SerializeToString,
                response_deserializer=prototype__pb2.CartResponse.FromString,
                )
        self.CheckoutCart = channel.unary_unary(
                '/prototype.Cart/CheckoutCart',
                request_serializer=prototype__pb2.CartRequest.SerializeToString,
                response_deserializer=prototype__pb2.CartResponse.FromString,
                )
        self.ListProducts = channel.unary_unary(
                '/prototype.Cart/ListProducts',
                request_serializer=prototype__pb2.CartRequest.SerializeToString,
                response_deserializer=prototype__pb2.CartResponse.FromString,
                )


class CartServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckoutCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CartServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProduct,
                    request_deserializer=prototype__pb2.CartRequest.FromString,
                    response_serializer=prototype__pb2.CartResponse.SerializeToString,
            ),
            'CheckoutCart': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckoutCart,
                    request_deserializer=prototype__pb2.CartRequest.FromString,
                    response_serializer=prototype__pb2.CartResponse.SerializeToString,
            ),
            'ListProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListProducts,
                    request_deserializer=prototype__pb2.CartRequest.FromString,
                    response_serializer=prototype__pb2.CartResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prototype.Cart', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Cart(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Cart/AddProduct',
            prototype__pb2.CartRequest.SerializeToString,
            prototype__pb2.CartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckoutCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Cart/CheckoutCart',
            prototype__pb2.CartRequest.SerializeToString,
            prototype__pb2.CartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Cart/ListProducts',
            prototype__pb2.CartRequest.SerializeToString,
            prototype__pb2.CartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CheckoutStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddCart = channel.unary_unary(
                '/prototype.Checkout/AddCart',
                request_serializer=prototype__pb2.CheckoutRequest.SerializeToString,
                response_deserializer=prototype__pb2.CheckoutResponse.FromString,
                )
        self.ListCheckouts = channel.unary_unary(
                '/prototype.Checkout/ListCheckouts',
                request_serializer=prototype__pb2.CheckoutRequest.SerializeToString,
                response_deserializer=prototype__pb2.CheckoutResponse.FromString,
                )


class CheckoutServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddCart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCheckouts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CheckoutServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddCart': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCart,
                    request_deserializer=prototype__pb2.CheckoutRequest.FromString,
                    response_serializer=prototype__pb2.CheckoutResponse.SerializeToString,
            ),
            'ListCheckouts': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCheckouts,
                    request_deserializer=prototype__pb2.CheckoutRequest.FromString,
                    response_serializer=prototype__pb2.CheckoutResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prototype.Checkout', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Checkout(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddCart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Checkout/AddCart',
            prototype__pb2.CheckoutRequest.SerializeToString,
            prototype__pb2.CheckoutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCheckouts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prototype.Checkout/ListCheckouts',
            prototype__pb2.CheckoutRequest.SerializeToString,
            prototype__pb2.CheckoutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
