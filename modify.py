#!/usr/bin/env python3

from pymongo import MongoClient
import sys


client = MongoClient( '127.0.0.1', 27017 )
db = client['pan1']
collection = db['resume']

#def modify_doc(NAME):
name =input("which person do you want to chang?")
key = input("which key do you want to change? ")
new_result = input("what result do you want to change to? ")
collection.update_one({'name':name},{'$set':{key:new_result}})
for document in collection.find():
    print(document)

#modify_doc(sys.argv[1:])