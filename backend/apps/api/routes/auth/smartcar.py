"""
Smartcar OAuth routes.
"""
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from db.base import get_db
from apps.api.controllers.auth_controller import AuthController

router = APIRouter(prefix="/auth/smartcar", tags=["auth"])


@router.get("/connect")
async def connect_smartcar(
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Redirect to Smartcar OAuth authorization page.
    
    Returns:
        Redirect response to Smartcar OAuth
    """
    # TODO: implement logic
    controller = AuthController(db)
    auth_url = controller.generate_smartcar_auth_url()
    return RedirectResponse(url=auth_url)


@router.get("/callback")
async def smartcar_callback(
    code: str,
    state: str = None,
    error: str = None,
    db: Session = Depends(get_db)
):
    """
    Handle Smartcar OAuth callback.
    
    Args:
        code: Authorization code
        state: State parameter
        error: Error code if OAuth failed
        
    Returns:
        Success response or error
    """
    # TODO: implement logic
    if error:
        raise HTTPException(status_code=400, detail=f"OAuth error: {error}")
    
    controller = AuthController(db)
    result = await controller.handle_smartcar_callback(code, state)
    return {"status": "success", "data": result}
