import pymongo
import pprint


mongo_uri = "mongodb://192.168.0.113:27017/"
client = pymongo.MongoClient(mongo_uri)

mydb=client.testDB
mycoll=mydb.testColl
testInsert=mycoll.insert_one({"country":'India'}).inserted_id
#print(client.list_database_names())
print(client.get_database('testDB'))