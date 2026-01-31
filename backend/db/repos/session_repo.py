"""
Charging session repository for session-related database operations.
"""
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import Session

from db.models.charging_session import ChargingSession, SessionStatus
from db.repos.base_repo import BaseRepository


class ChargingSessionRepository(BaseRepository[ChargingSession]):
    """
    Repository for ChargingSession model operations.
    """
    
    def __init__(self, db: Session):
        super().__init__(ChargingSession, db)
    
    def get_by_session_id(self, session_id: str) -> Optional[ChargingSession]:
        """
        Get session by session ID.
        
        Args:
            session_id: Session identifier
            
        Returns:
            ChargingSession instance or None
        """
        # TODO: implement logic
        return (
            self.db.query(ChargingSession)
            .filter(ChargingSession.session_id == session_id)
            .first()
        )
    
    def get_active_by_vehicle(self, vehicle_id: int) -> Optional[ChargingSession]:
        """
        Get active session for a vehicle.
        
        Args:
            vehicle_id: Vehicle ID
            
        Returns:
            Active ChargingSession or None
        """
        # TODO: implement logic
        return (
            self.db.query(ChargingSession)
            .filter(
                ChargingSession.vehicle_id == vehicle_id,
                ChargingSession.status == SessionStatus.ACTIVE
            )
            .first()
        )
    
    def get_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> List[ChargingSession]:
        """
        Get sessions for a user.
        
        Args:
            user_id: User ID
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of charging sessions
        """
        # TODO: implement logic
        return (
            self.db.query(ChargingSession)
            .filter(ChargingSession.user_id == user_id)
            .order_by(ChargingSession.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_active_sessions(self) -> List[ChargingSession]:
        """
        Get all active charging sessions.
        
        Returns:
            List of active sessions
        """
        # TODO: implement logic
        return (
            self.db.query(ChargingSession)
            .filter(ChargingSession.status == SessionStatus.ACTIVE)
            .all()
        )
