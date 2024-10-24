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
from typing import Any


class Cache:
    """cache class that so far converts"""

    def __init__(self) -> redis.Redis:
        """Initialize an instance with a new a new instance of
        redis.
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """ a store method that takes a data argument and returns a
        string. The method should generate a random key
        (e.g. using uuid), store the input data in Redis using the
        random key and return the key.
        """

        new_key = f"{uuid4()}"

        # set into db
        self._redis.set(new_key, data)
        return new_key
