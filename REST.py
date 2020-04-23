import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Lara:Hiran@cluster0-12idc.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

post ={"_id":0, "name":"Lahiru","score":100}

collection.insert_one(post)
