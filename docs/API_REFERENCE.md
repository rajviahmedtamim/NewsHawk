# 🔌 NewsHawk API & RSS Feed Reference

## Table of Contents

1. [Google News RSS API](#google-news-rss-api)
2. [Prothom Alo RSS](#prothom-alo-rss)
3. [NewsAPI Integration](#newsapi-integration)
4. [Output JSON Schema](#output-json-schema)
5. [Python API](#python-api)

---

## Google News RSS API

### Base URL

```
https://news.google.com/rss
```

### English Feeds

#### General Bangladesh News
```
https://news.google.com/rss/search?q=Bangladesh+when:1d&hl=en-BD&gl=BD&ceid=BD:en
```

#### Topic-Specific Feeds

**Politics:**
```
https://news.google.com/rss/search?q=Bangladesh+politics+when:1d&hl=en-BD&gl=BD&ceid=BD:en
```

**Cricket:**
```
https://news.google.com/rss/search?q=Bangladesh+cricket+when:1d&hl=en-BD&gl=BD&ceid=BD:en
```

**Economy:**
```
https://news.google.com/rss/search?q=Bangladesh+economy+when:1d&hl=en-BD&gl=BD&ceid=BD:en
```

**Dhaka:**
```
https://news.google.com/rss/search?q=Dhaka+when:1d&hl=en-BD&gl=BD&ceid=BD:en
```

### Bangla Feeds (বাংলা)

#### General Bangladesh News
```
https://news.google.com/rss?hl=bn&gl=BD&ceid=BD:bn
```

#### Topic-Specific Feeds

**রাজনীতি (Politics):**
```
https://news.google.com/rss/search?q=বাংলাদেশ+রাজনীতি+when:1d&hl=bn&gl=BD&ceid=BD:bn
```

**ক্রিকেট (Cricket):**
```
https://news.google.com/rss/search?q=বাংলাদেশ+ক্রিকেট+when:1d&hl=bn&gl=BD&ceid=BD:bn
```

**অর্থনীতি (Economy):**
```
https://news.google.com/rss/search?q=বাংলাদেশ+অর্থনীতি+when:1d&hl=bn&gl=BD&ceid=BD:bn
```

**ঢাকা (Dhaka):**
```
https://news.google.com/rss/search?q=ঢাকা+when:1d&hl=bn&gl=BD&ceid=BD:bn
```

### URL Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `q` | Search query | `Bangladesh+cricket` |
| `when:1d` | Time filter (1 day) | `when:1d`, `when:7d` |
| `hl` | Language | `en-BD`, `bn` |
| `gl` | Country | `BD` |
| `ceid` | Country-language ID | `BD:en`, `BD:bn` |

### Response Format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Bangladesh - Google News</title>
    <link>https://news.google.com/</link>
    <item>
      <title>Article Title</title>
      <link>https://news.google.com/articles/...</link>
      <pubDate>Sat, 20 Dec 2025 10:27:33 GMT</pubDate>
      <source url="https://aljazeera.com">Al Jazeera</source>
      <description>Article summary...</description>
    </item>
  </channel>
</rss>
```

---

## Prothom Alo RSS

### Feed URL

```
https://www.prothomalo.com/feed/
```

### Other Bangladesh RSS Feeds

**Daily Star:**
```
https://www.thedailystar.net/rss.xml
```

**bdnews24:**
```
https://bdnews24.com/?widgetName=rssfeed&widgetId=1
```

**Dhaka Tribune:**
```
https://www.dhakatribune.com/feed
```

### Response Format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>প্রথম আলো</title>
    <link>https://www.prothomalo.com/</link>
    <item>
      <title>শিরোনাম</title>
      <link>https://www.prothomalo.com/...</link>
      <pubDate>Sat, 20 Dec 2025 10:00:00 +0600</pubDate>
      <description>সংবাদের সারসংক্ষেপ...</description>
    </item>
  </channel>
</rss>
```

---

## NewsAPI Integration

### Base URL

```
https://newsapi.org/v2/everything
```

### Authentication

```bash
# Add to docker/.env
NEWS_API_KEY=your_api_key_here
```

### Request Example

```bash
curl "https://newsapi.org/v2/everything?q=Bangladesh&apiKey=YOUR_API_KEY"
```

### Python Example

```python
import requests

API_KEY = "your_api_key_here"
url = "https://newsapi.org/v2/everything"

params = {
    "q": "Bangladesh",
    "language": "en",
    "sortBy": "publishedAt",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

for article in data['articles']:
    print(article['title'])
```

### Response Format

```json
{
  "status": "ok",
  "totalResults": 100,
  "articles": [
    {
      "source": {
        "id": null,
        "name": "Reuters"
      },
      "author": "John Doe",
      "title": "Article Title",
      "description": "Article description",
      "url": "https://reuters.com/...",
      "urlToImage": "https://reuters.com/image.jpg",
      "publishedAt": "2025-12-20T10:27:33Z",
      "content": "Article content..."
    }
  ]
}
```

### Rate Limits

- **Free Tier:** 100 requests/day
- **Developer Tier:** 500 requests/day ($449/month)
- **Business Tier:** Unlimited ($999/month)

---

## Output JSON Schema

### NewsHawk JSON Format

```json
{
  "timestamp": "2025-12-20T16:57:37.123456",
  "language": "en",
  "total_articles": 330,
  "feeds": {
    "Google News - Bangladesh (Latest)": [
      {
        "title": "Article Title",
        "link": "https://news.google.com/...",
        "published": "Sat, 20 Dec 2025 10:27:33 GMT",
        "source": "Al Jazeera",
        "description": "Article summary..."
      }
    ]
  }
}
```

### Schema Definition

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp of when news was fetched"
    },
    "language": {
      "type": "string",
      "enum": ["en", "bn"],
      "description": "Language code (en=English, bn=Bangla)"
    },
    "total_articles": {
      "type": "integer",
      "description": "Total number of articles fetched"
    },
    "feeds": {
      "type": "object",
      "description": "Articles grouped by feed name",
      "patternProperties": {
        ".*": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": {"type": "string"},
              "link": {"type": "string", "format": "uri"},
              "published": {"type": "string"},
              "source": {"type": "string"},
              "description": {"type": "string"}
            },
            "required": ["title", "link", "published", "source"]
          }
        }
      }
    }
  },
  "required": ["timestamp", "language", "total_articles", "feeds"]
}
```

---

## Python API

### Fetcher Functions

#### fetch_rss_feed()

Fetch and parse an RSS feed with optional time filtering.

```python
def fetch_rss_feed(feed_url: str, filter_recent: bool = True) -> List[Dict]:
    """
    Fetch and parse RSS feed, optionally filtering for recent articles only
    
    Args:
        feed_url: RSS feed URL
        filter_recent: Whether to filter by MAX_ARTICLE_AGE_HOURS
        
    Returns:
        List of article dictionaries
    """
