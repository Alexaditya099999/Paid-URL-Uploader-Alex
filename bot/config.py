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
    # Corrected variable names (API_ID, API_HASH, etc.)
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "tg_bot")
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "False"), False)
    THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "").split()))

    # Constants
    CANCEL_DATA = {}
    PROCESS_DATA = {}


class Script(object):
    START_MESSAGE = (
        "Hello {mention},\n\nSend any link or set of links in a txt file to download them."
    )
    DEV_MESSAGE = """Hey there, I'm Caption Alex - your go-to Telegram bot developer!

Love having bots that do the heavy lifting for you? That's my jam! I'm all about crafting super cool and custom Telegram bots that make your life a breeze.

**What I Do**

- **Bot Magic:** From automating tasks to interactive games, I create bots that do it all. Seriously, ask me anything!
- **Tailored to You:** Your bot, your rules. I'll whip up a bot that's as unique as you are.
- **Chill Vibes:** I keep your data super safe, so you can relax and enjoy the bot party.
- **Always Improving:** Telegram evolves, and my bots grow with it. I'm here to keep things fresh and fab.

Ready for your own bot buddy? Ping me on Telegram (https://telegram.me/Alex_Aditya9) or check out me on GitHub (https://github.com/The_real_xTaR). Wanna hire me? Find me on Fiverr (https://www.fiverr.com/The_real_xTaR)!

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

Caption Alex"""

    DEFAULT_CAPTION = """[File] File_ID : {file_index}

Name : {file_name}

Size : {file_size}

Batch Name : {batch_name}

Downloaded By : Caption Alex"""


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
