from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import hashlib

app = FastAPI(title="URL Shortener API", version="1.0.0")

url_database = {}

def generate_short_code(url: str) -> str:
    """Generate a short code from URL"""
    return hashlib.md5(url.encode()).hexdigest()[:8]

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "URL Shortener API",
        "version": "1.0.0",
        "endpoints": {
            "shorten": "POST /shorten?url=YOUR_URL",
            "redirect": "GET /{short_code}",
            "stats": "GET /stats/{short_code}",
            "health": "GET /health"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "url-shortener",
        "version": "1.0.0",
        "timestamp": "2024-01-09T19:30:00Z"
    }

@app.post("/shorten")
async def shorten_url(url: str, custom_code: str = None):
    """Shorten a URL"""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    short_code = custom_code or generate_short_code(url)
    
    if short_code in url_database:
        raise HTTPException(status_code=400, detail="Short code already exists")
    
    url_database[short_code] = {
        "original_url": url,
        "clicks": 0,
        "created_at": "2024-01-01T00:00:00Z"
    }
    
    return {
        "short_url": f"http://localhost:8000/{short_code}",
        "short_code": short_code,
        "original_url": url
    }

@app.get("/{short_code}")
async def redirect_url(short_code: str):
    """Redirect to original URL"""
    if short_code not in url_database:
        raise HTTPException(status_code=404, detail="URL not found")
    
    url_database[short_code]["clicks"] += 1
    return RedirectResponse(url=url_database[short_code]["original_url"])

@app.get("/stats/{short_code}")
async def get_stats(short_code: str):
    """Get URL statistics"""
    if short_code not in url_database:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return url_database[short_code]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
