import requests
from pyrogram import filters
import asyncio

from .. import app as quantum


@quantum.on_message(filters.command(["truth", f"truth@{quantum.username}"]))
async def truth(bot, message):

    truth = requests.get(f"https://api.truthordarebot.xyz/v1/truth").json()["question"]
    await message.reply_text(truth)
@quantum.on_message(filters.command(["dare", f"dare@{quantum.username}"]))
async def dare(bot, message):

    dare = requests.get(f"https://api.truthordarebot.xyz/v1/dare").json()["question"]
    await message.reply_text(dare)