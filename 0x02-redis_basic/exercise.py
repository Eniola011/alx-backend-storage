#!/usr/bin/env python3
""" writing strings into redis """


import redis
import uuid
from typing import Union


class Cache:
    """ redis client """
    def __init__(self):
        """ An instance of the Redis client as a private variable. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
