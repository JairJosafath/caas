"""
flask app to interact with k8s cluster
"""
from flask import Flask, jsonify
from kubernetes import client, config

config.load_incluster_config()
v1 = client.CoreV1Api()
ret = v1.list_namespace(watch=False)
print(f"""List of namespaces in the cluster:
{ret.to_dict()}
""")

app = Flask(__name__)


@app.route('/pods')
def get_pods():
    """
    Get all pods in the cluster
    """
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    return jsonify(ret.to_dict())

@app.route('/namespaces')
def get_namespaces():
    """
    Get all namespaces in the cluster
    """
    v1 = client.CoreV1Api()
    ret = v1.list_namespace(watch=False)
    return jsonify(ret.to_dict())

if __name__ == '__main__':
    app.run()