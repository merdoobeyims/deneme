from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

session_name = getenv("session_name", "")
api_id = int(getenv("api_id", ""))
api_hash = getenv("api_hash", "")
channel_id = getenv("channel_id", "")
last_messages_amount = 50 
