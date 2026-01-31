"""
User model for driver accounts.
"""
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship

from db.base import Base


class User(Base):
    """
    User model representing a driver/operator account.
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    is_fleet_operator = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(Text, nullable=True)  # JSON metadata
    
    # Relationships
    vehicles = relationship("Vehicle", back_populates="owner")
    sessions = relationship("ChargingSession", back_populates="user")
    tokens = relationship("Token", back_populates="user")
