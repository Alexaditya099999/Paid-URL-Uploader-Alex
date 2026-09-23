import logging
from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import Config

logger = logging.getLogger(__name__)

try:
    # MongoDB connection
    client = AsyncIOMotorClient(Config.DATABASE_URL)
    db_client = client[Config.DATABASE_NAME]

    # Define all collections used by the bot
    db = type("Database", (), {
        "users": db_client["users"],
        "premium_users": db_client["premium_users"],
        "config": db_client["config"],       # <--- YEH LINE ZAROORI HAI (SINGULAR)
        "configs": db_client["configs"],     # YEH BHI RAHEGI (PLURAL)
        "batch": db_client["batch"],
        "admins": db_client["admins"],
        "client": client,
        "db": db_client
    })()

    logger.info("Database connected successfully!")

except Exception as e:
    logger.error(f"Database connection failed: {e}")
    raise e
