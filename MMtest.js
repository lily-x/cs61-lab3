// Barry Yang and Lily Xu
// CS 61 Lab 2a
// May 21, 2017

// Test queries for the JERK research journal manuscript data management system. 
// MongoDB schema implementation


db = db.getSiblingDB("Team28DB");

print("Begin tests. \n");

print("\nFind specific manuscript number 2:");
printjson(db.manuscript.findOne( {"manuscriptID": 2} ));

print("\nNo reviewer found:");
printjson(db.feedback.findOne( {"manuscriptID": 2, "reviewerID": 500} ));

print("\nFind all manuscripts with Pablo Picasso as a secondary author:");
cursor = db.manuscript.find( {"secondaryAuthor": "Pablo Picasso"} );
while( cursor.hasNext() ){
  printjson( cursor.next() );
}

print("\nFind all editors, ordered by decrementing personID:");
cursor = db.person.find( {"type": "editor"} ).sort( {"personID": -1} )
while( cursor.hasNext() ){
  printjson( cursor.next() );
}

print("\nFind feedback of manuscript number 2 from reviewer 300:");
printjson(db.feedback.findOne( {"manuscriptID": 2, "reviewerID": 300} ));

print("\nFind dateReceived of manuscript number 2 from reviewer 300:");
print(" "+db.feedback.findOne( {"manuscriptID": 2, "reviewerID": 300} ).dateReceived);

print("\nCount how many editors are in the system:");
print(" There are " + db.person.count( {"type": "editor"} ) + " editor(s) in the person table");

print("\nFind the area of interest name of the RICode for manuscript number 2:");
let RIC_string = db.RICode.findOne( {"RICodeID":db.manuscript.findOne( {"manuscriptID": 2} ).ricodeID} ).interest;
print(" "+RIC_string);

print("\nFind the first and last name of the author of manuscript 2 :");
let manuscript = db.manuscript.findOne( {"manuscriptID": 2} );
let person = db.person.findOne( {"personID":manuscript.authorID} );
let fname = person.fname;
let lname = person.lname;
print(" The person's name is " + fname + " " + lname + ".");

print("\nFind count of feedbacks that are filled in (without null values):");

// assume if there's no recommendation, there's no feedback
let count = db.feedback.find( {"recommendation": {$ne:null} } ).count()
print(" " + count + " manuscripts are filled in.");

print("\nTests completed. ");
