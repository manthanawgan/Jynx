"""
Slot model for charging time slots.
"""
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Enum, Boolean
from sqlalchemy.orm import relationship
import enum

from db.base import Base


class SlotStatus(str, enum.Enum):
    """Slot status enumeration."""
    AVAILABLE = "available"
    RESERVED = "reserved"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Slot(Base):
    """
    Slot model representing a charging time slot allocation.
    """
    __tablename__ = "slots"
    
    id = Column(Integer, primary_key=True, index=True)
    slot_id = Column(String(255), unique=True, index=True, nullable=False)
    status = Column(Enum(SlotStatus), default=SlotStatus.AVAILABLE)
    
    # Allocation
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Timing
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    
    # Power allocation
    allocated_power_kw = Column(Float, nullable=False)
    max_power_kw = Column(Float, nullable=True)
    
    # Priority
    priority_score = Column(Float, default=0.0)
    is_emergency = Column(Boolean, default=False)
    
    # Grid cluster
    grid_cluster_id = Column(Integer, ForeignKey("grid_clusters.id"), nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(Text, nullable=True)  # JSON metadata
    
    # Relationships
    vehicle = relationship("Vehicle", back_populates="slots")
    grid_cluster = relationship("GridCluster", back_populates="slots")
    sessions = relationship("ChargingSession", back_populates="slot")
