// Barry Yang and Lily Xu
// CS 61 Lab 2a
// May 21, 2017

// Test queries for the JERK research journal manuscript data management system. 
// MongoDB schema implementation


db = db.getSiblingDB('Team28DB');

db.person.drop();
db.RICode.drop();
db.issue.drop();
db.feedback.drop();
db.manuscript.drop();

db.createCollection("person");
db.createCollection("RICode");
db.createCollection("issue");
db.createCollection("feedback");
db.createCollection("manuscript");


// insert person

db.person.insertMany([
  {
      "personID": 100,
      "fname": "Jasper",
      "lname": "Johns",
      "type": "author",
      "email": "jasper@sydney.org",
      "address": "42 Wallaby Way",
      "affiliation": "Pop Art"
  },
  {
      "personID": 101,
      "fname": "Piet",
      "lname": "Mondrian",
      "type": "author",
      "email": "piet@mondrian.com",
      "address": "17 Incident Road",
      "affiliation": "De Stijl"
  },
  {
      "personID": 102,
      "fname": "Mark",
      "lname": "Rothko",
      "type": "author",
      "email": "mark@rothko.com",
      "address": "49 Fifth Avenue",
      "affiliation": "Color Field"
  },
  {
      "personID": 103,
      "type": "author",
      "fname": "Willem",
      "lname": "de Kooning",
      "email": "willem@dekooning.com",
      "address": "12 East Hampton",
      "affiliation": "Abstract Expressionism"
  },
  {
      "personID": 400,
      "fname": "Georgia",
      "lname": "O'Keeffe",
      "type": "editor",
  },
  {
      "personID": 401,
      "fname": "Andy",
      "lname": "Warhol",
      "type": "editor",
  },
  {
      "personID": 402,
      "fname": "Wassily",
      "lname": "Kandinsky",
      "type": "editor",
  },
  {
      "personID": 300,
      "fname": "Henri",
      "lname": "Matisse",
      "type": "reviewer",
      "affiliation": "Fauvism",
      "email": "henri@matisse.com",
      "reviewer_status": "active",
      "ricodeID": [ 10, 20, 30 ]
  },
  {
      "personID": 301,
      "fname": "Otto",
      "lname": "Dix",
      "type": "reviewer",
      "affiliation": "New Objectivity",
      "email": "otto@dix.com",
      "reviewer_status": "active",
      "ricodeID": [ 10, 20, 30 ]
  },
  {
      "personID": 302,
      "fname": "Marc",
      "lname": "Chagall",
      "type": "reviewer",
      "affiliation": "Surrealism",
      "email": "marc@chagall.com",
      "reviewer_status": "active",
      "ricodeID": [ 10, 20, 30 ]
  },
  {
      "personID": 303,
      "fname": "Edward",
      "lname": "Hopper",
      "type": "reviewer",
      "affiliation": "Realism",
      "email": "edward@hopper.com",
      "reviewer_status": "active",
      "ricodeID": [ 10, 20, 30 ]
  },
  {
      "personID": 304,
      "fname": "Roy",
      "lname": "Lichtenstein",
      "type": "reviewer",
      "affiliation": "Pop Art",
      "email": "roy@lichtenstein.com",
      "reviewer_status": "active",
      "ricodeID": [ 10, 20, 30 ]
  }
]);


// insert RICodes

