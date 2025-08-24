from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    # Database Configuration
    database_url: str = "postgresql://swaasth_user:swaasth_password@localhost:5432/swaasth_db"
    
    # JWT Configuration
    jwt_secret_key: str = "your-super-secret-jwt-key-change-this-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 30
    
    # Redis Configuration
    redis_url: str = "redis://localhost:6379/0"
    
    # Firebase Configuration
    firebase_project_id: str = ""
    firebase_private_key_id: str = ""
    firebase_private_key: str = ""
    firebase_client_email: str = ""
    firebase_client_id: str = ""
    firebase_client_x509_cert_url: str = ""
    
    # CORS Configuration
    cors_origins: List[str] = [
        "http://localhost:3000", 
        "http://localhost:19006", 
        "exp://192.168.1.100:19000"
    ]
    
    # Sentry Configuration
    sentry_dsn: str = ""
    
    # App Configuration
    app_name: str = "Swaasth Elder Health API"
    app_version: str = "1.0.0"
    debug: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()