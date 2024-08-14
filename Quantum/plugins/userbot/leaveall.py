# MIT License
#
# Copyright (c) 2023 MukeshmousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio

from pyrogram import filters,Client 
from pyrogram.errors import FloodWait
from pyrogram.types import Message

@Client.on_message(filters.command(["leaveall", "assleaveall"],".")& filters.me)
async def leaveall_chats(client, message: Message):
    lear = await message.reply_text(f"» sᴛᴀʀᴛᴇᴅ ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛs...")
    left = 0
    failed = 0
    chats = []
    async for dialog in client.get_dialogs():
        chats.append(int(dialog.chat.id))
    for i in chats:
        try:
            await client.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
            failed += 1
    try:
        await lear.edit_text(
            f"<u>**»  sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :**</u>\n\n**ʟᴇғᴛ :** `{left}`\n**ғᴀɪʟᴇᴅ :** `{failed}`"
        )
    except:
        await message.reply_text(
            f"<u>**»  sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :**</u>\n\n**ʟᴇғᴛ :** `{left}`\n**ғᴀɪʟᴇᴅ :** `{failed}`"
        )
        

