#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method, store an
instance of the Redis client as a private variable named _redis
(using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a
string. The method should generate a random key (e.g. using uuid),
store the input data in Redis using the random key and return the
key.

Type-annotate store correctly. Remember that data can be a str,
bytes, int or float.
"""

import redis
from uuid import uuid4
import json
from functools import wraps
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """ As a key, use the qualified name of method using the
    __qualname__ dunder
    method. Create and return function that increments the count for that
    key every time the method is called and returns the value returned by
    the original method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """Wraps base function wrapper_func to count_calls"""

        return self._redis.incr(key)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for the decorated function"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = method(self, *args, **kwargs)

        self._redis.rpush(method.__qualname__ + ":outputs", str(output))
        return output

    return wrapper


class Cache:
    """cache class that so far converts"""

    def __init__(self):
        """Initialize an instance with a new a new instance of
        redis.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets the """
        value = self._redis.get(key)

        if value is None:
            print(f'key {key} does not exist.')

        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        value = self._redis.get(key)

        return value

    def get_int(self, key: str) -> int:
        value = self._redis.get(key)

        return int(value.decode('utf-8'))

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ a store method that takes a data argument and returns a
        string. The method should generate a random key
        (e.g. using uuid), store the input data in Redis using the
        random key and return the key.
        """
        new_key = str(uuid4())

        # set into db
        self._redis.set(new_key, data)
        return new_key
