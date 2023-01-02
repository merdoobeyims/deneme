import logging
from pyrogram import Client, idle
import config import API_HASH, API_ID, SESSION_NAME 
from Hacking import timedcapture
from Hacking import app, LOGGER
 

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

app = Client("Timed", api_hash=API_HASH, api_id=API_ID, session_name=SESSION_NAME)

app.start()
LOGGER.info("Hadi iyisin hileci herif seni 😂😂😂")
idle()