db.RICode.insertMany([
  {
      "RICodeID": 1,
      "interest": "Agricultural engineering"
  },
  {
      "RICodeID": 2,
      "interest": "Biochemical engineering"
  },
  {
      "RICodeID": 3,
      "interest": "Biomechanical engineering"
  },
  {
      "RICodeID": 4,
      "interest": "Ergonomics"
  },
  {
      "RICodeID": 5,
      "interest": "Food engineering"
  },
  {
      "RICodeID": 6,
      "interest": "Bioprocess engineering"
  },
  {
      "RICodeID": 7,
      "interest": "Genetic engineering"
  },
  {
      "RICodeID": 8,
      "interest": "Human genetic engineering"
  },
  {
      "RICodeID": 9,
      "interest": "Metabolic engineering"
  },
  {
      "RICodeID": 10,
      "interest": "Molecular engineering"
  },
  {
      "RICodeID": 11,
      "interest": "Neural engineering"
  },
  {
      "RICodeID": 12,
      "interest": "Protein engineering"
  },
  {
      "RICodeID": 13,
      "interest": "Rehabilitation engineering"
  },
  {
      "RICodeID": 14,
      "interest": "Tissue engineering"
  },
  {
      "RICodeID": 15,
      "interest": "Aquatic and environmental engineering"
  },
  {
      "RICodeID": 16,
      "interest": "Architectural engineering"
  },
  {
      "RICodeID": 17,
      "interest": "Civionic engineering"
  },
  {
      "RICodeID": 18,
      "interest": "Construction engineering"
  },
  {
      "RICodeID": 19,
      "interest": "Earthquake engineering"
  },
  {
      "RICodeID": 20,
      "interest": "Earth systems engineering and management"
  },
  {
      "RICodeID": 21,
      "interest": "Ecological engineering"
  },
  {
      "RICodeID": 22,
      "interest": "Environmental engineering"
  },
  {
      "RICodeID": 23,
      "interest": "Geomatics engineering"
  },
  {
      "RICodeID": 24,
      "interest": "Geotechnical engineering"
  },
  {
      "RICodeID": 25,
      "interest": "Highway engineering"
  },
  {
      "RICodeID": 26,
      "interest": "Hydraulic engineering"
  },
  {
      "RICodeID": 27,
      "interest": "Landscape engineering"
  },
  {
      "RICodeID": 28,
      "interest": "Land development engineering"
  },
  {
      "RICodeID": 29,
      "interest": "Pavement engineering"
  },
  {
      "RICodeID": 30,
      "interest": "Railway systems engineering"
  },
  {
      "RICodeID": 31,
      "interest": "River engineering"
  },
  {
      "RICodeID": 32,
      "interest": "Sanitary engineering"
  },
  {
      "RICodeID": 33,
      "interest": "Sewage engineering"
  },
  {
      "RICodeID": 34,
      "interest": "Structural engineering"
  },
  {
      "RICodeID": 35,
      "interest": "Surveying"
  },
  {
      "RICodeID": 36,
      "interest": "Traffic engineering"
  },
  {
      "RICodeID": 37,
      "interest": "Transportation engineering"
  },
  {
      "RICodeID": 38,
      "interest": "Urban engineering"
  },
  {
      "RICodeID": 39,
      "interest": "Irrigation and agriculture engineering"
  },
  {
      "RICodeID": 40,
      "interest": "Explosives engineering"
  },
  {
      "RICodeID": 41,
      "interest": "Biomolecular engineering"
  },
  {
      "RICodeID": 42,
      "interest": "Ceramics engineering"
  },
  {
      "RICodeID": 43,
      "interest": "Broadcast engineering"
  },
  {
      "RICodeID": 44,
      "interest": "Building engineering"
  },
  {
      "RICodeID": 45,
      "interest": "Signal Processing"
  },
  {
      "RICodeID": 46,
      "interest": "Computer engineering"
  },
  {
      "RICodeID": 47,
      "interest": "Power systems engineering"
  },
  {
      "RICodeID": 48,
      "interest": "Control engineering"
  },
  {
      "RICodeID": 49,
      "interest": "Telecommunications engineering"
  },
  {
      "RICodeID": 50,
      "interest": "Electronic engineering"
  },
  {
      "RICodeID": 51,
      "interest": "Instrumentation engineering"
  },
  {
      "RICodeID": 52,
      "interest": "Network engineering"
  },
  {
      "RICodeID": 53,
      "interest": "Neuromorphic engineering"
  },
  {
      "RICodeID": 54,
      "interest": "Engineering Technology"
  },
  {
      "RICodeID": 55,
      "interest": "Integrated engineering"
  },
  {
      "RICodeID": 56,
      "interest": "Value engineering"
  },
  {
      "RICodeID": 57,
      "interest": "Cost engineering"
  },
  {
      "RICodeID": 58,
      "interest": "Fire protection engineering"
  },
  {
      "RICodeID": 59,
      "interest": "Domain engineering"
  },
  {
      "RICodeID": 60,
      "interest": "Engineering economics"
  },
  {
      "RICodeID": 61,
      "interest": "Engineering management"
  },
  {
      "RICodeID": 62,
      "interest": "Engineering psychology"
  },
  {
      "RICodeID": 63,
      "interest": "Ergonomics"
  },
  {
      "RICodeID": 64,
      "interest": "Facilities Engineering"
  },
  {
      "RICodeID": 65,
      "interest": "Logistic engineering"
  },
  {
      "RICodeID": 66,
      "interest": "Model-driven engineering"
  },
  {
      "RICodeID": 67,
      "interest": "Performance engineering"
  },
  {
      "RICodeID": 68,
      "interest": "Process engineering"
  },
  {
      "RICodeID": 69,
      "interest": "Product Family Engineering"
  },
  {
      "RICodeID": 70,
      "interest": "Quality engineering"
  },
  {
      "RICodeID": 71,
      "interest": "Reliability engineering"
  },
  {
      "RICodeID": 72,
      "interest": "Safety engineering"
  },
  {
      "RICodeID": 73,
      "interest": "Security engineering"
  },
  {
      "RICodeID": 74,
      "interest": "Support engineering"
  },
  {
      "RICodeID": 75,
      "interest": "Systems engineering"
  },
  {
      "RICodeID": 76,
      "interest": "Metallurgical Engineering"
  },
  {
      "RICodeID": 77,
      "interest": "Surface Engineering"
  },
  {
      "RICodeID": 78,
      "interest": "Biomaterials Engineering"
  },
  {
      "RICodeID": 79,
      "interest": "Crystal Engineering"
  },
  {
      "RICodeID": 80,
      "interest": "Amorphous Metals"
  },
  {
      "RICodeID": 81,
      "interest": "Metal Forming"
  },
  {
      "RICodeID": 82,
      "interest": "Ceramic Engineering"
  },
  {
      "RICodeID": 83,
      "interest": "Plastics Engineering"
  },
  {
      "RICodeID": 84,
      "interest": "Forensic Materials Engineering"
  },
  {
      "RICodeID": 85,
      "interest": "Composite Materials"
  },
  {
      "RICodeID": 86,
      "interest": "Casting"
  },
  {
      "RICodeID": 87,
      "interest": "Electronic Materials"
  },
  {
      "RICodeID": 88,
      "interest": "Nano materials"
  },
  {
      "RICodeID": 89,
      "interest": "Corrosion Engineering"
  },
  {
      "RICodeID": 90,
      "interest": "Vitreous Materials"
  },
  {
      "RICodeID": 91,
      "interest": "Welding"
  },
  {
      "RICodeID": 92,
      "interest": "Acoustical engineering"
  },
  {
      "RICodeID": 93,
      "interest": "Aerospace engineering"
  },
  {
      "RICodeID": 94,
      "interest": "Audio engineering"
  },
  {
      "RICodeID": 95,
      "interest": "Automotive engineering"
  },
  {
      "RICodeID": 96,
      "interest": "Building services engineering"
  },
  {
      "RICodeID": 97,
      "interest": "Earthquake engineering"
  },
  {
      "RICodeID": 98,
      "interest": "Forensic engineering"
  },
  {
      "RICodeID": 99,
      "interest": "Marine engineering"
  },
  {
      "RICodeID": 100,
      "interest": "Mechatronics"
  },
  {
      "RICodeID": 101,
      "interest": "Nanoengineering"
  },
  {
      "RICodeID": 102,
      "interest": "Naval architecture"
  },
  {
      "RICodeID": 103,
      "interest": "Sports engineering"
  },
  {
      "RICodeID": 104,
      "interest": "Structural engineering"
  },
  {
      "RICodeID": 105,
      "interest": "Vacuum engineering"
  },
  {
      "RICodeID": 106,
      "interest": "Military engineering"
  },
  {
      "RICodeID": 107,
      "interest": "Combat engineering"
  },
  {
      "RICodeID": 108,
      "interest": "Offshore engineering"
  },
  {
      "RICodeID": 109,
      "interest": "Optical engineering"
  },
  {
      "RICodeID": 110,
      "interest": "Geophysical engineering"
  },
  {
      "RICodeID": 111,
      "interest": "Mineral engineering"
  },
  {
      "RICodeID": 112,
      "interest": "Mining engineering"
  },
  {
      "RICodeID": 113,
      "interest": "Reservoir engineering"
  },
  {
      "RICodeID": 114,
      "interest": "Climate engineering"
  },
  {
      "RICodeID": 115,
      "interest": "Computer-aided engineering"
  },
  {
      "RICodeID": 116,
      "interest": "Cryptographic engineering"
  },
  {
      "RICodeID": 117,
      "interest": "Information engineering"
  },
  {
      "RICodeID": 118,
      "interest": "Knowledge engineering"
  },
  {
      "RICodeID": 119,
      "interest": "Language engineering"
  },
  {
      "RICodeID": 120,
      "interest": "Release engineering"
  },
  {
      "RICodeID": 121,
      "interest": "Teletraffic engineering"
  },
  {
      "RICodeID": 122,
      "interest": "Usability engineering"
  },
  {
      "RICodeID": 123,
      "interest": "Web engineering"
  },
  {
      "RICodeID": 124,
      "interest": "Systems engineering"
  }
]);

