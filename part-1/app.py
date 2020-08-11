from flask import Flask, request
from .src.utils import gethash, sortdict, build_message, isdevmode
from .src.cache import has_key, save_cache

app = Flask(__name__)

@app.route('/v1/products', methods=['POST'])
def products():
  body = request.get_json()
  body_hash = gethash(sortdict(body))

  if has_key(body_hash):
    return build_message('error', 'repeated product', body), 403
  else:
    save_cache(body_hash, body)
    return build_message('success', 'saved product'), 200

if __name__ == '__main__':
  app.run(debug=isdevmode())
