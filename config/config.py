import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "AQATVSHx2cszakv4d8jF7x7zxJs8RleWLT-lHgjK---hDUxeMmf_QuBdSoUf0SIOrcHJoZzFSSCYnN9CwZnvEfM6vjyyrL7nrkGWZwRneCvBOSjorC2Yx3L-KFKgp3Q_z04UGqOURia70RijF9xtTezDV54lf6hyZue03WoKoK3AAAAAWfX9u8A")
API_ID = int(getenv("api_id", "29736877"))
API_HASH = getenv("api_hash", "6238bdbf7f4a191a71e7e768dcfccc97")
CHANNEL_ID = getenv("channel_id", "-1001688405125")
last_messages_amount = 50
