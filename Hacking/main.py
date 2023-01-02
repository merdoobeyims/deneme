from Hacking import app
from pyrogram import idle
from pyrogram import Client
from config import API_ID, API_HASH, SESSION_NAME


app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    session_name=SESSION_NAME,
    plugins=dict(root="Hacking/modules")
)

app.run()
idle() 
