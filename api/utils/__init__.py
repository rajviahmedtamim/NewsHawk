"""
Utils package
"""
from .data_loader import data_loader
from .search import search_articles, filter_articles, get_latest_articles
from .analytics import analyze_trending_topics, calculate_statistics, get_category_counts

__all__ = [
    "data_loader",
    "search_articles",
    "filter_articles",
    "get_latest_articles",
    "analyze_trending_topics",
    "calculate_statistics",
    "get_category_counts"
]
