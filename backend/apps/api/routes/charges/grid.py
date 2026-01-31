"""
Grid cluster routes.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.base import get_db
from apps.api.controllers.grid_controller import GridController

router = APIRouter(prefix="/grid/cluster", tags=["grid"])


@router.get("")
async def get_grid_cluster(
    cluster_id: str = None,
    db: Session = Depends(get_db)
):
    """
    Get grid cluster information.
    
    Args:
        cluster_id: Optional cluster ID (defaults to configured cluster)
        db: Database session
        
    Returns:
        Grid cluster information including:
        - cluster_id
        - transformer capacity
        - current load
        - available capacity
    """
    # TODO: implement logic
    controller = GridController(db)
    result = await controller.get_cluster_info(cluster_id)
    if not result:
        raise HTTPException(status_code=404, detail="Grid cluster not found")
    return result
