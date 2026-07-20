import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_HTML_DIR = os.path.join(BASE_DIR, "raw_html")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")
LOG_DIR = os.path.join(BASE_DIR, "logs")

MAX_CONCURRENT_REQUESTS = 10
REQUEST_TIMEOUT = 30
