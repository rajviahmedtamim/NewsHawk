#!/usr/bin/env python3
"""
Test RSS Feeds - Verify which Bangladesh newspaper RSS feeds are working
"""

import feedparser
import sys

# Test feeds with alternatives
TEST_FEEDS = [
    # Working feeds
    ("Prothom Alo", "https://www.prothomalo.com/feed/"),
    ("Daily Star Frontpage", "https://www.thedailystar.net/frontpage/rss.xml"),
    
    # Test these with alternatives
    ("Jugantor - Option 1", "https://www.jugantor.com/feed/rss.xml"),
    ("Jugantor - Option 2", "https://www.jugantor.com/rss.xml"),
    
    ("Daily Star Latest - Option 1", "https://www.thedailystar.net/feeds/latest"),
    ("Daily Star Latest - Option 2", "https://www.thedailystar.net/rss.xml"),
    
    ("bdnews24 - Option 1", "https://bdnews24.com/?widgetName=rssfeed&widgetId=1150&getXmlFeed=true"),
    ("bdnews24 - Option 2", "https://bdnews24.com/rss/rss.xml"),
    ("bdnews24 - Option 3", "https://bdnews24.com/?widgetName=rssfeed&widgetId=1"),
    
    ("Dhaka Tribune - Option 1", "https://www.dhakatribune.com/feed"),
    ("Dhaka Tribune - Option 2", "https://www.dhakatribune.com/rss.xml"),
    
    ("New Age - Option 1", "https://www.newagebd.net/feed"),
    ("New Age - Option 2", "https://www.newagebd.net/rss.xml"),
    
    ("Business Standard - Option 1", "https://www.tbsnews.net/feed"),
    ("Business Standard - Option 2", "https://www.tbsnews.net/rss.xml"),
    
    ("Financial Express - Option 1", "https://thefinancialexpress.com.bd/feed"),
    ("Financial Express - Option 2", "https://thefinancialexpress.com.bd/rss.xml"),
    
    ("UNB - Option 1", "https://unb.com.bd/feed"),
    ("UNB - Option 2", "https://unb.com.bd/rss.xml"),
    
    # Additional feeds to test
    ("Kaler Kantho", "https://www.kalerkantho.com/rss.xml"),
    ("Samakal", "https://samakal.com/feed"),
    ("The Independent", "http://www.theindependentbd.com/feed"),
    ("Dhaka Post", "https://www.dhakapost.com/feed"),
]

def test_feed(name, url):
    """Test a single RSS feed"""
    try:
        print(f"Testing {name:40} ", end="")
        sys.stdout.flush()
        
        feed = feedparser.parse(url)
        
        if hasattr(feed, 'bozo') and feed.bozo:
            print(f"❌ Parse error")
            return False
        
        if not feed.entries:
            print(f"⚠️  0 articles")
            return False
        
        article_count = len(feed.entries)
        print(f"✅ {article_count} articles")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)[:30]}")
        return False

def main():
    print("🧪 Testing Bangladesh Newspaper RSS Feeds\n")
    print("=" * 80)
    
    working_feeds = []
    failed_feeds = []
    
    for name, url in TEST_FEEDS:
        if test_feed(name, url):
            working_feeds.append((name, url))
        else:
            failed_feeds.append((name, url))
    
    print("\n" + "=" * 80)
    print(f"\n✅ Working Feeds: {len(working_feeds)}")
    print(f"❌ Failed Feeds: {len(failed_feeds)}")
    
    if working_feeds:
        print("\n📋 Working Feeds List:")
        print("-" * 80)
        for name, url in working_feeds:
            print(f"  ✅ {name}")
            print(f"     {url}")
    
    if failed_feeds:
        print("\n❌ Failed Feeds:")
        print("-" * 80)
        for name, url in failed_feeds:
            print(f"  ❌ {name}")

if __name__ == "__main__":
    main()
