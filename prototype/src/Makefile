.PHONY : grpc
.PHONY : frontend-image
.PHONY : pictures-image
.PHONY : specs-image
.PHONY : cart-image
.PHONY : checkout-image
.PHONY : images
.PHONY : all
.PHONY : run

PUSH_IMAGES ?= 1

LABEL ?= v1

FRONTEND_IMAGE_LABEL ?= $(LABEL)
PICTURES_IMAGE_LABEL ?= $(LABEL)
SPECS_IMAGE_LABEL ?= $(LABEL)
CART_IMAGE_LABEL ?= $(LABEL)
CHECKOUT_IMAGE_LABEL ?= $(LABEL)

grpc: ./protos/prototype.proto
	@python3 -m grpc_tools.protoc -I./protos --python_out=./protos/ --grpc_python_out=./protos/ ./protos/prototype.proto
	@cp protos/prototype_pb2_grpc.py pictures/prototype_pb2_grpc.py
	@cp protos/prototype_pb2_grpc.py example/prototype_pb2_grpc.py
	@cp protos/prototype_pb2_grpc.py frontend/prototype_pb2_grpc.py
	@cp protos/prototype_pb2_grpc.py specs/prototype_pb2_grpc.py
	@cp protos/prototype_pb2_grpc.py cart/prototype_pb2_grpc.py
	@cp protos/prototype_pb2_grpc.py checkout/prototype_pb2_grpc.py
	@cp protos/prototype_pb2.py pictures/prototype_pb2.py
	@cp protos/prototype_pb2.py example/prototype_pb2.py
	@cp protos/prototype_pb2.py frontend/prototype_pb2.py
	@cp protos/prototype_pb2.py specs/prototype_pb2.py
	@cp protos/prototype_pb2.py cart/prototype_pb2.py
	@cp protos/prototype_pb2.py checkout/prototype_pb2.py

images: frontend-image pictures-image specs-image cart-image checkout-image

frontend-image:
	@echo "Building frontend-image"
	@pip-compile --output-file frontend/requirements.txt frontend/requirements.in
	@docker image build -t milovanovicsnikola/frontend:$(FRONTEND_IMAGE_LABEL) frontend/
ifneq ($(PUSH_IMAGES), 0)
	@echo "Pushing frontend-image with tag $(FRONTEND_IMAGE_LABEL)"
	@docker image push milovanovicsnikola/frontend:$(FRONTEND_IMAGE_LABEL)
endif

pictures-image:
	@echo "Building pictures-image with tag $(PICTURES_IMAGE_LABEL)"
	@pip-compile --output-file pictures/requirements.txt pictures/requirements.in
	@docker image build -t milovanovicsnikola/pictures:$(PICTURES_IMAGE_LABEL) pictures/
ifneq ($(PUSH_IMAGES), 0)
	@echo "Pushing pictures-image with tag $(PICTURES_IMAGE_LABEL)"
	@docker image push milovanovicsnikola/pictures:$(PICTURES_IMAGE_LABEL)
endif

specs-image:
	@echo "Building specs-image with tag $(SPECS_IMAGE_LABEL)"
	@pip-compile --output-file specs/requirements.txt specs/requirements.in
	@docker image build -t milovanovicsnikola/specs:$(SPECS_IMAGE_LABEL) specs/
ifneq ($(PUSH_IMAGES), 0)
	@echo "Pushing specs-image with tag $(SPECS_IMAGE_LABEL)"
	@docker image push milovanovicsnikola/specs:$(SPECS_IMAGE_LABEL)
endif

cart-image:
	@echo "Building cart-image with tag $(CART_IMAGE_LABEL)"
	@pip-compile --output-file cart/requirements.txt cart/requirements.in
	@docker image build -t milovanovicsnikola/cart:$(CART_IMAGE_LABEL) cart/
ifneq ($(PUSH_IMAGES), 0)
	@echo "Pushing cart-image with tag $(CART_IMAGE_LABEL)"
	@docker image push milovanovicsnikola/cart:$(CART_IMAGE_LABEL)
endif

checkout-image:
	@echo "Building checkout-image with tag $(CHECKOUT_IMAGE_LABEL)"
	@pip-compile --output-file checkout/requirements.txt checkout/requirements.in
	@docker image build -t milovanovicsnikola/checkout:$(CART_IMAGE_LABEL) checkout/
ifneq ($(PUSH_IMAGES), 0)
	@echo "Pushing checkout-image with tag $(CART_IMAGE_LABEL)"
	@docker image push milovanovicsnikola/checkout:$(CART_IMAGE_LABEL)
endif

all: grpc images# k8s-yaml
	
k8s-yaml:
	cd ../kubernetes-manifests && kompose convert -f ../compose-manifests/docker-compose.yaml && cd -

KUBERNETES_YAML_DIR ?= ../kubernetes-manifests
ISTIO_YAML_DIR ?= ../istio-manifests

run:
	# first manually edit yaml files, then run this recipe
	$(foreach file, $(wildcard $(KUBERNETES_YAML_DIR)/*), sudo microk8s kubectl apply -f $(file);)
	#$(foreach file, $(wildcard $(ISTIO_YAML_DIR)/*), sudo microk8s kubectl apply -f $(file);)
	#cd ../kubernetes-manifests && sudo microk8s kubectl apply -f *.yaml && cd ../istio-manifests && sudo microk8s kubectl apply -f *.yaml

clean:
	rm frontend/requirements.txt
	rm picures/requirements.txt
	rm specs/requirements.txt
	rm cart/requirements.txt
	rm checkout/requirements.txt