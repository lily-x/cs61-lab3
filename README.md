# Barry Yang and Lily Xu
# CS 61 Lab 2a
# May 21, 2017


Run the following two commands.

The first command sests up the database and collections on Atlas (using the login information for Team 28). It also inserts all the example data that we have created.
```
mongo "mongodb://cluster0-shard-00-00-ppp7l.mongodb.net:27017,cluster0-shard-00-01-ppp7l.mongodb.net:27017,cluster0-shard-00-02-ppp7l.mongodb.net:27017/Team28DB?replicaSet=Cluster0-shard-0" --authenticationDatabase admin --ssl --username Team28 --password NMYFQgRPYTQd5MgT MMsetup.js
```

The second command executes test queries and displays the output to demonstrate correctness.
```
mongo "mongodb://cluster0-shard-00-00-ppp7l.mongodb.net:27017,cluster0-shard-00-01-ppp7l.mongodb.net:27017,cluster0-shard-00-02-ppp7l.mongodb.net:27017/Team28DB?replicaSet=Cluster0-shard-0" --authenticationDatabase admin --ssl --username Team28 --password NMYFQgRPYTQd5MgT MMtest.js
```

use this to import the zipcode.json file
```
mongoimport --db=cs61 --collection=zipcodes --drop zipcode.json
```