// insert issue

db.issue.insertMany([
  {
      "publicationYear": 2015,
      "periodNumber": 1,
      "datePrinted": "2015-02-17"
  },
  {
      "publicationYear": 2015,
      "periodNumber": 2,
      "datePrinted": "2015-05-14"
  },
  {
      "publicationYear": 2015,
      "periodNumber": 3,
      "datePrinted": "2015-08-19"
  },
  {
      "publicationYear": 2015,
      "periodNumber": 4,
      "datePrinted": "2015-10-23"
  }
]);


// insert manuscripts

db.manuscript.insertMany([
  {
      "manuscriptID": 1,
      "authorID": 100,
      "editorID": 400,
      "title": "Flag on Orange Field",
      "status": "received",
      "ricodeID": 10,
      "numPages": "None",
      "startingPage": null,
      "issueOrder": null,
      "dateReceived": "2014-02-22",
      "dateSentForReview": null,
      "dateAccepted": null,
      "issue_publicationYear": null,
      "issue_periodNumber": null,
      "secondaryAuthor": [ "Marcel Duchamp", "Hart Crane", "Tatyana Grosman" ]
  },
  {
      "manuscriptID": 2,
      "authorID": 101,
      "editorID": 401,
      "title": "Composition with Large Red Plane, Yellow, Black, Gray and Blue",
      "status": "rejected",
      "ricodeID": 10,
      "numPages": "None",
      "startingPage": null,
      "issueOrder": null,
      "dateReceived": "2013-09-02",
      "dateSentForReview": null,
      "dateAccepted": null,
      "issue_publicationYear": null,
      "issue_periodNumber": null,
      "secondaryAuthor": [ "Pablo Picasso", "Kazimir Malevich", "Wassily Kandinsky" ]
  },
  {
      "manuscriptID": 3,
      "authorID": 101,
      "editorID": 400,
      "title": "White Over Red",
      "status": "underReview",
      "ricodeID": 10,
      "numPages": "None",
      "startingPage": null,
      "issueOrder": null,
      "dateReceived": "2014-03-21",
      "dateSentForReview": "2013-11-15",
      "dateAccepted": null,
      "issue_publicationYear": null,
      "issue_periodNumber": null,
      "secondaryAuthor": [ "Friedrich Nietzsche", "Milton Avery", "John Graham" ]
  },
  {
      "manuscriptID": 4,
      "authorID": 100,
      "editorID": 402,
      "title": "Target with Four Faces",
      "status": "accepted",
      "ricodeID": 10,
      "numPages": "None",
      "startingPage": null,
      "issueOrder": null,
      "dateReceived": "2015-02-18",
      "dateSentForReview": "2015-02-29",
      "dateAccepted": "2015-06-21",
      "issue_publicationYear": null,
      "issue_periodNumber": null,
      "secondaryAuthor": [ "Robert Rauschenberg", "John Cage" ]
  },
  {
      "manuscriptID": 5,
      "authorID": 103,
      "editorID": 401,
      "title": "A Tree in Naples",
      "status": "scheduled",
      "ricodeID": 10,
      "numPages": "None",
      "startingPage": null,
      "issueOrder": null,
      "dateReceived": "2014-06-21",
      "dateSentForReview": "2014-09-28",
      "dateAccepted": "2015-01-24",
      "issue_publicationYear": "2015",
      "issue_periodNumber": "3",
      "secondaryAuthor": [ "Jackson Pollock", "Frank Kline", "Mark Rothko" ]
  },
  {
      "manuscriptID": 6,
      "authorID": 102,
      "editorID": 400,
      "title": "Slow Swirl at the Edge of the Sea",
      "status": "typeset",
      "ricodeID": 10,
      "numPages": "None",
      "startingPage": null,
      "issueOrder": null,
      "dateReceived": "2013-06-21",
      "dateSentForReview": null,
      "dateAccepted": "2013-",
      "issue_publicationYear": "2015",
      "issue_periodNumber": "1",
      "secondaryAuthor": [ "Barnett Newman", "Pablo Picasso" ]
  },
  {
      "manuscriptID": 7,
      "authorID": 101,
      "editorID": 402,
      "title": "Still Life with Gingerpot 2",
      "status": "published",
      "ricodeID": 10,
      "numPages": "3",
      "startingPage": "1",
      "issueOrder": "4",
      "dateReceived": "2013-06-19",
      "dateSentForReview": "2014-01-25",
      "dateAccepted": "2014-03-21",
      "issue_publicationYear": "2015",
      "issue_periodNumber": "2",
      "secondaryAuthor": [ "Georges Braque" ]
  }
]);


