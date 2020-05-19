import json
import datetime
from influxdb import InfluxDBClient
import http.client
from http.server import BaseHTTPRequestHandler, HTTPServer

# https://github.com/flugel-it/k8s-metacontroller-operator
# https://github.com/shovanmaity/metacontroller-by-example

client = None


def get_num_replicas(mode, string_spans, time):
    if mode == 'day':
        # format: "00:00:00-01:05:00-1#01:05:00-17:05:00-2#17:05:00-23:59:59-3"
        time = time.strftime("%X")
        time = 3600 * int(time[0:2]) + 60 * int(time[3:5]) + int(time[6:8])
        splits = string_spans.split('#')
        spans = list(map(lambda x: (3600 * int(x[0][0:2]) + 60 * int(x[0][3:5]) + int(x[0][6:8]),
                                    3600 * int(x[1][0:2]) + 60 * int(x[1][3:5]) + int(x[1][6:8]), int(x[2])),
                         list(map(lambda x: x.split('-'), splits))))
        for item in spans:
            if item[0] <= time <= item[1]:
                return item[2]
        return 1
    elif mode == 'week':
        # format: "1-2-1#3-4-2#5-7-3"
        splits = string_spans.split('#')
        spans = list(map(lambda x: (int(x[0]), int(x[1]), int(x[2])), list(map(lambda x: x.split('-'), splits))))
        time = int(time.strftime("%w"))
        if time == 0:
            time = 7
        for item in spans:
            if item[0] <= time <= item[1]:
                return item[2]
    elif mode == 'month':
        # format: "1-10-1#11-15-15#16-31-10"
        splits = string_spans.split('#')
        spans = list(map(lambda x: (int(x[0]), int(x[1]), int(x[2])), list(map(lambda x: x.split('-'), splits))))
        time = int(time.strftime("%d"))
        for item in spans:
            if item[0] <= time <= item[1]:
                return item[2]
    else:
        return 1

def estimate_num_replicas(parent, children):
    if len(children) == 0:
        return 1
    else:
        connection = http.client.HTTPConnection('192.168.1.6:8001')
        connection.request('GET', '/apis/metrics.k8s.io/v1beta1/pods')
        response = connection.getresponse()
        items = json.loads(response.read().decode())['items']
        pods = [(x['metadata']['name'], x['containers'][0]) for x in items]
        pod_resources = {}
        for pod in pods:
            pod_resources[pod[0]] = 0
            container = pod[1]
            val = 0
            if not container['usage']['cpu'][:-1] == '':
                val += int(container['usage']['cpu'][:-1])
            pod_resources[pod[0]] += val
        # pod_resources za svaki pod u sistemu (pretpostavlja da svaki pod ima samo jedan kontejner
        # sto je i slucaj sa "nasim" replikama) sadrzi kolicinu CPU resursa koje taj pod zauzima (0-1000)
        pod_names = children.keys()
        # pod_names sadrzi imena svake od replika za parenta sa kojim se trenutno radi
        sum = 0
        for pod_name in pod_names:
            sum += pod_resources.get(pod_name, 0)

        if sum > 900*len(pod_names):
            return len(pod_names)+1
        elif sum < 400*len(pod_names):
            return len(pod_names)/2
        else:
            return len(pod_names)

def sync(parent, children):
    desired = []
    # num_replicas = int(parent['spec']['replicas'])
    if not parent['spec']['mode'] == 'auto':
        num_replicas = get_num_replicas(parent['spec']['mode'], parent['spec']['replicas'], datetime.datetime.now())
    else:
        num_replicas = estimate_num_replicas(parent, children['Pod.v1'])
    json_body = [
        {
            "measurement": "replicas"+"-"+parent['metadata']['name'],
            "fields": {
                "desired": num_replicas,
                "current": len(children['Pod.v1'])
            }
        }
    ]
    if client is not None:
        client.write_points(json_body)

    for i in range(0, num_replicas):
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
    #client = InfluxDBClient('192.168.1.10', 8086, 'root', 'root', 'metricsdb').create_database('metricsdb')
    HTTPServer(('', 8080), Controller).serve_forever()
