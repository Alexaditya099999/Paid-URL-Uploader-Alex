import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv("config.env")
else:
    load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


class Config(object):
    # All data hardcoded here so you don't need to add anything on Railway
    API_ID = 20346550
    API_HASH = "bc79c3bea7a626887bdc0871eecf0327"
    BOT_TOKEN = "8979171607:AAHx9a8p9YtvOjyjyKcT7q87ASVUhN7pj1I"
    DATABASE_NAME = "drmtest"
    
    # ⚠️ PASTE YOUR MONGODB URL HERE (If you don't have one, leave it as it is)
    DATABASE_URL = "mongodb+srv://alexaditya:alexaditya950@cluster0.7j1hfjk.mongodb.net/?appName=Cluster0" 
    
    OWNER_ID = 8460497291
    LOG_CHANNEL = -1002463068122
    WEB_SERVER = False
    THUMBNAILS = []

    # Constants
    CANCEL_DATA = {}
    PROCESS_DATA = {}


class Script(object):
    START_MESSAGE = (
        " {mention}\n\nSend any link or set of links in a txt file to download them."
    )
    
    DEV_MESSAGE = """Hey there, I'm Alex Aditya - your go-to Telegram bot developer!

Love having bots that do the heavy lifting for you? That's my jam! I'm all about crafting super cool and custom Telegram bots that make your life a breeze.

**What I Do**

- **Bot Magic:** From automating tasks to interactive games, I create bots that do it all. Seriously, ask me anything!
- **Tailored to You:** Your bot, your rules. I'll whip up a bot that's as unique as you are.
- **Chill Vibes:** I keep your data super safe, so you can relax and enjoy the bot party.
- **Always Improving:** Telegram evolves, and my bots grow with it. I'm here to keep things fresh and fab.

Ready for your own bot buddy? Ping me on Telegram (https://telegram.me/Reason_Someone) or check out me on GitHub (https://github.com/The_real_xTaR). Wanna hire me? Find me on Fiverr (https://www.fiverr.com/The_real_xTaR)!

Let's bot up and have some fun!"""
    
    HELP_MESSAGE = os.environ.get("HELP_MESSAGE", "Help message")
    
    PROGRESS_MESSAGE = """**Uploading...**

Progress: {percentage}%

{progress}

{finished} of {total}

Speed: {speed}/s

ETA: {eta}"""
    
    NEW_USER_MESSAGE = """#NewUser

User ID: `{user_id}`
User: {mention}
"""
    
    DOWNLOADING = """Downloading :- {start_index}/{end_index}

Name » {link_no}) » {name}

Original Index: {orginal_start_index}/{orginal_end_index}

[Alex Aditya](https://t.me/Reason_Someone)"""

    DEFAULT_CAPTION = """[File] File_ID : {file_index}

Name : {file_name}

Size : {file_size}

Batch Name : {batch_name}

Downloaded By : [Alex Aditya](https://t.me/ReaSon_SomeOne_Bot)"""


    CAPTION_CB = """**Set Caption**

Available Variables:

File Name : `{file_name}`
File Size : `{file_size}`
File Extension : `{file_extension}`
File Duration : `{file_duration}`
File URL : `{file_url}`
File Index : `{file_index}`
Batch Name : `{batch_name}`

==============================

Current:
`{current_caption}`

==============================

**Default:**
`{default_caption}`

**Status:** {status}"""
