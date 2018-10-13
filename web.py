import json

from flask import Flask, request

from mymusiclib import __version__
from mymusiclib.scales import MajorScale

app = Flask(__name__)


@app.route("/")
def hello():
    return f"This is my library version {__version__}"


@app.route("/major")
def major():
    key = request.args.get('key', type=str)
    if len(key) == 3 and key.endswith('sh'):
        key = key.replace('sh', '#')
    m = MajorScale().key(key)
    data = {'key': key, 'scale': m}
    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=True)
