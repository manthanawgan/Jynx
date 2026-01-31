"""
Grid cluster repository for grid-related database operations.
"""
from typing import Optional, List
from sqlalchemy.orm import Session

from db.models.grid_cluster import GridCluster
from db.repos.base_repo import BaseRepository


class GridClusterRepository(BaseRepository[GridCluster]):
    """
    Repository for GridCluster model operations.
    """
    
    def __init__(self, db: Session):
        super().__init__(GridCluster, db)
    
    def get_by_cluster_id(self, cluster_id: str) -> Optional[GridCluster]:
        """
        Get grid cluster by cluster ID.
        
        Args:
            cluster_id: Cluster identifier
            
        Returns:
            GridCluster instance or None
        """
        # TODO: implement logic
        return (
            self.db.query(GridCluster)
            .filter(GridCluster.cluster_id == cluster_id)
            .first()
        )
    
    def update_load(self, cluster_id: str, load_kw: float) -> Optional[GridCluster]:
        """
        Update current load for a grid cluster.
        
        Args:
            cluster_id: Cluster identifier
            load_kw: Current load in kW
            
        Returns:
            Updated GridCluster or None
        """
        # TODO: implement logic
        cluster = self.get_by_cluster_id(cluster_id)
        if cluster:
            cluster.current_load_kw = load_kw
            self.db.commit()
            self.db.refresh(cluster)
        return cluster
