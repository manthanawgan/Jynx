"""
Driver controller for driver-related operations.
"""
from typing import Optional, Dict
from datetime import datetime
from sqlalchemy.orm import Session

from domain.scheduling.slot_allocator import SlotAllocator
from domain.scheduling.emergency_classifier import EmergencyVerifier
from domain.charging.session_manager import ChargingSessionManager
from db.repos.slot_repo import SlotRepository
from db.repos.grid_repo import GridClusterRepository
from db.repos.session_repo import ChargingSessionRepository
from integrations.vehicles.smartcar_adapter import SmartcarAdapter
from auth.oauth.token_manager import TokenManager


class DriverController:
    """
    Controller for driver operations.
    """
    
    def __init__(self, db: Session):
        """
        Initialize driver controller.
        
        Args:
            db: Database session
        """
        self.db = db
        slot_repo = SlotRepository(db)
        grid_repo = GridClusterRepository(db)
        session_repo = ChargingSessionRepository(db)
        token_manager = TokenManager(db)
        
        self.slot_allocator = SlotAllocator(slot_repo, grid_repo)
        self.emergency_verifier = EmergencyVerifier()
        self.session_manager = ChargingSessionManager(session_repo, slot_repo)
        self.vehicle_adapter = SmartcarAdapter(token_manager)
    
    async def request_slot(
        self,
        user_id: int,
        vehicle_id: int,
        requested_start: datetime,
        duration_minutes: int,
        grid_cluster_id: Optional[int] = None
    ) -> Dict:
        """
        Request a charging slot.
        
        Args:
            user_id: User ID
            vehicle_id: Vehicle ID
            requested_start: Requested start time
            duration_minutes: Duration in minutes
            grid_cluster_id: Optional grid cluster preference
            
        Returns:
            Dictionary with slot allocation result
        """
        # TODO: implement logic
        slot = self.slot_allocator.allocate_slot(
            vehicle_id=vehicle_id,
            requested_start=requested_start,
            duration_minutes=duration_minutes,
            grid_cluster_id=grid_cluster_id
        )
        return {"slot": slot, "status": "allocated" if slot else "unavailable"}
    
    async def request_emergency(
        self,
        user_id: int,
        vehicle_id: int,
        reason: Optional[str] = None
    ) -> Dict:
        """
        Request emergency charging verification.
        
        Args:
            user_id: User ID
            vehicle_id: Vehicle ID
            reason: Optional emergency reason
            
        Returns:
            Dictionary with verification result
        """
        # TODO: implement logic
        # 1. Get vehicle telemetry
        # 2. Verify emergency
        # 3. Allocate priority slot if verified
        telemetry = self.vehicle_adapter.get_vehicle_data(str(vehicle_id))
        verification = self.emergency_verifier.verify(vehicle_id, telemetry, reason)
        return verification
    
    async def get_charging_status(
        self,
        user_id: int,
        vehicle_id: int
    ) -> Optional[Dict]:
        """
        Get current charging session status.
        
        Args:
            user_id: User ID
            vehicle_id: Vehicle ID
            
        Returns:
            Dictionary with charging status or None
        """
        # TODO: implement logic
        session = self.session_manager.get_active_session(vehicle_id)
        if not session:
            return None
        
        return {
            "session_id": session.session_id,
            "status": session.status,
            "energy_delivered_kwh": session.energy_delivered_kwh,
            "start_soc": session.start_soc,
            "current_soc": None,  # TODO: Get from vehicle adapter
            "started_at": session.started_at.isoformat() if session.started_at else None
        }
