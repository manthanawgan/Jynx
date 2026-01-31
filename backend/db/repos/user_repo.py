"""
User repository for user-related database operations.
"""
from typing import Optional, List
from sqlalchemy.orm import Session

from db.models.user import User
from db.repos.base_repo import BaseRepository


class UserRepository(BaseRepository[User]):
    """
    Repository for User model operations.
    """
    
    def __init__(self, db: Session):
        super().__init__(User, db)
    
    def get_by_email(self, email: str) -> Optional[User]:
        """
        Get user by email address.
        
        Args:
            email: User email
            
        Returns:
            User instance or None
        """
        # TODO: implement logic
        return self.db.query(User).filter(User.email == email).first()
    
    def get_fleet_operators(self, skip: int = 0, limit: int = 100) -> List[User]:
        """
        Get all fleet operators.
        
        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of fleet operator users
        """
        # TODO: implement logic
        return (
            self.db.query(User)
            .filter(User.is_fleet_operator == True)
            .offset(skip)
            .limit(limit)
            .all()
        )
