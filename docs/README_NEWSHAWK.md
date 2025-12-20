# 🇧🇩 NewsHawk - Bangladesh News Aggregator

**A customized fork of [TrendRadar](https://github.com/sansan0/TrendRadar) specifically designed for Bangladesh news monitoring**

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![RSS](https://img.shields.io/badge/RSS-Powered-orange.svg)](https://en.wikipedia.org/wiki/RSS)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [News Sources](#-news-sources)
- [Usage](#-usage)
- [Output Format](#-output-format)
- [Automation](#-automation)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Documentation](#-documentation)
- [Troubleshooting](#-troubleshooting)
- [Credits](#-credits)
- [License](#-license)

---

## 🎯 Overview

NewsHawk is a powerful news aggregation system that fetches, filters, and delivers Bangladesh-specific news from multiple sources. It supports both **English** and **Bangla (বাংলা)** languages with intelligent filtering and customizable notifications.

### Why NewsHawk?

- ✅ **Bilingual Support** - English and Bangla news in separate, organized folders
- ✅ **Multiple Sources** - Google News, RSS feeds, NewsAPI
- ✅ **Free & Unlimited** - No API keys required for primary sources
- ✅ **Smart Filtering** - Keyword-based filtering for relevant news only
- ✅ **Time-Based** - Only latest news from past 24 hours
- ✅ **Multiple Formats** - TXT and JSON output
- ✅ **Automation Ready** - Easy to schedule with cron
- ✅ **AI Analysis** - Optional MCP server for intelligent insights

---

## ✨ Features

### 🌐 Multi-Source News Aggregation

| Source | Articles | Language | API Required | Status |
|--------|----------|----------|--------------|--------|
| **Google News (English)** | 330+ | English | No | ✅ Active |
| **Google News (Bangla)** | 289+ | বাংলা | No | ✅ Active |
| **Prothom Alo RSS** | 20 | বাংলা | No | ✅ Active |
| **NewsAPI** | 1-3 | English | Yes (100/day) | ⚠️ Limited |

### 🎨 Key Capabilities

- **Separate Language Outputs** - English and Bangla news in dedicated directories
- **Topic-Specific Feeds** - Politics, Cricket, Economy, Dhaka, General News
- **Time Filtering** - Automatic filtering for news from past 24 hours
- **Smart Deduplication** - Removes duplicate articles across sources
- **UTF-8 Support** - Proper Bangla text encoding
- **Dual Format Output** - Both human-readable TXT and machine-readable JSON

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- `feedparser` library

### Installation

```bash
# Clone the repository
git clone https://github.com/rajviahmedtamim/NewsHawk.git
cd NewsHawk

# Install dependencies
pip3 install feedparser
```

### Fetch News

```bash
# English news only
python3 fetch_google_news_en.py

# Bangla news only (বাংলা)
python3 fetch_google_news_bn.py

# Both languages
python3 fetch_google_news_en.py && python3 fetch_google_news_bn.py
```

### View Results

```bash
# English news
cat output_google_news_en/$(date +%Y-%m-%d)/*.txt

# Bangla news
cat output_google_news_bn/$(date +%Y-%m-%d)/*.txt
```

---

## 📰 News Sources

### Google News RSS Feeds

#### English Feeds
- **General Bangladesh News** - Latest Bangladesh coverage
- **Politics** - Bangladesh political news
- **Cricket** - Bangladesh cricket updates
- **Dhaka** - Dhaka-specific news
- **Economy** - Bangladesh economic news

#### Bangla Feeds (বাংলা)
- **সাধারণ সংবাদ** - Latest Bangladesh news in Bangla
- **রাজনীতি** - Political news
- **ক্রিকেট** - Cricket updates
- **ঢাকা** - Dhaka news
- **অর্থনীতি** - Economic news

### RSS Feeds
- **Prothom Alo** - Leading Bangla newspaper
- Direct RSS feed, no API required

### NewsAPI (Optional)
- International Bangladesh coverage
- Requires free API key (100 requests/day)
- Setup: Add key to `docker/.env`

---

## 💻 Usage

### Basic Commands

```bash
# Fetch English news
python3 fetch_google_news_en.py

# Fetch Bangla news
python3 fetch_google_news_bn.py

# Fetch Prothom Alo RSS
python3 fetch_bd_rss.py

# Fetch NewsAPI (requires API key)
python3 fetch_bd_news.py
```

### Command Options

All fetchers support the following features:
- Automatic time filtering (past 24 hours)
- Duplicate removal
- UTF-8 encoding for Bangla text
- Both TXT and JSON output

---

## 📊 Output Format

### Directory Structure

```
NewsHawk/
├── output_google_news_en/     # English news
│   └── 2025-12-20/
│       ├── 16-57.txt          # 330 articles
│       └── 16-57.json
│
├── output_google_news_bn/     # Bangla news
│   └── 2025-12-20/
│       ├── 16-57.txt          # 289 articles
│       └── 16-57.json
│
├── output_bd_rss/             # Prothom Alo RSS
│   └── 2025-12-20/
│       ├── 17-33.txt
│       └── 17-33.json
│
└── output_bd/                 # NewsAPI
    └── 2025-12-20/
        ├── 17-29.txt
        └── 17-29.json
```

### TXT Format Example

```
Google News - Bangladesh LATEST News (Past 24 Hours)
Language: ENGLISH
Fetched at: 2025-12-20 16:57:37
================================================================================

Total LATEST articles fetched: 330
Filter: Only news from past 24 hours

================================================================================
📰 Google News - Bangladesh (Latest) (100 articles)
================================================================================

1. Bangladesh holds state mourning, funeral for slain uprising activist
   Source: Al Jazeera
   Published: Sat, 20 Dec 2025 10:27:33 GMT
   Link: https://news.google.com/...
   Description: ...

2. Bangladesh Protests News Live Updates...
   Source: Times of India
   Published: Sat, 20 Dec 2025 09:15:22 GMT
   Link: https://news.google.com/...
```

### JSON Format Example

```json
{
  "timestamp": "2025-12-20T16:57:37.123456",
  "language": "en",
  "total_articles": 330,
  "feeds": {
    "Google News - Bangladesh (Latest)": [
      {
        "title": "Bangladesh holds state mourning...",
        "link": "https://news.google.com/...",
        "published": "Sat, 20 Dec 2025 10:27:33 GMT",
        "source": "Al Jazeera",
        "description": "..."
      }
    ]
  }
}
```

---

## 🔄 Automation

### Using Cron (Linux/Mac)

```bash
# Edit crontab
crontab -e

# Add these lines (fetch every 2 hours):
0 */2 * * * cd /path/to/NewsHawk && python3 fetch_google_news_en.py
0 */2 * * * cd /path/to/NewsHawk && python3 fetch_google_news_bn.py
0 */3 * * * cd /path/to/NewsHawk && python3 fetch_bd_rss.py
```

### Using Task Scheduler (Windows)

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., every 2 hours)
4. Action: Start a program
5. Program: `python3`
6. Arguments: `fetch_google_news_en.py`
7. Start in: `C:\path\to\NewsHawk`

---

## ⚙️ Configuration

### NewsAPI Setup (Optional)

1. Get free API key from [newsapi.org](https://newsapi.org/register)
2. Edit `docker/.env`:
   ```env
   NEWS_API_KEY=your_api_key_here
   ```

### Custom Keywords

Edit `config/frequency_words.txt` to filter news by keywords:

```
# Politics
+Hasina
+BNP
+Awami League

# Cricket
+Bangladesh Cricket
+Tigers
+Shakib

# Business
+Dhaka Stock Exchange
+Grameen Bank
```

### Time Filter

Modify `MAX_ARTICLE_AGE_HOURS` in fetcher scripts:

```python
# Default: 24 hours
MAX_ARTICLE_AGE_HOURS = 24

# Change to 12 hours
MAX_ARTICLE_AGE_HOURS = 12
```

---

## 📂 Project Structure

```
NewsHawk/
├── 📜 News Fetchers
│   ├── fetch_google_news_en.py    # English Google News
│   ├── fetch_google_news_bn.py    # Bangla Google News
│   ├── fetch_bd_rss.py            # Prothom Alo RSS
│   ├── fetch_bd_news.py           # NewsAPI
│   └── fetch_google_news.py       # Original (combined)
│
├── ⚙️ Configuration
│   ├── config/
│   │   ├── config.yaml            # Main settings
│   │   └── frequency_words.txt    # Keywords
│   └── docker/.env                # API keys
│
├── 📊 Output Directories
│   ├── output_google_news_en/     # English news
│   ├── output_google_news_bn/     # Bangla news
│   ├── output_bd_rss/             # RSS news
│   └── output_bd/                 # NewsAPI
│
├── 🤖 AI Analysis (Optional)
│   ├── mcp_server/                # MCP server
│   └── main.py                    # NewsHawk core
│
└── 📚 Documentation
    ├── README.md                  # This file
    ├── QUICK_START.md             # Quick reference
    ├── BANGLA_NEWS_QUICK_START.md # Bangla guide
    ├── BANGLADESH_NEWS_GUIDE.md   # BD news sources
    └── SETUP_COMPLETE.md          # Setup summary
```

---

## 📚 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Quick reference guide
- **[BANGLA_NEWS_QUICK_START.md](BANGLA_NEWS_QUICK_START.md)** - Bangla news guide
- **[BANGLADESH_NEWS_GUIDE.md](BANGLADESH_NEWS_GUIDE.md)** - Bangladesh news sources
- **[SETUP_COMPLETE.md](SETUP_COMPLETE.md)** - Complete setup summary
- **[CONVERSION_SUMMARY.md](CONVERSION_SUMMARY.md)** - Translation details

---

## 🔧 Troubleshooting

### No Articles Returned

```bash
# Check internet connection
curl -I https://news.google.com

# Verify feed URLs manually
curl "https://news.google.com/rss?hl=bn&gl=BD&ceid=BD:bn"
```

### Bangla Text Not Displaying

- Ensure terminal supports UTF-8 encoding
- Use a font that supports Bangla characters
- Check file encoding: `file -I output_google_news_bn/*/16-57.txt`

### Old Cached Data

```bash
# Clear output directories
rm -rf output_google_news_en/2025*
rm -rf output_google_news_bn/2025*

# Fetch fresh data
python3 fetch_google_news_en.py
python3 fetch_google_news_bn.py
```

### Import Errors

```bash
# Install missing dependencies
pip3 install feedparser pytz requests pyyaml

# Or use requirements file
pip3 install -r requirements.txt
```

---

## 🤝 Credits

- **Original Project:** [TrendRadar](https://github.com/sansan0/TrendRadar) by [sansan0](https://github.com/sansan0)
- **Bangladesh Customization:** [rajviahmedtamim](https://github.com/rajviahmedtamim)
- **News Sources:**
  - Google News RSS
  - Prothom Alo
  - NewsAPI.org

---

## 📜 License

GPL-3.0 License - Same as original TrendRadar project

See [LICENSE](LICENSE) file for details.

---

## 🌟 Features Comparison

| Feature | NewsHawk (Bangladesh) | TrendRadar (Original) |
|---------|----------------------|----------------------|
| Language Support | English + Bangla | Chinese + English |
| Primary Source | Google News RSS | Chinese Platforms |
| API Required | No (optional) | No |
| Bangladesh Focus | ✅ Yes | ❌ No |
| Separate Language Outputs | ✅ Yes | ❌ No |
| Bangla Interface | ✅ Yes | ❌ No |

---

## 📞 Support

For issues or questions:
1. Check [Troubleshooting](#-troubleshooting) section
2. Review [Documentation](#-documentation)
3. Open an issue on GitHub

---

**Enjoy your Bangladesh news aggregator! 🇧🇩**

*Last Updated: December 20, 2025*
