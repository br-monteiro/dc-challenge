import redis
import json

_cache = None
_expiration = 600000 # 1000 * 60 * 10 = 600000 | 10 minutes

def get_cache():
  """
  Returns the connection with cache server
  """
  global _cache
  if _cache:
    return _cache
  _cache = redis.Redis(host='redis', port=6379)
  return _cache

def has_key(key):
  """
  Check if the key ixists in cache server
  """
  return bool(get_cache().get(key))

def save_cache(key: str, value):
  """
  Save a value in cache server.
  By default the value expires according the value of _expiration
  """
  if type(key) != str:
    return

  data = json.dumps(value)
  return get_cache().set(key, data, px=_expiration)
