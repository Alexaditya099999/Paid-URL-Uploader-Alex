import logging
from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import Config

logger = logging.getLogger(__name__)

try:
    client = AsyncIOMotorClient(Config.DATABASE_URL)
    db_client = client[Config.DATABASE_NAME]

    db = type("Database", (), {
        "users": db_client["users"],
        "configs": db_client["configs"],
        "batch": db_client["batch"],
        "client": client,
        "db": db_client
    })()

    logger.info("Database connected successfully.")

except Exception as e:
    logger.error(f"Database connection failed: {e}")
    raise e
