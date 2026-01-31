"""
Driver emergency request routes.
"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base import get_db
from apps.api.controllers.driver_controller import DriverController

router = APIRouter(prefix="/drivers/emergency", tags=["drivers"])


class EmergencyRequest(BaseModel):
    """Emergency request model."""
    vehicle_id: int
    reason: str = None


@router.post("/request")
async def request_emergency(
    request: EmergencyRequest,
    user_id: int = 1,  # TODO: Get from auth token
    db: Session = Depends(get_db)
):
    """
    Request emergency charging verification.
    
    Args:
        request: Emergency request data
        user_id: Current user ID (from auth)
        db: Database session
        
    Returns:
        Emergency verification result
    """
    # TODO: implement logic
    controller = DriverController(db)
    result = await controller.request_emergency(
        user_id=user_id,
        vehicle_id=request.vehicle_id,
        reason=request.reason
    )
    return result