```

**Usage:**
```python
articles = fetch_rss_feed("https://news.google.com/rss?hl=bn&gl=BD&ceid=BD:bn")
print(f"Fetched {len(articles)} articles")
```

#### is_recent_article()

Check if an article was published within the specified time window.

```python
def is_recent_article(published_date_str: str, max_hours: int = 24) -> bool:
    """
    Check if article was published within the specified hours
    
    Args:
        published_date_str: RFC 2822 date string
        max_hours: Maximum age in hours
        
    Returns:
        True if article is recent, False otherwise
    """
```

**Usage:**
```python
is_recent = is_recent_article("Sat, 20 Dec 2025 10:27:33 GMT", max_hours=24)
print(f"Article is recent: {is_recent}")
```

#### save_articles()

Save articles to TXT and JSON files.

```python
def save_articles(all_articles: Dict[str, List[Dict]], output_dir: Path):
    """
    Save articles to TXT and JSON files
    
    Args:
        all_articles: Dictionary of feed_name -> articles
        output_dir: Output directory path
    """
```

**Usage:**
```python
from pathlib import Path

output_dir = Path("output_google_news_en/2025-12-20")
output_dir.mkdir(parents=True, exist_ok=True)

save_articles(all_articles, output_dir)
```

### Custom Integration Example

```python
import feedparser
from datetime import datetime
from pathlib import Path
from typing import List, Dict

# Import NewsHawk functions
from fetch_google_news_en import fetch_rss_feed, save_articles

# Define custom feeds
CUSTOM_FEEDS = [
    {
        "name": "My Custom Feed",
        "url": "https://news.google.com/rss/search?q=Bangladesh+technology+when:1d&hl=en-BD&gl=BD&ceid=BD:en",
        "language": "en"
    }
]

# Fetch news
all_articles = {}
for feed_info in CUSTOM_FEEDS:
    articles = fetch_rss_feed(feed_info['url'])
    if articles:
        all_articles[feed_info['name']] = articles

# Save to custom directory
output_dir = Path("my_custom_output") / datetime.now().strftime("%Y-%m-%d")
output_dir.mkdir(parents=True, exist_ok=True)
save_articles(all_articles, output_dir)

print(f"Saved {sum(len(a) for a in all_articles.values())} articles")
```

---

## Rate Limits & Best Practices

### Google News RSS
- **Rate Limit:** None (free, unlimited)
- **Best Practice:** Fetch every 2-3 hours
- **Caching:** Not required (always fresh data)

### Prothom Alo RSS
- **Rate Limit:** None (free, unlimited)
- **Best Practice:** Fetch every 3-4 hours
- **Caching:** Recommended for high-frequency access

### NewsAPI
- **Rate Limit:** 100 requests/day (free tier)
- **Best Practice:** Fetch once per day
- **Caching:** Required to stay within limits

---

## Error Handling

### Common HTTP Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Process normally |
| 429 | Too Many Requests | Wait and retry |
| 500 | Server Error | Retry after delay |
| 503 | Service Unavailable | Retry after delay |

### Python Error Handling Example

```python
import time
import requests

def fetch_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Error: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"Failed after {max_retries} attempts")
                raise
```

---

**For more information, see [README_NEWSHAWK.md](README_NEWSHAWK.md) and [USAGE_GUIDE.md](USAGE_GUIDE.md)**
