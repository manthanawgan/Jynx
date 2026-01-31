"""
Grid cluster model for transformer and grid management.
"""
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.orm import relationship

from db.base import Base


class GridCluster(Base):
    """
    Grid cluster model representing a transformer and its connected chargers.
    """
    __tablename__ = "grid_clusters"
    
    id = Column(Integer, primary_key=True, index=True)
    cluster_id = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    
    # Transformer capacity
    max_capacity_kw = Column(Float, nullable=False)
    current_load_kw = Column(Float, default=0.0)
    efficiency = Column(Float, default=0.95)
    
    # Location
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    address = Column(String(500), nullable=True)
    
    # Status
    is_active = Column(Boolean, default=True)
    emergency_reserve_percent = Column(Float, default=10.0)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(Text, nullable=True)  # JSON metadata
    
    # Relationships
    slots = relationship("Slot", back_populates="grid_cluster")
