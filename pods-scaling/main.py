import os
import subprocess
from kubernetes import client, config

# adding envs

KUBE_CONFIG = "/root/.kube/config"

config.load_config(config_file=KUBE_CONFIG)

# define potential deployment sets

deployments = ["nginx-test"]
current_namespace = "hood-production"

api_instance = client.AppsV1Api()


# create a function which takes workloads to scale down to 50%
def scale_down(workloads, namespace):
    for deployment in workloads:
        deploy_read = api_instance.read_namespaced_deployment(namespace=namespace, name=deployment)
        current_replica_count = int(deploy_read.spec.replicas)
        print(f"current-replica {current_replica_count}")
        # to scale to 50% of current replica
        calculate_scaling_down = int(current_replica_count // 2)
        # scaling down
        print(f"new replica is {calculate_scaling_down}")
        if calculate_scaling_down <= 2:
            print(f"{calculate_scaling_down} is too low for scaling down")
            break
        new_replica_count = calculate_scaling_down
        body = client.V1Scale(spec=client.V1ScaleSpec(replicas=new_replica_count))
        updated_deployment = api_instance.patch_namespaced_deployment_scale(namespace=namespace, name=deployment,
                                                                            body=body)
        print(f"Deployment {deployment} has been scaled down to {new_replica_count} replicas")


# scale down

scale_down(workloads=deployments, namespace=current_namespace)