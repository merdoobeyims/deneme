from pyrogram import *
from pyrogram.types import *
import os


# Yazilim calistiginda terminal temizleme fonksiyonu SILME bunu :D
def sil():
    os.system('cls' if os.name == 'nt' else 'clear')

api_id = 28113782
api_hash = "72ac0911ddf53a020560e0dde09650a6"
session = "BAGs-3YAm6SAEBlWpS6H3ZM9FC6wuF2PkAFuqGTVlQV5KGznP5NEOFYkozE59caacuVMmY9x6K1-BWhnQ_rjDf-fyc932t-VkzTbqK0snxVjMA6xGt6zMIaiUEOS8DjQm7M2iS_tzsrf9HrRm7WSfz65GHfyLvAOhF7f6XXmJeHkLbKih0FrbkNitIvDg1bE-hvIIP260yicaSmQ4cJb716noF61YO5oYpqlaWtFVEA6j3ZKzZ0yr7vKfh8naSp1seSjFeudxZ6DSx54-XgEAySAFXBfug4WwMW6zpJSH9BIghzdMuOpX7O9lA0toIZgcV0QMx5UBoKQzGbpOhVayJc2hQP-bgAAAAGsZqZ2AA"

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
