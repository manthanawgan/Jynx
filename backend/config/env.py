"""
Environment configuration management.
Loads and validates environment variables for the application.
"""
import os
from typing import Optional
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    APP_NAME: str = Field(default="EV Charging Load Balancer", env="APP_NAME")
    DEBUG: bool = Field(default=False, env="DEBUG")
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    
    # Server
    API_HOST: str = Field(default="0.0.0.0", env="API_HOST")
    API_PORT: int = Field(default=8000, env="API_PORT")
    REALTIME_PORT: int = Field(default=8001, env="REALTIME_PORT")
    
    # Database
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    DB_POOL_SIZE: int = Field(default=10, env="DB_POOL_SIZE")
    DB_MAX_OVERFLOW: int = Field(default=20, env="DB_MAX_OVERFLOW")
    
    # Redis (for pub/sub and caching)
    REDIS_URL: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    
    # Smartcar OAuth
    SMARTCAR_CLIENT_ID: str = Field(..., env="SMARTCAR_CLIENT_ID")
    SMARTCAR_CLIENT_SECRET: str = Field(..., env="SMARTCAR_CLIENT_SECRET")
    SMARTCAR_REDIRECT_URI: str = Field(..., env="SMARTCAR_REDIRECT_URI")
    SMARTCAR_API_URL: str = Field(default="https://api.smartcar.com", env="SMARTCAR_API_URL")
    
    # JWT/Session
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    JWT_ALGORITHM: str = Field(default="HS256", env="JWT_ALGORITHM")
    JWT_EXPIRATION_HOURS: int = Field(default=24, env="JWT_EXPIRATION_HOURS")
    
    # OCPP Charger Integration
    OCPP_WEBSOCKET_URL: Optional[str] = Field(default=None, env="OCPP_WEBSOCKET_URL")
    
    # Grid/Transformer Settings
    GRID_CLUSTER_ID: str = Field(default="default", env="GRID_CLUSTER_ID")
    MAX_TRANSFORMER_CAPACITY_KW: float = Field(default=100.0, env="MAX_TRANSFORMER_CAPACITY_KW")
    
    # Worker Settings
    WORKER_CONCURRENCY: int = Field(default=4, env="WORKER_CONCURRENCY")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
