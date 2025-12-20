#!/usr/bin/env python3
"""
Bangladesh News Fetcher using NewsAPI
Get your free API key from: https://newsapi.org/
"""

import requests
import json
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from docker/.env file
load_dotenv("docker/.env")

# ========== CONFIGURATION ==========
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")  # Get from docker/.env file
KEYWORDS = [
    "Bangladesh",
    "Dhaka",
    "Cricket",
    "BNP",
    "Awami League",
    "Hasina"
]

# Bangladesh news sources
BD_SOURCES = "the-times-of-india,the-hindu"  # Add more as needed

# ========== FUNCTIONS ==========
def fetch_bangladesh_news(api_key, keywords, sources=None, page_size=50):
    """Fetch Bangladesh news using NewsAPI"""
    
    url = "https://newsapi.org/v2/everything"
    
    # Build query with keywords
    query = " OR ".join(keywords)
    
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": api_key
    }
    
    if sources:
        params["sources"] = sources
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching news: {e}")
        return None


def save_news(articles, output_dir="output_bd"):
    """Save news articles to file"""
    
    # Filter articles that actually mention Bangladesh keywords
    bd_keywords = ["bangladesh", "dhaka", "chittagong", "hasina", "bnp", "awami", 
                   "cricket bangladesh", "tigers", "shakib", "tamim", "mushfiqur"]
    
    filtered_articles = []
    for article in articles:
        title = (article.get('title') or '').lower()
        description = (article.get('description') or '').lower()
        content = (article.get('content') or '').lower()
        
        # Check if any Bangladesh keyword is in the article
        if any(keyword in title or keyword in description or keyword in content 
               for keyword in bd_keywords):
            filtered_articles.append(article)
    
    if not filtered_articles:
        print(f"⚠️  No Bangladesh-specific articles found in {len(articles)} results")
        return None
    
    print(f"✅ Filtered to {len(filtered_articles)} Bangladesh-specific articles (from {len(articles)} total)")
    
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
        f.write(f"Bangladesh News Report\n")
        f.write(f"Generated: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Articles: {len(filtered_articles)}\n")
        f.write("=" * 80 + "\n\n")
        
        for i, article in enumerate(filtered_articles, 1):
            f.write(f"{i}. {article['title']}\n")
            if article.get('source', {}).get('name'):
                f.write(f"   Source: {article['source']['name']}\n")
            if article.get('publishedAt'):
                f.write(f"   Published: {article['publishedAt']}\n")
            if article.get('url'):
                f.write(f"   URL: {article['url']}\n")
            if article.get('description'):
                f.write(f"   Description: {article['description']}\n")
            f.write("\n")
    
    # Save as JSON
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(filtered_articles, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved {len(filtered_articles)} articles to:")
    print(f"   Text: {txt_file}")
    print(f"   JSON: {json_file}")
    
    return txt_file


def main():
    """Main function"""
    
    if not NEWS_API_KEY:
        print("❌ Please set NEWS_API_KEY in docker/.env file!")
        print("   1. Open docker/.env file")
        print("   2. Add/update: NEWS_API_KEY=your_actual_api_key")
        print("   3. Get a free key from: https://newsapi.org/register")
        return
    
    print("📰 Fetching Bangladesh news...")
    print(f"   Keywords: {', '.join(KEYWORDS)}")
    
    data = fetch_bangladesh_news(
        api_key=NEWS_API_KEY,
        keywords=KEYWORDS,
        sources=None  # Remove sources to get all
    )
    
    if data and data.get("status") == "ok":
        articles = data.get("articles", [])
        print(f"✅ Found {len(articles)} articles")
        
        if articles:
            save_news(articles)
        else:
            print("ℹ️  No articles found")
    else:
        error_msg = data.get("message", "Unknown error") if data else "No response"
        print(f"❌ Error: {error_msg}")


if __name__ == "__main__":
    main()
