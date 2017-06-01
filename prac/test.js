db.zipcodes.aggregate([ 
    { $group: { _id: { state: "$state", city: "$city", zipcode: "_id"}, zip: { $sum: "$city"} } },
    { $group: {  _id: "$_id.city", zcount: {$sum: "$zip"}} },
    { $sort: {zcount: -1} }
 ]);

db.zipcodes.findOne({});