"""
Routes package
"""
from .news import router as news_router
from .analytics import router as analytics_router

__all__ = ["news_router", "analytics_router"]
