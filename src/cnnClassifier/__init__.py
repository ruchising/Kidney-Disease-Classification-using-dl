import logging
import os

# create logs folder
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),  
        logging.StreamHandler()          
    ]
)

logger = logging.getLogger("cnnClassifier")