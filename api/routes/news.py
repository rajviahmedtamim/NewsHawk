"""
News API routes
"""
from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from datetime import datetime

from api.models import NewsResponse, SearchResponse, HealthResponse
from api.utils import (
    data_loader,
    filter_articles,
    search_articles,
    get_latest_articles
)
from api.config import settings

router = APIRouter(prefix="/news", tags=["news"])


@router.get("/", response_model=NewsResponse)
async def get_all_news(
    language: Optional[str] = Query("all", description="Language filter: en, bn, all"),
    source: Optional[str] = Query(None, description="Source filter"),
    limit: int = Query(settings.DEFAULT_LIMIT, le=settings.MAX_LIMIT),
    offset: int = Query(0, ge=0)
):
    """Get all news articles"""
    
    # Validate language
    if language not in ['en', 'bn', 'all']:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "INVALID_LANGUAGE",
                    "message": "Language must be 'en', 'bn', or 'all'",
                    "timestamp": datetime.now().isoformat()
                }
            }
        )
    
    # Load all articles
    articles = data_loader.load_all_news()
    
    # Apply filters
    filtered = filter_articles(
        articles,
        language=language,
        source=source,
        limit=limit,
        offset=offset
    )
    
    return NewsResponse(
        total=len(articles),
        count=len(filtered),
        language=language if language != 'all' else None,
        date=datetime.now().strftime("%Y-%m-%d"),
        articles=filtered
    )


@router.get("/english", response_model=NewsResponse)
async def get_english_news(
    limit: int = Query(settings.DEFAULT_LIMIT, le=settings.MAX_LIMIT),
    offset: int = Query(0, ge=0)
):
    """Get English news only"""
    articles = data_loader.load_latest_news(settings.OUTPUT_DIR_EN, "en")
    
    # Apply pagination
    filtered = filter_articles(articles, limit=limit, offset=offset)
    
    return NewsResponse(
        total=len(articles),
        count=len(filtered),
        language="en",
        date=datetime.now().strftime("%Y-%m-%d"),
        articles=filtered
    )


@router.get("/bangla", response_model=NewsResponse)
async def get_bangla_news(
    limit: int = Query(settings.DEFAULT_LIMIT, le=settings.MAX_LIMIT),
    offset: int = Query(0, ge=0)
):
    """Get Bangla news only (বাংলা)"""
    articles = data_loader.load_latest_news(settings.OUTPUT_DIR_BN, "bn")
    
    # Apply pagination
    filtered = filter_articles(articles, limit=limit, offset=offset)
    
    return NewsResponse(
        total=len(articles),
        count=len(filtered),
        language="bn",
        date=datetime.now().strftime("%Y-%m-%d"),
        articles=filtered
    )


@router.get("/search", response_model=SearchResponse)
async def search_news(
    q: str = Query(..., description="Search query"),
    language: Optional[str] = Query(None, description="Language filter: en, bn"),
    category: Optional[str] = Query(None, description="Category filter"),
    limit: int = Query(settings.DEFAULT_LIMIT, le=settings.MAX_LIMIT),
    offset: int = Query(0, ge=0)
):
    """Search news articles"""
    
    # Load all articles
    articles = data_loader.load_all_news()
    
    # Search
    results = search_articles(articles, q, language, category)
    
    # Apply pagination
    paginated = results[offset:offset+limit]
    
    return SearchResponse(
        query=q,
        total=len(results),
        count=len(paginated),
        articles=paginated
    )


@router.get("/latest", response_model=NewsResponse)
async def get_latest_news(
    limit: int = Query(20, le=100),
    language: Optional[str] = Query(None, description="Language filter: en, bn")
):
    """Get latest news articles"""
    
    # Load all articles
    articles = data_loader.load_all_news()
    
    # Filter by language if specified
    if language:
        articles = [a for a in articles if a.language == language]
    
    # Get latest
    latest = get_latest_articles(articles, limit)
    
    return NewsResponse(
        total=len(articles),
        count=len(latest),
        language=language,
        date=datetime.now().strftime("%Y-%m-%d"),
        articles=latest
    )


@router.get("/category/{category}", response_model=NewsResponse)
async def get_news_by_category(
    category: str,
    language: Optional[str] = Query(None, description="Language filter: en, bn"),
    limit: int = Query(settings.DEFAULT_LIMIT, le=settings.MAX_LIMIT)
):
    """Get news by category"""
    
    # Load all articles
    articles = data_loader.load_all_news()
    
    # Filter by category
    filtered = filter_articles(articles, language=language, category=category, limit=limit)
    
    if not filtered:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "NO_RESULTS",
                    "message": f"No articles found for category '{category}'",
                    "timestamp": datetime.now().isoformat()
                }
            }
        )
    
    return NewsResponse(
        total=len(filtered),
        count=len(filtered),
        language=language,
        date=datetime.now().strftime("%Y-%m-%d"),
        articles=filtered
    )


@router.get("/source/{source}", response_model=NewsResponse)
async def get_news_by_source(
    source: str,
    limit: int = Query(settings.DEFAULT_LIMIT, le=settings.MAX_LIMIT)
):
    """Get news from specific source"""
    
    # Load all articles
    articles = data_loader.load_all_news()
    
    # Filter by source
    filtered = filter_articles(articles, source=source, limit=limit)
    
    if not filtered:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "NO_RESULTS",
                    "message": f"No articles found from source '{source}'",
                    "timestamp": datetime.now().isoformat()
                }
            }
        )
    
    return NewsResponse(
        total=len(filtered),
        count=len(filtered),
        date=datetime.now().strftime("%Y-%m-%d"),
        articles=filtered
    )
