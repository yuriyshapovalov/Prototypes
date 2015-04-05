#!/usr/bin/env python3
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
collecton = db.test_collection
posts = db.posts

post = {"author": "Yuriy Shapovalov", "text": "This is a test example!"}

post_id = posts.insert(post)
print(post_id)

client.close()