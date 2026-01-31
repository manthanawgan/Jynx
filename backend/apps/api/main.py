"""
Main FastAPI application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.env import settings
from config.logging import setup_logging
from apps.api.routes.auth.smartcar import router as auth_router
from apps.api.routes.drivers.slot import router as slot_router
from apps.api.routes.drivers.emergency import router as emergency_router
from apps.api.routes.drivers.charging import router as charging_router
from apps.api.routes.fleets.vehicles import router as fleet_router
from apps.api.routes.analytics.fairness import router as analytics_router
from apps.api.routes.charges.grid import router as grid_router

# Setup logging
setup_logging()

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="Community EV Charging Load Balancer API",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Configure properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(slot_router)
app.include_router(emergency_router)
app.include_router(charging_router)
app.include_router(fleet_router)
app.include_router(analytics_router)
app.include_router(grid_router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "EV Charging Load Balancer API", "version": "1.0.0"}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}
