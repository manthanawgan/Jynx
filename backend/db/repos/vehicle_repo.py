"""
Vehicle repository for vehicle-related database operations.
"""
from typing import Optional, List
from sqlalchemy.orm import Session

from db.models.vehicle import Vehicle, VehicleStatus
from db.repos.base_repo import BaseRepository


class VehicleRepository(BaseRepository[Vehicle]):
    """
    Repository for Vehicle model operations.
    """
    
    def __init__(self, db: Session):
        super().__init__(Vehicle, db)
    
    def get_by_smartcar_id(self, smartcar_vehicle_id: str) -> Optional[Vehicle]:
        """
        Get vehicle by Smartcar vehicle ID.
        
        Args:
            smartcar_vehicle_id: Smartcar vehicle identifier
            
        Returns:
            Vehicle instance or None
        """
        # TODO: implement logic
        return (
            self.db.query(Vehicle)
            .filter(Vehicle.smartcar_vehicle_id == smartcar_vehicle_id)
            .first()
        )
    
    def get_by_owner(self, owner_id: int) -> List[Vehicle]:
        """
        Get all vehicles owned by a user.
        
        Args:
            owner_id: User ID
            
        Returns:
            List of vehicles
        """
        # TODO: implement logic
        return self.db.query(Vehicle).filter(Vehicle.owner_id == owner_id).all()
    
    def get_by_fleet(self, fleet_id: int) -> List[Vehicle]:
        """
        Get all vehicles in a fleet.
        
        Args:
            fleet_id: Fleet ID
            
        Returns:
            List of vehicles
        """
        # TODO: implement logic
        return self.db.query(Vehicle).filter(Vehicle.fleet_id == fleet_id).all()
    
    def get_by_status(self, status: VehicleStatus) -> List[Vehicle]:
        """
        Get vehicles by status.
        
        Args:
            status: Vehicle status
            
        Returns:
            List of vehicles
        """
        # TODO: implement logic
        return self.db.query(Vehicle).filter(Vehicle.status == status).all()
