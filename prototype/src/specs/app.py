import grpc
import prototype_pb2_grpc
import prototype_pb2
import base64
from concurrent import futures
from sqlitedict import SqliteDict
import json
import uuid

mydict = None


class SpecsService(prototype_pb2_grpc.SpecsServicer):

    def ListProducts(self, request, context):
        print('Handling ListProducts method')
        response_dict = dict()
        for key, value in mydict.iteritems():
            response_dict[key] = json.loads(value)
        response_json = json.dumps(response_dict, indent=4)
        print(response_json)
        response = prototype_pb2.SpecsResponse(content=response_json)
        return response

    def AddProduct(self, request, context):
        product_json = request.content
        product_dict = json.loads(product_json)
        print('Handling AddProduct method: ' + product_dict['productid'])
        mydict[product_dict['productid']] = product_json
        response = prototype_pb2.SpecsResponse(content='')
        return response

    def GetProduct(self, request, context):
        print('Handling GetProduct method: ' + request.content)
        productid = request.content
        product_dict = mydict[productid]
        response = prototype_pb2.SpecsResponse(content=product_dict)
        return response
        

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prototype_pb2_grpc.add_SpecsServicer_to_server(SpecsService(), server)
    server.add_insecure_port('0.0.0.0:50000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    mydict = SqliteDict('./specs.sqlite', autocommit=True)
    serve()
    mydict.close()