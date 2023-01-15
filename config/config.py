import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAA5lpK2q5GPFdcY6sVs_KIMS7eQwQYvzyBUnczcn5lVBTaeG6ZIY_olDKBv_UFleotU1MXe18TAXUg2LTxj8DlTm8sjG-yni2cFXQHgzoM2pl_vwdD6WRfmIuKPoU8EKdTm6pj-ueFEz2tnsAYSSU1X5E4yTiEXq83ctQAoD-HunbZaPTfh89R5tX21tzmsh4sCLQUiNH_Z5KfmzJxtSfaL1JgiKD3BvALhLMCZFj_17Vclc05F7PFIFlksf2e-EXnVwiOMjvxaR1s42U8sQ7MV7JH0pPKA8UVrBOro8M7vL7ub9z0yrxRtIbJ22srM9GwBeVYUw7QUXzkT4fvHcxrnAAAAAV9WO64A")
API_ID = int(getenv("api_id", "20765181"))
API_HASH = getenv("api_hash", "e8ec2b740ac91dfce31faa3ef654d1a4")
CHANNEL_ID = getenv("channel_id", "-1001853114058")
last_messages_amount = 50 
