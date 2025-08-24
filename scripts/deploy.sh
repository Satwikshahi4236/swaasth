#!/bin/bash

# Swaasth Elder Health App Deployment Script
set -e

echo "🚀 Starting Swaasth Elder Health App Deployment..."

# Configuration
ENVIRONMENT=${1:-development}
echo "📋 Environment: $ENVIRONMENT"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "🔍 Checking prerequisites..."

if ! command_exists docker; then
    echo "❌ Docker is not installed. Please install Docker and try again."
    exit 1
fi

if ! command_exists docker-compose; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose and try again."
    exit 1
fi

echo "✅ Prerequisites check passed!"

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p logs
mkdir -p data/postgres
mkdir -p data/redis

# Environment specific configurations
if [ "$ENVIRONMENT" = "production" ]; then
    echo "🏭 Setting up production environment..."
    COMPOSE_FILE="docker-compose.prod.yml"
    
    # Check if production secrets exist
    if [ ! -f ".env.prod" ]; then
        echo "❌ Production environment file (.env.prod) not found!"
        echo "Please create .env.prod with production configurations."
        exit 1
    fi
    
    # Load production environment
    export $(grep -v '^#' .env.prod | xargs)
    
elif [ "$ENVIRONMENT" = "staging" ]; then
    echo "🔧 Setting up staging environment..."
    COMPOSE_FILE="docker-compose.staging.yml"
    
else
    echo "🛠️ Setting up development environment..."
    COMPOSE_FILE="docker-compose.yml"
fi

# Build and start services
echo "🏗️ Building and starting services..."

if [ "$ENVIRONMENT" = "production" ]; then
    # Production deployment
    docker-compose -f $COMPOSE_FILE down --remove-orphans
    docker-compose -f $COMPOSE_FILE pull
    docker-compose -f $COMPOSE_FILE up -d --build
else
    # Development/Staging deployment
    docker-compose -f $COMPOSE_FILE down --remove-orphans
    docker-compose -f $COMPOSE_FILE up -d --build
fi

# Wait for services to be healthy
echo "⏳ Waiting for services to be healthy..."
sleep 30

# Check service health
echo "🏥 Checking service health..."

# Check database
if docker-compose -f $COMPOSE_FILE exec -T database pg_isready -U swaasth_user -d swaasth_db; then
    echo "✅ Database is healthy"
else
    echo "❌ Database health check failed"
fi

# Check backend
if curl -f http://localhost:8000/health >/dev/null 2>&1; then
    echo "✅ Backend is healthy"
else
    echo "❌ Backend health check failed"
fi

# Check web app
if curl -f http://localhost:3000/health >/dev/null 2>&1; then
    echo "✅ Web app is healthy"
else
    echo "❌ Web app health check failed"
fi

# Run database migrations
echo "🗃️ Running database migrations..."
docker-compose -f $COMPOSE_FILE exec -T backend alembic upgrade head

# Display service information
echo "📊 Service Information:"
echo "========================"
docker-compose -f $COMPOSE_FILE ps

echo ""
echo "🌐 Application URLs:"
echo "========================"
echo "📱 Web App: http://localhost:3000"
echo "🔧 API Documentation: http://localhost:8000/docs"
echo "📊 API Health Check: http://localhost:8000/health"

if [ "$ENVIRONMENT" = "development" ]; then
    echo "🗃️ Database: localhost:5432"
    echo "🔴 Redis: localhost:6379"
fi

echo ""
echo "✅ Deployment completed successfully!"
echo ""
echo "📝 Useful commands:"
echo "  - View logs: docker-compose -f $COMPOSE_FILE logs -f"
echo "  - Stop services: docker-compose -f $COMPOSE_FILE down"
echo "  - Restart services: docker-compose -f $COMPOSE_FILE restart"
echo "  - Update services: ./scripts/deploy.sh $ENVIRONMENT"