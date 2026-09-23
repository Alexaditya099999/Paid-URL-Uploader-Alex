import logging
from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import Config

logger = logging.getLogger(__name__)


class ConfigCollection:
    def __init__(self, collection):
        self.collection = collection

    async def get_config(self, key):
        doc = await self.collection.find_one({"key": key})
        if doc:
            return doc.get("value")
        return None

    async def update_config(self, key, value):
        await self.collection.update_one(
            {"key": key}, {"$set": {"value": value}}, upsert=True
        )
        return True

    # Wrapper methods taaki standard MongoDB functions bhi kaam karein
    async def find_one(self, *args, **kwargs):
        return await self.collection.find_one(*args, **kwargs)
        
    async def update_one(self, *args, **kwargs):
        return await self.collection.update_one(*args, **kwargs)
        
    async def insert_one(self, *args, **kwargs):
        return await self.collection.insert_one(*args, **kwargs)
        
    async def delete_one(self, *args, **kwargs):
        return await self.collection.delete_one(*args, **kwargs)


class Database:
    def __init__(self, client, db_name):
        self.client = client
        self.db = client[db_name]

        # Raw Collections
        self.users = self.db["users"]
        self.premium_users = self.db["premium_users"]
        self.batch = self.db["batch"]
        self.admins = self.db["admins"]

        # Custom Wrapped Collections (jo get_config aur update_config support karein)
        self.config = ConfigCollection(self.db["config"])
        self.configs = ConfigCollection(self.db["configs"])


try:
    client = AsyncIOMotorClient(Config.DATABASE_URL)
    db = Database(client, Config.DATABASE_NAME)
    logger.info("Database connected successfully!")
except Exception as e:
    logger.error(f"Database connection failed: {e}")
    raise e
