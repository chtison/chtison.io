.PHONY: all

all:
	$(MAKE) -C hugo/ build
	$(MAKE) -C k8s/ bucket
