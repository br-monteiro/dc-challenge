import hashlib
from os import getenv
from functools import reduce
from flask import jsonify

def _acc(values):
  """
  Returs the accumulated from values
  """
  return reduce(lambda i, v: i + toint(v), values, 0)

def toint(value):
  """
  Returns a number int from value
  """
  if type(value) == int:
    return value
  elif type(value) == bool:
    return int(value)
  elif type(value) == str:
    if len(value) == 1:
      return ord(value)
    return _acc(value)
  elif type(value) == dict:
    return _acc(value.keys())
  elif type(value) == list:
    return _acc(value)
  else:
    return 0


def getdictkeys(value):
  """
  Returns the ordered keys of a dict
  """
  if type(value) == dict:
    keys = list(value.keys())
    keys.sort(key=toint)
    return keys
  return []


def sortlist(value):
  """
  Retuns the list ordered
  """
  if type(value) != list:
    return value

  result = []
  value.sort(key=toint)

  for val in value:
    if type(val) == dict:
      result.append(sortdict(val))
    elif type(val) == list:
      result.append(sortlist(val))
    else:
      result.append(val)
  return result


def sortdict(value):
  """
  Returns the dict ordered
  """
  result = {}
  keys = getdictkeys(value)

  for key in keys:
    attr = value[key]
    if type(attr) == dict:
      attr = sortdict(attr)
    elif type(attr) == list:
      attr = sortlist(attr)
    result[key] = attr

  return result


def gethash(value):
  """
  Returns the hash (sha1) from a value
  """
  return hashlib.sha1(str(value).encode('utf-8')).hexdigest()


def build_message(status, message='', data={}):
  """
  Retuns an instance of flask.wrappers.Response with the attributes status, message and data
  """
  return jsonify(status=status, message=message, data=data)


def isdevmode():
  """
  Check if the DEV-MODE is enabled
  """
  return getenv('DEV_MODE') == 'true'
