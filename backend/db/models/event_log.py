"""
Event log model for system events and audit trail.
"""
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
import enum

from db.base import Base


class EventType(str, enum.Enum):
    """Event type enumeration."""
    SLOT_REQUESTED = "slot_requested"
    SLOT_ALLOCATED = "slot_allocated"
    SLOT_CANCELLED = "slot_cancelled"
    SESSION_STARTED = "session_started"
    SESSION_ENDED = "session_ended"
    EMERGENCY_REQUESTED = "emergency_requested"
    TOKEN_REFRESHED = "token_refreshed"
    GRID_ALERT = "grid_alert"
    ABUSE_DETECTED = "abuse_detected"


class EventLog(Base):
    """
    Event log model for tracking system events and audit trail.
    """
    __tablename__ = "event_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(Enum(EventType), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=True)
    session_id = Column(Integer, ForeignKey("charging_sessions.id"), nullable=True)
    
    # Event data
    message = Column(Text, nullable=True)
    metadata = Column(Text, nullable=True)  # JSON metadata
    
    # Timestamp
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
