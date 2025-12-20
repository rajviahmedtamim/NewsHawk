"""
CRUD operations for database
"""
from sqlalchemy.orm import Session
from sqlalchemy import func, desc, or_
from typing import List, Optional, Dict
from datetime import datetime, timedelta
from dateutil import parser as date_parser

from api.models.db_models import Article as DBArticle
from api.models import Article as ArticleModel


def parse_date(date_string: str) -> Optional[datetime]:
    """Parse date string in various formats"""
    if not date_string:
        return None
    try:
        # Use dateutil parser which handles many formats
        return date_parser.parse(date_string)
    except Exception:
        return None


def create_article(db: Session, article: ArticleModel) -> DBArticle:
    """Create new article in database"""
    db_article = DBArticle(
        id=article.id,
        title=article.title,
        source=article.source,
        url=article.url,
        published=parse_date(article.published),
        language=article.language,
        feed=article.feed,
        description=article.description,
        category=article.category,
        content=article.dict()
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_article(db: Session, article_id: str) -> Optional[DBArticle]:
    """Get article by ID"""
    return db.query(DBArticle).filter(DBArticle.id == article_id).first()


def get_articles(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    language: Optional[str] = None,
    category: Optional[str] = None,
    source: Optional[str] = None
) -> List[DBArticle]:
    """Get articles with filters"""
    query = db.query(DBArticle)
    
    if language and language != 'all':
        query = query.filter(DBArticle.language == language)
    
    if category:
        query = query.filter(DBArticle.category == category)
    
    if source:
        query = query.filter(DBArticle.source.ilike(f'%{source}%'))
    
    return query.order_by(desc(DBArticle.published)).offset(skip).limit(limit).all()


def search_articles(
    db: Session,
    query_text: str,
    skip: int = 0,
    limit: int = 100,
    language: Optional[str] = None
) -> List[DBArticle]:
    """Search articles by text"""
    query = db.query(DBArticle)
    
    # Simple text search (works with both SQLite and PostgreSQL)
    search_filter = or_(
        DBArticle.title.ilike(f'%{query_text}%'),
        DBArticle.description.ilike(f'%{query_text}%'),
        DBArticle.source.ilike(f'%{query_text}%')
    )
    query = query.filter(search_filter)
    
    if language and language != 'all':
        query = query.filter(DBArticle.language == language)
    
    return query.order_by(desc(DBArticle.published)).offset(skip).limit(limit).all()


def get_latest_articles(db: Session, limit: int = 20) -> List[DBArticle]:
    """Get latest articles"""
    return db.query(DBArticle).order_by(desc(DBArticle.published)).limit(limit).all()


def get_articles_by_category(
    db: Session,
    category: str,
    limit: int = 100
) -> List[DBArticle]:
    """Get articles by category"""
    return db.query(DBArticle).filter(
        DBArticle.category == category
    ).order_by(desc(DBArticle.published)).limit(limit).all()


def get_articles_by_source(
    db: Session,
    source: str,
    limit: int = 100
) -> List[DBArticle]:
    """Get articles by source"""
    return db.query(DBArticle).filter(
        DBArticle.source.ilike(f'%{source}%')
    ).order_by(desc(DBArticle.published)).limit(limit).all()


def count_articles(
    db: Session,
    language: Optional[str] = None,
    category: Optional[str] = None
) -> int:
    """Count articles with filters"""
    query = db.query(func.count(DBArticle.id))
    
    if language and language != 'all':
        query = query.filter(DBArticle.language == language)
    
    if category:
        query = query.filter(DBArticle.category == category)
    
    return query.scalar()


def get_statistics(db: Session) -> Dict:
    """Get database statistics"""
    total = db.query(func.count(DBArticle.id)).scalar()
    
    # Count by language
    lang_counts = db.query(
        DBArticle.language,
        func.count(DBArticle.id)
    ).group_by(DBArticle.language).all()
    
    by_language = {lang: count for lang, count in lang_counts}
    
    # Count by source
    source_counts = db.query(
        DBArticle.source,
        func.count(DBArticle.id)
    ).group_by(DBArticle.source).all()
    
    by_source = {source: count for source, count in source_counts}
    
    # Get categories
    categories = db.query(DBArticle.category).distinct().all()
    categories = [cat[0] for cat in categories if cat[0]]
    
    # Get latest update
    latest = db.query(DBArticle).order_by(desc(DBArticle.published)).first()
    last_updated = latest.published.isoformat() if latest and latest.published else None
    
    return {
        "total_articles": total,
        "by_language": by_language,
        "by_source": by_source,
        "last_updated": last_updated,
        "sources_count": len(by_source),
        "categories": sorted(categories)
    }


def delete_old_articles(db: Session, days: int = 30) -> int:
    """Delete articles older than specified days"""
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    deleted = db.query(DBArticle).filter(DBArticle.published < cutoff_date).delete()
    db.commit()
    return deleted


def article_exists(db: Session, article_id: str) -> bool:
    """Check if article exists"""
    return db.query(DBArticle).filter(DBArticle.id == article_id).count() > 0
