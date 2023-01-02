from pyrogram import Client, idle

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
