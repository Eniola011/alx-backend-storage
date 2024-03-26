#!/usr/bin/env python3
""" Top Students Sorted By Average Score. """
import pymongo


def top_students(mongo_collection):
    """
        Args:
            mongo_collection: pymongo collection object.
        The top must be ordered
        The average score must be part of each item
        returns with key = averageScore
    """
    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_students
