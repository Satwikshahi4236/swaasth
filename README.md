# Swaasth Elder Health App

![CI/CD Pipeline](https://github.com/swaasth/elder-health/actions/workflows/ci-cd.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Node.js](https://img.shields.io/badge/node.js-18+-green.svg)
![React](https://img.shields.io/badge/react-18-blue.svg)
![React Native](https://img.shields.io/badge/react%20native-0.72-blue.svg)

A comprehensive health application designed for elder care with personalized medicine reminders and secure family communication features.

> **✅ PR-Ready**: This project is production-ready and fully set up for Pull Requests with CI/CD, testing, linting, and comprehensive documentation.

## 🎯 Features

- **Medicine Reminders**: Personalized medication schedules with push notifications
- **Family Communication**: Secure messaging between family members and caregivers
- **Health Tracking**: Monitor vital signs, symptoms, and medication adherence
- **Privacy-Focused**: End-to-end encryption for sensitive health data
- **Cross-Platform**: Available on mobile (Android/iOS) and desktop (PWA)

## 🏗️ Tech Stack

### Frontend
- **React Native**: Cross-platform mobile app (Android + iOS)
- **React Native Paper**: Material Design UI components
- **React Navigation**: Navigation and routing
- **PWA**: Progressive Web App for desktop access

### Backend
- **FastAPI**: High-performance Python API framework
- **PostgreSQL**: Main relational database
- **SQLAlchemy**: ORM for database operations
- **JWT**: Authentication and authorization

### Cloud & Deployment
- **Docker**: Containerization
- **Railway**: Cloud hosting platform
- **GitHub Actions**: CI/CD pipeline

## 📁 Project Structure

```
swaasth-elder-health/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # FastAPI app entry point
│   │   ├── models/         # Database models
│   │   ├── routes/         # API endpoints
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utility functions
│   ├── tests/              # Backend tests
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile         # Backend container
├── mobile/                 # React Native app
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── screens/        # App screens
│   │   ├── services/       # API services
│   │   └── utils/          # Utility functions
│   ├── package.json
│   └── app.json
├── web/                    # PWA for desktop
│   ├── public/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   └── services/       # API services
│   └── package.json
├── scripts/                # Deployment scripts
├── .github/workflows/      # CI/CD pipelines
└── docker-compose.yml      # Development environment
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- Docker & Docker Compose
- PostgreSQL (or use Docker)

### Quick Start with Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/your-username/swaasth-elder-health.git
cd swaasth-elder-health

# Start all services
./scripts/deploy.sh development

# Access the applications:
# - Web App: http://localhost:3000
# - API Documentation: http://localhost:8000/docs
# - API Health Check: http://localhost:8000/health
```

### Development Setup

#### 1. Backend Setup

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

#### 2. Web App Setup

```bash
cd web

# Install dependencies
npm install

# Set up environment variables
echo "REACT_APP_API_URL=http://localhost:8000/api/v1" > .env

# Start development server
npm start
```

#### 3. Mobile App Setup

```bash
cd mobile

# Install dependencies
npm install

# Start Expo development server
npx expo start

# Use Expo Go app on your phone to scan QR code
# Or press 'a' for Android emulator, 'i' for iOS simulator
```

## 🧪 Testing

### Run All Tests

```bash
# Backend tests
cd backend && python -m pytest tests/ -v

# Frontend tests
cd web && npm test

# Mobile type checking
cd mobile && npm run type-check

# Linting
cd backend && flake8 app/
```

### CI/CD Pipeline

The project includes a comprehensive GitHub Actions pipeline that:

- ✅ **Tests backend** with pytest and PostgreSQL
- ✅ **Tests frontend** with Jest and React Testing Library
- ✅ **Type checks mobile** app with TypeScript
- ✅ **Lints code** with flake8 and ESLint
- ✅ **Builds Docker images** for production
- ✅ **Deploys automatically** on main branch

## 🔧 Configuration

### Backend Environment Variables
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/swaasth_db
JWT_SECRET_KEY=your-super-secret-jwt-key-change-this-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
REDIS_URL=redis://localhost:6379/0
DEBUG=true
```

### Frontend Environment Variables
```bash
# Web App (.env)
REACT_APP_API_URL=http://localhost:8000/api/v1

# Mobile App (.env)
API_BASE_URL=http://localhost:8000/api/v1
```

## 📱 Mobile App Features

- Cross-platform compatibility (iOS & Android)
- Push notifications for medicine reminders
- Secure family messaging
- Health data synchronization
- Offline capability

## 💻 Web App Features

- Progressive Web App (PWA)
- Desktop-optimized interface
- Real-time updates
- Responsive design
- Offline functionality

## 🔐 Security Features

- JWT-based authentication
- End-to-end encryption for messages
- HIPAA-compliant data handling
- Role-based access control
- Secure API endpoints

## 🚀 Deployment

### Using Docker Compose (Recommended)
```bash
./scripts/deploy.sh production
```

### Railway Deployment
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy backend
cd backend && railway deploy

# Deploy web app
cd web && railway deploy
```

### Other Cloud Platforms

The application is containerized and can be deployed to:
- **AWS**: ECS, EKS, or Elastic Beanstalk
- **Google Cloud**: Cloud Run, GKE, or App Engine
- **Azure**: Container Instances, AKS, or App Service

## 📊 Monitoring

- Error tracking with Sentry
- Performance monitoring
- Health checks for all services
- Database monitoring

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Ensure all tests pass: `npm test` and `pytest`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Development Standards

- ✅ **Code quality**: ESLint, Prettier, flake8
- ✅ **Testing**: Jest, pytest, React Testing Library
- ✅ **Type safety**: TypeScript for frontend, type hints for Python
- ✅ **Documentation**: Comprehensive docs and code comments
- ✅ **Security**: HIPAA compliance, data encryption, secure authentication

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:

1. Check the [Setup Guide](SETUP.md)
2. Review [Contributing Guidelines](CONTRIBUTING.md)
3. Search existing issues
4. Create a new issue if needed

## 🙏 Acknowledgments

- Built with ❤️ for elder care and family health management
- Designed with accessibility and user experience in mind
- HIPAA-compliant and security-focused
- Open source and community-driven

---

**Ready for Production** 🚀 | **PR-Ready** ✅ | **CI/CD Enabled** 🔄 | **Docker Ready** 🐳