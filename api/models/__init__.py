"""
Models package
"""
from .article import (
    Article,
    NewsResponse,
    SearchResponse,
    TrendingTopic,
    TrendingResponse,
    Statistics,
    HealthResponse,
    ErrorResponse
)

__all__ = [
    "Article",
    "NewsResponse",
    "SearchResponse",
    "TrendingTopic",
    "TrendingResponse",
    "Statistics",
    "HealthResponse",
    "ErrorResponse"
]
