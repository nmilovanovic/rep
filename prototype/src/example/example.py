import grpc
import prototype_pb2
import prototype_pb2_grpc


with grpc.insecure_channel('pictures:50000') as channel:
    stub = prototype_pb2_grpc.PicturesStub(channel)
    request = prototype_pb2.PicturesRequest(productid='image')
    response = stub.GetPictures(request)
    for resp in response:
        print(resp.content)
