import pymongo
from pymongo import MongoClient
    #URl to connect DB
c1 = pymongo.MongoClient("mongodb://127.0.0.1:27017")
document = {"Name": "Nikhil", "Roll No": 1,"Branch":"CSE","Gender":"Male"}
    #c1.PFSD.PFSD.insert_one(document)
print(c1.list_database_names())
    #specifying the DB name
database_name = "PFSD"
student1 = c1[database_name]
    #specifying the Collection name
collection_name = "PFSD"
obj1 = student1[collection_name]
    #Insert Data
document = {"Name": "Nikhil", "Roll No": 1,"Branch":"CSE"}
obj1.insert_one(document)
print(c1.database_name)
print("Inserted Data - 1 Successfully")
document = { "Name": "Jatla Nikhil", "Roll No": 1141, "Branch":"CSE"}
obj1.insert_one(document)