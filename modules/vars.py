import os

API_ID    = os.environ.get("API_ID", "25129557")
API_HASH  = os.environ.get("API_HASH", "83c9546cfdee154fd2d16759c4d0582a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7014436725:AAH1uW3D79o0vMmphVgGE_1LQwIFxUj7pZY") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
