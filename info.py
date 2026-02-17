import re
from os import environ, getenv
from typing import Set, Optional, List, Dict
from Script import script  # Custom script file with caption & other settings
from pyrogram import Client, filters # কমান্ড হ্যান্ডেল করার জন্য
from motor.motor_asyncio import AsyncIOMotorClient # ডাটাবেজের জন্য

# 🚀 Bot Session and Token Information
SESSION = environ.get('SESSION', 'Webavbot')  # Pyrogram client session name

API_ID = int(environ.get('API_ID', '28870226'))  # Telegram API ID
API_HASH = environ.get('API_HASH', 'a5b1ff3f75941649bf5bc159782f0f00')  # Telegram API Hash
BOT_TOKEN = environ.get('BOT_TOKEN', '672782:AAE3VrD2SewKmu6ytwU4H1vRtfc')  # Telegram Bot Token

# 👑 Admins, Channels & Logs
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1002792118372'))  # File storage channel
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1003003272057'))  # General log channel
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", '-1002792118372'))  # Premium user actions log
VERIFIED_LOG = int(environ.get('VERIFIED_LOG', '-1002792118372'))  # Verified user actions log
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1001972036367"))

# Admin IDs and Auth Channel IDs
ADMINS = list(map(int, environ.get('ADMINS', '728528543').split()))  # List of admin user IDs
AUTH_CHANNEL = list(map(int, environ.get("AUTH_CHANNEL", "-1002735342037").split()))  # Allowed channels for authorization

# Username add without @
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'Ctgmovies270')  # Owner's username
BOT_USERNAME = environ.get("BOT_USERNAME", 'CTGFileToLink_Bot')  # Bot's username

# 🔗 Channel & Support Links
CHANNEL = environ.get('CHANNEL', 'https://t.me/TGLinkBase')  # Updates channel
SUPPORT = environ.get('SUPPORT', 'https://t.me/Movie_Request_Group_23')  # Support group
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/')  # Verification guide link
HOW_TO_OPEN = environ.get('HOW_TO_OPEN', 'https://t.me/')  # File access guide link

# ✅ Feature Toggles (True/False)
VERIFY = environ.get("VERIFY", False)  # Enable user verification
FSUB = environ.get("FSUB", True)  # Force Subscribe feature
ENABLE_LIMIT = environ.get("ENABLE_LIMIT", True)  # Enable file limits
BATCH_VERIFY = environ.get("BATCH_VERIFY", False)  # Verify files in batch
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))  # Enable channel shortlink creation
MAINTENANCE_MODE = environ.get("MAINTENANCE_MODE", False)  # Put bot in maintenance
PROTECT_CONTENT = environ.get('PROTECT_CONTENT', False)  # Enable content protection
PUBLIC_FILE_STORE = environ.get('PUBLIC_FILE_STORE', True)  # Public or private file visibility
BATCH_PROTECT_CONTENT = environ.get('BATCH_PROTECT_CONTENT', False)  # Batch file protection

# 🔗 Shortlink Configuration
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'techvjlink.site')  # Shortener site
SHORTLINK_API = environ.get('SHORTLINK_API', 'd73e70a35dc3877fa14afbf51fa8ec312c94780c')  # API key for shortlink

# 💾 MongoDB Connection Information
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://Filetolink270:Filetolink270@cluster0.tsr3api.mongodb.net/?appName=Cluster0")  # MongoDB connection URI
DB_NAME = environ.get('DATABASE_NAME', "cluster0")  # MongoDB database name

# 📸 all Media (Images)
QR_CODE = environ.get('QR_CODE', 'https://i.postimg.cc/mkHTmfYn/IMG-20251216-155449-415.jpg')  # QR Code image
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")  # Verify success image
AUTH_PICS = environ.get('AUTH_PICS', 'https://envs.sh/AwV.jpg')  # Auth step image
PICS = environ.get('PICS', 'https://i.ibb.co/p9N7X6R/photo-2025-10-28-07-23-34-7566169969528930340.jpg')  # Default info image
FILE_PIC = environ.get('FILE_PIC', 'https://i.ibb.co/bj4My0bW/photo-2025-07-21-02-15-21-7529360175656861700.jpg') # file image 

# 📝 File Captions
FILE_CAPTION = environ.get('FILE_CAPTION', f"{script.CAPTION}")  # Caption for single file
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', f"{script.CAPTION}")  # Caption for batch files
CHANNEL_FILE_CAPTION = environ.get('CHANNEL_FILE_CAPTION', f"{script.CAPTION}")  # Caption for channel posts

