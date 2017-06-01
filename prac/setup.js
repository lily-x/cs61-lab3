// Barry Yang and Lily Xu
// CS 61 Lab 2a
// May 21, 2017

// Test queries for the JERK research journal manuscript data management system.
// MongoDB schema implementation


db = db.getSiblingDB('cs61');

db.dirtBikes.drop();
db.sales.drop();
db.scores.drop();

db.createCollection("sales");
db.createCollection("scores");

// insert person

// db.sales.insertMany([
//   { "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : ISODate("2014-03-01T08:00:00Z") },
//   { "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : ISODate("2014-03-01T09:00:00Z") },
//   { "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 10, "date" : ISODate("2014-03-15T09:00:00Z") },
//   { "_id" : 4, "item" : "xyz", "price" : 5, "quantity" : 20, "date" : ISODate("2014-04-04T11:21:39.736Z") },
//   { "_id" : 5, "item" : "abc", "price" : 10, "quantity" : 10, "date" : ISODate("2014-04-04T21:23:13.331Z") }
// ]);

db.sales.insertMany([
  {
		"_id": 1,
		"item": "Duis elementum,",
		"price": 638,
		"quantity": 97,
		"date": ISODate("2017-12-19T02:53:49-08:00")
	},
	{
		"_id": 2,
		"item": "porttitor scelerisque",
		"price": 691,
		"quantity": 30,
		"date": ISODate("2017-06-25T19:44:54-07:00")
	},
	{
		"_id": 3,
		"item": "eros turpis",
		"price": 220,
		"quantity": 71,
		"date": ISODate("2017-12-16T08:54:03-08:00")
	},
	{
		"_id": 4,
		"item": "suscipit nonummy.",
		"price": 870,
		"quantity": 48,
		"date": ISODate("2017-07-01T22:57:16-07:00")
	},
	{
		"_id": 5,
		"item": "natoque penatibus",
		"price": 406,
		"quantity": 23,
		"date": ISODate("2016-09-25T21:48:16-07:00")
	},
	{
		"_id": 6,
		"item": "eu nibh",
		"price": 559,
		"quantity": 27,
		"date": ISODate("2017-10-10T05:11:51-07:00")
	},
	{
		"_id": 7,
		"item": "facilisis lorem",
		"price": 136,
		"quantity": 23,
		"date": ISODate("2017-11-14T16:16:45-08:00")
	},
	{
		"_id": 8,
		"item": "odio. Etiam",
		"price": 595,
		"quantity": 23,
		"date": ISODate("2017-12-18T17:33:09-08:00")
	},
	{
		"_id": 9,
		"item": "pellentesque, tellus",
		"price": 120,
		"quantity": 27,
		"date": ISODate("2017-09-07T01:23:31-07:00")
	},
	{
		"_id": 10,
		"item": "odio. Etiam",
		"price": 755,
		"quantity": 9,
		"date": ISODate("2016-09-06T05:32:28-07:00")
	},
	{
		"_id": 11,
		"item": "sagittis placerat.",
		"price": 66,
		"quantity": 80,
		"date": ISODate("2016-07-10T18:55:23-07:00")
	},
	{
		"_id": 12,
		"item": "tellus. Phasellus",
		"price": 373,
		"quantity": 23,
		"date": ISODate("2017-04-17T11:03:03-07:00")
	},
	{
		"_id": 13,
		"item": "sapien. Cras",
		"price": 999,
		"quantity": 82,
		"date": ISODate("2017-12-07T16:03:09-08:00")
	},
	{
		"_id": 14,
		"item": "id risus",
		"price": 903,
		"quantity": 95,
		"date": ISODate("2017-12-12T09:08:05-08:00")
	},
	{
		"_id": 15,
		"item": "ridiculus mus.",
		"price": 17,
		"quantity": 85,
		"date": ISODate("2017-11-01T12:17:56-07:00")
	},
	{
		"_id": 16,
		"item": "Morbi metus.",
		"price": 105,
		"quantity": 7,
		"date": ISODate("2018-04-23T05:45:11-07:00")
	},
	{
		"_id": 17,
		"item": "blandit. Nam",
		"price": 987,
		"quantity": 60,
		"date": ISODate("2017-04-26T08:12:33-07:00")
	},
	{
		"_id": 18,
		"item": "tellus sem",
		"price": 631,
		"quantity": 64,
		"date": ISODate("2018-03-23T07:30:01-07:00")
	},
	{
		"_id": 19,
		"item": "leo, in",
		"price": 308,
		"quantity": 67,
		"date": ISODate("2017-01-12T01:00:58-08:00")
	},
	{
		"_id": 20,
		"item": "eu elit.",
		"price": 892,
		"quantity": 24,
		"date": ISODate("2017-01-30T19:26:44-08:00")
	},
	{
		"_id": 21,
		"item": "posuere cubilia",
		"price": 498,
		"quantity": 35,
		"date": ISODate("2018-04-11T18:53:48-07:00")
	},
	{
		"_id": 22,
		"item": "eu tellus",
		"price": 396,
		"quantity": 39,
		"date": ISODate("2017-08-10T09:21:29-07:00")
	},
	{
		"_id": 23,
		"item": "erat vitae",
		"price": 834,
		"quantity": 63,
		"date": ISODate("2017-05-10T13:44:38-07:00")
	},
	{
		"_id": 24,
		"item": "Fusce aliquam,",
		"price": 817,
		"quantity": 57,
		"date": ISODate("2016-08-17T03:53:41-07:00")
	},
	{
		"_id": 25,
		"item": "lacus. Etiam",
		"price": 670,
		"quantity": 14,
		"date": ISODate("2018-04-24T16:41:24-07:00")
	},
	{
		"_id": 26,
		"item": "placerat velit.",
		"price": 564,
		"quantity": 52,
		"date": ISODate("2017-07-26T09:31:17-07:00")
	},
	{
		"_id": 27,
		"item": "lectus pede",
		"price": 706,
		"quantity": 51,
		"date": ISODate("2016-09-19T00:46:24-07:00")
	},
	{
		"_id": 28,
		"item": "Quisque varius.",
		"price": 450,
		"quantity": 37,
		"date": ISODate("2016-10-02T22:04:47-07:00")
	},
	{
		"_id": 29,
		"item": "ut odio",
		"price": 243,
		"quantity": 100,
		"date": ISODate("2017-02-16T06:57:41-08:00")
	},
	{
		"_id": 30,
		"item": "Cras interdum.",
		"price": 515,
		"quantity": 92,
		"date": ISODate("2016-12-02T18:07:46-08:00")
	},
	{
		"_id": 31,
		"item": "et risus.",
		"price": 13,
		"quantity": 1,
		"date": ISODate("2016-09-15T08:37:16-07:00")
	},
	{
		"_id": 32,
		"item": "luctus sit",
		"price": 955,
		"quantity": 62,
		"date": ISODate("2017-09-23T18:10:16-07:00")
	},
	{
		"_id": 33,
		"item": "senectus et",
		"price": 740,
		"quantity": 33,
		"date": ISODate("2017-05-12T11:37:13-07:00")
	},
	{
		"_id": 34,
		"item": "accumsan sed,",
		"price": 969,
		"quantity": 53,
		"date": ISODate("2016-08-06T21:02:01-07:00")
	},
	{
		"_id": 35,
		"item": "Integer tincidunt",
		"price": 39,
		"quantity": 10,
		"date": ISODate("2017-12-27T19:18:34-08:00")
	},
	{
		"_id": 36,
		"item": "lorem fringilla",
		"price": 443,
		"quantity": 57,
		"date": ISODate("2016-07-31T05:59:52-07:00")
	},
	{
		"_id": 37,
		"item": "erat, in",
		"price": 342,
		"quantity": 1,
		"date": ISODate("2017-12-16T02:17:06-08:00")
	},
	{
		"_id": 38,
		"item": "semper auctor.",
		"price": 874,
		"quantity": 28,
		"date": ISODate("2016-08-09T00:53:28-07:00")
	},
	{
		"_id": 39,
		"item": "mauris, rhoncus",
		"price": 171,
		"quantity": 24,
		"date": ISODate("2016-06-16T20:32:17-07:00")
	},
	{
		"_id": 40,
		"item": "auctor ullamcorper,",
		"price": 256,
		"quantity": 67,
		"date": ISODate("2018-03-09T16:18:15-08:00")
	},
	{
		"_id": 41,
		"item": "dui quis",
		"price": 703,
		"quantity": 35,
		"date": ISODate("2016-09-02T21:22:40-07:00")
	},
	{
		"_id": 42,
		"item": "fermentum convallis",
		"price": 657,
		"quantity": 12,
		"date": ISODate("2017-06-01T07:25:53-07:00")
	},
	{
		"_id": 43,
		"item": "pellentesque massa",
		"price": 330,
		"quantity": 28,
		"date": ISODate("2018-02-09T14:08:48-08:00")
	},
	{
		"_id": 44,
		"item": "imperdiet ornare.",
		"price": 117,
		"quantity": 14,
		"date": ISODate("2017-03-03T14:35:50-08:00")
	},
	{
		"_id": 45,
		"item": "ac, feugiat",
		"price": 747,
		"quantity": 69,
		"date": ISODate("2017-09-01T19:34:56-07:00")
	},
	{
		"_id": 46,
		"item": "rutrum magna.",
		"price": 891,
		"quantity": 79,
		"date": ISODate("2018-03-20T07:27:33-07:00")
	},
	{
		"_id": 47,
		"item": "Vivamus sit",
		"price": 263,
		"quantity": 51,
		"date": ISODate("2016-07-14T12:15:12-07:00")
	},
	{
		"_id": 48,
		"item": "sit amet",
		"price": 491,
		"quantity": 9,
		"date": ISODate("2018-05-02T06:29:24-07:00")
	},
	{
		"_id": 49,
		"item": "nunc interdum",
		"price": 43,
		"quantity": 14,
		"date": ISODate("2017-07-18T16:06:38-07:00")
	},
	{
		"_id": 50,
		"item": "nec urna",
		"price": 895,
		"quantity": 14,
		"date": ISODate("2017-08-24T09:27:30-07:00")
	},
	{
		"_id": 51,
		"item": "sed, facilisis",
		"price": 850,
		"quantity": 98,
		"date": ISODate("2017-11-11T00:28:22-08:00")
	},
	{
		"_id": 52,
		"item": "metus. In",
		"price": 412,
		"quantity": 53,
		"date": ISODate("2016-11-28T08:43:25-08:00")
	},
	{
		"_id": 53,
		"item": "ante. Maecenas",
		"price": 884,
		"quantity": 18,
		"date": ISODate("2018-03-19T23:35:01-07:00")
	},
	{
		"_id": 54,
		"item": "ac metus",
		"price": 349,
		"quantity": 35,
		"date": ISODate("2018-05-27T13:27:48-07:00")
	},
	{
		"_id": 55,
		"item": "ipsum. Donec",
		"price": 66,
		"quantity": 44,
		"date": ISODate("2017-11-06T12:54:39-08:00")
	},
	{
		"_id": 56,
		"item": "sem, vitae",
		"price": 516,
		"quantity": 74,
		"date": ISODate("2017-04-20T09:44:03-07:00")
	},
	{
		"_id": 57,
		"item": "Maecenas mi",
		"price": 617,
		"quantity": 61,
		"date": ISODate("2016-07-29T05:44:00-07:00")
	},
	{
		"_id": 58,
		"item": "turpis nec",
		"price": 327,
		"quantity": 3,
		"date": ISODate("2017-08-28T10:19:20-07:00")
	},
	{
		"_id": 59,
		"item": "mattis ornare,",
		"price": 338,
		"quantity": 67,
		"date": ISODate("2018-01-07T04:23:27-08:00")
	},
	{
		"_id": 60,
		"item": "nunc est,",
		"price": 617,
		"quantity": 31,
		"date": ISODate("2016-09-07T07:17:48-07:00")
	},
	{
		"_id": 61,
		"item": "porttitor interdum.",
		"price": 117,
		"quantity": 14,
		"date": ISODate("2018-03-19T08:08:21-07:00")
	},
	{
		"_id": 62,
		"item": "nec, euismod",
		"price": 240,
		"quantity": 56,
		"date": ISODate("2017-01-04T06:08:00-08:00")
	},
	{
		"_id": 63,
		"item": "luctus vulputate,",
		"price": 639,
		"quantity": 22,
		"date": ISODate("2016-12-17T10:23:31-08:00")
	},
	{
		"_id": 64,
		"item": "amet risus.",
		"price": 875,
		"quantity": 74,
		"date": ISODate("2017-02-13T12:48:38-08:00")
	},
	{
		"_id": 65,
		"item": "risus. Quisque",
		"price": 118,
		"quantity": 88,
		"date": ISODate("2016-07-20T04:17:19-07:00")
	},
	{
		"_id": 66,
		"item": "condimentum. Donec",
		"price": 84,
		"quantity": 39,
		"date": ISODate("2017-06-05T22:25:02-07:00")
	},
	{
		"_id": 67,
		"item": "sed, facilisis",
		"price": 975,
		"quantity": 96,
		"date": ISODate("2018-01-03T20:30:29-08:00")
	},
	{
		"_id": 68,
		"item": "vitae odio",
		"price": 22,
		"quantity": 17,
		"date": ISODate("2017-05-19T04:20:25-07:00")
	},
	{
		"_id": 69,
		"item": "congue a,",
		"price": 379,
		"quantity": 62,
		"date": ISODate("2016-07-04T02:11:39-07:00")
	},
	{
		"_id": 70,
		"item": "lacus. Ut",
		"price": 512,
		"quantity": 14,
		"date": ISODate("2016-11-18T23:47:15-08:00")
	},
	{
		"_id": 71,
		"item": "velit eget",
		"price": 667,
		"quantity": 4,
		"date": ISODate("2017-03-12T07:37:49-07:00")
	},
	{
		"_id": 72,
		"item": "Donec vitae",
		"price": 342,
		"quantity": 41,
		"date": ISODate("2017-06-01T14:16:12-07:00")
	},
	{
		"_id": 73,
		"item": "dolor. Donec",
		"price": 111,
		"quantity": 49,
		"date": ISODate("2018-01-10T04:51:26-08:00")
	},
	{
		"_id": 74,
		"item": "Phasellus at",
		"price": 766,
		"quantity": 18,
		"date": ISODate("2018-05-17T13:01:42-07:00")
	},
	{
		"_id": 75,
		"item": "mi felis,",
		"price": 611,
		"quantity": 99,
		"date": ISODate("2016-07-21T23:58:25-07:00")
	},
]);

db.scores.insertMany([
  { "_id" : 1, "subject" : "History", "score" : 88 },
  { "_id" : 2, "subject" : "History", "score" : 92 },
  { "_id" : 3, "subject" : "History", "score" : 97 },
  { "_id" : 4, "subject" : "History", "score" : 71 },
  { "_id" : 5, "subject" : "History", "score" : 79 },
  { "_id" : 6, "subject" : "History", "score" : 83 }
]);

db.sales.aggregate([
    {$match: {"price": { $lt:200 }} },
    {$count: "cheap" }
 ]);

 db.zipcodes.aggregate( [
    { $group: { "_id": "$state", "totalPop":{ "$sum": "$pop"} } },
    { $match: { "totalPop": {$gt: 10000000 } } }

] );
