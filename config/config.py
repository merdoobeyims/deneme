from pyrogram import *
from pyrogram.types import *
import os


# Yazilim calistiginda terminal temizleme fonksiyonu SILME bunu :D
def sil():
    os.system('cls' if os.name == 'nt' else 'clear')

api_id = 0
api_hash = ""
session = ""

app = Client(session_name='bot', api_id=api_id, api_hash=api_hash, session_string=session)


@app.on_message(filters.all & filters.private)
async def sureli_(client, message: Message):
    user = message.from_user
    if user.is_bot or user.is_self:
        return
    if not message.photo or not message.video:
        return
    
    if message.photo:
        if not message.photo.ttl_seconds:
            return
        caption = message.caption if message.caption else ""
        media = await message.download()
        sure = message.photo.ttl_seconds
    elif message.video:
        if not message.video.ttl_seconds:
            return
        caption = message.caption if message.caption else ""
        media = await message.download()
        sure = message.video.ttl_seconds
    caption += f"\n\n🕒 Sure: {sure} saniye"
    if message.photo:
        await client.send_photo('me', media, caption=caption)
    elif message.video:
        await client.send_video('me', media, caption=caption)
    return os.remove(media)



sil()
app.start()
print("Bot Calisiyor")
idle()
