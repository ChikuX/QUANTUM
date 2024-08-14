from pyrogram import Client, filters

@Client.on_message(filters.command("start",prefixes=".")& filters.me)
async def start(b,m):
    await m.reply(f"hi {m.from_user.first_name}")
    
@Client.on_message(filters.command(["ping","alive"],prefixes=".")& filters.me)
async def ping(b,m):
    await m.reply(f"hi {m.from_user.first_name} I am Alive")
    
from Quantum.utils.decorators import AdminActual, language
@language   
@Client.on_message(filters.command("help",prefixes=".")& filters.me)
async def help(b,m,_):
    await m.reply(_["ub_help"])