import json
import datetime
from influxdb import InfluxDBClient
from http.server import BaseHTTPRequestHandler, HTTPServer

# https://github.com/flugel-it/k8s-metacontroller-operator
# https://github.com/shovanmaity/metacontroller-by-example

client = None

def getNumReplicas(stringSpans, time):
    time = 3600*int(time[0:2])+60*int(time[3:5])+int(time[6:8])
    splits = stringSpans.split('#')
    spans = list(map(lambda x: (3600*int(x[0][0:2])+60*int(x[0][3:5])+int(x[0][6:8]), 3600*int(x[1][0:2])+60*int(x[1][3:5])+int(x[1][6:8]), int(x[2])),list(map(lambda x: x.split('-'), splits))))
    for item in spans:
        if time >= item[0] and time <= item[1]:
            return item[2]
    return 1

def sync(parent, children):
    desired = []
    #num_replicas = int(parent['spec']['replicas'])
    num_replicas = getNumReplicas(parent['spec']['replicas'], datetime.datetime.now().strftime("%X"))
    json_body = [
        {
            "measurement": "replicas",
            "fields": {
                "desired": num_replicas,
                "current": len(children['Pod.v1'])
            }
        }
    ]
    client.write_points(json_body)

    for i in range(0,num_replicas):
        desired.append(
            {
                'apiVersion': 'v1',
                'kind': 'Pod',
                'metadata': {
                    'name': parent['metadata']['name'] + '-podnumber-' + str(i),
                    'namespace': parent['metadata']['namespace'],
                },
                'spec': {
                    'restartPolicy': 'OnFailure',
                    'containers': [
                        {
                            'name': 'acontainer',
                            'image': parent['spec']['image'],
                        }
                    ]
                }
            }
        )
    return {'status': {}, 'children': desired}


class Controller(BaseHTTPRequestHandler):
    def do_POST(self):
        # Serve the sync() function as a JSON webhook.
        self.headers
        observed = json.loads(self.rfile.read(int(self.headers.get('content-length'))))
        desired = sync(observed['parent'], observed['children'])

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(desired).encode())


if __name__ == '__main__':
    print("server starting...")
    client = InfluxDBClient('192.168.1.10', 8086, 'root', 'root', 'metricsdb')
    client.create_database('metricsdb')
    HTTPServer(('', 8080), Controller).serve_forever()