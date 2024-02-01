```bash

brew install minikube
minikube start --memory=8096 --cpus=4

brew install helm

helm repo add community-charts https://community-charts.github.io/helm-charts
helm install my-mlflow community-charts/mlflow --version 0.7.19

```

```bash
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=mlflow,app.kubernetes.io/instance=my-mlflow" -o jsonpath="{.items[0].metadata.name}")

export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")

kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT

Now, open your web browser and enter the address http://127.0.0.1:8080. 
```


### install kubeflow

curl -O https://raw.githubusercontent.com/kubeflow/kubeflow/v0.2-branch/bootstrap/bootstrapper.yaml
kubectl create -f bootstrapper.yaml
 kubectl get ns
 kubectl -n kubeflow get svc



 ### Install Kubeflow on AWS

```bash
export KUBEFLOW_RELEASE_VERSION=v1.7.0
export AWS_RELEASE_VERSION=v1.7.0-aws-b1.0.3
git clone https://github.com/awslabs/kubeflow-manifests.git && cd kubeflow-manifests
git checkout ${AWS_RELEASE_VERSION}
git clone --branch ${KUBEFLOW_RELEASE_VERSION} https://github.com/kubeflow/manifests.git upstream
```

https://github.com/awslabs/kubeflow-manifests/issues/250


### Install metaflow with Terraform on AWS EKS

Install instructions

https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops


https://docs.metaflow.org/getting-started/infrastructure

https://outerbounds.com/engineering/deployment/aws-k8s/deployment/


### display the pods instalation process 
watch kubectl get pods -n argocd

Once all the argo cd pods have been installed

kubectl port-forward svc/argocd-server -n argocd 8080:443


### Install Airflow on Kubernetes
https://medium.com/@kerrache.massipssa/deploy-apache-airflow-with-kubernetes-8f764a4cc984

get credentials
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
argocd admin initial-password -n argocd
```

initialize login via cli to use argocd cli commands
```bash
kubectl port-forward svc/airflow-webserver 2000:8080 --namespace airflow
argocd login 127.0.0.1:8000
# enter username  and password
```

```bash
## test the login cli method by creating an application
argocd app create webapp-kustom-prod \
--repo https://github.com/devopsjourney1/argo-examples.git \
--path kustom-webapp/overlays/prod --dest-server https://kubernetes.default.svc \
--dest-namespace prod
```

### Install MLFlow on Kubernetes
https://medium.com/@heisash24/-84bd8496f360

**Start the MLFlow server**

```bash
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=mlflow,app.kubernetes.io/instance=my-mlflow" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
kubectl --namespace default port-forward $POD_NAME 9000:$CONTAINER_PORT
```


### Instlal ArgoCD on Kubernetes
https://argo-cd.readthedocs.io/en/stable/getting_started/


**Start the ArgoCd web service**

```bash
kubectl port-forward svc/argocd-server -n argocd 8000:443
```