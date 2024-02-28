from src.database import Database
from src import get_config
from time import time
from random import randint
import bcrypt
from flask import Flask, jsonify
import json

db=Database.get_connection()
users =db.test
users1 =db.test1

class User:
    def __init__(self,id):
        print("{} the id".format(id))

    @staticmethod
    def show():
        result = users.find({}, {"_id": 0, "file_name": 1, "file_id": 1,"seq":1})
        return result 

    @staticmethod
    def rec(name):
        result_cursor = users.find_one({"file_name": name}, {'_id':0,"file_id": 1})
        print(result_cursor)
        return result_cursor['file_id']
      
    @staticmethod
    def rec2(name):
        result_cursor = users.find({"seq": name}, {'_id':0,"file_id": 1})
        return  result_cursor
    
    @staticmethod
    def insert1(data):
        id = users.insert_one(data)
        return id
    
    @staticmethod
    def insert2(data):
        id = users1.insert_one(data)
        return id