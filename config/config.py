import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAB40QFnfbLs0skhfCyxSKpmzOiUEAALzf9vqkrsrQc0SrrsG1a6Gz-CuM5k9wf0LyiXHOxupWFiZlXi7cUjLeOc1e3AA3yNo43Tmlai712BJVLSYutMOAYR6CE3_ZSskAe-rZQjDguFBSdDy0EejV95fnT3reuDssA-aRK-H7MvXVPcMnMAgIOGC_SOYsfgnh-yDqMbGXdXlGzwFvhKoknvjmmuj8qOqNp17QjReRaxvDS5g4jGsYQ1l_3wA_mmlHNpKz2FfHWh9b6DIeG_d6fCXwZTMxlssIMJ9OnjfmWuMDTFzeEKrT2p03bISYOClroXVSWBwFgvfQVyyrEfMDN9AAAAAVosfb0A")
API_ID = int(getenv("api_id", "15459549"))
API_HASH = getenv("api_hash", "bf21dbfacbc7157d2404f33f7185bd6f")
CHANNEL_ID = getenv("channel_id", "-1001809326053")
last_messages_amount = 50 
