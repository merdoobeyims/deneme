import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BAE82f0AKpbweao5CsTdDdemCBW-zw6HZ00gozZ0pg179yI_Ji_gFzP5Gvps75pN2kzzz8gxSdY0AbQuZUmiMXWiBraRHMUHM6zKhajIqBO09f4x_hUzrwcB7XzMDRGK6J0Eon9rj3YFEJJqXA3lyVusqyg3LSn9Dslg1Yr1we6rQTBsP2L61DlDnABOq-hjMVcC9cP-TqgoVCARn6o6nIwNI28yadfehYbwtsWqb7Ux6O9ZMt9mrMuGVinlY4govj_Y-IxUjMa6D2EyX5pDsyKGKyY9V7cXI2gzLjvRHkVnlXgSUENW1yCR5U-sEc74yGeLqo8z1jZOdPn7vH51Fa1JpXt0JQAAAAFfVjuuAA")
API_ID = int(getenv("api_id", "20765181"))
API_HASH = getenv("api_hash", "e8ec2b740ac91dfce31faa3ef654d1a4")
CHANNEL_ID = getenv("channel_id", "-1001688405125")
last_messages_amount = 50
