# Variables
DOCKER_IMAGE = grpc-service
DOCKER_TAG = latest
PORT = 50051
CONTAINER_NAME = grpc-service

# Get the latest commit SHA
GIT_COMMIT_SHA = $(shell git rev-parse --short HEAD)

# Build the Docker Image
build:
	docker build -t $(DOCKER_IMAGE):$(GIT_COMMIT_SHA) -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run the docker container
run:
	docker run -d -p $(PORT):$(PORT) --name $(CONTAINER_NAME) --rm $(DOCKER_IMAGE):$(DOCKER_TAG)


# Push the docker image with both tags
push:
	docker push $(DOCKER_IMAGE):$(GIT_COMMIT_SHA)
	docker push $(DOCKER_IMAGE)$(DOCKER_TAG)

# Stop and remove the running container (if named)
stop:
	docker stop $(CONTAINER_NAME) || true

# Clean up unused Docker images
clean:
	docker system prune

# Rebuild, tag, and run
rebuild: stop clean build run