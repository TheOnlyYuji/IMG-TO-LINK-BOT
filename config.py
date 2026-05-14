import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", "36428426"))
    API_HASH = os.getenv("API_HASH", "30cba30aa38699e77ce264365e327528")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8689091474:AAFO0XIP8EEH117kH-eV0vuG-hJcX6xWZBk")
    
    # Database
    MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://animekyoto:W5Itr6v2bZ3KpQF8@cluster0.trg5dtc.mongodb.net/?appName=Cluster0")
    
    # Admin
    ADMIN_STR = os.getenv("ADMINS", "7957802698")
    ADMINS = [int(x) for x in ADMIN_STR.split()] if ADMIN_STR else []
    
    # Channel
    FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "AnimeKyoto_Bots") # username or ID
    
    # UI
    START_PIC = os.getenv("START_PIC", "https://ibb.co/W4zqMjB2") # Default image
    
    # Log Channel
    LOG_CHANNEL = os.getenv("LOG_CHANNEL", "-1003732729909") # Channel ID (e.g. -100xxxx)

