"""
API Configuration
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """API Settings"""
    
    # API Info
    API_TITLE: str = "NewsHawk API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "Bangladesh News Aggregator API with bilingual support"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    
    # CORS
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
    ]
    
    # Data paths
    OUTPUT_DIR_EN: str = "output_google_news_en"
    OUTPUT_DIR_BN: str = "output_google_news_bn"
    OUTPUT_DIR_RSS: str = "output_bd_rss"
    
    # Database
    DATABASE_URL: str = "sqlite:///./newshawk.db"  # Default to SQLite
    # For PostgreSQL: "postgresql://user:password@localhost/newshawk"
    
    # Pagination
    DEFAULT_LIMIT: int = 100
    MAX_LIMIT: int = 1000
    
    # Cache
    CACHE_TTL: int = 300  # 5 minutes
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()
