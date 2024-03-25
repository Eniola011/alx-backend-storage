#!/usr/bin/env python3
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
        Insert a new document in a collection based on kwargs.
        Args:
            mongo_collection: pymongo collection object.
        Return:
            new _id
    """
    schl = mongo_collection.insert_one(kwargs)
    return schl.inserted_id
