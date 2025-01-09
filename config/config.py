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
session = "BAGs-3YAiAS4-7a_QIqz19OscARTH3H38FUj-aIshti-rPpqEzsaadGqdMBTuc8FDISxn0eBSLmy_Cd5ViOVgKtDgdutUR4jmheN6xY3ADB_KMndrmTf8jnyaBY42zvEXMThZYcCXi-K8EYCszqSo1e-g2iiwgjz82EWirKV_c_oo-mONYiSjrH_heWZq-znlcBZxTDMzB7TYvr8EqInDTYmJl95HfXTAYLf0umEcaXFUW9mkTuPu5tDPDp7shh2yUPoqErFky8Xgl4oOJOEUvgSZ4l4xix7nGfiLkkgoMZY5Al2izWZGQE3cg2WrBnkDGpe3yLqBKoFOkt_P55JYFNaiifyVQAAAAGsZqZ2AA"

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
