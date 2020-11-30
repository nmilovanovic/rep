import grpc
import prototype_pb2_grpc
import prototype_pb2
import base64
from concurrent import futures
from sqlitedict import SqliteDict
import uuid
import json

mydict = None


class CheckoutService(prototype_pb2_grpc.CheckoutServicer):

    def AddCart(self, request, context):
        print('Handling AddCart method: ' + request.userid)
        print(request.content)
        products_dict = json.loads(request.content)
        products_dict['userid'] = request.userid
        uid = uuid.uuid4().hex
        mydict[uid] = json.dumps(products_dict)
        response = prototype_pb2.CheckoutRequest(content='')
        return response

    def ListCheckouts(self, request, context):
        print('Handling ListCheckouts method: ')
        response_dict = dict()
        for key, value in mydict.iteritems():
            response_dict[key] = json.loads(value)
        response = prototype_pb2.CheckoutResponse(content=json.dumps(response_dict))
        print(json.dumps(response_dict, indent=4))
        return response

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prototype_pb2_grpc.add_CheckoutServicer_to_server(CheckoutService(), server)
    server.add_insecure_port('0.0.0.0:50000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    mydict = SqliteDict('./checkout.sqlite', autocommit=True)
    serve()
    mydict.close()