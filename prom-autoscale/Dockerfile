FROM python:alpine3.7
COPY ./rest.py /app/rest.py
WORKDIR /app
RUN pip install flask
RUN pip install prometheus_client
CMD python ./rest.py
