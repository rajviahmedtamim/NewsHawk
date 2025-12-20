#!/usr/bin/env python3
"""
Google News RSS Fetcher for Bangladesh News - ENGLISH ONLY
Fetches English news from Google News RSS feeds focused on Bangladesh topics
No API key required - completely free!
"""

import feedparser
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict
from email.utils import parsedate_to_datetime

# Google News RSS feeds for Bangladesh - ENGLISH ONLY - LATEST NEWS (past 24 hours)
GOOGLE_NEWS_FEEDS = [
    {
        "name": "Google News - Bangladesh (Latest)",
        "url": "https://news.google.com/rss/search?q=Bangladesh+when:1d&hl=en-BD&gl=BD&ceid=BD:en",
        "language": "en"
    },
    {
        "name": "Google News - Bangladesh Politics (Latest)",
        "url": "https://news.google.com/rss/search?q=Bangladesh+politics+when:1d&hl=en-BD&gl=BD&ceid=BD:en",
        "language": "en"
    },
    {
        "name": "Google News - Bangladesh Cricket (Latest)",
        "url": "https://news.google.com/rss/search?q=Bangladesh+cricket+when:1d&hl=en-BD&gl=BD&ceid=BD:en",
        "language": "en"
    },
    {
        "name": "Google News - Dhaka (Latest)",
        "url": "https://news.google.com/rss/search?q=Dhaka+when:1d&hl=en-BD&gl=BD&ceid=BD:en",
        "language": "en"
    },
    {
        "name": "Google News - Bangladesh Economy (Latest)",
        "url": "https://news.google.com/rss/search?q=Bangladesh+economy+when:1d&hl=en-BD&gl=BD&ceid=BD:en",
        "language": "en"
    }
]

# Time filter - only show articles from last 24 hours
MAX_ARTICLE_AGE_HOURS = 24

def is_recent_article(published_date_str: str, max_hours: int = MAX_ARTICLE_AGE_HOURS) -> bool:
    """Check if article was published within the specified hours"""
    if not published_date_str:
        return True  # Include if no date (better to include than exclude)
    
    try:
        # Parse the published date
        published_date = parsedate_to_datetime(published_date_str)
        
        # Get current time
        now = datetime.now(published_date.tzinfo)
        
        # Calculate time difference
        time_diff = now - published_date
        
        # Check if within max hours
        return time_diff.total_seconds() <= (max_hours * 3600)
    except:
        return True  # Include if parsing fails

def fetch_rss_feed(feed_url: str, filter_recent: bool = True) -> List[Dict]:
    """Fetch and parse RSS feed, optionally filtering for recent articles only"""
    try:
        feed = feedparser.parse(feed_url)
        articles = []
        filtered_count = 0
        
        for entry in feed.entries:
            published = entry.get('published', '')
            
            # Filter by date if enabled
            if filter_recent and not is_recent_article(published):
                filtered_count += 1
                continue
            
            article = {
                'title': entry.get('title', 'No title'),
                'link': entry.get('link', ''),
                'published': published,
                'source': entry.get('source', {}).get('title', 'Unknown'),
                'description': entry.get('summary', '')
            }
            articles.append(article)
        
        if filtered_count > 0:
            print(f"(filtered {filtered_count} old articles)", end=' ')
        
        return articles
    except Exception as e:
        print(f"Error fetching feed: {e}")
        return []

def save_articles(all_articles: Dict[str, List[Dict]], output_dir: Path):
    """Save articles to TXT and JSON files"""
    # Create timestamp-based filename
    now = datetime.now()
    time_str = now.strftime("%H-%M")
    
    # Save as TXT
    txt_file = output_dir / f"{time_str}.txt"
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(f"Google News - Bangladesh LATEST News (Past 24 Hours)\n")
        f.write(f"Language: ENGLISH\n")
        f.write(f"Fetched at: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        
        total_count = sum(len(articles) for articles in all_articles.values())
        f.write(f"Total LATEST articles fetched: {total_count}\n")
        f.write(f"Filter: Only news from past {MAX_ARTICLE_AGE_HOURS} hours\n\n")

        for feed_name, articles in all_articles.items():
            f.write(f"\n{'='*80}\n")
            f.write(f"📰 {feed_name} ({len(articles)} articles)\n")
            f.write(f"{'='*80}\n\n")
            
            for idx, article in enumerate(articles, 1):
                f.write(f"{idx}. {article['title']}\n")
                f.write(f"   Source: {article['source']}\n")
                f.write(f"   Published: {article['published']}\n")
                f.write(f"   Link: {article['link']}\n")
                if article['description']:
                    f.write(f"   Description: {article['description'][:200]}...\n")
                f.write("\n")
    
    # Save as JSON
    json_file = output_dir / f"{time_str}.json"
    json_data = {
        'timestamp': now.isoformat(),
        'language': 'en',
        'total_articles': total_count,
        'feeds': all_articles
    }
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Saved {total_count} articles to:")
    print(f"   📄 {txt_file}")
    print(f"   📄 {json_file}")

def main():
    """Main function to fetch Google News RSS feeds"""
    print("🌐 Fetching Bangladesh news from Google News RSS feeds...")
    print("📰 Language: ENGLISH\n")
    
    # Create output directory
    now = datetime.now()
    date_folder = now.strftime("%Y-%m-%d")
    output_dir = Path("output_google_news_en") / date_folder
    output_dir.mkdir(parents=True, exist_ok=True)
    
    all_articles = {}
    
    for feed_info in GOOGLE_NEWS_FEEDS:
        feed_name = feed_info['name']
        feed_url = feed_info['url']
        
        print(f"📡 Fetching {feed_name}...", end=' ')
        articles = fetch_rss_feed(feed_url)
        
        if articles:
            all_articles[feed_name] = articles
            print(f"✅ {len(articles)} articles")
        else:
            print(f"⚠️  0 articles")
    
    if all_articles:
        save_articles(all_articles, output_dir)
    else:
        print("\n❌ No articles fetched from any feed")

if __name__ == "__main__":
    main()
