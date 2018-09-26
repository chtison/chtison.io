.PHONY: apply bucket configmap reload

apply:
	kubectl apply -f nginx.yaml

bucket:
	gsutil -m rsync -d -r ../web/dist gs://chtison

configmap:
	kubectl create configmap nginx --from-file=nginx/ --dry-run -o yaml | kubectl apply -f-

reload:
	for POD in `kubectl get pods -l app=nginx -o name | sed 's#^pod/##'`; do kubectl exec "$$POD" -- nginx -s reload ; done
