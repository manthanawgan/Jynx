"""
Driver charging status routes.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.base import get_db
from apps.api.controllers.driver_controller import DriverController

router = APIRouter(prefix="/drivers/charging", tags=["drivers"])


@router.get("/status")
async def get_charging_status(
    vehicle_id: int,
    user_id: int = 1,  # TODO: Get from auth token
    db: Session = Depends(get_db)
):
    """
    Get current charging session status.
    
    Args:
        vehicle_id: Vehicle ID
        user_id: Current user ID (from auth)
        db: Database session
        
    Returns:
        Charging session status
    """
    # TODO: implement logic
    controller = DriverController(db)
    result = await controller.get_charging_status(user_id, vehicle_id)
    if not result:
        raise HTTPException(status_code=404, detail="No active charging session")
    return result