# ⏱️ Time & Rate Limit Settings
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # Ping interval in seconds (20 minutes)
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))  # Threshold for sleep delay
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", "600"))  # Rate limit time (10 mins)
MAX_FILES = int(environ.get("MAX_FILES", "5"))  # Max files allowed per user
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 60))  # Time (in hours) after which verification expires

# ⚙️ Worker Configuration
WORKERS = int(getenv('WORKERS', '4'))  # Number of async workers
MULTI_CLIENT = True  # Enable multi-client handling (if needed)

# 🔧 App/Heroku Configuration
name = str(environ.get('name', 'avbotz'))  # Project name
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))  # Heroku app name (optional)
else:
    ON_HEROKU = False

# 🌐 Server Settings
PORT = int(getenv('PORT', '2626'))
NO_PORT = str(getenv("NO_PORT", False)).lower() in ("true", "1", "yes")
HAS_SSL = str(getenv("HAS_SSL", False)).lower() in ("true", "1", "yes")
BIND_ADDRESS = getenv("WEB_SERVER_BIND_ADDRESS", "127.0.0.1")
FQDN = getenv("FQDN", "") or BIND_ADDRESS
PORT_SEGMENT = "" if NO_PORT else f":{PORT}"
PROTOCOL = "https" if HAS_SSL else "http"
URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"

# 🔑 ================== MULTI-BOT API SYSTEM ================== 🔑
# এটি অন্য বটের সাথে কানেক্ট করার জন্য ব্যবহৃত হবে
API_KEY = environ.get('API_KEY', 'webav_secret_auth_key_2024') 

# MongoDB Setup for Client Bots
mongo_client = AsyncIOMotorClient(DB_URL)
db = mongo_client[DB_NAME]
client_bots_col = db['authorized_client_bots']

# ১. নতুন ক্লায়েন্ট বট অ্যাড করা (/add_bot ID)
@Client.on_message(filters.command("add_bot") & filters.user(ADMINS))
async def add_client_bot(client, message):
    if len(message.command) < 2:
        return await message.reply("<b>ব্যবহার:</b> `/add_bot 12345678`")
    try:
        bot_id = int(message.command[1])
        existing = await client_bots_col.find_one({"bot_id": bot_id})
        if existing:
            return await message.reply("⚠️ এই বট আইডি আগে থেকেই লিস্টে আছে।")
        await client_bots_col.insert_one({"bot_id": bot_id})
        await message.reply(f"✅ বট আইডি <code>{bot_id}</code> সফলভাবে যুক্ত করা হয়েছে।")
    except ValueError:
        await message.reply("❌ ভুল আইডি! শুধুমাত্র নম্বর দিন।")

# ২. ক্লায়েন্ট বট ডিলিট করা (/del_bot ID)
@Client.on_message(filters.command("del_bot") & filters.user(ADMINS))
async def remove_client_bot(client, message):
    if len(message.command) < 2:
        return await message.reply("<b>ব্যবহার:</b> `/del_bot 12345678`")
    try:
        bot_id = int(message.command[1])
        result = await client_bots_col.delete_one({"bot_id": bot_id})
        if result.deleted_count > 0:
            await message.reply(f"🗑️ বট আইডি <code>{bot_id}</code> লিস্ট থেকে ডিলিট করা হয়েছে।")
        else:
            await message.reply("❌ এই আইডিটি লিস্টে পাওয়া যায়নি।")
    except ValueError:
        await message.reply("❌ ভুল আইডি! শুধুমাত্র নম্বর দিন।")

# ৩. অনুমোদিত বটের লিস্ট দেখা (/view_bots)
@Client.on_message(filters.command("view_bots") & filters.user(ADMINS))
async def list_client_bots(client, message):
    bots = await client_bots_col.find().to_list(length=100)
    if not bots:
        return await message.reply("📭 বর্তমানে কোন ক্লায়েন্ট বট অনুমোদিত নেই।")
    msg = "<b>🤖 অনুমোদিত ক্লায়েন্ট বট লিস্ট:</b>\n\n"
    for i, bot in enumerate(bots, 1):
        msg += f"{i}. <code>{bot['bot_id']}</code>\n"
    await message.reply(msg)

# ফাংশন: অন্য বট অনুমোদিত কি না তা চেক করার জন্য (কোডিংয়ে ব্যবহারের জন্য)
async def is_bot_authorized(bot_id: int):
    bot = await client_bots_col.find_one({"bot_id": bot_id})
    return bool(bot)

# ফাইনাল স্ট্রিম URL যা অন্য বট ব্যবহার করবে
STREAM_LINK_URL = URL 
# ==============================================================
