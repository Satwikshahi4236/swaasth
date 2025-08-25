import AsyncStorage from '@react-native-async-storage/async-storage';
import axios, { AxiosResponse } from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1'; // Change this for production

export interface LoginData {
  email: string;
  password: string;
}

export interface RegisterData {
  email: string;
  password: string;
  first_name: string;
  last_name: string;
  role?: string;
  phone_number?: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
}

export interface User {
  id: number;
  email: string;
  role: string;
  is_active: boolean;
  is_verified: boolean;
  created_at: string;
}

class AuthServiceClass {
  private apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: {
      'Content-Type': 'application/json',
    },
  });

  constructor() {
    // Add token to requests automatically
    this.apiClient.interceptors.request.use(async (config) => {
      const token = await AsyncStorage.getItem('access_token');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    });

    // Handle token refresh on 401
    this.apiClient.interceptors.response.use(
      (response) => response,
      async (error) => {
        if (error.response?.status === 401) {
          await this.refreshToken();
          // Retry the original request
          return this.apiClient.request(error.config);
        }
        return Promise.reject(error);
      }
    );
  }

  async login(data: LoginData): Promise<TokenResponse> {
    try {
      const response: AxiosResponse<TokenResponse> = await this.apiClient.post('/auth/login', data);
      
      // Store tokens
      await AsyncStorage.setItem('access_token', response.data.access_token);
      await AsyncStorage.setItem('refresh_token', response.data.refresh_token);
      
      return response.data;
    } catch (error) {
      console.error('Login error:', error);
      throw new Error('Login failed. Please check your credentials.');
    }
  }

  async register(data: RegisterData): Promise<User> {
    try {
      const response: AxiosResponse<User> = await this.apiClient.post('/auth/register', data);
      return response.data;
    } catch (error) {
      console.error('Registration error:', error);
      throw new Error('Registration failed. Please try again.');
    }
  }

  async logout(): Promise<void> {
    try {
      await this.apiClient.post('/auth/logout');
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      // Clear stored tokens
      await AsyncStorage.removeItem('access_token');
      await AsyncStorage.removeItem('refresh_token');
    }
  }

  async refreshToken(): Promise<boolean> {
    try {
      const refreshToken = await AsyncStorage.getItem('refresh_token');
      if (!refreshToken) {
        throw new Error('No refresh token available');
      }

      const response: AxiosResponse<TokenResponse> = await this.apiClient.post('/auth/refresh', {
        refresh_token: refreshToken,
      });

      // Store new tokens
      await AsyncStorage.setItem('access_token', response.data.access_token);
      await AsyncStorage.setItem('refresh_token', response.data.refresh_token);
      
      return true;
    } catch (error) {
      console.error('Token refresh error:', error);
      // Clear tokens on refresh failure
      await AsyncStorage.removeItem('access_token');
      await AsyncStorage.removeItem('refresh_token');
      return false;
    }
  }

  async verifyToken(token: string): Promise<boolean> {
    try {
      // You would implement token verification with your backend
      // For now, we'll just check if the token exists and is not expired
      if (!token) return false;
      
      // Decode JWT payload (basic validation)
      const payload = JSON.parse(atob(token.split('.')[1]));
      const currentTime = Date.now() / 1000;
      
      return payload.exp > currentTime;
    } catch (error) {
      console.error('Token verification error:', error);
      return false;
    }
  }

  async getCurrentUser(): Promise<User | null> {
    try {
      const response: AxiosResponse<User> = await this.apiClient.get('/auth/me');
      return response.data;
    } catch (error) {
      console.error('Get current user error:', error);
      return null;
    }
  }

  async getStoredToken(): Promise<string | null> {
    try {
      return await AsyncStorage.getItem('access_token');
    } catch (error) {
      console.error('Error getting stored token:', error);
      return null;
    }
  }
}

export const AuthService = new AuthServiceClass();