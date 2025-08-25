import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { CssBaseline, Box } from '@mui/material';

// Components
import Header from './components/layout/Header';
import Sidebar from './components/layout/Sidebar';
import LoadingScreen from './components/common/LoadingScreen';

// Pages
import LoginPage from './pages/auth/LoginPage';
import RegisterPage from './pages/auth/RegisterPage';
import DashboardPage from './pages/dashboard/DashboardPage';
import MedicinesPage from './pages/medicines/MedicinesPage';
import FamilyPage from './pages/family/FamilyPage';
import HealthPage from './pages/health/HealthPage';
import ProfilePage from './pages/profile/ProfilePage';

// Services
import { AuthService } from './services/AuthService';

// Theme
const theme = createTheme({
  palette: {
    primary: {
      main: '#2196F3',
    },
    secondary: {
      main: '#03DAC6',
    },
    background: {
      default: '#f5f5f5',
    },
  },
  typography: {
    fontFamily: 'Roboto, Arial, sans-serif',
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
        },
      },
    },
  },
});

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(false);

  useEffect(() => {
    checkAuthState();
    // Hide initial loader when React loads
    document.body.classList.add('loaded');
  }, []);

  const checkAuthState = async () => {
    try {
      const token = localStorage.getItem('access_token');
      if (token) {
        const isValid = await AuthService.verifyToken(token);
        setIsAuthenticated(isValid);
      }
    } catch (error) {
      console.error('Error checking auth state:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  const handleLogout = async () => {
    try {
      await AuthService.logout();
      setIsAuthenticated(false);
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  if (isLoading) {
    return <LoadingScreen />;
  }

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Box sx={{ display: 'flex', minHeight: '100vh' }}>
          {isAuthenticated && (
            <>
              <Header onToggleSidebar={toggleSidebar} onLogout={handleLogout} />
              <Sidebar open={sidebarOpen} onClose={() => setSidebarOpen(false)} />
            </>
          )}
          
          <Box
            component="main"
            sx={{
              flexGrow: 1,
              pt: isAuthenticated ? 8 : 0, // Account for AppBar height
              pl: isAuthenticated && sidebarOpen ? { md: 30 } : 0,
              transition: theme.transitions.create(['margin'], {
                easing: theme.transitions.easing.sharp,
                duration: theme.transitions.duration.standard,
              }),
            }}
          >
            <Routes>
              {!isAuthenticated ? (
                <>
                  <Route path="/login" element={<LoginPage onLogin={handleLogin} />} />
                  <Route path="/register" element={<RegisterPage />} />
                  <Route path="*" element={<Navigate to="/login" replace />} />
                </>
              ) : (
                <>
                  <Route path="/" element={<DashboardPage />} />
                  <Route path="/dashboard" element={<DashboardPage />} />
                  <Route path="/medicines" element={<MedicinesPage />} />
                  <Route path="/family" element={<FamilyPage />} />
                  <Route path="/health" element={<HealthPage />} />
                  <Route path="/profile" element={<ProfilePage />} />
                  <Route path="*" element={<Navigate to="/" replace />} />
                </>
              )}
            </Routes>
          </Box>
        </Box>
      </Router>
    </ThemeProvider>
  );
}

export default App;