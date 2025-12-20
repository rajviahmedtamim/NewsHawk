#!/bin/bash
# Quick commit and push script for NewsHawk

echo "📦 NewsHawk - Git Commit & Push"
echo "================================"
echo ""

# Check git status
echo "📊 Current Status:"
git status --short | head -20
echo ""

# Show what will be committed
echo "📝 Files to commit:"
git status --short | wc -l | xargs echo "   Total files changed:"
echo ""

# Ask for commit message
read -p "Enter commit message (or press Enter for default): " commit_msg

if [ -z "$commit_msg" ]; then
    commit_msg="Update NewsHawk: Bangladesh news aggregator

- Enhanced documentation
- Added verified RSS feeds
- Organized project structure
- Improved bilingual support"
fi

echo ""
echo "🔄 Committing changes..."

# Add all changes
git add .

# Commit
git commit -m "$commit_msg"

echo ""
echo "📤 Pushing to GitHub..."

# Push
git push origin main

echo ""
echo "✅ Done! Changes pushed to GitHub"
echo ""
echo "🔗 View your repository:"
echo "   https://github.com/rajviahmedtamim/NewsHawk"
