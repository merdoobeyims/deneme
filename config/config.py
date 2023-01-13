import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BABpmu72j1duLmfXxBFay_wv0ZCPRyYibyzhvrUSRteOdmj6KU9hZunlIbrijMflW30U4VshD9lYKHM0yDrJgTXNv-FHUH94DIy6UWHWVI5NynpaPh5KHAr57KjglyRJAsod8QxZ9LjZoLC05tSkjcKtjhYNq5QW4hzHVxl6bj7xXXOg7OTjkywgqNgUtzPbwhFg_SAAJwV4q6Ib5ydyMh7b204AUiseF0mKotv5-gc_5gRj0uQY928Na0ZiLzRdBHIZtFJLZ7Apo3-D7YfAEnW4SFyfYPinZHhF_RUhjemXFSXA6cNA4MjYZXlw_xjTcxbis4LNKa6Iouvqas4cvNsZUhAOHgA")
API_ID = int(getenv("api_id", "9316256"))
API_HASH = getenv("api_hash", "5a8a277605c3038129c536a9e79cd761")
CHANNEL_ID = getenv("channel_id", "-1001853114058")
last_messages_amount = 50 
