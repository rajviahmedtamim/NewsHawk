#!/usr/bin/env python3
"""
Bangladesh RSS News Fetcher
Fetches news from Bangladeshi news sources directly via RSS feeds
No API key needed - completely free!
"""

import feedparser
import json
from datetime import datetime
from pathlib import Path

# Bangladesh news RSS feeds - VERIFIED WORKING FEEDS ONLY
# Last tested: 2025-12-20
BD_RSS_FEEDS = [
    # === Bangla Language Newspapers ===
    {
        "name": "Prothom Alo (প্রথম আলো)",
        "url": "https://www.prothomalo.com/feed/",
        "language": "bn",
        "articles": "~20"
    },
    
    # === English Language Newspapers ===
    {
        "name": "The Daily Star - Frontpage",
        "url": "https://www.thedailystar.net/frontpage/rss.xml",
        "language": "en",
        "articles": "~20"
    },
    {
        "name": "The Daily Star - Latest News",
        "url": "https://www.thedailystar.net/rss.xml",
        "language": "en",
        "articles": "~10"
    },
    {
        "name": "The Business Standard",
        "url": "https://www.tbsnews.net/rss.xml",
        "language": "en",
        "articles": "~10"
    }
]

# Note: Many other Bangladesh newspaper RSS feeds are currently not working
# or have parsing errors. These 4 feeds are verified and tested.
# To test additional feeds, run: python3 test_rss_feeds.py

# Keywords to filter (optional)
KEYWORDS = [
    "cricket", "politics", "economy", "election",
    "hasina", "bnp", "awami", "dhaka", "chittagong"
]


def fetch_rss_feed(feed_info):
    """Fetch and parse RSS feed"""
    try:
        print(f"  Fetching from {feed_info['name']}...", end=" ")
        feed = feedparser.parse(feed_info['url'])
        
        articles = []
        for entry in feed.entries[:30]:  # Get top 30 from each source (increased from 20)
            article = {
                "title": entry.get('title', ''),
                "source": feed_info['name'],
                "language": feed_info['language'],
                "url": entry.get('link', ''),
                "published": entry.get('published', ''),
                "description": entry.get('summary', entry.get('description', ''))
            }
            articles.append(article)
        
        print(f"✅ {len(articles)} articles")
        return articles
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return []


def filter_by_keywords(articles, keywords=None):
    """Filter articles by keywords (optional)"""
    if not keywords:
        return articles
    
    filtered = []
    for article in articles:
        text = f"{article['title']} {article.get('description', '')}".lower()
        if any(keyword.lower() in text for keyword in keywords):
            filtered.append(article)
    
    return filtered


def save_articles(all_articles, output_dir="output_bd_rss", use_filter=False):
    """Save articles to files"""
    
    # Apply keyword filter if requested
    if use_filter and KEYWORDS:
        original_count = len(all_articles)
        all_articles = filter_by_keywords(all_articles, KEYWORDS)
        print(f"\n🔍 Filtered: {len(all_articles)} / {original_count} articles match keywords")
    
    if not all_articles:
        print("⚠️  No articles to save")
        return
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    now = datetime.now()
    date_folder = now.strftime("%Y-%m-%d")
    time_file = now.strftime("%H-%M")
    
    date_dir = Path(output_dir) / date_folder
    date_dir.mkdir(parents=True, exist_ok=True)
    
    txt_file = date_dir / f"{time_file}.txt"
    json_file = date_dir / f"{time_file}.json"
    
    # Save as text
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(f"Bangladesh News Report (RSS)\n")
        f.write(f"Generated: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Articles: {len(all_articles)}\n")
        f.write("=" * 80 + "\n\n")
        
        # Group by source
        sources = {}
        for article in all_articles:
            source = article['source']
            if source not in sources:
                sources[source] = []
            sources[source].append(article)
        
        for source, articles in sources.items():
            f.write(f"\n{'='*80}\n")
            f.write(f"{source} ({len(articles)} articles)\n")
            f.write(f"{'='*80}\n\n")
            
            for i, article in enumerate(articles, 1):
                f.write(f"{i}. {article['title']}\n")
                if article.get('published'):
                    f.write(f"   Published: {article['published']}\n")
                if article.get('url'):
                    f.write(f"   URL: {article['url']}\n")
                if article.get('description'):
                    # Limit description length
                    desc = article['description'][:200]
                    f.write(f"   {desc}...\n")
                f.write("\n")
    
    # Save as JSON
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(all_articles, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Saved {len(all_articles)} articles to:")
    print(f"   Text: {txt_file}")
    print(f"   JSON: {json_file}")
    
    return txt_file


def main():
    """Main function"""
    
    print("📰 Fetching Bangladesh news from RSS feeds...\n")
    
    all_articles = []
    
    for feed_info in BD_RSS_FEEDS:
        articles = fetch_rss_feed(feed_info)
        all_articles.extend(articles)
    
    print(f"\n📊 Total articles fetched: {len(all_articles)}")
    
    if all_articles:
        # Save without filtering (get all news)
        save_articles(all_articles, use_filter=False)
        
        # Optionally save filtered version
        # save_articles(all_articles, output_dir="output_bd_rss_filtered", use_filter=True)
    else:
        print("❌ No articles fetched")


if __name__ == "__main__":
    main()
