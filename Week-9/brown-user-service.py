from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335

user = {
    "first_name": "John",
    "last_name": "Adams",
    "email": "AdamsJ@feds.gov",
    "employee_id": "385720538",
    "date_created": datetime.datetime.utcnow()
}
user_id = db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "385720538"}))