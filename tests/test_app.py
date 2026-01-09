from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "URL Shortener API" in response.json()["message"]

def test_health_check():
    """Test health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "version" in response.json()

def test_shorten_url():
    """Test URL shortening"""
    response = client.post("/shorten", params={"url": "https://google.com"})
    assert response.status_code == 200
    data = response.json()
    assert "short_url" in data
    assert "short_code" in data
    assert "original_url" in data
    assert data["original_url"] == "https://google.com"

def test_shorten_url_without_protocol():
    """Test URL without protocol (should auto-add https://)"""
    response = client.post("/shorten", params={"url": "example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["original_url"] == "https://example.com"

def test_duplicate_custom_code():
    """Test duplicate custom code error"""
    # First request
    response1 = client.post("/shorten", params={"url": "https://github.com", "custom_code": "gh"})
    assert response1.status_code == 200
    
    # Second request with same custom code should fail
    response2 = client.post("/shorten", params={"url": "https://gitlab.com", "custom_code": "gh"})
    assert response2.status_code == 400
    assert "already exists" in response2.json()["detail"]

def test_redirect_url():
    """Test URL redirection"""
    # Shorten a URL first
    shorten_response = client.post("/shorten", params={"url": "https://github.com"})
    short_code = shorten_response.json()["short_code"]
    
    # Try to redirect
    response = client.get(f"/{short_code}", follow_redirects=False)
    assert response.status_code in [307, 302]  # Redirect status

def test_nonexistent_url():
    """Test accessing non-existent short code"""
    response = client.get("/nonexistent")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_stats():
    """Test URL statistics"""
    # Shorten a URL
    shorten_response = client.post("/shorten", params={"url": "https://python.org"})
    short_code = shorten_response.json()["short_code"]
    
    # Access it once to increment clicks
    client.get(f"/{short_code}", follow_redirects=False)
    
    # Check stats
    response = client.get(f"/stats/{short_code}")
    assert response.status_code == 200
    data = response.json()
    assert "original_url" in data
    assert "clicks" in data
    assert data["clicks"] == 1  # Should be 1 after one access
