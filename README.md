
![Build and Test](https://github.com/ksdinesh-07/URL_Shorter/actions/workflows/build-test.yml/badge.svg)
![Security Scan](https://github.com/ksdinesh-07/URL_Shorter/actions/workflows/security-scan.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)

# 🔗 URL Shortener with GitHub Actions CI/CD

A complete URL shortening service with automated CI/CD pipeline using GitHub Actions.

## ✨ Features
- **🔗 URL Shortening**: Create short URLs with optional custom codes
- **📊 Analytics**: Track click statistics for each shortened URL
- **🚀 FastAPI**: High-performance REST API with automatic documentation
- **🐳 Docker**: Complete containerization for consistent deployments
- **⚡ CI/CD**: Automated testing and deployment with GitHub Actions
- **🔒 Security**: Regular vulnerability scanning and dependency checks
- **🧪 Testing**: Comprehensive test suite with 100% endpoint coverage

## 🛠️ Tech Stack
| Technology | Purpose |
|------------|---------|
| **FastAPI** | REST API framework |
| **Python 3.11** | Backend language |
| **Docker** | Containerization |
| **GitHub Actions** | CI/CD automation |
| **Pytest** | Testing framework |
| **Trivy** | Security scanning |
| **Uvicorn** | ASGI server |

## 🚀 Quick Start

### Local Development

# Clone repository
git clone https://github.com/ksdinesh-07/URL_Shorter.git
cd URL_Shorter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn src.app:app --reload
