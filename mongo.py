import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_USER = os.getenv("MONGO_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_ROOT_PASSWORD")

MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@inventory_mongo:27017/"

#Connect to the MongoDB server
client = AsyncIOMotorClient(MONGO_URL)

#Create a database called "inventory_logs_db"
db = client["inventory_logs_db"]

logs_collection = db["api_logs"]
