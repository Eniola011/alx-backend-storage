#!/usr/bin/env python3
""" Returns the list of school having a specific topic. """
import pymongo


def schools_by_topic(mongo_collection, topic: str):
    """
        Args:
            mongo_collection: pymongo collection object.
        Return:
            topic: (string) will be topic searched.
    """
    schools: list = []
    for school in mongo_collection.find({"topics": topic}):
        schools.append(school)

    return schools
