import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAAGMHu6XQAgPgRbeb3FDYhgMXDilZbHukHC6wiVOpbIqjvW2xpKO9KltcgUhYYl5TW_dNL3Qru12Y_HyzmU43ESijIjCkVImW5VHUx3sH4NygcztMnRFvwtJ_L2D-4hyZEJsEbN7uGOO1q_dHeKFn72Rmuw7MkhPYgPHpRvlScjL0Yh184QgI4SH2bUFVtPuozZzSf06HHKOliNZ2oxQWZAHi1m1JHjiNxP29-PhRrTLGa4hc7EZqlf9OP1Oe-urOKIBG_XRjnKt_zyTexO2r1U51rNq5P4l-1iEfYcuoVYQwRkDCD3AJ8FPSOEFvKIG8pVJBULkp3nv4aDcAYS0ccdAAAAAVB3_0EA")
API_ID = int(getenv("api_id", "23906886"))
API_HASH = getenv("api_hash", "5217aa480e59f3f2244558a4b66d8708")
CHANNEL_ID = getenv("channel_id", "-1001210894866")
last_messages_amount = 50 
