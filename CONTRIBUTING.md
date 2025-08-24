# Contributing to Swaasth Elder Health App

Thank you for your interest in contributing to the Swaasth Elder Health App! This document provides guidelines and instructions for contributing to this project.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue template** to provide necessary details
3. **Include steps to reproduce** the problem
4. **Add relevant labels** (bug, enhancement, documentation, etc.)

### Pull Request Process

1. **Fork the repository** and create your branch from `main`
2. **Follow the naming convention**: `feature/your-feature-name` or `fix/issue-description`
3. **Make your changes** with clear, descriptive commit messages
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Ensure CI/CD passes** before submitting
7. **Submit a pull request** with a detailed description

## 🛠️ Development Setup

### Prerequisites

- **Docker & Docker Compose** (recommended for quick setup)
- **Node.js 18+** and **Python 3.9+** (for local development)
- **Git** for version control

### Quick Start

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/swaasth-elder-health.git
cd swaasth-elder-health

# Start all services with Docker
./scripts/deploy.sh development

# Or set up individually (see SETUP.md for detailed instructions)
```

## 📋 Code Standards

### Python (Backend)

- **PEP 8** style guide compliance
- **Type hints** for function parameters and return values
- **Docstrings** for all public functions and classes
- **pytest** for testing

```python
def create_user(email: str, password: str) -> User:
    """Create a new user with email and password.
    
    Args:
        email: User's email address
        password: Plain text password (will be hashed)
        
    Returns:
        User: Created user instance
        
    Raises:
        ValueError: If email is already registered
    """
    # Implementation here
```

### TypeScript/JavaScript (Frontend)

- **ESLint** and **Prettier** for code formatting
- **TypeScript** for type safety
- **Functional components** with hooks for React
- **Proper error handling** and loading states

```typescript
interface Props {
  userId: number;
  onUpdate: (user: User) => void;
}

const UserProfile: React.FC<Props> = ({ userId, onUpdate }) => {
  // Component implementation
};
```

### React Native (Mobile)

- **Expo** best practices
- **React Native Paper** for UI components
- **TypeScript** for type safety
- **Platform-specific** code when necessary

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Frontend Tests

```bash
cd web
npm test -- --coverage
```

### Mobile Type Checking

```bash
cd mobile
npm run type-check
```

## 📦 Commit Message Convention

Use conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(auth): add JWT refresh token functionality
fix(mobile): resolve notification permission issue
docs(readme): update installation instructions
```

## 🏗️ Project Structure

```
swaasth-elder-health/
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── models/    # Database models
│   │   ├── routes/    # API endpoints
│   │   ├── schemas/   # Pydantic schemas
│   │   └── utils/     # Utility functions
│   └── tests/         # Backend tests
├── web/               # React PWA
│   ├── src/
│   │   ├── components/# React components
│   │   ├── pages/     # Page components
│   │   └── services/  # API services
│   └── public/        # Static assets
├── mobile/            # React Native app
│   └── src/
│       ├── screens/   # Mobile screens
│       ├── components/# Mobile components
│       └── services/  # Mobile services
└── scripts/           # Deployment scripts
```

## 🔐 Security Guidelines

### For Healthcare Data

1. **Never commit sensitive data** (API keys, passwords, PHI)
2. **Use environment variables** for configuration
3. **Follow HIPAA compliance** guidelines
4. **Encrypt sensitive data** in transit and at rest
5. **Validate all inputs** to prevent injection attacks

### Code Security

- **Dependency updates**: Keep dependencies up to date
- **Security scanning**: Use tools like `npm audit` and `safety`
- **Authentication**: Proper JWT handling and validation
- **Authorization**: Role-based access control

## 📚 Documentation

### Required Documentation

1. **API endpoints**: Document all new endpoints
2. **Component props**: Document React component interfaces
3. **Database changes**: Document schema modifications
4. **Configuration**: Document new environment variables

### Documentation Style

- **Clear descriptions** of functionality
- **Code examples** where helpful
- **Parameter types** and return values
- **Error cases** and handling

## 🚀 Release Process

### Version Management

- **Semantic versioning** (MAJOR.MINOR.PATCH)
- **Changelog** maintenance
- **Git tags** for releases

### Release Checklist

- [ ] All tests passing
- [ ] Documentation updated
- [ ] Version numbers bumped
- [ ] Changelog updated
- [ ] Security review completed
- [ ] Performance testing done

## 🤔 Questions and Support

### Getting Help

1. **Check existing documentation** first
2. **Search closed issues** for similar problems
3. **Ask in discussions** for general questions
4. **Create an issue** for bugs or feature requests

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Request Reviews**: Code-specific discussions

## 📄 Legal and Compliance

### Health Data Handling

- **HIPAA compliance** is mandatory
- **No PHI in logs** or error messages
- **Data minimization** principles
- **Proper consent** handling

### Licensing

- This project is **MIT licensed**
- **Third-party dependencies** must be compatible
- **Attribution** required for significant contributions

## 🎯 Contribution Areas

### High Priority

- **Security improvements**
- **Accessibility enhancements**
- **Performance optimizations**
- **Test coverage improvements**

### Welcome Contributions

- **Bug fixes**
- **Documentation improvements**
- **UI/UX enhancements**
- **Mobile app features**
- **Internationalization**

### Architecture Decisions

For major changes, please:

1. **Open an issue** first to discuss
2. **Provide technical details** and reasoning
3. **Consider backwards compatibility**
4. **Get maintainer approval** before starting

## 🙏 Recognition

Contributors will be recognized in:

- **CONTRIBUTORS.md** file
- **Release notes** for significant contributions
- **GitHub contributors** section

Thank you for helping make healthcare more accessible for elderly users! 💊❤️