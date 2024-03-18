# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
import logging
from pymongo import MongoClient
from Script import script
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
from config import API_ID, API_HASH, ADMINS, DB_NAME
from config import DB_URI as MONGO_URL

mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["cloned_vjbotz"]
mongo_collection = mongo_db[DB_NAME]

async def restart_bots():
    logging.info("Restarting all bots........")
    bots = list(mongo_db.bots.find())
    for bot in bots:
        bot_token = bot['token']
        try:
            ai = Client(
                f"{bot_token}", API_ID, API_HASH,
                bot_token=bot_token,
                plugins={"root": "clone_plugins"},
            )
            await ai.start()
        except Exception as e:
            logging.exception(f"Error while restarting bot with token {bot_token}: {e}")
