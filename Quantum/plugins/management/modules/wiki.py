
import wikipedia
from pyrogram import filters
from pyrogram.enums import ParseMode

from wikipedia.exceptions import DisambiguationError, PageError

from .. import app as quantum
@quantum.on_message(filters.command(["wiki", f"wiki@{quantum.username}"]))

async def wiki(_,m):
    global res
    if len(m.command) < 2:
        return await m.reply_text("**Example:**\n\n`/wiki India`")
    search = m.text.split(' ')[1]
    try:
        res = wikipedia.summary(search)
    except DisambiguationError as e:
        await m.reply_text(
            "Disambiguated pages found! Adjust your query accordingly.\n<i>{}</i>".format(
                e
            ),
            parse_mode=ParseMode.HTML,
        )
    except PageError as e:
        await m.reply_text(
            "<code>{}</code>".format(e), parse_mode=ParseMode.HTML
        )
    if res:
        result = f"<b>{search}</b>\n\n"
        result += f"<i>{res}</i>\n"
        result += f"""<a href="https://en.wikipedia.org/wiki/{search.replace(" ", "%20")}">​🇷​​🇪​​🇦​​🇩​ ​🇲​​🇴​​🇷​​🇪​...</a>"""
        if len(result) > 4000:
            with open("result.txt", "w") as f:
                f.write(f"{result}\n\n")
            with open("result.txt", "rb") as f:
                await m.reply_document(
                    document=f,quote=True,
                    filename=f.name,
                    reply_to_message_id=m.reply_to_message.id,
                    parse_mode=ParseMode.HTML,
                )
        else:
            await m.reply_text(
                result, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            )


# __help__ = """
# » /wiki (text) *:* sᴇᴀʀᴄʜs ᴀʙᴏᴜᴛ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡɪᴋɪᴘᴇᴅɪᴀ.
# """
# __mod_name__ = "Wɪᴋɪ"