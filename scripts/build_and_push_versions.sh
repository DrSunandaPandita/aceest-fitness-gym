#!/usr/bin/env bash
# =====================================================================
# Build and Push All Multi-Version Images to Docker Hub
# ACEest Fitness & Gym (DevOps Assignment 2)
# =====================================================================

set -e

IMAGE_REPO="drsunandapandita/aceest-fitness"
VERSIONS=("v1.0.0" "v2.0.0" "v3.0.0")

echo "====================================================================="
echo " Building Multi-Version Docker Images for ${IMAGE_REPO}"
echo "====================================================================="

for VER in "${VERSIONS[@]}"; do
    echo -e "\n--> Building version ${VER}..."
    docker build \
        --build-arg APP_VERSION="${VER#v}" \
        -t "${IMAGE_REPO}:${VER}" .
done

# Tag latest with v3.0.0
docker tag "${IMAGE_REPO}:v3.0.0" "${IMAGE_REPO}:latest"

echo -e "\n====================================================================="
echo " Successfully built images:"
docker images | grep "${IMAGE_REPO}"
echo "====================================================================="

echo -e "\nTo push these images to Docker Hub, run:"
echo "  docker login"
echo "  docker push ${IMAGE_REPO} --all-tags"
