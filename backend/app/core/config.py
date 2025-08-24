from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, Field
from typing import List
import os

class Settings(BaseSettings):
    env: str = Field(default=os.getenv("ENV", "local"))

    # CORS
    cors_allowed_origins: List[AnyHttpUrl] | List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8081",
        "http://127.0.0.1:8081",
        "http://localhost",
        "https://localhost",
        "http://0.0.0.0:3000",
        "http://0.0.0.0:8081",
        "http://192.168.0.0/16",
        "*",
    ]

    # Database
    database_url: str = Field(default=os.getenv("DATABASE_URL", "sqlite:///./swaasth.db"))

    # Auth0
    auth0_domain: str = Field(default=os.getenv("AUTH0_DOMAIN", ""))
    auth0_audience: str = Field(default=os.getenv("AUTH0_AUDIENCE", ""))
    auth_algorithms: List[str] = Field(default_factory=lambda: ["RS256"]) 

    # Sentry
    sentry_dsn: str | None = Field(default=os.getenv("SENTRY_DSN"))

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()