import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# https://github.com/flugel-it/k8s-metacontroller-operator
# https://github.com/shovanmaity/metacontroller-by-example

def sync(parent, children):

    desired = []
    num_replicas = int(parent['spec']['replicas'])
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
    HTTPServer(('', 8080), Controller).serve_forever()