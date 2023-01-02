from Hacking import 
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db



import logging
from pyrogram import Client, idle
from config import API_HASH, API_ID, SESSION_NAME 

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

app = Client("Timed", api_hash=API_HASH, api_id=API_ID, session_name=SESSION_NAME)

app.start()
LOGGER.info("Hadi iyisin hileci herif seni 😂😂😂")
idle()
