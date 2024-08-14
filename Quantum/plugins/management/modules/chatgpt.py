
from pyrogram import filters
import asyncio, requests
from pyrogram.enums import ParseMode
#  chatgpt
from MukeshAPI import api
from . import app as Client
async def question(message):
    """Extract the text from a message.
    
    Arguments:
    message -- the message to extract text from
    
    Returns:
    text -- the extracted text from the message, if available; otherwise, a response to provide a query
    
    """
    if message.reply_to_message:
        text = message.reply_to_message.text
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("Please provide a query too")
    
    return text

@Client.on_message(
    filters.command(
        ["chatgpt", "ask"]
    )
)        
async def chatgpt_reply(b, message):
    a=await question(message)
    search_result = api.gemini(a)["results"]
    await message.reply_text(f"{search_result}",parse_mode=ParseMode.MARKDOWN,quote=True)  