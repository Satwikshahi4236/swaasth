# Swaasth Elder Health App - Setup Guide

This guide will help you set up and deploy the complete Swaasth Elder Health application stack.

## 🏗️ Architecture Overview

The application consists of:
- **Backend**: FastAPI (Python) with PostgreSQL database
- **Mobile App**: React Native with Expo
- **Web App**: React PWA with Material-UI
- **Infrastructure**: Docker containers with Redis for caching

## 📋 Prerequisites

### Required Software
- **Docker** (v20.0 or later) & **Docker Compose** (v2.0 or later)
- **Node.js** (v18 or later) & **npm**
- **Python** (v3.9 or later)
- **Git**

### Optional (for mobile development)
- **Expo CLI**: `npm install -g @expo/cli`
- **Android Studio** (for Android development)
- **Xcode** (for iOS development, macOS only)

## 🚀 Quick Start (Docker)

The fastest way to get the entire application running:

```bash
# Clone the repository
git clone <repository-url>
cd swaasth-elder-health

# Start all services with Docker Compose
./scripts/deploy.sh development

# Access the applications:
# - Web App: http://localhost:3000
# - API Documentation: http://localhost:8000/docs
# - Database: localhost:5432
```

## 🛠️ Development Setup

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configurations

# Start the backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Backend Environment Variables:**
```bash
DATABASE_URL=postgresql://swaasth_user:swaasth_password@localhost:5432/swaasth_db
JWT_SECRET_KEY=your-super-secret-jwt-key-change-this-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
REDIS_URL=redis://localhost:6379/0
DEBUG=true
```

### 2. Web App Setup

```bash
cd web

# Install dependencies
npm install

# Set up environment variables
echo "REACT_APP_API_URL=http://localhost:8000/api/v1" > .env

# Start development server
npm start
```

The web app will be available at http://localhost:3000

### 3. Mobile App Setup

```bash
cd mobile

# Install dependencies
npm install

# Start Expo development server
npx expo start

# Use Expo Go app on your phone to scan QR code
# Or press 'a' for Android emulator, 'i' for iOS simulator
```

### 4. Database Setup

```bash
# Using Docker (recommended)
docker run --name swaasth-postgres \
  -e POSTGRES_DB=swaasth_db \
  -e POSTGRES_USER=swaasth_user \
  -e POSTGRES_PASSWORD=swaasth_password \
  -p 5432:5432 \
  -d postgres:15-alpine

# Or install PostgreSQL locally and create database
```

### 5. Redis Setup (for background tasks)

```bash
# Using Docker
docker run --name swaasth-redis -p 6379:6379 -d redis:7-alpine

# Or install Redis locally
```

## 🌐 Production Deployment

### Using Docker Compose (Recommended)

```bash
# 1. Create production environment file
cp .env.example .env.prod

# 2. Update .env.prod with production values:
#    - Strong JWT secret
#    - Production database credentials
#    - Firebase credentials for push notifications
#    - CORS origins for your domain

# 3. Deploy to production
./scripts/deploy.sh production
```

### Using Railway (Cloud Platform)

1. **Backend Deployment:**
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy backend
cd backend
railway login
railway init
railway add postgresql
railway deploy
```

2. **Web App Deployment:**
```bash
cd web
railway init
railway deploy
```

### Using AWS/Google Cloud/Azure

The application is containerized and can be deployed to any cloud platform that supports Docker containers:

- **AWS**: ECS, EKS, or Elastic Beanstalk
- **Google Cloud**: Cloud Run, GKE, or App Engine
- **Azure**: Container Instances, AKS, or App Service

## 📱 Mobile App Distribution

### Development Testing
- Use Expo Go app for quick testing
- Generate development builds for device testing

### Production Release

1. **Build for App Stores:**
```bash
cd mobile

# For iOS
npx expo build:ios

# For Android
npx expo build:android
```

2. **Alternative - EAS Build:**
```bash
# Install EAS CLI
npm install -g @expo/eas-cli

# Configure and build
eas build --platform all
```

## 🔧 Configuration

### Backend Configuration

Key configuration options in `backend/app/config.py`:

- **Database**: PostgreSQL connection string
- **Authentication**: JWT settings
- **CORS**: Allowed origins for web requests
- **Firebase**: Push notification credentials
- **Redis**: Cache and queue settings

### Frontend Configuration

**Web App (.env):**
```bash
REACT_APP_API_URL=https://your-api-domain.com/api/v1
REACT_APP_ENVIRONMENT=production
```

**Mobile App (.env):**
```bash
API_BASE_URL=https://your-api-domain.com/api/v1
```

## 🔐 Security Considerations

### Production Security Checklist

- [ ] Change default JWT secret key
- [ ] Use HTTPS in production
- [ ] Configure proper CORS origins
- [ ] Set up database connection encryption
- [ ] Enable rate limiting
- [ ] Configure proper firewall rules
- [ ] Use environment variables for secrets
- [ ] Enable database backups
- [ ] Set up monitoring and logging

### Firebase Setup (for Push Notifications)

1. Create Firebase project
2. Generate service account key
3. Add credentials to backend environment:
```bash
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_PRIVATE_KEY=your-private-key
FIREBASE_CLIENT_EMAIL=your-service-account@project.iam.gserviceaccount.com
```

## 📊 Monitoring and Maintenance

### Health Checks

The application includes built-in health check endpoints:

- Backend: `GET /health`
- Web App: `GET /health`
- Database: Automatic health checks in Docker

### Logging

- Backend logs: Application and access logs
- Web App: Console and error logs
- Database: Query and error logs

### Backup Strategy

1. **Database Backups:**
```bash
# Automated backup script
docker exec swaasth-postgres pg_dump -U swaasth_user swaasth_db > backup_$(date +%Y%m%d).sql
```

2. **File Storage**: If using file uploads, ensure regular backups

### Updates and Maintenance

```bash
# Update application
git pull origin main
./scripts/deploy.sh production

# Update dependencies
cd backend && pip install -r requirements.txt --upgrade
cd web && npm update
cd mobile && npm update
```

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Issues:**
   - Check PostgreSQL is running
   - Verify connection string
   - Check firewall settings

2. **CORS Errors:**
   - Update CORS_ORIGINS in backend config
   - Ensure proper protocol (http/https)

3. **Mobile App Not Loading:**
   - Check API_BASE_URL configuration
   - Verify backend is accessible
   - Check network connectivity

4. **Push Notifications Not Working:**
   - Verify Firebase configuration
   - Check device permissions
   - Validate FCM tokens

### Logs and Debugging

```bash
# View application logs
docker-compose logs -f backend
docker-compose logs -f web

# Database logs
docker-compose logs -f database

# Real-time monitoring
docker-compose top
```

## 📞 Support

For technical support or questions:

1. Check the troubleshooting section above
2. Review application logs
3. Open an issue in the repository
4. Contact the development team

## 🤝 Contributing

See CONTRIBUTING.md for development guidelines and contribution instructions.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.