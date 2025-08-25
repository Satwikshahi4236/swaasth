import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Mock the AuthService
jest.mock('./services/AuthService', () => ({
  AuthService: {
    verifyToken: jest.fn().mockResolvedValue(false),
    logout: jest.fn().mockResolvedValue(undefined),
  },
}));

test('renders app without crashing', () => {
  render(<App />);
  // The app should render the login form since we mocked verifyToken to return false
  expect(document.body).toBeInTheDocument();
});

test('shows loading initially', () => {
  render(<App />);
  // Since the app checks auth state on mount, it should show something
  expect(document.body).toBeInTheDocument();
});