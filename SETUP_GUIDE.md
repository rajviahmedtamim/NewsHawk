# 🚀 NewsHawk - Complete Setup Guide

**Bangladesh News Aggregator with FastAPI Backend**

This guide will help you set up NewsHawk from scratch in under 10 minutes.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Detailed Setup](#detailed-setup)
4. [Running the Project](#running-the-project)
5. [Testing](#testing)
6. [Troubleshooting](#troubleshooting)

---

## ✅ Prerequisites

### Required
- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **pip** - Comes with Python
- **Git** - [Download](https://git-scm.com/downloads)

### Optional (for production)
- **PostgreSQL 15+** - [Download](https://www.postgresql.org/download/)

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/NewsHawk.git
cd NewsHawk

# 2. Install dependencies
pip3 install -r requirements-api.txt

# 3. Fetch news data
python3 fetch_google_news_en.py
python3 fetch_google_news_bn.py
python3 fetch_bd_rss.py

# 4. Setup database
python3 migrate_to_db.py

# 5. Start API server
./run_api.sh
```

**Done!** Visit http://localhost:8000/docs

---

## 📦 Detailed Setup

### Step 1: Clone Repository

```bash
# Clone the project
git clone https://github.com/YOUR_USERNAME/NewsHawk.git
cd NewsHawk

# Verify files
ls -la
```

**Expected output:**
```
api/
docs/
output_google_news_en/
output_google_news_bn/
output_bd_rss/
fetch_google_news_en.py
fetch_google_news_bn.py
fetch_bd_rss.py
run_api.sh
...
```

---

### Step 2: Install Python Dependencies

#### Option A: Using pip (Recommended)

```bash
# Install API dependencies
pip3 install -r requirements-api.txt

# Install database dependencies
pip3 install -r requirements-db.txt
```

#### Option B: Using Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements-api.txt
pip install -r requirements-db.txt
```

**Verify installation:**
```bash
python3 -c "import fastapi, sqlalchemy; print('✅ Dependencies installed')"
```

---

### Step 3: Fetch News Data

NewsHawk fetches news from multiple sources. Run these scripts to get initial data:

#### Fetch English News (330+ articles)

```bash
python3 fetch_google_news_en.py
```

**Output:**
```
🌐 Fetching English news from Google News RSS feeds...
✅ Saved 330 articles to:
   Text: output_google_news_en/2025-12-20/16-57.txt
   JSON: output_google_news_en/2025-12-20/16-57.json
```

#### Fetch Bangla News (289+ articles)

```bash
python3 fetch_google_news_bn.py
```

**Output:**
```
🌐 বাংলা গুগল নিউজ আরএসএস ফিড থেকে খবর সংগ্রহ করা হচ্ছে...
✅ সংরক্ষিত হয়েছে 289টি নিবন্ধ
```

#### Fetch RSS Feeds (60 articles)

```bash
python3 fetch_bd_rss.py
```

**Output:**
```
📰 Fetching Bangladesh news from RSS feeds...
✅ Saved 60 articles
```

---

### Step 4: Setup Database

NewsHawk uses SQLite by default (no installation needed). For production, you can use PostgreSQL.

#### Initialize Database

```bash
python3 migrate_to_db.py
```

**Output:**
```
🔄 Starting data migration to database...
📊 Creating database tables...
✅ Database initialized

📥 Loading articles from JSON files...
✅ Loaded 679 articles from JSON files

💾 Inserting articles into database...
  Processed 100/679 articles...
  Processed 200/679 articles...
  ...

============================================================
📊 Migration Summary:
  ✅ Inserted: 643 articles
  ⏭️  Skipped (duplicates): 36 articles
  ❌ Errors: 0 articles
============================================================

✅ Migration complete!
```

**Verify database:**
```bash
ls -lh newshawk.db
# Output: -rw-r--r--  1 user  staff   2.9M Dec 20 19:22 newshawk.db

sqlite3 newshawk.db "SELECT COUNT(*) FROM articles;"
# Output: 643
```

---

### Step 5: Start API Server

#### Option A: Using Startup Script (Recommended)

```bash
./run_api.sh
```

#### Option B: Manual Start

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

**Output:**
```
🚀 Starting NewsHawk API...

✅ Dependencies installed

🌐 Starting API server...
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc
   - API: http://localhost:8000/api/v1

INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

---

## 🎯 Running the Project

### Access API Documentation

Once the server is running, visit:

- **Swagger UI (Interactive):** http://localhost:8000/docs
- **ReDoc (Alternative):** http://localhost:8000/redoc
- **API Root:** http://localhost:8000/

### Test API Endpoints

#### Health Check

```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-12-20T19:14:17.722614"
}
```

#### Get News

```bash
curl "http://localhost:8000/api/v1/news?limit=5"
```

#### Search News

```bash
curl "http://localhost:8000/api/v1/news/search?q=cricket&limit=5"
```

#### Get Trending Topics

```bash
curl "http://localhost:8000/api/v1/trending?limit=10"
```

#### Get Statistics

```bash
curl "http://localhost:8000/api/v1/stats"
```

---

## 🔄 Automation (Optional)

### Setup Cron Jobs

Automatically fetch news every 2 hours:

```bash
# Edit crontab
crontab -e

# Add these lines:
0 */2 * * * cd /path/to/NewsHawk && python3 fetch_google_news_en.py
0 */2 * * * cd /path/to/NewsHawk && python3 fetch_google_news_bn.py
0 */3 * * * cd /path/to/NewsHawk && python3 fetch_bd_rss.py
0 */6 * * * cd /path/to/NewsHawk && python3 migrate_to_db.py
```

---

## 🧪 Testing

### Test News Fetchers

```bash
# Test English news
python3 fetch_google_news_en.py
ls output_google_news_en/$(date +%Y-%m-%d)/

# Test Bangla news
python3 fetch_google_news_bn.py
ls output_google_news_bn/$(date +%Y-%m-%d)/

# Test RSS feeds
python3 fetch_bd_rss.py
ls output_bd_rss/$(date +%Y-%m-%d)/
```

### Test Database

```bash
# Check database
sqlite3 newshawk.db "SELECT COUNT(*) FROM articles;"

# Check by language
sqlite3 newshawk.db "SELECT language, COUNT(*) FROM articles GROUP BY language;"

# Check latest articles
sqlite3 newshawk.db "SELECT title FROM articles ORDER BY published DESC LIMIT 5;"
```

### Test API

```bash
# Health check
curl http://localhost:8000/health

# Get news
curl http://localhost:8000/api/v1/news?limit=3

# Search
curl "http://localhost:8000/api/v1/news/search?q=bangladesh"

# Trending
curl http://localhost:8000/api/v1/trending

# Statistics
curl http://localhost:8000/api/v1/stats
```

---

## 🐛 Troubleshooting

### Issue: "Module not found"

**Solution:**
```bash
pip3 install -r requirements-api.txt
pip3 install -r requirements-db.txt
```

### Issue: "Port 8000 already in use"

**Solution:**
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use different port
uvicorn api.main:app --port 8001
```

### Issue: "Database locked"

**Solution:**
```bash
# Stop API server
# Delete database
rm newshawk.db

# Re-migrate
python3 migrate_to_db.py
```

### Issue: "No articles fetched"

**Solution:**
```bash
# Check internet connection
ping google.com

# Try fetching again
python3 fetch_google_news_en.py

# Check output directory
ls -la output_google_news_en/
```

### Issue: "Permission denied: ./run_api.sh"

**Solution:**
```bash
chmod +x run_api.sh
./run_api.sh
```

---

## 📁 Project Structure

```
NewsHawk/
├── api/                          # FastAPI backend
│   ├── main.py                   # Main application
│   ├── config.py                 # Configuration
│   ├── database.py               # Database connection
│   ├── crud.py                   # CRUD operations
│   ├── models/                   # Data models
│   │   ├── article.py            # Pydantic models
│   │   └── db_models.py          # SQLAlchemy models
│   ├── routes/                   # API routes
│   │   ├── news.py               # News endpoints
│   │   └── analytics.py          # Analytics endpoints
│   └── utils/                    # Utilities
│       ├── data_loader.py        # Data loader
│       ├── search.py             # Search utilities
│       └── analytics.py          # Analytics utilities
│
├── docs/                         # Documentation
│   ├── API_DOCUMENTATION.md      # Full API docs
│   ├── API_QUICK_REFERENCE.md    # Quick reference
│   ├── USAGE_GUIDE.md            # Usage guide
│   └── ...
│
├── output_google_news_en/        # English news output
├── output_google_news_bn/        # Bangla news output
├── output_bd_rss/                # RSS news output
│
├── fetch_google_news_en.py       # English news fetcher
├── fetch_google_news_bn.py       # Bangla news fetcher
├── fetch_bd_rss.py               # RSS news fetcher
├── migrate_to_db.py              # Database migration
├── run_api.sh                    # API startup script
├── requirements-api.txt          # API dependencies
├── requirements-db.txt           # Database dependencies
└── newshawk.db                   # SQLite database
```

---

## 🔧 Configuration

### API Configuration (`api/config.py`)

```python
# Server
HOST = "0.0.0.0"
PORT = 8000

# Database
DATABASE_URL = "sqlite:///./newshawk.db"
# For PostgreSQL: "postgresql://user:password@localhost/newshawk"

# CORS
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
]

# Pagination
DEFAULT_LIMIT = 100
MAX_LIMIT = 1000
```

### Environment Variables (Optional)

Create `.env` file:

```env
DATABASE_URL=sqlite:///./newshawk.db
API_PORT=8000
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

---

## 🚀 Production Deployment

### Using PostgreSQL

```bash
# 1. Install PostgreSQL
brew install postgresql@15
brew services start postgresql@15

# 2. Create database
createdb newshawk

# 3. Update config
# Edit api/config.py:
DATABASE_URL = "postgresql://user:password@localhost/newshawk"

# 4. Migrate data
python3 migrate_to_db.py

# 5. Start API
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### Using Docker (Coming Soon)

```bash
docker-compose up -d
```

---

## 📚 Additional Resources

- **Full Documentation:** [docs/README_NEWSHAWK.md](docs/README_NEWSHAWK.md)
- **API Reference:** [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)
- **Usage Guide:** [docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md)
- **Test Report:** [API_TEST_REPORT.md](API_TEST_REPORT.md)

---

## 🤝 Support

**Issues?** Check:
1. [Troubleshooting](#troubleshooting) section
2. [GitHub Issues](https://github.com/YOUR_USERNAME/NewsHawk/issues)
3. Documentation in `docs/` folder

---

## ✅ Setup Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip3 install -r requirements-api.txt`)
- [ ] News data fetched (English, Bangla, RSS)
- [ ] Database initialized (`python3 migrate_to_db.py`)
- [ ] API server running (`./run_api.sh`)
- [ ] Tested endpoints (http://localhost:8000/docs)
- [ ] (Optional) Cron jobs configured
- [ ] (Optional) PostgreSQL setup for production

---

**🎉 Congratulations! NewsHawk is now running!**

Visit http://localhost:8000/docs to explore the API.
