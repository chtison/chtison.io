.PHONY: create list set-k8s-creds

NAME := infra

create:
	gcloud deployment-manager deployments create --config main.yaml $(NAME)

list:
	gcloud deployment-manager deployments list --filter 'name = $(NAME)'

set-k8s-creds:
	gcloud container clusters get-credentials $(NAME)-cluster
