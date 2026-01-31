"""
Background worker for slot rebalancing.
"""
import asyncio
from typing import Dict
from sqlalchemy.orm import Session

from db.base import SessionLocal
from domain.scheduling.slot_allocator import SlotAllocator
from db.repos.slot_repo import SlotRepository
from db.repos.grid_repo import GridClusterRepository
from config.env import settings


class SlotRebalancerWorker:
    """
    Worker for rebalancing slot allocations.
    """
    
    def __init__(self):
        """Initialize rebalancer worker."""
        pass
    
    async def run(self):
        """
        Run the rebalancer worker.
        """
        # TODO: implement logic
        while True:
            try:
                db = SessionLocal()
                try:
                    slot_repo = SlotRepository(db)
                    grid_repo = GridClusterRepository(db)
                    allocator = SlotAllocator(slot_repo, grid_repo)
                    
                    # Rebalance slots
                    stats = allocator.rebalance_slots()
                    print(f"Rebalanced: {stats}")
                finally:
                    db.close()
                
                # Wait before next run
                await asyncio.sleep(60)  # Run every minute
            except Exception as e:
                print(f"Error in rebalancer: {e}")
                await asyncio.sleep(60)
