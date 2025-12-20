# 🇧🇩 NewsHawk - Bangladesh News Aggregator

**A customized fork of [TrendRadar](https://github.com/sansan0/TrendRadar) for Bangladesh news monitoring**

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![RSS](https://img.shields.io/badge/RSS-Powered-orange.svg)](https://en.wikipedia.org/wiki/RSS)

---

## 📖 Documentation

**👉 [Complete Setup Guide](SETUP_GUIDE.md)** - Start here for step-by-step setup instructions!

**📚 [All Documentation](docs/README.md)** - Browse all guides and references

---

## 🚀 Quick Start

```bash
# Fetch English news
python3 fetch_google_news_en.py

# Fetch Bangla news (বাংলা)
python3 fetch_google_news_bn.py

# Fetch RSS news
python3 fetch_bd_rss.py
```

---

## ✨ Features

- **Bilingual Support** - English and Bangla news in separate folders
- **Multiple Sources** - Google News RSS (free, unlimited) + Bangladesh newspapers
- **Smart Filtering** - Only latest news from past 24 hours
- **Dual Format** - Both TXT and JSON output
- **No API Required** - Primary sources are completely free

---

## 📊 News Sources

| Source | Articles | Language | API Required |
|--------|----------|----------|--------------|
| Google News (English) | 330+ | English | No |
| Google News (Bangla) | 289+ | বাংলা | No |
| RSS Feeds | 60 | Both | No |

**Total:** ~679 articles per fetch

---

## 📂 Project Structure

```
NewsHawk/
├── 📜 News Fetchers
│   ├── fetch_google_news_en.py    # English Google News
│   ├── fetch_google_news_bn.py    # Bangla Google News
│   └── fetch_bd_rss.py            # Bangladesh RSS feeds
│
├── 📊 Output Directories
│   ├── output_google_news_en/     # English news
│   ├── output_google_news_bn/     # Bangla news
│   └── output_bd_rss/             # RSS news
│
├── ⚙️ Configuration
│   ├── config/config.yaml         # Settings
│   └── docker/.env                # API keys
│
└── 📚 Documentation
    └── docs/                      # All documentation files
```

---

## 📚 Documentation

**Main Documentation:**
- **[docs/README_NEWSHAWK.md](docs/README_NEWSHAWK.md)** - Complete project guide
- **[docs/DOCUMENTATION_INDEX.md](docs/DOCUMENTATION_INDEX.md)** - Documentation hub

**Quick Guides:**
- **[docs/QUICK_START.md](docs/QUICK_START.md)** - Quick reference
- **[docs/BANGLA_NEWS_QUICK_START.md](docs/BANGLA_NEWS_QUICK_START.md)** - Bangla guide

**Detailed Guides:**
- **[docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md)** - Complete usage guide
- **[docs/API_REFERENCE.md](docs/API_REFERENCE.md)** - API & RSS reference
- **[docs/BANGLADESH_NEWS_GUIDE.md](docs/BANGLADESH_NEWS_GUIDE.md)** - BD news sources

**Setup & Reference:**
- **[docs/SETUP_COMPLETE.md](docs/SETUP_COMPLETE.md)** - Setup summary
- **[docs/BD_RSS_FEEDS_LIST.md](docs/BD_RSS_FEEDS_LIST.md)** - RSS feeds list
- **[docs/CLEANUP_GUIDE.md](docs/CLEANUP_GUIDE.md)** - Cleanup guide

---

## 🔧 Installation

```bash
# Clone repository
git clone https://github.com/rajviahmedtamim/NewsHawk.git
cd NewsHawk

# Install dependencies
pip3 install feedparser

# Test
python3 fetch_google_news_en.py
```

---

## 💻 Usage

### Fetch News

```bash
# English news (330+ articles)
python3 fetch_google_news_en.py

# Bangla news (289+ articles)
python3 fetch_google_news_bn.py

# RSS feeds (60 articles)
python3 fetch_bd_rss.py
```

### View Results

```bash
# View latest English news
cat output_google_news_en/$(date +%Y-%m-%d)/*.txt

# View latest Bangla news
cat output_google_news_bn/$(date +%Y-%m-%d)/*.txt

# View RSS news
cat output_bd_rss/$(date +%Y-%m-%d)/*.txt
```

---

## 🔄 Automation

```bash
# Edit crontab
crontab -e

# Add these lines (fetch every 2 hours):
0 */2 * * * cd /path/to/NewsHawk && python3 fetch_google_news_en.py
0 */2 * * * cd /path/to/NewsHawk && python3 fetch_google_news_bn.py
0 */3 * * * cd /path/to/NewsHawk && python3 fetch_bd_rss.py
```

---

## 🛠️ Utilities

```bash
# Test RSS feeds
python3 test_rss_feeds.py

# Clean up old files
./cleanup.sh
```

---

## 📖 Learn More

- **Full Documentation:** [docs/README_NEWSHAWK.md](docs/README_NEWSHAWK.md)
- **Usage Guide:** [docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md)
- **API Reference:** [docs/API_REFERENCE.md](docs/API_REFERENCE.md)
- **Documentation Index:** [docs/DOCUMENTATION_INDEX.md](docs/DOCUMENTATION_INDEX.md)

---

## 🤝 Credits

- **Original Project:** [TrendRadar](https://github.com/sansan0/TrendRadar) by [sansan0](https://github.com/sansan0)
- **Bangladesh Fork:** [rajviahmedtamim](https://github.com/rajviahmedtamim)

---

## 📜 License

GPL-3.0 License - Same as original TrendRadar

---

**Enjoy your Bangladesh news aggregator! 🇧🇩**