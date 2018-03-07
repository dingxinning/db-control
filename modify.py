#!/usr/bin/env python3

from pymongo import MongoClient
import sys


client = MongoClient( '127.0.0.1', 27017 )
db = client['pan1']
collection = db['resume']

list=["name","age","sex","company"]

def modify_doc(NAME):
    num=collection.find_one({'name':NAME})
    if num:    
        print("Which key do you want to change ? ")
        print("name | age | sex | company")
        keys=input()
        if keys in list:
            key=keys
            value = input(key+":")
            collection.update_one({'name':NAME},{'$set':{key:value}})
            for document in collection.find():
                print(document)
        else:
            print("Error , you input a wrong key")
    else:
        print("Sorry,don't find this person ")
NAME=sys.argv[1]
modify_doc(NAME)
