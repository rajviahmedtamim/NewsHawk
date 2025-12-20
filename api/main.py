"""
NewsHawk FastAPI Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime

from api.config import settings
from api.models import HealthResponse
from api.routes import news_router, analytics_router

# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description=settings.API_DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check():
    """API health check"""
    return HealthResponse(
        status="healthy",
        version=settings.API_VERSION,
        timestamp=datetime.now().isoformat()
    )


# Root endpoint
@app.get("/", tags=["root"])
async def root():
    """API root endpoint"""
    return {
        "message": "NewsHawk API - Bangladesh News Aggregator",
        "version": settings.API_VERSION,
        "docs": "/docs",
        "health": "/health",
        "endpoints": {
            "news": "/api/v1/news",
            "search": "/api/v1/news/search",
            "trending": "/api/v1/trending",
            "stats": "/api/v1/stats"
        }
    }


# Include routers with API prefix
app.include_router(news_router, prefix="/api/v1")
app.include_router(analytics_router, prefix="/api/v1")


# Exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": str(exc),
                "timestamp": datetime.now().isoformat()
            }
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )
