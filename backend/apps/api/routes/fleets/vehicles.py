"""
Fleet vehicle routes.
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from db.base import get_db
from apps.api.controllers.fleet_controller import FleetController

router = APIRouter(prefix="/fleet/vehicles", tags=["fleet"])


@router.get("")
async def get_fleet_vehicles(
    fleet_id: int = None,
    user_id: int = 1,  # TODO: Get from auth token
    db: Session = Depends(get_db)
):
    """
    Get fleet vehicle list.
    
    Args:
        fleet_id: Optional fleet ID filter
        user_id: Current user ID (from auth)
        db: Database session
        
    Returns:
        List of vehicles
    """
    # TODO: implement logic
    controller = FleetController(db)
    result = await controller.get_vehicles(user_id, fleet_id)
    return result


@router.get("/{vehicle_id}")
async def get_vehicle_details(
    vehicle_id: int,
    user_id: int = 1,  # TODO: Get from auth token
    db: Session = Depends(get_db)
):
    """
    Get vehicle details.
    
    Args:
        vehicle_id: Vehicle ID
        user_id: Current user ID (from auth)
        db: Database session
        
    Returns:
        Vehicle details
    """
    # TODO: implement logic
    controller = FleetController(db)
    result = await controller.get_vehicle_details(user_id, vehicle_id)
    if not result:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return result
