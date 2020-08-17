# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return Hello['a']

@app.route("/file")
def file():
    filename = request.args.get('filename')
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return 'error'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)