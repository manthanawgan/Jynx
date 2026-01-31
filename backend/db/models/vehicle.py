"""
Vehicle model for EV vehicles.
"""
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
import enum

from db.base import Base


class VehicleStatus(str, enum.Enum):
    """Vehicle status enumeration."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    CHARGING = "charging"
    PENDING = "pending"


class Vehicle(Base):
    """
    Vehicle model representing an EV vehicle.
    """
    __tablename__ = "vehicles"
    
    id = Column(Integer, primary_key=True, index=True)
    smartcar_vehicle_id = Column(String(255), unique=True, index=True, nullable=True)
    vin = Column(String(17), unique=True, index=True, nullable=True)
    make = Column(String(100), nullable=True)
    model = Column(String(100), nullable=True)
    year = Column(Integer, nullable=True)
    battery_capacity_kwh = Column(Float, nullable=True)
    max_charging_power_kw = Column(Float, nullable=True)
    status = Column(Enum(VehicleStatus), default=VehicleStatus.ACTIVE)
    
    # Location
    last_known_latitude = Column(Float, nullable=True)
    last_known_longitude = Column(Float, nullable)
    last_location_update = Column(DateTime, nullable=True)
    
    # Owner
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    fleet_id = Column(Integer, ForeignKey("fleets.id"), nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(Text, nullable=True)  # JSON metadata
    
    # Relationships
    owner = relationship("User", back_populates="vehicles")
    fleet = relationship("Fleet", back_populates="vehicles")
    sessions = relationship("ChargingSession", back_populates="vehicle")
    slots = relationship("Slot", back_populates="vehicle")
