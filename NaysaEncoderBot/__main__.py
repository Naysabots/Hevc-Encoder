# oof
from datetime import datetime as dt
import os
from bot import (
    APP_ID,
    API_HASH,
    AUTH_USERS,
    DOWNLOAD_LOCATION,
    LOGGER,
    TG_BOT_TOKEN,
    BOT_USERNAME,
    SESSION_NAME,
    
    data,
    app,
    crf,
    resolution,
    audio_b,
    preset,
    codec,
    watermark 
)
from bot.helper_funcs.utils import add_task, on_task_complete
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from translation import Translation
from bot.plugins.incoming_message_fn import (
    incoming_start_message_f,
    incoming_compress_message_f,
    incoming_cancel_message_f
)

from bot.plugins.status_message_fn import (
    eval_message_f,
    exec_message_f,
    upload_log_file
)

from bot.commands import Command

sudo_users = "1666551439" 
crf.append("30")
codec.append("libx265")
resolution.append("1280x720")
preset.append("veryfast")
audio_b.append("30k")
# 🤣

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
uptime = dt.now()

def ts(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    
    
    #
    app.set_parse_mode("html")
    #
    # STATUS ADMIN Command

    # START command

    
   
    @app.on_message(filters.incoming & filters.command(["start", f"start@{BOT_USERNAME}"]))
    async def start(bot, update):   
        await update.reply_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=Translation.START_BUTTONS
        )
             
            
        
     
 
    @app.on_message(filters.incoming & filters.command(["restart", f"restart@{BOT_USERNAME}"]))
    async def restarter(app, message):
        if message.from_user.id in AUTH_USERS:
            await message.reply_text("•Restarting")
            quit(1)
        
    @app.on_message(filters.incoming & filters.command(["clear", f"clear@{BOT_USERNAME}"]))
    async def restarter(app, message):
      data.clear()
      await message.reply_text("Successfully cleared Queue ...")
    @app.on_message(filters.incoming & filters.command(["crf", f"crf@{BOT_USERNAME}"]))
    async def changecrf(app, message):
            cr = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {cr} crf"
            crf.insert(0, f"{cr}")
            await message.reply_text(OUT)
            
    @app.on_message(filters.incoming & filters.command(["settings", f"settings@{BOT_USERNAME}"]))
    async def settings(app, message):
            await message.reply_text(f"<b>The current settings will be added to your video file :</b>\n\n<b>Codec</b> : {codec[0]} \n<b>Crf</b> : {crf[0]} \n<b>Resolution</b> : {resolution[0]} \n<b>Preset</b> : {preset[0]} \n<b>Audio Bitrates</b> : {audio_b[0]}")
            
            
               
    @app.on_message(filters.incoming & filters.command(["resolution", f"resolution@{BOT_USERNAME}"]))
    async def changer(app, message):
            r = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {r} resolution"
            resolution.insert(0, f"{r}")
            await message.reply_text(OUT)

            
               
    @app.on_message(filters.incoming & filters.command(["preset", f"preset@{BOT_USERNAME}"]))
    async def changepr(app, message):
            pop = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {pop} preset"
            preset.insert(0, f"{pop}")
            await message.reply_text(OUT)

            
    @app.on_message(filters.incoming & filters.command(["codec", f"codec@{BOT_USERNAME}"]))
    async def changecode(app, message):
            col = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {col} codec"
            codec.insert(0, f"{col}")
            await message.reply_text(OUT)
             
    @app.on_message(filters.incoming & filters.command(["audio", f"audio@{BOT_USERNAME}"]))
    async def changea(app, message):
            aud = message.text.split(" ", maxsplit=1)[1]
            OUT = f"I will be using : {aud} audio"
            audio_b.insert(0, f"{aud}")
            await message.reply_text(OUT)         
        
    @app.on_message(filters.incoming & (filters.video | filters.document))
    async def help_message(app, message):
        query = await message.reply_text("Added to Queue ⏰...\nPlease be patient, Compress will start soon", quote=True)
        data.append(message)
        if len(data) == 1:
         await query.delete()   
         await add_task(message)
            
    @app.on_message(filters.incoming & (filters.photo))
    async def help_message(app, message):
        os.system('rm thumb.jpg')
        await message.download(file_name='/app/thumb.jpg')
        await message.reply_text('Thumbnail Added')
        
    @app.on_callback_query()
    async def button(bot, update):
        if update.data == "home":
            await update.message.edit_text(
                text=Translation.START_TEXT.format(update.from_user.mention),
                reply_markup=Translation.START_BUTTONS,
                disable_web_page_preview=True
            )
        elif update.data == "help":
            await update.message.edit_text(
                text=Translation.HELP_TEXT,
                reply_markup=Translation.HELP_BUTTONS,
                disable_web_page_preview=True
            )
        elif update.data == "about":
            await update.message.edit_text(
                text=Translation.ABOUT_TEXT,
                reply_markup=Translation.ABOUT_BUTTONS,
                disable_web_page_preview=True
            )
        else:
            await update.message.delete()
  
    @app.on_message(filters.incoming & filters.command(["log", f"log@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await upload_log_file(app, message)
    @app.on_message(filters.incoming & filters.command(["ping", f"ping@{BOT_USERNAME}"]))
    async def up(app, message):
      stt = dt.now()
      ed = dt.now()
      v = ts(int((ed - uptime).seconds) * 1000)
      ms = (ed - stt).microseconds / 1000
      p = f"🌋Pɪɴɢ = {ms}ms"
      await message.reply_text(v + "\n" + p)


             

    app.run()


