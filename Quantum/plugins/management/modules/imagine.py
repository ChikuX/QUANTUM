from .. import app
import time,os
from pyrogram import Client, filters
import asyncio
import logging, requests
from pyrogram.types import InputMediaPhoto
from pyrogram.enums import ChatAction,ParseMode
from MukeshAPI import api
@app.on_message(
    filters.command(
        ["generate", "imagine"],
        prefixes=["+", ".", "/", "-", "?", "$", "#", "&"],
    )
)
async def imagine(b, m):
    if len(m.command) < 2:
        return await m.reply_text(
            "Usᴀɢᴇ /imagine <prompt>.\n`/imagine cute girl picture `",
            parse_mode=ParseMode.MARKDOWN,
        )
    else:
        text = m.text.split(" ", 1)[1]
    try:
        mukesh = await m.reply_text(
            f"{m.from_user.first_name} Pʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ Qᴜᴇʀʏ. {text}\nᴡᴀɪᴛ ғᴇᴡ sᴇᴄᴄᴏɴᴅ...\t💕",
            disable_web_page_preview=True,
        )
        await b.send_chat_action(m.chat.id, ChatAction.UPLOAD_PHOTO)
        x=api.ai_image(text)
        with open("mukesh.jpg", 'wb') as f:
            f.write(x)
        caption = f"""
    💘sᴜᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ : {text}
    ✨ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ : [{app.mention})
    🥀ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {m.from_user.mention}
    """
        await mukesh.delete()
        await m.reply_photo("mukesh.jpg",caption=caption,quote=True)
    except Exception as e:
        await m.reply(f"error {e}")