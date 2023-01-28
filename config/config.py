import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BACxAt9wvsaKWzkFIZMgDJh_RhHBw4Ssok23gFxmILePtY1C2C9f_OJJdsutrf4-_vRAKwTaWhigITqQ3C8MiNIBy70uW7PLpEoJOF_s9jq24CwAL9phx_rNKR-INxpgB5fO2YspmuuAT5_uvZGopAyhyRmnqDHkjUUmQ539XNXePRsoOhnlb5vQCwn-QRl_SWm_NqUgkd1gEgfA93HjW8t7cKUUS6bIQdXuPmQY9uHWr4ybYAiR1w5REsei0dNPyeVhUUZXfQdANQvTRlMojjpLj5rNz5f6uszzvtrgVF4Zo38Smc1VugzU-ewIhWFBssoQhSYM5ZDMbY9cSiWMMCwSAAAAAV9WO64A")
API_ID = int(getenv("api_id", "20765181"))
API_HASH = getenv("api_hash", "e8ec2b740ac91dfce31faa3ef654d1a4")
CHANNEL_ID = getenv("channel_id", "-1001853114058")
last_messages_amount = 50
