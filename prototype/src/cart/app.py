import grpc
import prototype_pb2_grpc
import prototype_pb2
import base64
from concurrent import futures
from sqlitedict import SqliteDict
import uuid
import json

mydict = None


class CartService(prototype_pb2_grpc.CartServicer):

    def AddProduct(self, request, context):
        print('Handling AddProduct method: ' + request.productid + ' ' + request.userid)
        productid = request.productid
        userid = request.userid
        if userid in mydict:
            d = json.loads(mydict[userid])
            if productid not in d['list']:
                d['list'].append(productid)
                mydict[userid] = json.dumps(d)
        else:
            d = {'list' : [ productid ]}
            mydict[userid] = json.dumps(d)
        response = prototype_pb2.CartResponse(content='')
        return response

    def CheckoutCart(self, request, context):
        print('Handling CheckoutCart method: ' + request.userid)
        # call checkout service
        temp = prototype_pb2.CartResponse(content=mydict[request.userid])
        del mydict[request.userid]
        return temp

    def ListProducts(self, request, context):
        print('Handling ListProducts method: ' + request.userid)
        if not request.userid in mydict:
            return prototype_pb2.PictureResponse(content='{"list":[]}'.encode('ascii'))
        return prototype_pb2.PictureResponse(content=mydict[request.userid].encode('ascii'))
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prototype_pb2_grpc.add_CartServicer_to_server(CartService(), server)
    server.add_insecure_port('0.0.0.0:50000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    mydict = SqliteDict('./cart.sqlite', autocommit=True)
    serve()
    mydict.close()