#!/usr/bin/env python3
import pymongo


def list_all(mongo_collection) -> list:
    """
        Lists all documents in a collection.
        Args:
            mongo_collection: pymongo collection object.
        Return:
            an empty list if no document in the collection.
    """
    document: list = []
    for doc in mongo_collection.find():
        document.append(doc)

    return document
