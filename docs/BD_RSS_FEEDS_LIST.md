# 📰 Bangladesh Newspaper RSS Feeds - Complete List

## Currently Working Feeds ✅

### Bangla Language (বাংলা)

1. **Prothom Alo (প্রথম আলো)**
   - URL: `https://www.prothomalo.com/feed/`
   - Status: ✅ Working (20+ articles)
   - Language: Bangla
   - Coverage: General news

### English Language

2. **The Daily Star - Frontpage**
   - URL: `https://www.thedailystar.net/frontpage/rss.xml`
   - Status: ✅ Working (20+ articles)
   - Language: English
   - Coverage: Front page news

## Additional Feeds (To Verify)

### Bangla Newspapers

3. **Jugantor (যুগান্তর)**
   - URL: `https://www.jugantor.com/feed/rss.xml`
   - Alternative: `https://www.jugantor.com/rss.xml`
   - Language: Bangla

4. **Kaler Kantho (কালের কণ্ঠ)**
   - URL: `https://www.kalerkantho.com/rss.xml`
   - Language: Bangla

5. **Samakal (সমকাল)**
   - URL: `https://samakal.com/feed`
   - Language: Bangla

### English Newspapers

6. **The Daily Star - Latest**
   - URL: `https://www.thedailystar.net/feeds/latest`
   - Alternative: `https://www.thedailystar.net/rss.xml`
   - Language: English

7. **bdnews24**
   - URL: `https://bdnews24.com/?widgetName=rssfeed&widgetId=1150&getXmlFeed=true`
   - Alternative: `https://bdnews24.com/rss/rss.xml`
   - Language: English

8. **Dhaka Tribune**
   - URL: `https://www.dhakatribune.com/feed`
   - Alternative: `https://www.dhakatribune.com/rss.xml`
   - Language: English

9. **New Age Bangladesh**
   - URL: `https://www.newagebd.net/feed`
   - Language: English

10. **The Business Standard**
    - URL: `https://www.tbsnews.net/feed`
    - Language: English

11. **The Financial Express**
    - URL: `https://thefinancialexpress.com.bd/feed`
    - Alternative: `https://thefinancialexpress.com.bd/rss.xml`
    - Language: English

12. **United News of Bangladesh (UNB)**
    - URL: `https://unb.com.bd/feed`
    - Language: English

13. **The Independent**
    - URL: `http://www.theindependentbd.com/feed`
    - Language: English

14. **Dhaka Post**
    - URL: `https://www.dhakapost.com/feed`
    - Language: English

## Category-Specific Feeds

### Daily Star Categories

- **Politics:** `https://www.thedailystar.net/politics/rss.xml`
- **Business:** `https://www.thedailystar.net/business/rss.xml`
- **Sports:** `https://www.thedailystar.net/sports/rss.xml`
- **Entertainment:** `https://www.thedailystar.net/entertainment/rss.xml`
- **Opinion:** `https://www.thedailystar.net/opinion/rss.xml`

### Prothom Alo Categories

- **Bangladesh:** `https://www.prothomalo.com/bangladesh/rss.xml`
- **Sports:** `https://www.prothomalo.com/sports/rss.xml`
- **Entertainment:** `https://www.prothomalo.com/entertainment/rss.xml`

## How to Test RSS Feeds

### Method 1: Browser
```
Open the RSS URL in your browser
Look for XML content with <rss> or <feed> tags
```

### Method 2: curl
```bash
curl "https://www.prothomalo.com/feed/" | head -50
```

### Method 3: Python
```python
import feedparser
feed = feedparser.parse("https://www.prothomalo.com/feed/")
print(f"Found {len(feed.entries)} articles")
for entry in feed.entries[:5]:
    print(f"- {entry.title}")
```

## Recommended Feeds for NewsHawk

### For Maximum Coverage (10 feeds)
1. Prothom Alo (Bangla)
2. Jugantor (Bangla)
3. Kaler Kantho (Bangla)
4. Daily Star - Frontpage (English)
5. Daily Star - Latest (English)
6. bdnews24 (English)
7. Dhaka Tribune (English)
8. Business Standard (English)
9. Financial Express (English)
10. UNB (English)

### For Quick Updates (5 feeds)
1. Prothom Alo (Bangla)
2. Daily Star - Frontpage (English)
3. bdnews24 (English)
4. Dhaka Tribune (English)
5. UNB (English)

### For Bangla Only (3 feeds)
1. Prothom Alo
2. Jugantor
3. Kaler Kantho

### For English Only (5 feeds)
1. Daily Star - Frontpage
2. bdnews24
3. Dhaka Tribune
4. Business Standard
5. Financial Express

## Feed Update Frequency

| Newspaper | Update Frequency | Articles per Update |
|-----------|------------------|---------------------|
| Prothom Alo | Every 30 min | 20-30 |
| Daily Star | Every 1 hour | 20-30 |
| bdnews24 | Every 30 min | 15-25 |
| Dhaka Tribune | Every 1 hour | 15-20 |
| Jugantor | Every 1 hour | 20-30 |

## Troubleshooting

### Feed Returns 0 Articles

**Possible Reasons:**
1. Feed URL changed
2. Website blocking automated requests
3. Feed temporarily down
4. SSL certificate issues

**Solutions:**
1. Try alternative URL
2. Add user-agent header
3. Check website directly
4. Wait and retry later

### Example: Testing with User-Agent

```python
import feedparser

# Add user-agent to avoid blocking
feedparser.USER_AGENT = "Mozilla/5.0 (compatible; NewsBot/1.0)"
feed = feedparser.parse("https://www.jugantor.com/feed/rss.xml")
```

## Notes

- Some feeds may require specific user-agent headers
- RSS feeds can change URLs without notice
- Always have backup feeds
- Test feeds regularly
- Some websites may rate-limit RSS requests

---

**Last Updated:** December 20, 2025  
**Verified Feeds:** 2/10  
**Status:** Testing in progress
