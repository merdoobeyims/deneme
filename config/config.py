import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAB7649GQmV_xINo0WBVOYNb_N1yunayWxG_byVyDBfNCw_xcgNkhVX87klJTarr2OLEx6No8PR90-nAFLbx9bZa4LaoZKm217WKGPsI7oBlXHZfxchwy10Lxqgdghs2IznFvjtFT1lrRi5DW0QA5A72J83kJsbpkz3iE5jmjbiwHBDWpnbbdY4Tuc_FS6pmvignzniY1uO5OthS5siQagbkZbrnDszjaOcPnaXI4YDtLnulcJKn1JSRH28_vLSrFaeCZolZKAdfOg2gvl6gIAyXgxbD3_fHRnOYt_NlnhwpQWxaaDwtjI_oWGsiyg4Bl6FXGYXpNMxswCxVen-o0fsTUhAOHgA")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-100185384542")
last_messages_amount = 50
