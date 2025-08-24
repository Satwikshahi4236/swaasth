# Swaasth Elder Health App

A comprehensive health application designed for elder care with personalized medicine reminders and secure family communication features.

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
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utility functions
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
│   └── package.json
└── docker-compose.yml      # Development environment
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.8+
- Docker & Docker Compose
- PostgreSQL (or use Docker)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd swaasth-elder-health
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Mobile App Setup**
   ```bash
   cd mobile
   npm install
   npx expo start
   ```

4. **Web App Setup**
   ```bash
   cd web
   npm install
   npm start
   ```

5. **Docker Development**
   ```bash
   docker-compose up -d
   ```

## 🔧 Configuration

Create `.env` files in each directory with appropriate configuration:

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/swaasth_db
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
```

### Mobile (.env)
```
API_BASE_URL=http://localhost:8000
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

### Railway Deployment
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy backend
cd backend
railway deploy

# Deploy web app
cd web
railway deploy
```

### Docker Deployment
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 📊 Monitoring

- Error tracking with Sentry
- Performance monitoring
- Health checks
- Database monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions, please contact the development team.