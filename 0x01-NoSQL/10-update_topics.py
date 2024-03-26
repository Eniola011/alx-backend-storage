#!/usr/bin/env python3
""" Change all topics of a school document on the name. """
import pymongo


def update_topics(mongo_collection, name, topics):
    """
        Change all topics of a school document based on the name.
        Args:
            mongo_collection: pymongo collection object.
            name: school name to update.
            topics: the list of topics approached in the school.
        Return nothing.
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
