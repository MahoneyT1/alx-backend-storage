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
from typing import Collection


client = MongoClient('mongodb://127.0.0.1:27017')
collection_manager = client.logs.nginx


def count_methods(collection_object: Collection) -> None:
    """Counts the total number of methods called in this database"""

    # list of methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(collection_object.count_documents({}), "Logs")
    print("Methods: ")

    for method in methods:
        counted_method = collection_object.count_documents({"method": method})
        print("    method {}: {}".format(method, counted_method))

    status_check = collection_object.count_documents({"path": "/status"})
    print("{} status check".format(status_check))


if __name__ == "__main__":
    count_methods(collection_manager)
