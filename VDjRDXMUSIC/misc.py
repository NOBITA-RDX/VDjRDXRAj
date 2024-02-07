import socket
import time

import heroku3
from pyrogram import filters

import config
from VDjRDXMUSIC.core.mongo import mongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "master",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Ɖᴀᴛᴀʙᴀsᴇ ʟᴏᴀᴅ ʜᴏ ɢʏᴇ ʙᴀʙʏ........")


async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER(__name__).info(f"sᴜᴅᴏ ᴜsᴇʀ ʙʜɪ ʜᴏ ɢʏᴀ ʙᴀʙʏ❀.")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ ʙʜɪ ʟᴏᴀᴅ ʜᴏ ɢʏᴀ......🥀")
            except BaseException:
                LOGGER(__name__).warning(
                    f"ʏᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ғɪʟʟᴇᴅ ʜᴇʀᴏᴋᴜ ᴀᴘɪ ᴋᴇʏ ᴀɴᴅ ʜᴇʀᴏᴋᴜ ᴀᴘᴘ ɴᴀᴍᴇ ❀ᴄᴏʀʀᴇᴄᴛ❀...."
)
