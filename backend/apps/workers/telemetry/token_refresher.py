"""
Background worker for refreshing OAuth tokens.
"""
import asyncio
from sqlalchemy.orm import Session

from db.base import SessionLocal
from auth.oauth.token_manager import TokenManager
from auth.oauth.smartcar_oauth import SmartcarOAuth
from db.repos.token_repo import TokenRepository


class TokenRefreshWorker:
    """
    Worker for refreshing expiring OAuth tokens.
    """
    
    def __init__(self):
        """Initialize token refresh worker."""
        pass
    
    async def run(self):
        """
        Run the token refresh worker.
        """
        # TODO: implement logic
        while True:
            try:
                db = SessionLocal()
                try:
                    token_repo = TokenRepository(db)
                    token_manager = TokenManager(db)
                    smartcar_oauth = SmartcarOAuth(token_manager)
                    
                    # Get expiring tokens
                    expiring_tokens = token_repo.get_expiring_tokens(buffer_seconds=300)
                    
                    for token in expiring_tokens:
                        # Refresh token
                        if token.provider == "smartcar":
                            smartcar_oauth.refresh_token(token.user_id)
                    
                finally:
                    db.close()
                
                # Wait before next run
                await asyncio.sleep(60)  # Run every minute
            except Exception as e:
                print(f"Error in token refresher: {e}")
                await asyncio.sleep(60)
