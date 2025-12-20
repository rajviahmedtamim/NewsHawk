# 📖 NewsHawk - Complete Usage Guide

## Table of Contents

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Advanced Usage](#advanced-usage)
4. [Output Management](#output-management)
5. [Customization](#customization)
6. [Automation](#automation)
7. [Best Practices](#best-practices)

---

## Installation

### System Requirements

- **Operating System:** Linux, macOS, or Windows
- **Python:** 3.8 or higher
- **Disk Space:** ~100MB for code + outputs
- **Internet:** Required for fetching news

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/rajviahmedtamim/NewsHawk.git
cd NewsHawk
```

#### 2. Install Dependencies

```bash
# Install required Python packages
pip3 install feedparser

# Optional: Install all dependencies
pip3 install -r requirements.txt
```

#### 3. Verify Installation

```bash
# Test English fetcher
python3 fetch_google_news_en.py

# Test Bangla fetcher
python3 fetch_google_news_bn.py
```

---

## Basic Usage

### Fetching News

#### English News

```bash
python3 fetch_google_news_en.py
```

**Output:**
- Location: `output_google_news_en/YYYY-MM-DD/HH-MM.txt`
- Articles: ~330 per run
- Language: English only

#### Bangla News (বাংলা)

```bash
python3 fetch_google_news_bn.py
```

**Output:**
- Location: `output_google_news_bn/YYYY-MM-DD/HH-MM.txt`
- Articles: ~289 per run
- Language: Bangla only
- Interface: Fully in Bangla

#### Prothom Alo RSS

```bash
python3 fetch_bd_rss.py
```

**Output:**
- Location: `output_bd_rss/YYYY-MM-DD/HH-MM.txt`
- Articles: ~20 per run
- Language: Bangla
- Source: Prothom Alo direct RSS

#### NewsAPI (Optional)

```bash
# Requires API key in docker/.env
python3 fetch_bd_news.py
```

**Output:**
- Location: `output_bd/YYYY-MM-DD/HH-MM.txt`
- Articles: 1-3 per run (limited)
- Language: English
- Requires: Free API key from newsapi.org

### Viewing Results

#### View Latest English News

```bash
# View text file
cat output_google_news_en/$(date +%Y-%m-%d)/*.txt

# View JSON file
cat output_google_news_en/$(date +%Y-%m-%d)/*.json | python3 -m json.tool
```

#### View Latest Bangla News

```bash
# View text file
cat output_google_news_bn/$(date +%Y-%m-%d)/*.txt

# View JSON file
cat output_google_news_bn/$(date +%Y-%m-%d)/*.json | python3 -m json.tool
```

#### List All Output Files

```bash
# List all English news files
ls -lh output_google_news_en/

# List all Bangla news files
ls -lh output_google_news_bn/

# List all files from today
find output_google_news_* -name "$(date +%Y-%m-%d)" -type d
```

---

## Advanced Usage

### Fetch All Sources at Once

```bash
#!/bin/bash
# fetch_all.sh

echo "Fetching English news..."
python3 fetch_google_news_en.py

echo "Fetching Bangla news..."
python3 fetch_google_news_bn.py

echo "Fetching Prothom Alo RSS..."
python3 fetch_bd_rss.py

echo "All news fetched successfully!"
```

Make executable and run:
```bash
chmod +x fetch_all.sh
./fetch_all.sh
```

### Filter News by Keywords

```bash
# Search for specific topics in English news
grep -i "cricket" output_google_news_en/$(date +%Y-%m-%d)/*.txt

# Search for specific topics in Bangla news
grep "ক্রিকেট" output_google_news_bn/$(date +%Y-%m-%d)/*.txt

# Count articles about politics
grep -c "politics" output_google_news_en/$(date +%Y-%m-%d)/*.txt
```

### Extract Links Only

```bash
# Extract all links from English news
grep "Link:" output_google_news_en/$(date +%Y-%m-%d)/*.txt | cut -d' ' -f4

# Extract all links from Bangla news
grep "লিংক:" output_google_news_bn/$(date +%Y-%m-%d)/*.txt | awk '{print $2}'
```

### Parse JSON with jq

```bash
# Install jq (if not installed)
# macOS: brew install jq
# Linux: sudo apt install jq

# Get total article count
jq '.total_articles' output_google_news_en/$(date +%Y-%m-%d)/*.json

# Get all article titles
jq '.feeds[].[] | .title' output_google_news_en/$(date +%Y-%m-%d)/*.json

# Get articles from specific source
jq '.feeds["Google News - Bangladesh Cricket (Latest)"]' output_google_news_en/$(date +%Y-%m-%d)/*.json
```

---

## Output Management

### Organize by Date

```bash
# Create monthly archive
mkdir -p archives/$(date +%Y-%m)
mv output_google_news_en/$(date +%Y-%m)-* archives/$(date +%Y-%m)/

# Create compressed archive
tar -czf archives/news_$(date +%Y-%m).tar.gz output_google_news_*
```

### Clean Old Files

```bash
# Remove files older than 7 days
find output_google_news_en -type f -mtime +7 -delete
find output_google_news_bn -type f -mtime +7 -delete

# Remove files older than 30 days
find output_* -type f -mtime +30 -delete
```

### Backup to Cloud

```bash
# Backup to Google Drive (using rclone)
rclone sync output_google_news_en/ gdrive:NewsHawk/english/
rclone sync output_google_news_bn/ gdrive:NewsHawk/bangla/

# Backup to Dropbox
rclone sync output_google_news_en/ dropbox:NewsHawk/english/
```

---

## Customization

### Modify Time Filter

Edit the fetcher script to change the time window:

```python
# In fetch_google_news_en.py or fetch_google_news_bn.py

# Default: 24 hours
MAX_ARTICLE_AGE_HOURS = 24

# Change to 12 hours
MAX_ARTICLE_AGE_HOURS = 12

# Change to 48 hours
MAX_ARTICLE_AGE_HOURS = 48
```

### Add Custom Topics

Edit the `GOOGLE_NEWS_FEEDS` list in the fetcher:

```python
# In fetch_google_news_en.py
GOOGLE_NEWS_FEEDS = [
    # Existing feeds...
    
    # Add new topic
    {
        "name": "Google News - Bangladesh Technology (Latest)",
        "url": "https://news.google.com/rss/search?q=Bangladesh+technology+when:1d&hl=en-BD&gl=BD&ceid=BD:en",
        "language": "en"
    }
]
```

### Change Output Format

Modify the `save_articles()` function to customize output:

```python
def save_articles(all_articles, output_dir):
    # Add custom header
    f.write(f"Custom Header: My News Feed\n")
    
    # Change date format
    f.write(f"Date: {now.strftime('%d/%m/%Y %I:%M %p')}\n")
    
    # Add custom footer
    f.write(f"\n--- End of Report ---\n")
```

---

## Automation

### Cron Jobs (Linux/Mac)

#### Basic Cron Setup

```bash
# Edit crontab
crontab -e

# Fetch English news every 2 hours
0 */2 * * * cd /Users/wind-tamim/wokstation/NewsHawk && python3 fetch_google_news_en.py

# Fetch Bangla news every 2 hours
0 */2 * * * cd /Users/wind-tamim/wokstation/NewsHawk && python3 fetch_google_news_bn.py

# Fetch RSS every 3 hours
0 */3 * * * cd /Users/wind-tamim/wokstation/NewsHawk && python3 fetch_bd_rss.py
```

#### Advanced Cron with Logging

```bash
# Fetch with logging
0 */2 * * * cd /Users/wind-tamim/wokstation/NewsHawk && python3 fetch_google_news_en.py >> logs/english.log 2>&1

# Fetch with email notification
0 */2 * * * cd /Users/wind-tamim/wokstation/NewsHawk && python3 fetch_google_news_en.py && echo "News fetched" | mail -s "NewsHawk Update" your@email.com
```

#### Cron Schedule Examples

```bash
# Every hour
0 * * * * /path/to/script

# Every 30 minutes
*/30 * * * * /path/to/script

# Every day at 8 AM
0 8 * * * /path/to/script

# Every Monday at 9 AM
0 9 * * 1 /path/to/script

# Every 6 hours
0 */6 * * * /path/to/script
```

### Task Scheduler (Windows)

#### Create Scheduled Task

1. Open Task Scheduler
2. Click "Create Basic Task"
3. Name: "NewsHawk English Fetcher"
4. Trigger: Daily
5. Start time: 08:00 AM
6. Recur every: 1 days
7. Action: Start a program
8. Program: `C:\Python38\python.exe`
9. Arguments: `fetch_google_news_en.py`
10. Start in: `C:\Users\YourName\NewsHawk`

#### PowerShell Script

```powershell
# fetch_all.ps1
cd C:\Users\YourName\NewsHawk

Write-Host "Fetching English news..."
python fetch_google_news_en.py

Write-Host "Fetching Bangla news..."
python fetch_google_news_bn.py

Write-Host "Done!"
```

---

## Best Practices

### 1. Regular Fetching

- Fetch news every 2-3 hours for fresh content
- Avoid fetching more than once per hour (unnecessary load)
- Use cron/Task Scheduler for consistency

### 2. Storage Management

- Archive old files monthly
- Delete files older than 30 days
- Compress archives to save space

### 3. Error Handling

```bash
# Add error handling to cron
0 */2 * * * cd /path/to/NewsHawk && python3 fetch_google_news_en.py || echo "Fetch failed" | mail -s "NewsHawk Error" admin@example.com
```

### 4. Monitoring

```bash
# Check last fetch time
ls -lt output_google_news_en/ | head -5

# Count total articles today
find output_google_news_en/$(date +%Y-%m-%d) -name "*.txt" -exec wc -l {} \; | awk '{sum+=$1} END {print sum}'
```

### 5. Backup Strategy

- Daily: Sync to cloud storage
- Weekly: Create compressed archives
- Monthly: Long-term backup to external drive

---

## Troubleshooting

### Common Issues

#### 1. No Articles Fetched

```bash
# Check internet connection
ping -c 3 news.google.com

# Test feed URL directly
curl "https://news.google.com/rss?hl=bn&gl=BD&ceid=BD:bn"
```

#### 2. Encoding Issues

```bash
# Check file encoding
file -I output_google_news_bn/*/16-57.txt

# Convert encoding if needed
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt
```

#### 3. Permission Errors

```bash
# Fix permissions
chmod +x fetch_google_news_en.py
chmod +x fetch_google_news_bn.py

# Fix directory permissions
chmod -R 755 output_google_news_*
```

---

**For more help, see [README_NEWSHAWK.md](README_NEWSHAWK.md)**