// insert feedback

db.feedback.insertMany([
  {
      "manuscriptID": 2,
      "reviewerID": 300,
      "appropriateness": 10,
      "clarity": 8,
      "methodology": 8,
      "contribution": 7,
      "recommendation": 1,
      "dateReceived": "2014-11-12"
  },
  {
      "manuscriptID": 2,
      "reviewerID": 300,
      "appropriateness": 10,
      "clarity": 8,
      "methodology": 8,
      "contribution": 7,
      "recommendation": 1,
      "dateReceived": "2014-06-17"
  },
  {
      "manuscriptID": 2,
      "reviewerID": 300,
      "appropriateness": 10,
      "clarity": 8,
      "methodology": 8,
      "contribution": 7,
      "recommendation": 1,
      "dateReceived": "2014-05-02"
  },
  {
      "manuscriptID": 3,
      "reviewerID": 300,
      "appropriateness": null,
      "clarity": null,
      "methodology": null,
      "contribution": null,
      "recommendation": null,
      "dateReceived": null
  },
  {
      "manuscriptID": 3,
      "reviewerID": 301,
      "appropriateness": null,
      "clarity": null,
      "methodology": null,
      "contribution": null,
      "recommendation": null,
      "dateReceived": null
  },
  {
      "manuscriptID": 3,
      "reviewerID": 303,
      "appropriateness": null,
      "clarity": null,
      "methodology": null,
      "contribution": null,
      "recommendation": null,
      "dateReceived": null
  },
  {
      "manuscriptID": 4,
      "reviewerID": 301,
      "appropriateness": 6,
      "clarity": 8,
      "methodology": 8,
      "contribution": 7,
      "recommendation": 1,
      "dateReceived": "2014-10-12"
  },
  {
      "manuscriptID": 4,
      "reviewerID": 304,
      "appropriateness": 7,
      "clarity": 8,
      "methodology": 8,
      "contribution": 8,
      "recommendation": 0,
      "dateReceived": "2014-05-15"
  },
  {
      "manuscriptID": 4,
      "reviewerID": 302,
      "appropriateness": 4,
      "clarity": 5,
      "methodology": 7,
      "contribution": 7,
      "recommendation": 1,
      "dateReceived": "2014-02-07"
  },
  {
      "manuscriptID": 5,
      "reviewerID": 300,
      "appropriateness": 10,
      "clarity": 8,
      "methodology": 8,
      "contribution": 7,
      "recommendation": 1,
      "dateReceived": "2014-10-12"
  },
  {
      "manuscriptID": 5,
      "reviewerID": 301,
      "appropriateness": 9,
      "clarity": 8,
      "methodology": 8,
      "contribution": 9,
      "recommendation": 1,
      "dateReceived": "2014-05-15"
  },
  {
      "manuscriptID": 5,
      "reviewerID": 302,
      "appropriateness": 8,
      "clarity": 8,
      "methodology": 7,
      "contribution": 9,
      "recommendation": 1,
      "dateReceived": "2014-02-07"
  },
  {
      "manuscriptID": 6,
      "reviewerID": 301,
      "appropriateness": 9,
      "clarity": 8,
      "methodology": 8,
      "contribution": 9,
      "recommendation": 1,
      "dateReceived": "2014-08-14"
  },
  {
      "manuscriptID": 6,
      "reviewerID": 304,
      "appropriateness": 9,
      "clarity": 8,
      "methodology": 8,
      "contribution": 8,
      "recommendation": 0,
      "dateReceived": "2015-01-12"
  },
  {
      "manuscriptID": 6,
      "reviewerID": 303,
      "appropriateness": 8,
      "clarity": 8,
      "methodology": 7,
      "contribution": 7,
      "recommendation": 1,
      "dateReceived": "2016-02-17"
  },
  {
      "manuscriptID": 7,
      "reviewerID": 301,
      "appropriateness": 9,
      "clarity": 8,
      "methodology": 8,
      "contribution": 9,
      "recommendation": 1,
      "dateReceived": "2014-08-14"
  },
  {
      "manuscriptID": 7,
      "reviewerID": 304,
      "appropriateness": 9,
      "clarity": 8,
      "methodology": 8,
      "contribution": 8,
      "recommendation": 0,
      "dateReceived": "2015-01-12"
  },
  {
      "manuscriptID": 7,
      "reviewerID": 302,
      "appropriateness": 8,
      "clarity": 8,
      "methodology": 7,
      "contribution": 7,
      "recommendation": 1,
      "dateReceived": "2016-02-17"
  }
]);
