"""
Search and filter utilities
"""
from typing import List, Optional
from api.models import Article


def search_articles(
    articles: List[Article],
    query: str,
    language: Optional[str] = None,
    category: Optional[str] = None
) -> List[Article]:
    """
    Search articles by query with optional filters
    
    Args:
        articles: List of articles to search
        query: Search query (case-insensitive)
        language: Optional language filter ('en', 'bn')
        category: Optional category filter
    
    Returns:
        List of matching articles with relevance scores
    """
    if not query:
        results = articles
    else:
        query_lower = query.lower()
        results = []
        
        for article in articles:
            # Calculate relevance score
            relevance = 0.0
            title_lower = article.title.lower()
            desc_lower = (article.description or '').lower()
            
            # Title match (higher weight)
            if query_lower in title_lower:
                relevance += 0.7
                # Exact match bonus
                if query_lower == title_lower:
                    relevance += 0.3
            
            # Description match
            if query_lower in desc_lower:
                relevance += 0.3
            
            # Source match
            if query_lower in article.source.lower():
                relevance += 0.2
            
            if relevance > 0:
                article.relevance = min(relevance, 1.0)
                results.append(article)
        
        # Sort by relevance
        results.sort(key=lambda x: x.relevance or 0, reverse=True)
    
    # Apply filters
    if language and language != 'all':
        results = [a for a in results if a.language == language]
    
    if category:
        results = [a for a in results if a.category == category]
    
    return results


def filter_articles(
    articles: List[Article],
    language: Optional[str] = None,
    category: Optional[str] = None,
    source: Optional[str] = None,
    limit: Optional[int] = None,
    offset: int = 0
) -> List[Article]:
    """
    Filter articles by various criteria
    
    Args:
        articles: List of articles to filter
        language: Language filter ('en', 'bn', 'all')
        category: Category filter
        source: Source filter
        limit: Maximum number of results
        offset: Pagination offset
    
    Returns:
        Filtered list of articles
    """
    results = articles
    
    # Apply filters
    if language and language != 'all':
        results = [a for a in results if a.language == language]
    
    if category:
        results = [a for a in results if a.category == category]
    
    if source:
        source_lower = source.lower()
        results = [a for a in results if source_lower in a.source.lower() or source_lower in a.feed.lower()]
    
    # Apply pagination
    if offset > 0:
        results = results[offset:]
    
    if limit:
        results = results[:limit]
    
    return results


def get_latest_articles(articles: List[Article], limit: int = 20) -> List[Article]:
    """
    Get latest articles sorted by publication date
    
    Args:
        articles: List of articles
        limit: Number of articles to return
    
    Returns:
        Latest articles
    """
    # Sort by published date (newest first)
    sorted_articles = sorted(
        articles,
        key=lambda x: x.published,
        reverse=True
    )
    
    return sorted_articles[:limit]
