import grpc
import prototype_pb2_grpc
import prototype_pb2
import base64
from concurrent import futures
from sqlitedict import SqliteDict
import uuid

mydict = None


class PictureService(prototype_pb2_grpc.PicturesServicer):

    def GetPicture(self, request, context):
        print('Handling GetPicture method: ' + request.productid)
        image_bytes = mydict[request.productid]
        if image_bytes == None:
            with open("images/image.jpg", "rb") as image_file:
                image_bytes = image_file.read()
        response = prototype_pb2.PictureResponse(content=image_bytes)
        return response

    def AddPicture(self, request, context):
        print('Handling AddPicture method: ' + request.productid)
        image_bytes = request.content
        product_id = request.productid
        mydict[product_id] = image_bytes
        return prototype_pb2.PictureResponse(content=b'')
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prototype_pb2_grpc.add_PicturesServicer_to_server(PictureService(), server)
    server.add_insecure_port('0.0.0.0:50000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    mydict = SqliteDict('./pictures.sqlite', autocommit=True)
    serve()
    mydict.close()