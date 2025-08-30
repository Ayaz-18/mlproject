# logger.py
import logging
import os
from datetime import datetime

# Create logs directory
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Complete path for log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logger Configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] Line: %(lineno)d | %(name)s | %(levelname)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# Example usage
