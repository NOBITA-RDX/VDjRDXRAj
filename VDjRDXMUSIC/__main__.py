import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VDjRDXMUSIC import LOGGER, app, userbot
from VDjRDXMUSIC.core.call import RDX
from VDjRDXMUSIC.misc import sudo
from VDjRDXMUSIC.plugins import ALL_MODULES
from VDjRDXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("sᴛʀɪɴɢ sᴇssɪᴏɴ ɴᴏʏ ғɪʟʟᴇᴅ, ᴘʟᴇsᴇ ғɪʟʟ ᴀ ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VDjRDXMUSIC.plugins" + all_module)
    LOGGER("VDjRDXMUSIC.plugins").info("sᴀʀᴇ ғᴇᴀᴛᴜʀᴇs ʟᴏᴀᴅ ʜᴏ ɢʏᴇ ʙᴀʙʏ😍...")
    await userbot.start()
    await RDX.start()
    try:
        await RDX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("VDjRDXMUSIC").error(
            "ᴘʟᴢ sᴛᴀʀᴛ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇᴄʜᴀᴛ\ᴄʜᴀɴɴᴇʟ\n\nʀᴅx ʙᴏᴛ sᴛᴏᴘ........"
        )
        exit()
    except:
        pass
    await RDX.decorators()
    LOGGER("VDjRDXMUSIC").info(
        "⭒☆•────•°•❀•°•────•☆⭒\n  ✪ᴍᴀᴅᴇ ʙʏ ʀᴅx ʀᴀᴊ✪\n⭒☆•────•°•❀•°•────•☆⭒"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("VDjRDXMUSIC").info("sᴛᴏᴘ ᴠᴅᴊ ʀᴅx ʀᴀᴊ ᴍᴜsɪᴄ ♪ ʙᴏᴛ..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
