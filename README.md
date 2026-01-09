
A simple URL shortener service with automated CI/CD pipeline using GitHub Actions.

## 🚀 Features
- URL shortening with custom codes
- Click statistics
- REST API with FastAPI
- Docker containerization
- Automated testing and security scanning

## 🛠️ Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn src.app:app --reload

# Run tests
pytest tests/

# Build and run with Docker
docker build -t url-shortener .
docker run -p 8000:8000 url-shortener