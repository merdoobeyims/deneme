import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BABokzZBgvllYFsv-hqUiFc-i5ym7IJ-LHd4uJnMbYdmJzcPBZ0JgqCgzvc7mSKH3fg6MQ3h5R3TBvVzYV2HdfYeqeqYpei-nx2yIKUFcWUa7rSwE9if76ddMC98HxdloGRPxo8j3Ctf0Pgd4nyVywTZHst9yjckVFkdTB0y9LDrRJHm9i-Nl2QpvtJEYVeU5hU5i6kjQ3YgWmVTi2nLfXUS1n_sfveeNH2H76oijIOgivi2TqqjxRmatP1xd2sp8gCrowD16WkDUIenjIslrta6R-_HAOCge5BbZJSNnwuJy5HqLKrGYG1doKOcdPWP_iY051eXM1SjeBPxgG_cFQlvAAAAAV9WO64A")
API_ID = int(getenv("api_id", "20765181"))
API_HASH = getenv("api_hash", "e8ec2b740ac91dfce31faa3ef654d1a4")
CHANNEL_ID = getenv("channel_id", "-1001853114058")
last_messages_amount = 50 
