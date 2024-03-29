#!/usr/bin/env python3
""" writing strings into redis """


import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable = None) -> Callable:
    """ Count Calls Decorator """
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(name)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """ redis client """
    def __init__(self):
        """ An instance of the Redis client as a private variable. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) ->\
        Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if fn:
            return fn(key)
        return key

    def get_str(self, key: str) -> str:
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0

        return value
