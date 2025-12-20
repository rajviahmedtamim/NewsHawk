"""
Analytics utilities - Trending topics and statistics
"""
from collections import Counter
from typing import List, Dict
from api.models import Article, TrendingTopic, Statistics


def analyze_trending_topics(articles: List[Article], limit: int = 10) -> List[TrendingTopic]:
    """
    Analyze trending topics from articles
    
    Args:
        articles: List of articles to analyze
        limit: Number of top topics to return
    
    Returns:
        List of trending topics
    """
    # Extract keywords from titles
    keywords = []
    keyword_languages = {}
    
    for article in articles:
        title_words = article.title.lower().split()
        
        # Filter common words and short words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        
        for word in title_words:
            # Clean word
            word = word.strip('.,!?;:()[]{}"\'-')
            
            # Skip if too short or stop word
            if len(word) < 4 or word in stop_words:
                continue
            
            keywords.append(word)
            
            # Track languages
            if word not in keyword_languages:
                keyword_languages[word] = set()
            keyword_languages[word].add(article.language)
    
    # Count keywords
    keyword_counts = Counter(keywords)
    total_articles = len(articles)
    
    # Create trending topics
    trending_topics = []
    for keyword, count in keyword_counts.most_common(limit):
        percentage = (count / total_articles) * 100 if total_articles > 0 else 0
        languages = list(keyword_languages.get(keyword, set()))
        
        # Simple trend detection (placeholder - could be improved with historical data)
        trend = "stable"
        if percentage > 15:
            trend = "up"
        elif percentage < 5:
            trend = "down"
        
        trending_topics.append(
            TrendingTopic(
                keyword=keyword,
                count=count,
                percentage=round(percentage, 2),
                languages=languages,
                trend=trend
            )
        )
    
    return trending_topics


def calculate_statistics(articles: List[Article]) -> Statistics:
    """
    Calculate overall statistics
    
    Args:
        articles: List of all articles
    
    Returns:
        Statistics object
    """
    # Count by language
    by_language = Counter(a.language for a in articles)
    
    # Count by source
    by_source = Counter(a.source for a in articles)
    
    # Get unique sources
    sources = set(a.source for a in articles)
    
    # Get categories
    categories = list(set(a.category for a in articles if a.category))
    
    # Get latest update time
    if articles:
        latest = max(articles, key=lambda x: x.published)
        last_updated = latest.published
    else:
        from datetime import datetime
        last_updated = datetime.now().isoformat()
    
    return Statistics(
        total_articles=len(articles),
        by_language=dict(by_language),
        by_source=dict(by_source),
        last_updated=last_updated,
        sources_count=len(sources),
        categories=sorted(categories)
    )


def get_category_counts(articles: List[Article]) -> Dict[str, int]:
    """
    Get article counts by category
    
    Args:
        articles: List of articles
    
    Returns:
        Dictionary of category counts
    """
    return dict(Counter(a.category for a in articles if a.category))
