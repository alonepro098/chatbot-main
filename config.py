from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Telegram API credentials
API_ID = int(getenv("API_ID", "22243185"))
API_HASH = getenv("API_HASH", "39d926a67155f59b722db787a23893ac")

# Bot configuration
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)

# Owner & Support info
OWNER_ID = int(getenv("OWNER_ID", "1999645649"))
SUPPORT_GRP = getenv("SUPPORT_GRP", "dil_kee_alfaz")
UPDATE_CHNL = getenv("UPDATE_CHNL", "about_candyy")
OWNER_USERNAME = getenv("OWNER_USERNAME", "http_candy")

