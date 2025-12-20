"""
Pydantic models for NewsHawk API
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Article(BaseModel):
    """Article model"""
    id: str = Field(..., description="Unique article identifier")
    title: str = Field(..., description="Article title")
    source: str = Field(..., description="News source name")
    url: str = Field(..., description="Article URL")
    published: str = Field(..., description="Publication datetime (ISO 8601)")
    language: str = Field(..., description="Language code (en or bn)")
    feed: str = Field(..., description="Feed name")
    description: Optional[str] = Field(None, description="Article summary")
    category: Optional[str] = Field(None, description="Auto-detected category")
    relevance: Optional[float] = Field(None, description="Search relevance score (0-1)")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "abc123",
                "title": "Bangladesh Cricket Team wins match",
                "source": "ESPN Cricinfo",
                "url": "https://news.google.com/...",
                "published": "2025-12-20T10:27:33Z",
                "language": "en",
                "feed": "Google News - Bangladesh Cricket",
                "description": "Bangladesh cricket team secured victory...",
                "category": "cricket",
                "relevance": 0.95
            }
        }


class NewsResponse(BaseModel):
    """Response model for news endpoints"""
    total: int = Field(..., description="Total articles available")
    count: int = Field(..., description="Number of articles in response")
    language: Optional[str] = Field(None, description="Language filter applied")
    date: Optional[str] = Field(None, description="Date filter applied")
    articles: list[Article] = Field(..., description="List of articles")


class SearchResponse(BaseModel):
    """Response model for search endpoints"""
    query: str = Field(..., description="Search query")
    total: int = Field(..., description="Total matching articles")
    count: int = Field(..., description="Number of articles in response")
    articles: list[Article] = Field(..., description="Matching articles")


class TrendingTopic(BaseModel):
    """Trending topic model"""
    keyword: str = Field(..., description="Topic keyword")
    count: int = Field(..., description="Article count")
    percentage: float = Field(..., description="Percentage of total articles")
    languages: list[str] = Field(..., description="Languages where topic appears")
    trend: str = Field(..., description="Trend direction: up, down, stable")

    class Config:
        json_schema_extra = {
            "example": {
                "keyword": "cricket",
                "count": 125,
                "percentage": 20.5,
                "languages": ["en", "bn"],
                "trend": "up"
            }
        }


class TrendingResponse(BaseModel):
    """Response model for trending endpoints"""
    period: str = Field(..., description="Time period analyzed")
    date: str = Field(..., description="Analysis date")
    topics: list[TrendingTopic] = Field(..., description="Trending topics")


class Statistics(BaseModel):
    """Statistics model"""
    total_articles: int = Field(..., description="Total articles")
    by_language: dict[str, int] = Field(..., description="Articles by language")
    by_source: dict[str, int] = Field(..., description="Articles by source")
    last_updated: str = Field(..., description="Last update timestamp")
    sources_count: int = Field(..., description="Number of sources")
    categories: list[str] = Field(..., description="Available categories")


class HealthResponse(BaseModel):
    """Health check response"""
    status: str = Field(..., description="API status")
    version: str = Field(..., description="API version")
    timestamp: str = Field(..., description="Current timestamp")


class ErrorResponse(BaseModel):
    """Error response model"""
    error: dict = Field(..., description="Error details")
    
    class Config:
        json_schema_extra = {
            "example": {
                "error": {
                    "code": "INVALID_LANGUAGE",
                    "message": "Language must be 'en', 'bn', or 'all'",
                    "timestamp": "2025-12-20T19:06:00Z"
                }
            }
        }
