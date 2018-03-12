#!/usr/bin/env python3

from pymongo import MongoClient
import sys


client = MongoClient( '127.0.0.1', 27017 )
db = client['pan1']
collection = db['resume']

def modify_doc(NAME):
    num=collection.find_one({'name':NAME})
    #judge whether have this person
    if num:    
        
        #read the key in "tamplate.json"
        with open ('tamplate.json') as template:
            str_template = template.read()
            dir_template=eval(str_template)

        #output prompt message
        print ("Which key do you want to change ?")
        for list_key in dir_template.keys():    
            print('| '+list_key,end=" | ")
        

        key=input()
        #judge the key
        if key in dir_template.keys():
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