from loguru import logger
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger.add(
    f"{LOG_DIR}/graphone.log",
    rotation="5 MB",
    retention="5 days",
    level="INFO"
)

app_logger = logger