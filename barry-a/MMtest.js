db = db.getSiblingDB("Team17DB");

print("Start\n");

print("\nFind specific manuscript number 2:");
printjson(db.manuscript.findOne( {"manuscriptID": 2} ));

print("\nNo Reviewer found:");
printjson(db.feedback.findOne( {"manuscriptID": 2, "reviewerID": 500} ));

print("\nFind all manuscripts with Pablo Picasso as a secondary author:");
cursor = db.manuscript.find( {"secondaryAuthor": "Pablo Picasso"} );
while( cursor.hasNext() ){
  printjson( cursor.next() );
}

print("\nCount how many people are in the system:");
print("There are " + db.person.count() + " people in the person table");

print("\nFind all editors, order in reverse personID:");
cursor = db.editor.find({}).sort( {"personID": -1} )
while( cursor.hasNext() ){
  printjson( cursor.next() );
}

print("\nFind feedback of manuscript number 2 from reviewer 300:");
printjson(db.feedback.findOne( {"manuscriptID": 2, "reviewerID": 300} ));

print("\nFind dateReceived of manuscript number 2 from reviewer 300:");
print(db.feedback.findOne( {"manuscriptID": 2, "reviewerID": 300} ).dateReceived);

print("\nFinish");
