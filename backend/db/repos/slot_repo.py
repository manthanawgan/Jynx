"""
Slot repository for slot-related database operations.
"""
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import Session

from db.models.slot import Slot, SlotStatus
from db.repos.base_repo import BaseRepository


class SlotRepository(BaseRepository[Slot]):
    """
    Repository for Slot model operations.
    """
    
    def __init__(self, db: Session):
        super().__init__(Slot, db)
    
    def get_by_slot_id(self, slot_id: str) -> Optional[Slot]:
        """
        Get slot by slot ID.
        
        Args:
            slot_id: Slot identifier
            
        Returns:
            Slot instance or None
        """
        # TODO: implement logic
        return (
            self.db.query(Slot)
            .filter(Slot.slot_id == slot_id)
            .first()
        )
    
    def get_available_slots(
        self,
        start_time: datetime,
        end_time: datetime,
        grid_cluster_id: Optional[int] = None
    ) -> List[Slot]:
        """
        Get available slots in a time range.
        
        Args:
            start_time: Start of time range
            end_time: End of time range
            grid_cluster_id: Optional grid cluster filter
            
        Returns:
            List of available slots
        """
        # TODO: implement logic
        query = (
            self.db.query(Slot)
            .filter(
                Slot.status == SlotStatus.AVAILABLE,
                Slot.start_time >= start_time,
                Slot.end_time <= end_time
            )
        )
        if grid_cluster_id:
            query = query.filter(Slot.grid_cluster_id == grid_cluster_id)
        return query.all()
    
    def get_by_vehicle(self, vehicle_id: int) -> List[Slot]:
        """
        Get slots allocated to a vehicle.
        
        Args:
            vehicle_id: Vehicle ID
            
        Returns:
            List of slots
        """
        # TODO: implement logic
        return self.db.query(Slot).filter(Slot.vehicle_id == vehicle_id).all()
    
    def get_active_slots(self) -> List[Slot]:
        """
        Get all active slots.
        
        Returns:
            List of active slots
        """
        # TODO: implement logic
        return (
            self.db.query(Slot)
            .filter(Slot.status == SlotStatus.ACTIVE)
            .all()
        )
