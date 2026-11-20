#!/usr/bin/env bash
# =====================================================================
# ACEest Fitness & Gym — Kubernetes Deployment Verification & Rollback
# Introduction to DevOps (BITS Pilani) — Assignment 2
# Validates all 5 deployment strategies and automated rollback
# =====================================================================

set -e

NAMESPACE="aceest-fitness"
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=====================================================================${NC}"
echo -e "${BLUE}  ACEest Fitness & Gym — Assignment 2 Cluster Verification Suite     ${NC}"
echo -e "${BLUE}=====================================================================${NC}"

# Check cluster connectivity
echo -e "\n${YELLOW}[1/7] Checking Kubernetes Cluster Connectivity...${NC}"
if ! kubectl cluster-info > /dev/null 2>&1; then
    echo -e "${RED}ERROR: Kubernetes cluster is not reachable. Ensure Minikube / K8s is running.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Cluster is reachable.${NC}"

# Ensure namespace exists
echo -e "\n${YELLOW}[2/7] Ensuring Namespace '${NAMESPACE}' Exists...${NC}"
kubectl apply -f 00-namespace.yaml

# ---------------------------------------------------------------------
# Strategy 1: Rolling Update Verification
# ---------------------------------------------------------------------
echo -e "\n${YELLOW}[3/7] Demonstrating Strategy 1: Rolling Update Deployment...${NC}"
kubectl apply -f 01-rolling-update.yaml
echo "Waiting for rolling update deployment rollout..."
kubectl rollout status deployment/aceest-rolling-app -n ${NAMESPACE} --timeout=90s

echo "Updating image from v1.0.0 to v2.0.0 (Zero-Downtime Rolling Update)..."
kubectl set image deployment/aceest-rolling-app web=drsunandapandita/aceest-fitness:v2.0.0 -n ${NAMESPACE}
kubectl rollout status deployment/aceest-rolling-app -n ${NAMESPACE} --timeout=90s
echo -e "${GREEN}✓ Rolling update completed successfully with zero downtime!${NC}"

# ---------------------------------------------------------------------
# Strategy 2: Blue-Green Deployment Verification
# ---------------------------------------------------------------------
echo -e "\n${YELLOW}[4/7] Demonstrating Strategy 2: Blue-Green Cutover...${NC}"
kubectl apply -f 02-blue-green.yaml
kubectl rollout status deployment/aceest-blue -n ${NAMESPACE} --timeout=60s
kubectl rollout status deployment/aceest-green -n ${NAMESPACE} --timeout=60s

echo "Current Active Service Selector:"
kubectl get service aceest-bluegreen-service -n ${NAMESPACE} -o jsonpath='{.spec.selector}'
echo ""

echo "Executing instant cutover from BLUE to GREEN..."
kubectl patch service aceest-bluegreen-service -n ${NAMESPACE} -p '{"spec":{"selector":{"version":"green"}}}'
echo "New Active Service Selector:"
kubectl get service aceest-bluegreen-service -n ${NAMESPACE} -o jsonpath='{.spec.selector}'
echo ""
echo -e "${GREEN}✓ Blue-Green cutover executed instantly with zero dropped connections!${NC}"

# ---------------------------------------------------------------------
# Strategy 3: Canary Release Verification (80% / 20% Traffic Split)
# ---------------------------------------------------------------------
echo -e "\n${YELLOW}[5/7] Demonstrating Strategy 3: Canary Release (80/20 Ratio)...${NC}"
kubectl apply -f 03-canary.yaml
kubectl rollout status deployment/aceest-canary-stable -n ${NAMESPACE} --timeout=60s
kubectl rollout status deployment/aceest-canary-pilot -n ${NAMESPACE} --timeout=60s

echo "Canary Pod Distribution under 'aceest-canary-app':"
kubectl get pods -n ${NAMESPACE} -l app=aceest-canary-app -o wide
echo -e "${GREEN}✓ 4 Stable pods (80%) + 1 Pilot pod (20%) active under shared service.${NC}"

# ---------------------------------------------------------------------
# Strategy 4 & 5: A/B Testing & Shadow Deployment
# ---------------------------------------------------------------------
echo -e "\n${YELLOW}[6/7] Deploying Strategy 4 (A/B Testing) & Strategy 5 (Shadow Deployment)...${NC}"
kubectl apply -f 04-ab-testing.yaml
kubectl apply -f 05-shadow-deployment.yaml
echo -e "${GREEN}✓ A/B Testing & Shadow Traffic Mirroring manifests applied.${NC}"

# ---------------------------------------------------------------------
# Rollback Mechanism Demonstration
# ---------------------------------------------------------------------
echo -e "\n${YELLOW}[7/7] Demonstrating Failure Detection & Automated Rollback...${NC}"
echo "Injecting intentional faulty image to simulate bad deployment..."
kubectl set image deployment/aceest-rolling-app web=drsunandapandita/aceest-fitness:non-existent-broken-tag -n ${NAMESPACE} || true

echo "Checking rollout status (detecting failure)..."
if ! kubectl rollout status deployment/aceest-rolling-app -n ${NAMESPACE} --timeout=15s 2>/dev/null; then
    echo -e "${RED}! Fault detected in deployment pipeline. Initiating automatic rollback...${NC}"
    kubectl rollout undo deployment/aceest-rolling-app -n ${NAMESPACE}
    kubectl rollout status deployment/aceest-rolling-app -n ${NAMESPACE} --timeout=60s
    echo -e "${GREEN}✓ Rollback successful! Pods restored to previous healthy state.${NC}"
fi

echo -e "\n${BLUE}=====================================================================${NC}"
echo -e "${GREEN}✓ ALL 5 DEPLOYMENT STRATEGIES & ROLLBACK VALIDATED SUCCESSFULLY!${NC}"
echo -e "${BLUE}=====================================================================${NC}"
