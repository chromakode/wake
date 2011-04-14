#!/usr/bin/env python
from been.couch import CouchStore
from flask import Flask, render_template
from filters import relative_time, tweet

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.filters["relativetime"] = relative_time
app.jinja_env.filters["tweet"] = tweet

store = CouchStore()
store.load()

@app.route('/')
def wake():
    return render_template('stream.html', events=store.events())

if __name__ == '__main__':
    app.run(debug=True)
