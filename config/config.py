import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "BACpw5M0PJzZ1KiaJMTUyqfH8J0D23kPPeqV4oT5_A_SVwHj2u8R3ImvxebMzGTeDUkjsE4iqN6Gzl0xPA8elOuCBxyDeSSNuQV9CvcP1j9CgnNkUKkZrym4pD3FOZbAhiYAnh6P6no3GJWGaiom429vgmaYSgFlfqW7QILkr7Y-0F73aFOMXNCaJ6HDZbatL6ReMfTbQG0dCu5zvo7E_wPTe2GBbhnEVhS11hcyhh9_tAMVFKcwHFRX4TT6ozEzKe5oimollR9KpLMjNgBC1Q_Pp5yaUT1QA3bQvdQQPRO25LEMLMESc70W6yb9GM_fDWkryjs7mF4mP6ccXIW5_CyBAAAAAV9WO64A")
API_ID = int(getenv("api_id", "20765181"))
API_HASH = getenv("api_hash", "e8ec2b740ac91dfce31faa3ef654d1a4")
CHANNEL_ID = getenv("channel_id", "-1001853114058")
last_messages_amount = 50 
