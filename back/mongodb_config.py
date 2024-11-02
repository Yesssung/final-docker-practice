from pymongo import MongoClient

# MongoDB 클라이언트 설정
client = MongoClient("mongodb://mongodb:27017/")
db = client["counter_db"]
counter_collection = db["counters"]