import pymongo
from config import DB_NAME, COLLECTION_NAME, MONGO_HOST

db_client = pymongo.MongoClient(MONGO_HOST)
db = db_client[DB_NAME]
collection = db[COLLECTION_NAME]