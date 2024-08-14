from unidecode import unidecode

from pyrogram import filters
import asyncio
from pyrogram.enums import ParseMode
from .. import app as quantum
@quantum.on_message(filters.command(["unidecode", f"unidecode@{quantum.username}"]))
async def unide_text(bot, message):
    try:
        if message.reply_to_message:
            text = message.reply_to_message.text
        elif not message.reply_to_message and len(message.command) != 1:
            text = message.text.split(None, 1)[1]
        await message.reply_text(unidecode(text),quote=True)
    except Exception as e:
        await message.reply(e,quote=True)