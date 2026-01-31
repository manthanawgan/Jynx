"""
Integration tests for external integrations.
"""
import pytest
from unittest.mock import Mock, patch

from integrations.vehicles.smartcar_adapter import SmartcarAdapter
from integrations.vehicles.mock_adapter import MockAdapter


class TestSmartcarAdapter:
    """Tests for SmartcarAdapter."""
    
    @pytest.fixture
    def adapter(self):
        """Create adapter instance."""
        token_manager = Mock()
        return SmartcarAdapter(token_manager)
    
    def test_get_soc(self, adapter):
        """Test getting SOC."""
        # TODO: implement test with mocked API calls
        pass


class TestMockAdapter:
    """Tests for MockAdapter."""
    
    @pytest.fixture
    def adapter(self):
        """Create adapter instance."""
        return MockAdapter()
    
    def test_get_soc(self, adapter):
        """Test getting SOC from mock."""
        soc = adapter.get_soc("test_vehicle")
        assert soc is not None
        assert 0.0 <= soc <= 1.0
    
    def test_get_location(self, adapter):
        """Test getting location from mock."""
        location = adapter.get_location("test_vehicle")
        assert location is not None
        assert "latitude" in location
        assert "longitude" in location
