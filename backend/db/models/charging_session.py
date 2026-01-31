"""
Charging session model.
"""
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
import enum

from db.base import Base


class SessionStatus(str, enum.Enum):
    """Charging session status enumeration."""
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"


class ChargingSession(Base):
    """
    Charging session model representing an active or completed charging session.
    """
    __tablename__ = "charging_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(255), unique=True, index=True, nullable=False)
    status = Column(Enum(SessionStatus), default=SessionStatus.PENDING)
    
    # Participants
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    slot_id = Column(Integer, ForeignKey("slots.id"), nullable=True)
    
    # Charging metrics
    start_soc = Column(Float, nullable=True)  # State of charge at start (%)
    end_soc = Column(Float, nullable=True)  # State of charge at end (%)
    energy_delivered_kwh = Column(Float, default=0.0)
    average_power_kw = Column(Float, nullable=True)
    max_power_kw = Column(Float, nullable=True)
    
    # Timing
    requested_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime, nullable=True)
    ended_at = Column(DateTime, nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    
    # Pricing
    cost = Column(Float, nullable=True)
    tariff_rate = Column(Float, nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(Text, nullable=True)  # JSON metadata
    
    # Relationships
    user = relationship("User", back_populates="sessions")
    vehicle = relationship("Vehicle", back_populates="sessions")
    slot = relationship("Slot", back_populates="sessions")
