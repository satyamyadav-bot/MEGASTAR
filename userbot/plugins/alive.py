import asyncio
import os
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MEGASTAR"
ALIVE_PIC = os.environ.get("ALIVE_PIC", None)

global megastar
megastar = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/ea5c671288eaede7f5407.jpg"
file2 = "https://telegra.ph/file/3a8f1d5e1d6243337a405.jpg"
file3 = "https://telegra.ph/file/2727d041dfa5335fcf244.jpg"
file4 = "https://telegra.ph/file/bde1379997eb26df7b695.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "**🄼🄴🄶🄰🅂🅃🄰🅁 🄸🅂 🄾🄽🄻🄸🄽🄴 **\n\n"
pm_caption += (
    "**Yeah, I Am Alive 😎😎 And Systems Are Working Perfectly As It Should Be...**\n\n"
)
pm_caption += "༒About My System༒ \n\n"
pm_caption += "➥ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n"
pm_caption += "➥ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/MEGASTAR_USERBOT)\n"
pm_caption += "➥ **ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ** ☞ [ᴊᴏɪɴ](https://t.me/MEGASTAR_SUPPORT)\n"
pm_caption += "➥ **ʟɪᴄᴇɴꜱᴇ**  ☞ [ AGPL-3.0 License](https://github.com/Bristi-OP/MEGASTAR/blob/master/LICENSE)\n"
pm_caption += "➥ **𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈** ☞ [Repo](https://github.com/Bristi-OP/MEGASTAR)\n"
pm_caption += "➥ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [🄼🄴🄶🄰🅂🅃🄰🅁](https://t.me/none1p)\n\n"
pm_caption += f"➥ **ᴍʏ 𝙾𝚆𝙽𝙴𝚁** ☞ [{DEFAULTUSER}](tg://user?id={megastar})\n"


@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(yes):
    await yes.get_chat()
    global megastar
    megastar = borg.uid
    await yes.delete()
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    await on.edit(file=file2)

    await asyncio.sleep(edit_time)
    await on.edit(file=file3)

    await asyncio.sleep(edit_time)
    await on.edit(file=file1)

    await asyncio.sleep(edit_time)
    await on.edit(file=file3)

    await asyncio.sleep(edit_time)
    await on.edit(file=file2)

    await asyncio.sleep(edit_time)
    await on.edit(file=file1)

    await asyncio.sleep(edit_time)
    await on.edit(file=file4)


    """ For .alive command, check if the bot is running.  """

    await borg.send_file(yes.chat_id, caption=pm_caption)
    await yes.delete()


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@borg.on(admin_cmd(outgoing=True, pattern="salive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "**🄼🄴🄶🄰🅂🅃🄰🅁 🄸🅂 🄾🄽🄻🄸🄽🄴**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.1\n"
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/MEGASTAR_USERBOT)\n"
        )
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/MEGASTAR_SUPPORT)\n"
        )
        pm_caption += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](http://www.gnu.org/licenses/gpl-3.0.en.html)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ @YOU_ARE_UNDER_ARREST ](https://t.me/YOU_ARE_UNDER_ARREST)\n"
        pm_caption += "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n ───█▒▒░░░░░░░░░▒▒█───\n    ────█░░█░░░░░█░░█────\n   ─▄▄──█░░░▀█▀░░░█──▄▄─\n    █░░█─▀▄░░░░░░░▄▀─█░░█\n    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n    █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n    █░░║║║╠─║─║─║║║║║╠─░░█\n   █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
        await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(
            alive.chat_id, ALIVE_PIC, caption=pm_caption, link_preview=False
        )
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/a47ec82a3a5c96f4aa5fe.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(
            alive.chat_id,
            "**🄼🄴🄶🄰🅂🅃🄰🅁 🄸🅂 🄾🄽🄻🄸🄽🄴**\n"
            f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
            "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
            "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/MEGASTAR_USERBOT)\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/MEGASTAR_SUPPORT)\n"
            "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](http://www.gnu.org/licenses/gpl-3.0.en.html)\n"
            "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ @YOU_ARE_UNDER_ARREST ](https://t.me/YOU_ARE_UNDER_ARREST)\n"
            "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n ───█▒▒░░░░░░░░░▒▒█───\n    ────█░░█░░░░░█░░█────\n   ─▄▄──█░░░▀█▀░░░█──▄▄─\n    █░░█─▀▄░░░░░░░▄▀─█░░█\n    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n    █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n    █░░║║║╠─║─║─║║║║║╠─░░█\n   █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n",
            link_preview=False,
        )
        await event.delete()
