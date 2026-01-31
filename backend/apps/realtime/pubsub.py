"""
Pub/Sub manager for real-time events.
"""
from typing import Dict, List, Callable
import asyncio
import json


class PubSubManager:
    """
    Simple pub/sub manager for WebSocket events.
    """
    
    def __init__(self):
        """Initialize pub/sub manager."""
        self.subscribers: Dict[str, List[Callable]] = {}
    
    def subscribe(self, topic: str, callback: Callable):
        """
        Subscribe to a topic.
        
        Args:
            topic: Topic name
            callback: Callback function
        """
        # TODO: implement logic
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)
    
    def publish(self, topic: str, data: Dict):
        """
        Publish data to a topic.
        
        Args:
            topic: Topic name
            data: Data to publish
        """
        # TODO: implement logic
        if topic in self.subscribers:
            for callback in self.subscribers[topic]:
                asyncio.create_task(callback(data))
    
    def unsubscribe(self, topic: str, callback: Callable):
        """
        Unsubscribe from a topic.
        
        Args:
            topic: Topic name
            callback: Callback function
        """
        # TODO: implement logic
        if topic in self.subscribers:
            self.subscribers[topic].remove(callback)
