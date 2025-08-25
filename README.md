# Swaasth Elder Health App

![CI/CD](https://github.com/swaasth/elder-health/actions/workflows/ci-cd.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Node.js](https://img.shields.io/badge/node.js-18+-green.svg)
![React](https://img.shields.io/badge/react-18-blue.svg)
![React Native](https://img.shields.io/badge/react%20native-0.72-blue.svg)

**Swaasth** is an elder health app to manage medicines, track health, and stay connected with family securely.

## 🚀 Features

* Medicine reminders with push notifications
* Secure family messaging
* Health tracking (vitals, symptoms, adherence)
* HIPAA-compliant & end-to-end encryption
* Cross-platform: mobile (iOS/Android) & desktop (PWA)

## 🏗️ Tech Stack

**Frontend:** React Native, React Navigation, React Native Paper, PWA
**Backend:** FastAPI, PostgreSQL, SQLAlchemy, JWT
**Deployment:** Docker, Railway, GitHub Actions

## 🛠️ Quick Start

### Prerequisites

Node.js 18+, Python 3.9+, Docker & Docker Compose

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Web App

```bash
cd web
npm install
echo "REACT_APP_API_URL=http://localhost:8000/api/v1" > .env
npm start
```

### Mobile App

```bash
cd mobile
npm install
npx expo start
```

Scan QR code with Expo Go or use `a` / `i` for emulator/simulator.

## ⚡ Testing & Linting

```bash
# Backend tests
cd backend && python -m pytest -v

# Frontend tests
cd web && npm test

# Mobile type-check
cd mobile && npm run type-check

# Lint backend
cd backend && flake8 app/
```

## 🔧 Environment Variables

**Backend `.env`:**

```
DATABASE_URL=postgresql://user:password@localhost:5432/swaasth_db
JWT_SECRET_KEY=your-secret-key
REDIS_URL=redis://localhost:6379/0
DEBUG=true
```

**Frontend `.env`:**

```
REACT_APP_API_URL=http://localhost:8000/api/v1
API_BASE_URL=http://localhost:8000/api/v1
```

---

## 📦 Deployment

**Docker Compose:**

```bash
./scripts/deploy.sh production
```

**Railway:**

```bash
npm install -g @railway/cli
cd backend && railway deploy
cd web && railway deploy
```
**Standards:** ESLint, Prettier, flake8, TypeScript, type hints, HIPAA compliance

## 📄 License

MIT License — see [LICENSE](LICENSE)


**Ready for Production** 🚀 | **PR-Ready** ✅ | **CI/CD Enabled** 🔄 | **Docker Ready** 🐳
