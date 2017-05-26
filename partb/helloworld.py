import pprint
from pymongo import MongoClient
# from bson.objectid import ObjectId

client = MongoClient()

db = client['Team28DB']
coll = db.manuscript

print(coll.find_one( {"manuscriptID": 1} ).get("title"))

coll = db.person


# result = coll.find( {personID: {$gt:300} })
# for person in coll.find({"personID": {"$gt": 300 }}):
#   pprint.pprint(person)


result = coll.find( {"type": "editor"})

for x in result:
    print str(x)

# print("person is " + str(result))




# print(db.collection_names(include_system_collections=False))

# arr = []
# for obj in coll.find():
#     arr.append(obj['manuscriptID'])
# print arr
