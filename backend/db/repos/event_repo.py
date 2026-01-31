"""
Event log repository for event-related database operations.
"""
from typing import Optional, List
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from db.models.event_log import EventLog, EventType
from db.repos.base_repo import BaseRepository


class EventLogRepository(BaseRepository[EventLog]):
    """
    Repository for EventLog model operations.
    """
    
    def __init__(self, db: Session):
        super().__init__(EventLog, db)
    
    def get_by_type(
        self,
        event_type: EventType,
        skip: int = 0,
        limit: int = 100
    ) -> List[EventLog]:
        """
        Get events by type.
        
        Args:
            event_type: Event type
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of events
        """
        # TODO: implement logic
        return (
            self.db.query(EventLog)
            .filter(EventLog.event_type == event_type)
            .order_by(EventLog.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> List[EventLog]:
        """
        Get events for a user.
        
        Args:
            user_id: User ID
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of events
        """
        # TODO: implement logic
        return (
            self.db.query(EventLog)
            .filter(EventLog.user_id == user_id)
            .order_by(EventLog.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_recent(self, hours: int = 24) -> List[EventLog]:
        """
        Get recent events within specified hours.
        
        Args:
            hours: Number of hours to look back
            
        Returns:
            List of recent events
        """
        # TODO: implement logic
        threshold = datetime.utcnow() - timedelta(hours=hours)
        return (
            self.db.query(EventLog)
            .filter(EventLog.created_at >= threshold)
            .order_by(EventLog.created_at.desc())
            .all()
        )
