import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "AQATVSHx2cszakv4d8jF7x7zxJs8RleWLT-lHgjK-s0bBZplsWWE57q1FuA6EMFehCvhhEMeOXxY0vH0rsj-D4nMHD9GwG7SrNVNJfzHZP79OSxzRsLTWin8AgWp0ALNu2oKQxZMGNyIsy6Nto_igWDLEGr8RMWlKQE51GSkARRmkqiu1jO0CU5bW2naFv9l3YTPbGw1TmDdQQ_7FsXfKXO-hDUxeMmf_QuBdSoUf0SIOrcHJoZzFSSCYnN9CwZnvEfM6vjyyrL7nrkGWZwRneCvBOSjorC2Yx3L-KFKgp3Q_z04UGqOURia70RijF9xtTezDV54lf6hyZue03WoKoK3AAAAAWfX9u8A")
API_ID = int(getenv("api_id", "28398608"))
API_HASH = getenv("api_hash", "6c8016f3a568e5f2c5643f13f64d7138")
CHANNEL_ID = getenv("channel_id", "-1001688405125")
last_messages_amount = 50
