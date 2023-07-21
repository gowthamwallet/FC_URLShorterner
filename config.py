# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID","21612999"))
API_HASH = os.environ.get("API_HASH", "28b57b4620bb04435b03e49c3a396111")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6382739095:AAETqTBfLEfTvRYdIQOv-YAcjlCfbAUb4ao")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "955761511").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Link")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Link:Link@cluster0linkshortner.esfuqlf.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "955761511")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001919666814")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/+_efnDNQKnhM5YjVl") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "False"
