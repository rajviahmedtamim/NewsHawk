# 🇧🇩 NewsHawk - Quick Reference for Bangla News

## ✅ What's New

You now have **separate scripts** for English and Bangla news!

---

## 📥 Fetch News

### English News Only
```bash
python3 fetch_google_news_en.py
```
**Output:** `output_google_news_en/YYYY-MM-DD/HH-MM.txt`

### Bangla News Only (বাংলা)
```bash
python3 fetch_google_news_bn.py
```
**Output:** `output_google_news_bn/YYYY-MM-DD/HH-MM.txt`

### Both Languages
```bash
python3 fetch_google_news_en.py
python3 fetch_google_news_bn.py
```

---

## 📂 Output Directories

```
NewsHawk/
├── output_google_news_en/    # English news
│   └── 2025-12-20/
│       ├── 16-57.txt         # 330 articles
│       └── 16-57.json
│
└── output_google_news_bn/    # Bangla news (বাংলা)
    └── 2025-12-20/
        ├── 16-57.txt         # 289 articles
        └── 16-57.json
```

---

## 📊 What You Get

### English Fetcher
- ✅ 330+ articles per run
- ✅ Topics: Bangladesh, Politics, Cricket, Dhaka, Economy
- ✅ Sources: Reuters, BBC, Al Jazeera, Times of India, etc.
- ✅ Clean English interface

### Bangla Fetcher
- ✅ 289+ articles per run
- ✅ Topics: বাংলাদেশ, রাজনীতি, ক্রিকেট, ঢাকা, অর্থনীতি
- ✅ Sources: প্রথম আলো, বাংলাদেশ সংবাদ সংস্থা, etc.
- ✅ **Fully Bangla interface** (console + files)

---

## 🔄 Automate (Optional)

```bash
# Edit crontab
crontab -e

# Add these lines (fetch every 2 hours):
0 */2 * * * cd /Users/wind-tamim/wokstation/NewsHawk && python3 fetch_google_news_en.py
0 */2 * * * cd /Users/wind-tamim/wokstation/NewsHawk && python3 fetch_google_news_bn.py
```

---

## 🎯 Key Features

- ✅ **Separate folders** for each language
- ✅ **No API key required** - completely free
- ✅ **Latest news only** - past 24 hours
- ✅ **Bangla text support** - proper UTF-8 encoding
- ✅ **Both TXT and JSON** output formats

---

## 📝 Files

| File | Purpose |
|------|---------|
| `fetch_google_news_en.py` | English news fetcher |
| `fetch_google_news_bn.py` | Bangla news fetcher |
| `fetch_google_news.py` | Original (combined) |

---

**Enjoy your bilingual Bangladesh news! 🇧🇩**
