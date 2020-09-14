from kubernetes import client, config
import time
import http
import json

DEPLOYMENT_NAME = "rest"
DELAY = 5


# microk8s config > ~/.kube/config

def create_deployment_object():
    # Configure Pod template container
    container = client.V1Container(
        name="nginx",
        image="nginx:1.15.4",
        ports=[client.V1ContainerPort(container_port=80)],
        resources=client.V1ResourceRequirements(
            requests={"cpu": "100m", "memory": "200Mi"},
            limits={"cpu": "500m", "memory": "500Mi"}
        )
    )
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]))
    # Create the specification of deployment
    spec = client.V1DeploymentSpec(
        replicas=3,
        template=template,
        selector={'matchLabels': {'app': 'nginx'}})
    # Instantiate the deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=DEPLOYMENT_NAME),
        spec=spec)

    return deployment


def create_deployment(api_instance, deployment):
    # Create deployment
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def update_deployment(api_instance, deployment):
    # Update container image
    # deployment.spec.template.spec.containers[0].image = "nginx:1.16.0"
    deployment.spec.replicas = 1
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=deployment)
    print("Deployment updated. status='%s'" % str(api_response.status))


def delete_deployment(api_instance):
    # Delete deployment
    api_response = api_instance.delete_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


'''
Ova funkcija simulira deployment cpu usage.
'''
def get_deployment_cpu_usage(deployment_name):
    deployment = client.AppsV1Api().read_namespaced_deployment(deployment_name, "default", pretty=True)
    labels = deployment.spec.template.metadata.labels
    api_response_pods = client.CoreV1Api().list_pod_for_all_namespaces(label_selector=[x for x in labels.keys()][0])
    connection = http.client.HTTPConnection('127.0.0.1:8001')
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
    pod_names = [x.metadata.name for x in api_response_pods.items]
    # pod_names sadrzi imena svake od replika za parenta sa kojim se trenutno radi
    sum = 0
    for pod_name in pod_names:
        sum += pod_resources.get(pod_name, 0)

    return sum / float(10e6 * len(pod_names))


def get_deployment_replicas(deployment_name):
    deployment = client.AppsV1Api().read_namespaced_deployment(deployment_name, "default", pretty=True)
    return deployment.spec.replicas


def update_deployment_replicas(deployment_name, replicas):
    deployment = client.AppsV1Api().read_namespaced_deployment(deployment_name, "default", pretty=True)
    deployment.spec.replicas = replicas
    api_response = client.AppsV1Api().patch_namespaced_deployment(name=deployment_name, namespace="default",
                                                                  body=deployment)


def calculate_deployment_replicas(cpu_usage, replicas):
    if cpu_usage > 0.9:
        return replicas + 1
    elif cpu_usage < 0.25:
        return max(1, int(replicas * 0.35))
    else:
        return replicas


def main():
    while True:
        usage = get_deployment_cpu_usage(DEPLOYMENT_NAME)
        print("Usage ", usage)
        replicas_current = get_deployment_replicas(DEPLOYMENT_NAME)
        print("Replicas current ", replicas_current)
        replicas_desired = calculate_deployment_replicas(usage, replicas_current)
        print("Replicas desired ", replicas_desired)
        update_deployment_replicas(DEPLOYMENT_NAME, replicas_desired)
        time.sleep(DELAY)


if __name__ == '__main__':
    main()
 
