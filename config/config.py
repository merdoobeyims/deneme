import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BABVgLqVQc6nzVId22Yps0B69UMmsaeUdkOR-o8XXSA50YD_LKNNIVjsZttkzU7JuP-xejn5_aLQLN_tgopVB8wC3L5y0OTBbTnZnxxkcHh5v4ps7wpasopOrx9kkwfYYfYRd2JnraasozgfftgPSL9w2W7qzydhFxNT46J10uhgECDQQPOeqJqcicQCGRo7N0SLyiW4aAwVNxMV7SucUbzK7ZhwGfTlK0CkbRfTxS_YYQU0T2U0WFUm_IpUCsk2HrK_gO8j32J96trJkNHwPHmeRsDruE_s2lZd0xdWwlITYb_UbHNAadq3bWKsELWvSbAp6hTZgnHJgvXok1ta_DflAAAAAaxmpnYA")
API_ID = int(getenv("api_id", "28112"))
API_HASH = getenv("api_hash", "72ac0911ddf53a020560e0dde09650a6")
CHANNEL_ID = getenv("channel_id", "-100231165")
last_messages_amount = 90
