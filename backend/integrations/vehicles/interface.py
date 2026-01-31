"""
Vehicle data interface and models.
"""
from typing import Optional, Dict
from dataclasses import dataclass
from datetime import datetime


@dataclass
class VehicleData:
    """
    Vehicle telemetry data structure.
    """
    vehicle_id: str
    soc: Optional[float] = None  # State of charge (0.0 to 1.0)
    location_latitude: Optional[float] = None
    location_longitude: Optional[float] = None
    odometer_km: Optional[float] = None
    is_charging: Optional[bool] = None
    charging_power_kw: Optional[float] = None
    battery_capacity_kwh: Optional[float] = None
    timestamp: Optional[datetime] = None
    metadata: Optional[Dict] = None


class VehicleAdapterInterface:
    """
    Interface for vehicle data adapters (Smartcar, mock, etc.).
    """
    
    def get_soc(self, vehicle_id: str) -> Optional[float]:
        """
        Get state of charge for a vehicle.
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            SOC as float (0.0 to 1.0) or None
        """
        raise NotImplementedError
    
    def get_location(self, vehicle_id: str) -> Optional[Dict[str, float]]:
        """
        Get vehicle location.
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            Dictionary with 'latitude' and 'longitude' or None
        """
        raise NotImplementedError
    
    def get_odometer(self, vehicle_id: str) -> Optional[float]:
        """
        Get vehicle odometer reading.
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            Odometer reading in km or None
        """
        raise NotImplementedError
    
    def get_charging_status(self, vehicle_id: str) -> Optional[Dict]:
        """
        Get charging status for a vehicle.
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            Dictionary with charging status or None
        """
        raise NotImplementedError
    
    def get_vehicle_data(self, vehicle_id: str) -> Optional[VehicleData]:
        """
        Get comprehensive vehicle data.
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            VehicleData instance or None
        """
        raise NotImplementedError
