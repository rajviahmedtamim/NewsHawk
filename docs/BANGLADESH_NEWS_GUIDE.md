# Fetching Bangladesh News from Your Selected Sites

## Problem
NewsHawk uses the **newsnow API** which only supports **Chinese platforms** (Zhihu, Weibo, Douyin, etc.). It cannot directly scrape Bangladeshi news sites like Prothom Alo, Daily Star, bdnews24, etc.

## Solution Options

### Option 1: Use NewsAPI (Recommended) ⭐

**File:** `fetch_bd_news.py`

**Setup:**
1. Get a free API key from [newsapi.org](https://newsapi.org/register)
   - Free tier: 100 requests/day, 1-month historical data
   
2. Edit `fetch_bd_news.py` and add your API key:
   ```python
   NEWS_API_KEY = "your_actual_api_key_here"
   ```

3. Customize keywords:
   ```python
   KEYWORDS = [
       "Bangladesh",
       "Dhaka",
       "Cricket",
       "Hasina",
       "Economy"
   ]
   ```

4. Run it:
   ```bash
   python3 fetch_bd_news.py
   ```

**Output:** Saves to `output_bd/YYYY-MM-DD/HH-MM.txt` and `.json`

---

### Option 2: Use RSS Feeds (Free, No API Needed)

**Bangladeshi News Sites with RSS:**
- **Prothom Alo**: https://www.prothomalo.com/feed/
- **Daily Star**: https://www.thedailystar.net/rss.xml
- **bdnews24**: https://bdnews24.com/?widgetName=rssfeed&widgetId=1
- **Dhaka Tribune**: https://www.dhakatribune.com/feed

**Simple RSS Script** (create `fetch_bd_rss.py`):
```python
import feedparser
from datetime import datetime

# RSS feeds
FEEDS = [
    ("Prothom Alo", "https://www.prothomalo.com/feed/"),
    ("Daily Star", "https://www.thedailystar.net/rss.xml"),
    ("bdnews24", "https://bdnews24.com/?widgetName=rssfeed&widgetId=1"),
]

for name, url in FEEDS:
    print(f"\n📰 {name}")
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]:  # Top 5
        print(f"  - {entry.title}")
        print(f"    {entry.link}\n")
```

---

### Option 3: Continue Using NewsHawk for International News

**Keep current setup** but optimize keywords for Bangladesh coverage:

`config/frequency_words.txt`:
```
Bangladesh
বাংলাদেশ
Dhaka
ঢাকা
Chittagong
চট্টগ্রাম
+Hasina
+Sheikh Hasina
+BNP
+Awami League
+Jamaat

Cricket
+Bangladesh Cricket
+Tigers
+BCB
+Shakib
+Mushfiqur
+Tamim

Economy
+Taka
+Dollar
+Inflation
+Stock Market
+Bangladesh Bank

Politics
+Election
+Parliament
+Khaleda
+Yunus
```

**This works because:**
- International news platforms (Reuters, BBC, etc.) cover major Bangladesh events
- Chinese platforms report on Bangladesh-China relations, cricket, etc.
- You'll catch international coverage of Bangladesh news

---

## Comparison

| Method | Pros | Cons | Cost |
|--------|------|------|------|
| **NewsAPI** | - Easy integration<br>- Many sources<br>- English articles | - 100 req/day limit (free)<br>- 1-month history only | Free/$449/mo |
| **RSS Feeds** | - Completely free<br>- Direct from BD sites<br>- No API limits | - Need to parse each feed<br>- Different structures | Free |
| **Keep NewsHawk** | - Already working<br>- Auto-updates<br>- Nice UI | - Limited BD coverage<br>- Chinese platforms only | Free |

---

## My Recommendation

**Use all three combined:**

1. **NewsHawk** (current) → International Bangladesh coverage
2. **fetch_bd_news.py** → Daily Bangladesh news from NewsAPI
3. **Schedule both** in cron or Docker:
   ```bash
   # Run NewsHawk every 30 min (already setup)
   # Run BD news fetch every 2 hours
   0 */2 * * * cd /path/to/NewsHawk && python3 fetch_bd_news.py
   ```

This gives you **comprehensive Bangladesh news coverage** from both international and local sources!

---

## Need Help?

Let me know if you want me to:
1. Set up NewsAPI integration
2. Create RSS feed aggregator
3. Modify NewsHawk to combine both sources
