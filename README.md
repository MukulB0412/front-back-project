
# 🚀 Fullstack Dockerized App (React + FastAPI)

This is a fullstack web application built using **React (Vite + Tailwind CSS)** for the frontend and **FastAPI** for the backend. The entire app is containerized with Docker and deployed using Docker Compose on a cloud VM (e.g., AWS EC2 or DigitalOcean Droplet).

---

## 🗂️ Project Structure

```
📁 NEW-PROJECT
├── backend
│   ├── main.py
│   ├── requirements.txt
│   └── .env
├── frontend
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── Dockerfile.backend
├── Dockerfile.frontend
└── docker-compose.yml
```

---

## 🐳 Docker Images

Images are built and pushed to [Docker Hub](https://hub.docker.com/):

- `mukul0412/frontend-image:latest`
- `mukul0412/backend-image:latest`

---

## ⚙️ How to Run (Locally with Docker Compose)

```bash
docker-compose up --build
```

Visit:

- Frontend: [http://localhost](http://localhost)
- Backend API: [http://localhost:8000](http://localhost:8000)

---

## 🚀 Deployment on Cloud (e.g., AWS EC2 / DigitalOcean)

### 1. SSH into your VM

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

### 2. Install Docker & Docker Compose

```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
```

### 3. Create `docker-compose.yml`

```yaml
version: "3.8"

services:
  backend:
    image: mukul0412/backend-image:latest
    ports:
      - "8000:8000"
    networks:
      - appnet

  frontend:
    image: mukul0412/frontend-image:latest
    ports:
      - "80:80"
    networks:
      - appnet

networks:
  appnet:
```

### 4. Start the app

```bash
docker-compose up -d
```

### 5. Access the App

- Frontend: `http://your-server-ip`
- Backend API: `http://your-server-ip:8000`

---

## 🔄 CI/CD with GitHub Actions

This project uses GitHub Actions to automatically build and push images to Docker Hub on every push to the `main` branch.

```yaml
name: Build and Push Docker Images

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push backend
        uses: docker/build-push-action@v5
        with:
          context: .
          file: Dockerfile.backend
          push: true
          tags: mukul0412/backend-image:latest

      - name: Build and push frontend
        uses: docker/build-push-action@v5
        with:
          context: .
          file: Dockerfile.frontend
          push: true
          tags: mukul0412/frontend-image:latest
```

---

## 📦 Technologies Used

- **Frontend:** React, Vite, Tailwind CSS
- **Backend:** FastAPI (Python 3.11)
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Cloud:** AWS EC2 / DigitalOcean Droplet

---
