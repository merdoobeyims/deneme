import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAAqPHWib7l4d-xV8O0iCB5XxcXlsdwsHAB9ffFlraU8Ax9PicYywsy9iutNJsc4Am4zdgLv8ZM8AzxNdQx79S0SgNGiITTT43LHrobLAwSzfcRb4u6sq3DDMt-9eIXS1nIgOgudlnA8sKox8pw7CdIYowUnCyZr6AwM9SVjZb4GXUJ-8ArY7rv7fqlH4oJS-fPZWqEogS_zia8J693ZSOSTYuFJf1gNhbmOkYxHd97KX8GDTAWk1D6oIEcjD74h-Z7cWsaDk3djGjWgFjueMBSnnHggNrPe_YJkryUzhil2n9nDluaI9ce8xM2-QiOSrmd0O095OOA0xhK_mN4dHEMJUhAOHgA")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-100185384542")
last_messages_amount = 50
