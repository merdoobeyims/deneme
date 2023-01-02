import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "")
API_ID = int(getenv("api_id", ""))
API_HASH = getenv("api_hash", "")
CHANNEL_ID = getenv("channel_id", "")
last_messages_amount = 50 
