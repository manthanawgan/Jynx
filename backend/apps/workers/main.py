"""
Main worker application.
"""
import asyncio
from apps.workers.scheduler.rebalancer import SlotRebalancerWorker
from apps.workers.alerts.abuse_detector import AbuseDetectionWorker
from apps.workers.telemetry.token_refresher import TokenRefreshWorker


async def main():
    """
    Run all background workers.
    """
    # Create workers
    rebalancer = SlotRebalancerWorker()
    abuse_detector = AbuseDetectionWorker()
    token_refresher = TokenRefreshWorker()
    
    # Run workers concurrently
    await asyncio.gather(
        rebalancer.run(),
        abuse_detector.run(),
        token_refresher.run()
    )


if __name__ == "__main__":
    asyncio.run(main())
