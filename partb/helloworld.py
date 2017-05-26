import pprint
from pymongo import MongoClient
# from bson.objectid import ObjectId

client = MongoClient()

db = client['Team28DB']
coll = db.manuscript

print(coll.find_one( {"manuscriptID": 1} ).get("title"))

# print(db.collection_names(include_system_collections=False))

arr = []
for obj in coll.find():
    arr.append(obj['manuscriptID'])
print arr
