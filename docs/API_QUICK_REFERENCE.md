# 📋 NewsHawk API - Quick Reference

## 🎯 API Overview

**Base URL:** `http://localhost:8000/api/v1`  
**Docs:** `http://localhost:8000/docs` (auto-generated)

---

## 🚀 Key Endpoints

### Get All News
```http
GET /news?language=en&limit=50
```

### Search News
```http
GET /news/search?q=cricket&language=en
```

### Trending Topics
```http
GET /news/trending?limit=10
```

### Latest News
```http
GET /news/latest?limit=20
```

### By Category
```http
GET /news/category/cricket
```

### Statistics
```http
GET /stats
```

---

## 📊 Response Example

```json
{
  "total": 330,
  "count": 50,
  "articles": [
    {
      "id": "abc123",
      "title": "Bangladesh Cricket Team wins...",
      "source": "ESPN Cricinfo",
      "url": "https://...",
      "published": "2025-12-20T10:27:33Z",
      "language": "en",
      "category": "cricket"
    }
  ]
}
```

---

## 🛠️ Next Steps

1. **Review full documentation:** [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
2. **Ready to build?** Let me know and I'll create the FastAPI implementation!

---

**Features:**
- ✅ 10 endpoints
- ✅ Search & filter
- ✅ Trending analysis
- ✅ Auto-generated docs
- ✅ Bilingual support
