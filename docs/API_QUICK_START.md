# 🚀 NewsHawk API - Quick Start Guide

## Installation

```bash
# Install dependencies
pip install -r requirements-api.txt
```

## Running the API

### Option 1: Using the startup script (Recommended)

```bash
./run_api.sh
```

### Option 2: Manual start

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

## Access the API

Once running, visit:

- **Swagger UI (Interactive Docs):** http://localhost:8000/docs
- **ReDoc (Alternative Docs):** http://localhost:8000/redoc
- **API Root:** http://localhost:8000/
- **Health Check:** http://localhost:8000/health

## Quick Test

```bash
# Health check
curl http://localhost:8000/health

# Get all news
curl http://localhost:8000/api/v1/news?limit=10

# Search news
curl "http://localhost:8000/api/v1/news/search?q=cricket&limit=5"

# Get trending topics
curl http://localhost:8000/api/v1/trending

# Get statistics
curl http://localhost:8000/api/v1/stats
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /health` | Health check |
| `GET /api/v1/news` | Get all news |
| `GET /api/v1/news/english` | Get English news |
| `GET /api/v1/news/bangla` | Get Bangla news |
| `GET /api/v1/news/search` | Search news |
| `GET /api/v1/news/latest` | Get latest news |
| `GET /api/v1/news/category/{category}` | Get news by category |
| `GET /api/v1/news/source/{source}` | Get news by source |
| `GET /api/v1/trending` | Get trending topics |
| `GET /api/v1/stats` | Get statistics |

## Configuration

Edit `api/config.py` to change:
- Port number
- CORS origins
- Data directories
- Pagination limits

## Next Steps

1. Start the API: `./run_api.sh`
2. Visit Swagger UI: http://localhost:8000/docs
3. Test endpoints interactively
4. Build your frontend dashboard!

---

**For full documentation, see:** [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)
