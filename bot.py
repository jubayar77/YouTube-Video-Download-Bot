# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.API_ID,24848670 
    api_hash=Config.API_HASH,64fc72973bc5a6f067c015beaa1c1fab
    bot_token=Config.BOT_TOKEN,7149847066:AAFtXeadhGxtyFxiZ2WO2z6qXXRHb0Rxubk
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
