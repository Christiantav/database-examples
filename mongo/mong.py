import pymongo
import datetime

db_client = pymongo.MongoClient("mongodb://localhost:27017/")

user = {
  "username": "user123",
  "first_name": "Jane",
  "last_name": "Doe",
  "phone": "123-456-7890",
  "birthday": "12/31/1999",
  "created_at": datetime.datetime.utcnow(),
}

users = db["users"]
user_id = users.insert_one(user).inserted_id
user_id

print(users.find_one({"user": "user123"}))