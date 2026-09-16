"""Worker task definition and processing."""

import structlog
from tenacity import retry, stop_after_attempt, wait_exponential

logger = structlog.get_logger()


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
async def process_task(task_id: str) -> bool:
    """Execute single unit of background work with retries."""
    logger.info("processing_task", task_id=task_id)
    # Business logic execution
    return True
