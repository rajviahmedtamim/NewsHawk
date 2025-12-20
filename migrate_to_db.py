#!/usr/bin/env python3
"""
Migrate existing JSON data to database
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from api.database import init_db, SessionLocal
from api.crud import create_article, article_exists
from api.utils.data_loader import DataLoader
from api.models import Article

def migrate_data():
    """Migrate JSON data to database"""
    print("🔄 Starting data migration to database...")
    print("")
    
    # Initialize database
    print("📊 Creating database tables...")
    init_db()
    print("✅ Database initialized")
    print("")
    
    # Load data from JSON files
    print("📥 Loading articles from JSON files...")
    loader = DataLoader()
    
    # Load all articles
    all_articles = loader.load_all_news()
    print(f"✅ Loaded {len(all_articles)} articles from JSON files")
    print("")
    
    # Insert into database
    print("💾 Inserting articles into database...")
    db = SessionLocal()
    
    inserted = 0
    skipped = 0
    errors = 0
    
    try:
        for i, article in enumerate(all_articles, 1):
            try:
                # Check if article already exists
                if article_exists(db, article.id):
                    skipped += 1
                    continue
                
                # Insert article
                create_article(db, article)
                inserted += 1
                
                # Progress indicator
                if i % 100 == 0:
                    print(f"  Processed {i}/{len(all_articles)} articles...")
                    
            except Exception as e:
                errors += 1
                print(f"  ❌ Error inserting article {article.id}: {e}")
                continue
        
        print("")
        print("=" * 60)
        print("📊 Migration Summary:")
        print(f"  ✅ Inserted: {inserted} articles")
        print(f"  ⏭️  Skipped (duplicates): {skipped} articles")
        print(f"  ❌ Errors: {errors} articles")
        print(f"  📈 Total processed: {len(all_articles)} articles")
        print("=" * 60)
        print("")
        print("✅ Migration complete!")
        
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    migrate_data()
