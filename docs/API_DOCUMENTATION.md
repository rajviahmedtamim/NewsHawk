# 🚀 NewsHawk API Documentation

**Version:** 1.0.0  
**Base URL:** `http://localhost:8000/api/v1`  
**Technology:** FastAPI + Python 3.8+

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Authentication](#authentication)
3. [Endpoints](#endpoints)
4. [Data Models](#data-models)
5. [Error Handling](#error-handling)
6. [Rate Limiting](#rate-limiting)
7. [Examples](#examples)

---

## 🎯 Overview

NewsHawk API provides access to aggregated Bangladesh news from multiple sources including Google News RSS and Bangladesh newspapers. The API supports both English and Bangla content with powerful search and filtering capabilities.

### Key Features

- ✅ **600+ daily articles** from multiple sources
- ✅ **Bilingual support** (English + Bangla)
- ✅ **Real-time updates** (fetched every 2 hours)
- ✅ **Advanced search** and filtering
- ✅ **Trending topics** analysis
- ✅ **Auto-generated docs** at `/docs`

---

## 🔐 Authentication

**Current Version:** No authentication required (public API)

**Future:** API key authentication for rate limiting
```http
Authorization: Bearer YOUR_API_KEY
```

---

## 📡 Endpoints

### 1. Health Check

**GET** `/health`

Check API status and version.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-12-20T18:52:00Z"
}
```

---

### 2. Get All News

**GET** `/news`

Get all news articles from all sources.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `language` | string | `all` | Filter by language: `en`, `bn`, `all` |
| `source` | string | `all` | Filter by source: `google`, `rss`, `all` |
| `limit` | integer | `100` | Number of articles (max 1000) |
| `offset` | integer | `0` | Pagination offset |
| `date` | string | `today` | Date filter: `today`, `YYYY-MM-DD` |

**Example Request:**
```http
GET /api/v1/news?language=en&limit=50
```

**Response:**
```json
{
  "total": 330,
  "count": 50,
  "language": "en",
  "date": "2025-12-20",
  "articles": [
    {
      "id": "abc123",
      "title": "Bangladesh holds state mourning...",
      "source": "Al Jazeera",
      "url": "https://news.google.com/...",
      "published": "2025-12-20T10:27:33Z",
      "language": "en",
      "feed": "Google News - Bangladesh (Latest)",
      "description": "Article summary...",
      "category": "politics"
    }
  ]
}
```

---

### 3. Get English News

**GET** `/news/english`

Get English news only.

**Query Parameters:** Same as `/news`

**Example Request:**
```http
GET /api/v1/news/english?limit=20
```

**Response:**
```json
{
  "total": 330,
  "count": 20,
  "language": "en",
  "articles": [...]
}
```

---

### 4. Get Bangla News

**GET** `/news/bangla`

Get Bangla news only (বাংলা).

**Query Parameters:** Same as `/news`

**Example Request:**
```http
GET /api/v1/news/bangla?limit=20
```

**Response:**
```json
{
  "total": 289,
  "count": 20,
  "language": "bn",
  "articles": [...]
}
```

---

### 5. Search News

**GET** `/news/search`

Search articles by keyword.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string | ✅ Yes | Search query |
| `language` | string | No | Filter by language |
| `limit` | integer | No | Results limit |
| `offset` | integer | No | Pagination offset |

**Example Request:**
```http
GET /api/v1/news/search?q=cricket&language=en
```

**Response:**
```json
{
  "query": "cricket",
  "total": 53,
  "count": 53,
  "articles": [
    {
      "id": "xyz789",
      "title": "Bangladesh Cricket Team wins...",
      "source": "ESPN Cricinfo",
      "relevance": 0.95,
      ...
    }
  ]
}
```

---

### 6. Get Trending Topics

**GET** `/news/trending`

Get trending topics and keywords.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `language` | string | `all` | Language filter |
| `limit` | integer | `10` | Number of topics |
| `period` | string | `today` | Time period: `today`, `week` |

**Example Request:**
```http
GET /api/v1/news/trending?limit=5
```

**Response:**
```json
{
  "period": "today",
  "date": "2025-12-20",
  "topics": [
    {
      "keyword": "cricket",
      "count": 125,
      "percentage": 20.5,
      "languages": ["en", "bn"],
      "trend": "up"
    },
    {
      "keyword": "politics",
      "count": 98,
      "percentage": 16.1,
      "languages": ["en", "bn"],
      "trend": "stable"
    }
  ]
}
```

---

### 7. Get News by Category

**GET** `/news/category/{category}`

Get news by category.

**Path Parameters:**
- `category`: politics, cricket, economy, dhaka, general

**Example Request:**
```http
GET /api/v1/news/category/cricket
```

**Response:**
```json
{
  "category": "cricket",
  "total": 125,
  "articles": [...]
}
```

---

### 8. Get News by Source

**GET** `/news/source/{source}`

Get news from specific source.

**Path Parameters:**
- `source`: google-en, google-bn, prothom-alo, daily-star, business-standard

**Example Request:**
```http
GET /api/v1/news/source/prothom-alo
```

**Response:**
```json
{
  "source": "Prothom Alo",
  "language": "bn",
  "total": 20,
  "articles": [...]
}
```

---

### 9. Get Statistics

**GET** `/stats`

Get overall statistics.

**Example Request:**
```http
GET /api/v1/stats
```

**Response:**
```json
{
  "total_articles": 679,
  "by_language": {
    "en": 390,
    "bn": 289
  },
  "by_source": {
    "google_news_en": 330,
    "google_news_bn": 289,
    "rss_feeds": 60
  },
  "last_updated": "2025-12-20T16:57:37Z",
  "sources_count": 14,
  "categories": ["politics", "cricket", "economy", "dhaka", "general"]
}
```

---

### 10. Get Latest Updates

**GET** `/news/latest`

Get most recent articles.

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | integer | `20` | Number of articles |
| `language` | string | `all` | Language filter |

**Example Request:**
```http
GET /api/v1/news/latest?limit=10
```

**Response:**
```json
{
  "count": 10,
  "articles": [
    {
      "id": "latest1",
      "title": "Breaking: ...",
      "published": "2025-12-20T18:45:00Z",
      "age_minutes": 7,
      ...
    }
  ]
}
```

---

## 📊 Data Models

### Article Model

```json
{
  "id": "string (unique identifier)",
  "title": "string (article title)",
  "source": "string (news source name)",
  "url": "string (article URL)",
  "published": "string (ISO 8601 datetime)",
  "language": "string (en or bn)",
  "feed": "string (feed name)",
  "description": "string (article summary)",
  "category": "string (auto-detected category)",
  "relevance": "float (0-1, for search results)"
}
```

### Trending Topic Model

```json
{
  "keyword": "string (topic keyword)",
  "count": "integer (article count)",
  "percentage": "float (percentage of total)",
  "languages": ["array of language codes"],
  "trend": "string (up, down, stable)"
}
```

### Statistics Model

```json
{
  "total_articles": "integer",
  "by_language": {
    "en": "integer",
    "bn": "integer"
  },
  "by_source": {
    "source_name": "integer"
  },
  "last_updated": "string (ISO 8601 datetime)",
  "sources_count": "integer",
  "categories": ["array of category names"]
}
```

---

## ⚠️ Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": "Additional error details",
    "timestamp": "2025-12-20T18:52:00Z"
  }
}
```

### HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 400 | Bad Request | Invalid parameters |
| 404 | Not Found | Resource not found |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |

### Common Errors

**Invalid Language:**
```json
{
  "error": {
    "code": "INVALID_LANGUAGE",
    "message": "Language must be 'en', 'bn', or 'all'",
    "timestamp": "2025-12-20T18:52:00Z"
  }
}
```

**No Results:**
```json
{
  "error": {
    "code": "NO_RESULTS",
    "message": "No articles found matching criteria",
    "timestamp": "2025-12-20T18:52:00Z"
  }
}
```

---

## 🚦 Rate Limiting

**Current:** No rate limiting (development)

**Future Production:**
- **Free tier:** 100 requests/hour
- **Authenticated:** 1000 requests/hour
- **Premium:** Unlimited

**Headers:**
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1703097600
```

---

## 💡 Examples

### Example 1: Get Latest Cricket News

```bash
curl "http://localhost:8000/api/v1/news/search?q=cricket&language=en&limit=5"
```

### Example 2: Get Bangla Politics News

```bash
curl "http://localhost:8000/api/v1/news/category/politics?language=bn"
```

### Example 3: Get Trending Topics

```bash
curl "http://localhost:8000/api/v1/news/trending?limit=10"
```

### Example 4: Search with Pagination

```bash
curl "http://localhost:8000/api/v1/news/search?q=economy&limit=20&offset=20"
```

---

## 🔄 WebSocket Support (Future)

**Endpoint:** `ws://localhost:8000/ws/news`

Real-time news updates via WebSocket.

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/news');

ws.onmessage = (event) => {
  const article = JSON.parse(event.data);
  console.log('New article:', article.title);
};
```

---

## 📚 Interactive Documentation

Once the API is running, visit:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## 🛠️ Technology Stack

- **Framework:** FastAPI 0.104+
- **Python:** 3.8+
- **Data Source:** JSON files from news fetchers
- **CORS:** Enabled for frontend
- **Validation:** Pydantic models

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install fastapi uvicorn

# Run API server
uvicorn api.app:app --reload --port 8000

# Access API
curl http://localhost:8000/api/v1/news
```

---

## 📝 Notes

- All timestamps are in UTC (ISO 8601 format)
- Bangla text is UTF-8 encoded
- News data updates every 2 hours via cron
- Search is case-insensitive
- Categories are auto-detected from feed names

---

**Ready to build? Let's implement this API! 🚀**
