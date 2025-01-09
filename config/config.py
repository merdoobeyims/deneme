from pyrogram import *
from pyrogram.types import *
import os


# Yazilim calistiginda terminal temizleme fonksiyonu SILME bunu :D
def sil():
    os.system('cls' if os.name == 'nt' else 'clear')

api_id = 23428222
api_hash = "892cbbc560a6f38a26159a1e3c443c72"
session = "from pyrogram import *
from pyrogram.types import *
import os


# Yazilim calistiginda terminal temizleme fonksiyonu SILME bunu :D
def sil():
    os.system('cls' if os.name == 'nt' else 'clear')

api_id = 28113782
api_hash = "72ac0911ddf53a020560e0dde09650a6"
session = "BABS7v4nfkVKNqa_aPd2C4AWm5HwOgU1CCzCzcnKjGmSPI8g8SM1S3CjcTArhWANRNWd7OJuLr6aNI-c3LfOV342jv7nkHXkD3ye2TrFkifoCeqfKOsCHiZlM5eYArI1J7ciydN2WC6I7BRrvi004W6H-uiVZ7jl9FsDgoBvkfXXnEga1uDBBu1NEdqOue_CRRgSsjSME4QrU7wahSidFy91cC1BGdNgbnXOxB4nJmG6jglTvoL_LI-x2jJzM6JG8vMVpx1svpF2l-C16QgKOaZtuDMyZDIaHfqfN7f1YeTlVrOPGhch_O6ucGMXqOmBHmZGqBP57ZjvfdrFM74eSX3PAAAAAcyyJ5wA"

app = Client('bot', api_id=api_id, api_hash=api_hash, session_string=session)


@app.on_message(filters.private & (filters.video | filters.photo))
async def sureli_(client, message: Message):
    user = message.from_user
    if user.is_bot:
        return
    if user.is_self:
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
    caption += 'User: {}\n\nID: `{}`'.format(user.first_name, user.id)
    caption += f"\n\n🕒 Sure: `{sure}` saniye"
    if message.photo:
        await client.send_photo('me', media, caption=caption)
    elif message.video:
        await client.send_video('me', media, caption=caption)
    return os.remove(media)



sil()
app.start()
print("Bot Calisiyor")
idle()"

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
