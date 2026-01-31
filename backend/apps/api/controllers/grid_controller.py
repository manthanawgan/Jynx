"""
Grid controller for grid cluster operations.
"""
from typing import Optional, Dict
from sqlalchemy.orm import Session

from domain.grid.cluster_load import ClusterLoadManager
from db.repos.grid_repo import GridClusterRepository
from db.repos.slot_repo import SlotRepository
from config.env import settings


class GridController:
    """
    Controller for grid operations.
    """
    
    def __init__(self, db: Session):
        """
        Initialize grid controller.
        
        Args:
            db: Database session
        """
        self.db = db
        grid_repo = GridClusterRepository(db)
        slot_repo = SlotRepository(db)
        self.cluster_manager = ClusterLoadManager(grid_repo, slot_repo)
    
    async def get_cluster_info(
        self,
        cluster_id: Optional[str] = None
    ) -> Optional[Dict]:
        """
        Get grid cluster information.
        
        Args:
            cluster_id: Optional cluster ID (defaults to configured)
            
        Returns:
            Dictionary with cluster information or None
        """
        # TODO: implement logic
        cluster_id = cluster_id or settings.GRID_CLUSTER_ID
        status = self.cluster_manager.get_cluster_status(cluster_id)
        return status
