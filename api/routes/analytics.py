"""
Statistics and trending API routes
"""
from fastapi import APIRouter, Query
from datetime import datetime

from api.models import TrendingResponse, Statistics
from api.utils import data_loader, analyze_trending_topics, calculate_statistics

router = APIRouter(tags=["analytics"])


@router.get("/trending", response_model=TrendingResponse)
async def get_trending_topics(
    language: str = Query("all", description="Language filter: en, bn, all"),
    limit: int = Query(10, le=50)
):
    """Get trending topics"""
    
    # Load articles
    articles = data_loader.load_all_news()
    
    # Filter by language if specified
    if language != 'all':
        articles = [a for a in articles if a.language == language]
    
    # Analyze trending topics
    topics = analyze_trending_topics(articles, limit)
    
    return TrendingResponse(
        period="today",
        date=datetime.now().strftime("%Y-%m-%d"),
        topics=topics
    )


@router.get("/stats", response_model=Statistics)
async def get_statistics():
    """Get overall statistics"""
    
    # Load all articles
    articles = data_loader.load_all_news()
    
    # Calculate statistics
    stats = calculate_statistics(articles)
    
    return stats
