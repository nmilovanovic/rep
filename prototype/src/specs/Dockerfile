FROM python:latest
COPY ./app.py /app/app.py
COPY ./prototype_pb2_grpc.py /app/prototype_pb2_grpc.py
COPY ./prototype_pb2.py /app/prototype_pb2.py
COPY requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /app
EXPOSE 50000
CMD python3 ./app.py