#!/usr/bin/env python3
""" Write a Python function that lists all documents
in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""

import pymongo


def list_all(mongo_collection):
    """Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object
    """

    if mongo_collection is None:
        return []

    return [doc for doc in mongo_collection.find()]


if __name__ == '__main__':
    list_all()
