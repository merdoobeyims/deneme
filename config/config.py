import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "1BJWap1sBu6trRCB7Tf-5Cxijz8-ynzCyglYgEu6Vsp21EgxSdKAk2MCF4iLHSGkeHPhSrrecUQ3OtAw6JnbikZ_CIcFEOXOA6MYUfanNWEdbNxqaWxp6BlpZC-P0Lae0s0v4MMruAjoT1GskrGajgK3MKlDoM3LeSWVAqgXQmDr_BU_VSxLgqT4tGq4uYR-KSPsYk_5IAXMrCIm3vTLWpFFLxbnZzClWjAWSpgRSrFvl9FrNkiQC-ud1gnCXZBynfuYTfobvGdCvc9hPkfFxk3ozAGhMdBs2NLLL7p7dpzk2RE5IuGgF1wEqyK3IdpEEbxYJRGZVuYt-cHnCqUZCioSG3wIYH0g=")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-1001853114058")
last_messages_amount = 50 
