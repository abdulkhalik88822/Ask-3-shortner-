import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '21723146'))
API_HASH = environ.get('API_HASH', '07cd9c82699c28111cb33693ecbd9116')
BOT_TOKEN = environ.get('BOT_TOKEN', '6088261601:AAFUCUHztjmN_wBprFFSiASK-1Tsf0XpBg4')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6133440326').split()]
USERNAME = environ.get('USERNAME', 'https://t.me/Attitude2688')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001626107740'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/DD_Movies_Request')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001569815531').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://abdul:abdul@cluster0.tz24m3k.mongodb.net/?retryWrites=true&w=majority")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://abdul:abdul@cluster0.tz24m3k.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001626107740'))
QR_CODE = environ.get('QR_CODE', 'https://telegra.ph/file/e717ffdfb2394774e44f1.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1001626107740'))
URL = environ.get('URL', 'filetolin-f1cdaf30132f.herokuapp.com')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001626107740'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/bots_up/76")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/bots_up/165")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "ffc679dc9713585f2459bf286b80a086e17f190c")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "dollarurl.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "83bb4ec4449b378ae52b9f4e84a2bfb7970ed6ec")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "yamlinks.com")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1001954276464')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001626107740'))

# hastags request features
request_channel = environ.get('REQUEST_CHANNEL', '-1001626107740')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# bot settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
