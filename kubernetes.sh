minikube start
eval $(minikube docker-env)
docker build -t fastapi-app:latest .
kubectl apply -f kubernetes-conf.yaml
kubectl rollout restart deployment fastapi-deployment
firefox "$(minikube service fastapi-service --url)/docs"
