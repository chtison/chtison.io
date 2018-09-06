.PHONY: configmap

apply:
	kubectl apply -f nginx.yaml

configmap:
	kubectl create configmap html --from-file=html --dry-run -o yaml | kubectl apply -f-
