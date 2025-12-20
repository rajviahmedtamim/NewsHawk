#!/bin/bash
# Cleanup script for NewsHawk project
# Removes unnecessary files and old output directories

echo "🧹 NewsHawk Cleanup Script"
echo "=========================="
echo ""

# Function to get directory size
get_size() {
    du -sh "$1" 2>/dev/null | cut -f1
}

# Show current sizes
echo "📊 Current Directory Sizes:"
echo "  output/              $(get_size output)"
echo "  output_bd/           $(get_size output_bd)"
echo "  output_bd_rss/       $(get_size output_bd_rss)"
echo "  output_google_news/  $(get_size output_google_news)"
echo "  output_google_news_en/ $(get_size output_google_news_en)"
echo "  output_google_news_bn/ $(get_size output_google_news_bn)"
echo ""

# Items to clean
echo "🗑️  Items to Clean:"
echo ""

# 1. Old/unused output directories
echo "1. Unused Output Directories:"
if [ -d "output" ] && [ "$(ls -A output 2>/dev/null)" ]; then
    echo "   ✓ output/ (old NewsHawk output - not used)"
else
    echo "   - output/ (empty or doesn't exist)"
fi

if [ -d "output_bd" ] && [ "$(ls -A output_bd 2>/dev/null)" ]; then
    echo "   ✓ output_bd/ (NewsAPI - limited use)"
else
    echo "   - output_bd/ (empty or doesn't exist)"
fi

if [ -d "output_google_news" ] && [ "$(ls -A output_google_news 2>/dev/null)" ]; then
    echo "   ✓ output_google_news/ (old combined output - replaced by _en and _bn)"
else
    echo "   - output_google_news/ (empty or doesn't exist)"
fi

# 2. System files
echo ""
echo "2. System Files:"
find . -name ".DS_Store" -type f | while read file; do
    echo "   ✓ $file"
done

# 3. Python cache
echo ""
echo "3. Python Cache:"
find . -name "*.pyc" -type f | while read file; do
    echo "   ✓ $file"
done
find . -name "__pycache__" -type d | while read dir; do
    echo "   ✓ $dir/"
done

echo ""
echo "=========================="
echo ""
echo "⚠️  WARNING: This will delete the above files/directories!"
echo ""
read -p "Do you want to proceed? (yes/no): " confirm

if [ "$confirm" = "yes" ]; then
    echo ""
    echo "🧹 Cleaning..."
    
    # Remove unused output directories
    if [ -d "output" ]; then
        rm -rf output
        echo "   ✓ Removed output/"
    fi
    
    if [ -d "output_bd" ]; then
        rm -rf output_bd
        echo "   ✓ Removed output_bd/"
    fi
    
    if [ -d "output_google_news" ]; then
        rm -rf output_google_news
        echo "   ✓ Removed output_google_news/"
    fi
    
    # Remove .DS_Store files
    find . -name ".DS_Store" -type f -delete
    echo "   ✓ Removed .DS_Store files"
    
    # Remove Python cache
    find . -name "*.pyc" -type f -delete
    find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
    echo "   ✓ Removed Python cache"
    
    echo ""
    echo "✅ Cleanup complete!"
    echo ""
    echo "📊 Remaining Output Directories:"
    echo "  output_bd_rss/       $(get_size output_bd_rss)"
    echo "  output_google_news_en/ $(get_size output_google_news_en)"
    echo "  output_google_news_bn/ $(get_size output_google_news_bn)"
else
    echo ""
    echo "❌ Cleanup cancelled"
fi
