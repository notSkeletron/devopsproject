DevOps Engineer Showcase Project - Stage 1
Objective
Build a basic, production-style DevOps pipeline that provisions infrastructure, builds a Python app
into a binary, containers it, and deploys it to Kubernetes using GitLab CI/CD.
Technology Stack
- App: Python (Flask/FastAPI), HTML/JS
- Binaries: PyInstaller
- Containers: Docker
- CI/CD: GitLab CI
- Infrastructure: Terraform
- Cloud: GCP/GKE, AWS/EKS, or Azure/AKS
- Orchestration: Kubernetes
Phase 1: Application Setup
- Create a basic Python REST API (e.g., GET /api/hello)
- Create a minimal frontend (HTML/JS or Flask template)
- Set up local testing
- Add requirements.txt
Phase 2: Binary Packaging with PyInstaller
- Install and configure PyInstaller
- Build backend as a standalone executable
- Verify it runs without needing Python
- Document the build process
Phase 3: Dockerization
- Write Dockerfiles for backend and frontend
- Use multi-stage builds
- Test container locally
- Push images to GitLab Container Registry
Phase 4: Infrastructure as Code with Terraform
- Choose a cloud provider (GCP, AWS, Azure)
- Use Terraform to provision a K8s cluster
- Output kubeconfig or service account creds
- Validate cluster setup
Phase 5: Kubernetes Deployment
- Create Kubernetes manifests (Deployment, Service)
- Optional: Ingress controller
- Deploy via kubectl
- Verify external access
Phase 6: CI/CD with GitLab
- Set up .gitlab-ci.yml with build, docker, deploy stages
- Store secrets in GitLab CI variables
- Trigger on push to main
- Test full pipeline
Optional Enhancements
- Helm charts
- GitOps (ArgoCD, FluxCD)
- Monitoring (Prometheus, Grafana)
- Logging (Loki, ELK)
- HPA and advanced deployment strategies






-Created virtual environment (python3 -m venv venv)
-Run venv with "source venv/bin/activate"
-pip install pyinstaller fastapi uvicorn
-Created script app.py
-Made into a binary using pyinstaller (pyinstaller --onefile app.py)





--NEXT STEPS--
PHASE 3
install docker
package app binary into a simple image use "FROM scratch"
start the service as a docker container (don't run the binary localy, but on the docker container)

Had some issues runnig the image after building it and it was probably because of the way the app binary was build. To be checked again.
Image built succesfully.

-----
local host inside image to connect with localhost outside the image and port forward from the container to the local machine
First try port forward
With localhost(127.0.0.1) inside image the app was not working.
I used 0.0.0.0 as the host both in Dockerfile and the app.py and the app was working even if I was using the url localhost:8000/hello

--Jenkins CI--
run Jenkins from container to do the CI

running Jenking with docker-compose
next step : run the app from Jenkins