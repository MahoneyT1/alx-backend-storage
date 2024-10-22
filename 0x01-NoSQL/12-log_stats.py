#!/usr/bin/env python3
""" Write a Python script that provides some stats about
Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in
this collection

second line: Methods:
5 lines with the number of documents with the method =
["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
(see example below - warning: it’s a tabulation before each line)

one line with the number of documents with:
method=GET
path=/status
"""
import pymongo
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
collection_manager = client.logs.nginx

# list of methods

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print(collection_manager.count_documents({}), "Logs")
print("Methods: ")
print("\t methods GET: {}".format(
    collection_manager.count_documents({"method": "GET"})))
print("\t methods POST: {}".format(
    collection_manager.count_documents({"method": "POST"})))
print("\t methods PUT: {}".format(
    collection_manager.count_documents({"method": "PUT"})))
print("\t methods PATCH: {}".format(
    collection_manager.count_documents({"method": "PATCH"})))
print("\t methods DELETE: {}".format(
    collection_manager.count_documents({"method": "DELETE"})))
print("{} status check".format(
    collection_manager.count_documents({"path": "/status"})))
