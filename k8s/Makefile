.PHONY: apply configmap reload

apply:
	kubectl apply -f nginx.yaml

configmap:
	kubectl create configmap html --from-file=../web/dist/ --dry-run -o yaml | kubectl apply -f-
	kubectl create configmap nginx --from-file=nginx/ --dry-run -o yaml | kubectl apply -f-

reload:
	for POD in `kubectl get pods -l app=nginx -o name | sed 's#^pod/##'`; do kubectl exec "$$POD" -- nginx -s reload ; done
