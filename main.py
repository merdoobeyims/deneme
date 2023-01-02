from os import environ
from pyrogram import Client, idle

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
SESSION_NAME = environ["SESSION_NAME"]

plugins = dict(
    root="plugins",
    include=[
        "vc." + environ["Hacking"],
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=plugins)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> UserBot Başladı. Şansa bak.')
idle()
app.stop()
print('\n>>> Bu Proje @Mahoaga Tarafından Düzenlenmiştir.')
