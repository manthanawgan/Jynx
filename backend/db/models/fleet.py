"""
Fleet model for fleet operators.
"""
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from db.base import Base


class Fleet(Base):
    """
    Fleet model representing a fleet operator organization.
    """
    __tablename__ = "fleets"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    organization_id = Column(String(255), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    priority_level = Column(Integer, default=0)  # Higher = more priority
    
    # Contact
    contact_email = Column(String(255), nullable=True)
    contact_phone = Column(String(20), nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(Text, nullable=True)  # JSON metadata
    
    # Relationships
    vehicles = relationship("Vehicle", back_populates="fleet")
    operators = relationship("User", foreign_keys="User.fleet_id")
