"""
Event topic definitions.
"""
from enum import Enum


class EventTopic(str, Enum):
    """Event topic enumeration."""
    SLOT_REQUESTED = "slot_requested"
    SLOT_ALLOCATED = "slot_allocated"
    SLOT_CANCELLED = "slot_cancelled"
    SESSION_STARTED = "session_started"
    SESSION_ENDED = "session_ended"
    SESSION_UPDATED = "session_updated"
    EMERGENCY_REQUESTED = "emergency_requested"
    GRID_ALERT = "grid_alert"
    TOKEN_REFRESHED = "token_refreshed"
    ABUSE_DETECTED = "abuse_detected"
