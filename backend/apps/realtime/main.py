"""
WebSocket server for real-time updates.
"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from config.env import settings
from apps.realtime.pubsub import PubSubManager
from apps.realtime.handlers.charging import ChargingEventHandler

# Create FastAPI app
app = FastAPI(title="EV Charging Load Balancer - Realtime")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pub/Sub manager
pubsub = PubSubManager()
charging_handler = ChargingEventHandler(pubsub)


@app.websocket("/ws/charging/{session_id}")
async def websocket_charging(
    websocket: WebSocket,
    session_id: str
):
    """
    WebSocket endpoint for charging progress updates.
    
    Args:
        websocket: WebSocket connection
        session_id: Charging session ID
    """
    await websocket.accept()
    try:
        await charging_handler.handle_charging_progress(websocket, session_id)
    except WebSocketDisconnect:
        pass


@app.websocket("/ws/slots/{user_id}")
async def websocket_slots(
    websocket: WebSocket,
    user_id: int
):
    """
    WebSocket endpoint for slot allocation updates.
    
    Args:
        websocket: WebSocket connection
        user_id: User ID
    """
    await websocket.accept()
    try:
        await charging_handler.handle_slot_allocation(websocket, user_id)
    except WebSocketDisconnect:
        pass


@app.websocket("/ws/grid/alerts")
async def websocket_grid_alerts(websocket: WebSocket):
    """
    WebSocket endpoint for grid alerts.
    
    Args:
        websocket: WebSocket connection
    """
    await websocket.accept()
    try:
        await charging_handler.handle_grid_alerts(websocket)
    except WebSocketDisconnect:
        pass
