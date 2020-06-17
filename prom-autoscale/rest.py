import flask
from flask import request, jsonify
from prometheus_client import Counter, start_http_server
from multiprocessing.pool import ThreadPool

#https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#creating-a-basic-flask-application

app = flask.Flask(__name__)
app.config["DEBUG"] = False

REQUESTS = Counter('http_requests_total', 'Total number of requests to this API.')

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    REQUESTS.inc()
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    REQUESTS.inc()
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    REQUESTS.inc()
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

start_http_server(8000)
app.run('0.0.0.0', port=8001)
