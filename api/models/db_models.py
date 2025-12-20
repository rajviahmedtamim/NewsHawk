"""
SQLAlchemy database models
"""
from sqlalchemy import Column, String, Text, DateTime, Integer, Index, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import JSON
from datetime import datetime
from api.database import Base, engine


# Use JSONB for PostgreSQL, JSON for SQLite
JSONType = JSONB if engine.dialect.name == 'postgresql' else JSON


class Article(Base):
    """Article database model"""
    __tablename__ = "articles"
    
    # Primary key
    id = Column(String(12), primary_key=True, index=True)
    
    # Article data
    title = Column(Text, nullable=False, index=True)
    source = Column(String(255), index=True)
    url = Column(Text)
    published = Column(DateTime, index=True)
    language = Column(String(2), index=True)
    feed = Column(String(255))
    description = Column(Text)
    category = Column(String(50), index=True)
    
    # Full article data as JSON
    content = Column(JSONType)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Indexes
    __table_args__ = (
        Index('idx_published_desc', published.desc()),
        Index('idx_lang_category', language, category),
        Index('idx_source_lang', source, language),
    )
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "source": self.source,
            "url": self.url,
            "published": self.published.isoformat() if self.published else None,
            "language": self.language,
            "feed": self.feed,
            "description": self.description,
            "category": self.category,
        }
    
    def __repr__(self):
        return f"<Article {self.id}: {self.title[:50]}>"
