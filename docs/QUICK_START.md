# 🇧🇩 NewsHawk - Bangladesh News Aggregator

**Customized fork of TrendRadar for Bangladesh news monitoring**

## 🚀 Quick Start

```bash
# Fetch latest Bangladesh news (500+ articles)
python3 fetch_google_news.py

# View results
cat output_google_news/$(date +%Y-%m-%d)/*.txt
```

---

## 📰 News Sources

| Source | Articles | Language | Update | API Required |
|--------|----------|----------|--------|--------------|
| **Google News RSS** ⭐ | 500+ | English | Latest 24h | No |
| **Prothom Alo RSS** | 20 | Bangla | Real-time | No |
| **NewsAPI** | 1-3 | English | On-demand | Yes (100/day) |

---

## 📥 Available Scripts

### Primary (Recommended)
```bash
python3 fetch_google_news.py    # Google News - 500+ articles
```

### Alternative Sources
```bash
python3 fetch_bd_rss.py          # Prothom Alo - 20 Bangla articles
python3 fetch_bd_news.py         # NewsAPI - 1-3 articles (limited)
```

---

## 📂 Project Structure

```
NewsHawk/
├── fetch_google_news.py     ⭐ Primary news fetcher
├── fetch_bd_rss.py           Prothom Alo fetcher
├── fetch_bd_news.py          NewsAPI fetcher
├── main.py                   NewsHawk core (English)
├── config/
│   ├── config.yaml
│   └── frequency_words.txt   Bangladesh keywords
├── docker/
│   └── .env                  API keys & configuration
└── output_google_news/       Latest news output
```

---

## ⚙️ Configuration

### API Keys (Optional)
Only needed for NewsAPI:

Edit `docker/.env`:
```env
NEWS_API_KEY=your_api_key_here
```

Get free key: https://newsapi.org/

### Google News Topics
Edit `fetch_google_news.py` to add/remove topics:
```python
GOOGLE_NEWS_FEEDS = [
    {
        "name": "Google News - Bangladesh Sports",
        "url": "https://news.google.com/rss/search?q=Bangladesh+sports+when:1d&hl=en-BD&gl=BD&ceid=BD:en",
        "language": "en"
    }
]
```

---

## 🔄 Automation

### Schedule automatic fetching:
```bash
# Edit crontab
crontab -e

# Add these lines:
0 */2 * * * cd /path/to/NewsHawk && python3 fetch_google_news.py
0 */3 * * * cd /path/to/NewsHawk && python3 fetch_bd_rss.py
```

---

## 📊 Output Format

### Text Output (`output_google_news/YYYY-MM-DD/HH-MM.txt`)
```
Google News - Bangladesh News Update
Fetched at: 2025-12-04 10:30:15
================================================================================

Total articles fetched: 509

================================================================================
📰 Google News - Bangladesh (Latest) (100 articles)
================================================================================

1. Bangladesh Economy Shows Growth - Reuters
   Source: Reuters
   Published: Wed, 04 Dec 2025 08:15:00 GMT
   Link: https://...
```

### JSON Output (`output_google_news/YYYY-MM-DD/HH-MM.json`)
```json
{
  "timestamp": "2025-12-04T10:30:15",
  "total_articles": 509,
  "feeds": {
    "Google News - Bangladesh (Latest)": [
      {
        "title": "Bangladesh Economy Shows Growth",
        "source": "Reuters",
        "published": "Wed, 04 Dec 2025 08:15:00 GMT",
        "link": "https://...",
        "description": "..."
      }
    ]
  }
}
```

---

## 🛠️ Customization

### Add Bangladesh Keywords
Edit `config/frequency_words.txt`:
```
# Politics
+Hasina
+BNP
+Awami

# Cricket
+Bangladesh Cricket
+Tigers
+Shakib

# Business
+Dhaka Stock Exchange
+Grameen Bank
```

---

## 🌟 Features

✅ **Latest News Only** - Filters for last 24 hours  
✅ **No API Limits** - Google News is free and unlimited  
✅ **Multiple Languages** - English + Bangla sources  
✅ **Clean English Code** - Fully translated from Chinese  
✅ **Auto-filtering** - Bangladesh-specific content only  

---

## 📖 Documentation

- `SETUP_COMPLETE.md` - Full setup guide
- `CONVERSION_SUMMARY.md` - Translation details
- `BANGLADESH_NEWS_GUIDE.md` - BD news source guide

---

## 🔧 Troubleshooting

### No articles returned?
```bash
# Check internet connection
curl -I https://news.google.com

# Verify feed URLs manually
curl "https://news.google.com/rss/search?q=Bangladesh+when:1d&hl=en-BD&gl=BD&ceid=BD:en"
```

### Old cached data?
```bash
# Clear output directories
rm -rf output_google_news/2025*
rm -rf output_bd_rss/2025*
rm -rf output_bd/2025*

# Fetch fresh data
python3 fetch_google_news.py
```

---

## 📝 Notes

- **Chinese platform news disabled** - Not relevant for Bangladesh
- **Docker disabled** - Using direct Python scripts instead
- **Main NewsHawk features** - Available but not actively used
- **Focus** - Google News RSS as primary source

---

## 🤝 Credits

Based on [TrendRadar](https://github.com/sansan0/TrendRadar) by sansan0  
Customized for Bangladesh news by rajviahmedtamim

---

## 📜 License

GPL-3.0 - Same as original TrendRadar project

---

**Enjoy your Bangladesh news aggregator! 🇧🇩**
