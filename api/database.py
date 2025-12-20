"""
Database configuration and connection
Supports both SQLite (development) and PostgreSQL (production)
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from api.config import settings

# Database URL
# SQLite for development (no installation needed)
# PostgreSQL for production
if hasattr(settings, 'DATABASE_URL') and settings.DATABASE_URL:
    SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
else:
    # Default to SQLite
    SQLALCHEMY_DATABASE_URL = "sqlite:///./newshawk.db"

# Create engine
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    # PostgreSQL
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database - create all tables"""
    Base.metadata.create_all(bind=engine)
