import redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)


def set_cache_value(key, value):
    r.set(key, value, ex=7200)


def get_cache_value(key):
    return r.get(key)
