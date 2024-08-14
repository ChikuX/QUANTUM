from gpytranslate import SyncTranslator
from pyrogram import filters
from . import app as Client
from pyrogram.enums import ChatAction, ParseMode, ChatType
trans = SyncTranslator()
from Quantum.utils.decorators import AdminActual, language
@language
@Client.on_message(filters.command("tr"))
async def totranslate(b,m,_):
    message =  m.text
    reply_msg = m.reply_to_message
    if not reply_msg:
        await m.reply_text(
            _["trans_1"],
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = trans.detect(to_translate)
            dest = args
    except IndexError:
        source = trans.detect(to_translate)
        dest = "en"
    translation = trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"<b>ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} ᴛᴏ {dest}</b> :\n"
        f"<code>{translation.text}</code>"
    )

    await m.reply_text(reply, parse_mode=ParseMode.HTML)


