import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "8259122096").split()))

API_ID = int(os.getenv("API_ID", "29195279"))

API_HASH = os.getenv("API_HASH", "f7fc8826747b34739c7e588f4b3e899e")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8633948983:AAFYcusNenJDMb7A44XHnHNr9u0wEeNlKrE")

OWNER_ID = int(os.getenv("OWNER_ID", "8259122096"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003192483568").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://botxkimak_stock:bebas@cluster0.9ajhbcy.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003192483568"))
