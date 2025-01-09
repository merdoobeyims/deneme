from pyrogram import *
from pyrogram.types import *
import os


# Yazilim calistiginda terminal temizleme fonksiyonu SILME bunu :D
def sil():
    os.system('cls' if os.name == 'nt' else 'clear')

api_id = 23428222
api_hash = "892cbbc560a6f38a26159a1e3c443c72"
session = "BAFlfH4AgwZYbf94uu7uNkG8O48AaTxw_Ysl8uMekqHXDE9G6xoaqtYmSIk2Jil183QY3t6OCG933nJ1VdJ5PWqT1XK5ifRSwatqHJiEOBV6ErZxscSuzMDuwd4s5gQxY_SfDjWixUGkFyO-f22z1SXug3SZHs-_4zNrZeU4lVX67mpdyskAJ8uO847U4afe1uzkP3Dp7CmHniYZFEDXEHQ11jLixVyRo49BWp19Vx1DPBD_Hf01hURde2O0wC51JWFuxkck9ACx2EOtBbs8gt3-kIBLOXqql00UkgRRQzyzEYkAkN9aHzhJiI7mExBrY-VS4-l2v0aTLeypMHJjRwn428O3zgAAAAHMsiecAA"

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
