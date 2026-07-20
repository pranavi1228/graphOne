import asyncio
import random
import logging

logger = logging.getLogger(__name__)


async def async_retry(
    func,
    *args,
    retries=5,
    base_delay=1,
    exceptions=(Exception,),
    **kwargs
):
    """
    Generic async retry with exponential backoff and jitter.
    """

    for attempt in range(retries):
        try:
            return await func(*args, **kwargs)

        except exceptions as e:

            if attempt == retries - 1:
                logger.error(f"Retry failed after {retries} attempts")
                raise

            delay = base_delay * (2 ** attempt)
            jitter = random.uniform(0, 1)

            wait_time = delay + jitter

            logger.warning(
                f"{e} | retry {attempt+1}/{retries} | sleeping {wait_time:.2f}s"
            )

            await asyncio.sleep(wait_time)