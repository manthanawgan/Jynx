"""
Mock vehicle adapter for testing and development.
"""
from typing import Optional, Dict
from datetime import datetime
import random

from integrations.vehicles.interface import VehicleAdapterInterface, VehicleData


class MockAdapter(VehicleAdapterInterface):
    """
    Mock adapter for vehicle data (for testing/development).
    """
    
    def __init__(self):
        """Initialize mock adapter."""
        self._mock_data: Dict[str, VehicleData] = {}
    
    def get_soc(self, vehicle_id: str) -> Optional[float]:
        """
        Get state of charge for a vehicle (mock).
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            SOC as float (0.0 to 1.0) or None
        """
        # TODO: implement logic
        # Return random or stored mock SOC
        return random.uniform(0.2, 0.9)
    
    def get_location(self, vehicle_id: str) -> Optional[Dict[str, float]]:
        """
        Get vehicle location (mock).
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            Dictionary with 'latitude' and 'longitude' or None
        """
        # TODO: implement logic
        return {
            "latitude": random.uniform(12.0, 13.0),
            "longitude": random.uniform(77.0, 78.0)
        }
    
    def get_odometer(self, vehicle_id: str) -> Optional[float]:
        """
        Get vehicle odometer reading (mock).
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            Odometer reading in km or None
        """
        # TODO: implement logic
        return random.uniform(1000.0, 50000.0)
    
    def get_charging_status(self, vehicle_id: str) -> Optional[Dict]:
        """
        Get charging status for a vehicle (mock).
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            Dictionary with charging status or None
        """
        # TODO: implement logic
        return {
            "is_charging": random.choice([True, False]),
            "charging_power_kw": random.uniform(3.0, 22.0) if random.choice([True, False]) else 0.0
        }
    
    def get_vehicle_data(self, vehicle_id: str) -> Optional[VehicleData]:
        """
        Get comprehensive vehicle data (mock).
        
        Args:
            vehicle_id: Vehicle identifier
            
        Returns:
            VehicleData instance or None
        """
        # TODO: implement logic
        location = self.get_location(vehicle_id)
        charging = self.get_charging_status(vehicle_id)
        
        return VehicleData(
            vehicle_id=vehicle_id,
            soc=self.get_soc(vehicle_id),
            location_latitude=location["latitude"] if location else None,
            location_longitude=location["longitude"] if location else None,
            odometer_km=self.get_odometer(vehicle_id),
            is_charging=charging["is_charging"] if charging else None,
            charging_power_kw=charging.get("charging_power_kw") if charging else None,
            timestamp=datetime.utcnow()
        )
