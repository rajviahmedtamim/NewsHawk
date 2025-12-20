"""
Data loader utility - Load news from JSON files
"""
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
from api.models import Article


class DataLoader:
    """Load and manage news data from JSON files"""
    
    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self._cache = {}
        self._cache_time = {}
    
    def _generate_article_id(self, article: dict) -> str:
        """Generate unique ID for article"""
        unique_string = f"{article.get('title', '')}{article.get('link', '')}{article.get('published', '')}"
        return hashlib.md5(unique_string.encode()).hexdigest()[:12]
    
    def _detect_category(self, feed_name: str, title: str) -> str:
        """Auto-detect article category"""
        feed_lower = feed_name.lower()
        title_lower = title.lower()
        
        if 'cricket' in feed_lower or 'cricket' in title_lower or 'ক্রিকেট' in title_lower:
            return 'cricket'
        elif 'politics' in feed_lower or 'politics' in title_lower or 'রাজনীতি' in title_lower:
            return 'politics'
        elif 'economy' in feed_lower or 'economy' in title_lower or 'অর্থনীতি' in title_lower:
            return 'economy'
        elif 'dhaka' in feed_lower or 'dhaka' in title_lower or 'ঢাকা' in title_lower:
            return 'dhaka'
        else:
            return 'general'
    
    def _load_json_file(self, file_path: Path) -> Dict:
        """Load single JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return {}
    
    def _parse_article(self, article_data: dict, feed_name: str, language: str) -> Article:
        """Parse article data into Article model"""
        article_id = self._generate_article_id(article_data)
        category = self._detect_category(feed_name, article_data.get('title', ''))
        
        return Article(
            id=article_id,
            title=article_data.get('title', 'No title'),
            source=article_data.get('source', 'Unknown'),
            url=article_data.get('link', article_data.get('url', '')),
            published=article_data.get('published', ''),
            language=language,
            feed=feed_name,
            description=article_data.get('description', article_data.get('summary', '')),
            category=category
        )
    
    def load_latest_news(self, output_dir: str, language: str) -> List[Article]:
        """Load latest news from output directory"""
        cache_key = f"{output_dir}_{language}"
        
        # Check cache (5 min TTL)
        if cache_key in self._cache:
            cache_age = (datetime.now() - self._cache_time[cache_key]).seconds
            if cache_age < 300:  # 5 minutes
                return self._cache[cache_key]
        
        articles = []
        output_path = self.base_dir / output_dir
        
        if not output_path.exists():
            return articles
        
        # Get latest date folder
        date_folders = sorted([d for d in output_path.iterdir() if d.is_dir()], reverse=True)
        
        if not date_folders:
            return articles
        
        latest_folder = date_folders[0]
        
        # Load all JSON files from latest folder
        json_files = sorted(latest_folder.glob("*.json"), reverse=True)
        
        if not json_files:
            return articles
        
        # Load latest JSON file
        latest_file = json_files[0]
        data = self._load_json_file(latest_file)
        
        if not data:
            return articles
        
        # Parse articles
        # Handle both dict with 'feeds' key and direct dict of feeds
        if 'feeds' in data:
            feeds = data['feeds']
        else:
            feeds = data
        
        # feeds should be a dict of feed_name -> list of articles
        if isinstance(feeds, dict):
            for feed_name, feed_articles in feeds.items():
                if isinstance(feed_articles, list):
                    for article_data in feed_articles:
                        try:
                            article = self._parse_article(article_data, feed_name, language)
                            articles.append(article)
                        except Exception as e:
                            print(f"Error parsing article from {feed_name}: {e}")
                            continue
        elif isinstance(feeds, list):
            # If it's a list, treat as single feed
            for article_data in feeds:
                try:
                    article = self._parse_article(article_data, "Unknown Feed", language)
                    articles.append(article)
                except Exception as e:
                    print(f"Error parsing article: {e}")
                    continue
        
        # Cache results
        self._cache[cache_key] = articles
        self._cache_time[cache_key] = datetime.now()
        
        return articles
    
    def load_all_news(self) -> List[Article]:
        """Load all news from all sources"""
        all_articles = []
        
        # Load English news
        all_articles.extend(self.load_latest_news("output_google_news_en", "en"))
        
        # Load Bangla news
        all_articles.extend(self.load_latest_news("output_google_news_bn", "bn"))
        
        # Load RSS news
        rss_articles = self.load_latest_news("output_bd_rss", "mixed")
        # Detect language for RSS articles
        for article in rss_articles:
            # Simple language detection based on feed name
            if 'প্রথম আলো' in article.feed or 'বাংলা' in article.feed:
                article.language = 'bn'
            else:
                article.language = 'en'
        all_articles.extend(rss_articles)
        
        return all_articles
    
    def clear_cache(self):
        """Clear data cache"""
        self._cache = {}
        self._cache_time = {}


# Global data loader instance
data_loader = DataLoader()
