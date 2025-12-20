#!/bin/bash
# Start NewsHawk API server

echo "🚀 Starting NewsHawk API..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements-api.txt

echo ""
echo "✅ Dependencies installed"
echo ""
echo "🌐 Starting API server..."
echo "   - Swagger UI: http://localhost:8000/docs"
echo "   - ReDoc: http://localhost:8000/redoc"
echo "   - API: http://localhost:8000/api/v1"
echo ""

# Start server
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
