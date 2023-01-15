import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAAegSPjtzkiiWI4hpxZX0-k8AWWNb2sr9yZEjRS6ms11H32RFVeGLrt3hVFqZTB7pqpyhgKkRPiqXRKbSEp6JtK0BQ0qXOjruxHqgmrnCL3m13z3b1r59YncW2BKcfMftiMaffo4z8RKVd2NZGFTxjgz40i8fap76q_2IT4xCpDqQ6TwqH_m27PMzmwdGtBCCcS0-G2eoNw2aPy9JeHv2qI7Zb9ueHDRT3QVyGE7xxa9tx-N7VVmpxtTg-gLRycrR6UvcECFr2G16cv-MdKvZbRttaJr6eF6wv7UxwY0-lU6zYHuLZCZrQqbpqWMnSDr99wn-XYL5lEVm9LqF9_T2u8AAAAAV9WO64A")
API_ID = int(getenv("api_id", "20765181"))
API_HASH = getenv("api_hash", "e8ec2b740ac91dfce31faa3ef654d1a4")
CHANNEL_ID = getenv("channel_id", "-1001853114058")
last_messages_amount = 50 
