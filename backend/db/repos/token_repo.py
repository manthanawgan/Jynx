"""
Token repository for OAuth token-related database operations.
"""
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import Session

from db.models.token import Token
from db.repos.base_repo import BaseRepository


class TokenRepository(BaseRepository[Token]):
    """
    Repository for Token model operations.
    """
    
    def __init__(self, db: Session):
        super().__init__(Token, db)
    
    def get_by_user_and_provider(self, user_id: int, provider: str) -> Optional[Token]:
        """
        Get token for a user and provider.
        
        Args:
            user_id: User ID
            provider: Token provider (e.g., "smartcar")
            
        Returns:
            Token instance or None
        """
        # TODO: implement logic
        return (
            self.db.query(Token)
            .filter(Token.user_id == user_id, Token.provider == provider)
            .first()
        )
    
    def get_expiring_tokens(self, buffer_seconds: int = 300) -> List[Token]:
        """
        Get tokens that are expiring soon.
        
        Args:
            buffer_seconds: Seconds before expiry to consider
            
        Returns:
            List of tokens that need refresh
        """
        # TODO: implement logic
        threshold = datetime.utcnow().timestamp() + buffer_seconds
        return (
            self.db.query(Token)
            .filter(Token.expires_at <= datetime.fromtimestamp(threshold))
            .all()
        )
