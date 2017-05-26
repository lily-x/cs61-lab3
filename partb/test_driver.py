import pymongo                               # mongodb connector

HOST       = "mongodb://Team28:NMYFQgRPYTQd5MgT@cluster0-shard-00-00-ppp7l.mongodb.net:27017,cluster0-shard-00-01-ppp7l.mongodb.net:27017,cluster0-shard-00-02-ppp7l.mongodb.net:27017/Team28DB?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"

#"mongodb://localhost")   # Use this when access a local mongod

try:    # initialize db connection
    connection = pymongo.MongoClient(HOST)

    print("Connection established.")

    connection.server_info() # force connection on a request as the
                             # connect=True parameter of MongoClient seems
                             # to be useless here
except pymongo.errors.ServerSelectionTimeoutError as err:
    print("Connection failure:")
    print(err)

# Fetch list of all databases
print('DB\'s present on the system:')
for dbn in connection.database_names():
    print('    %s' % dbn)

db = connection.Team28DB
print("connected to db")

# get handle for test collection
collection = db.person
print("connected to db.testcoll")

try:
    iter = collection.find()
    print("back from find")
    for item in iter:
        print("..")
        print(item)
except Exception as e:
    print("Error trying to read collection:", type(e), e)

print("\nConnection closed.")
