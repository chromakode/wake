from been.couch import CouchStore
from flask import render_template, g
from wake import app

@app.before_request
def init_store():
    g.store = CouchStore()
    g.store.load()

@app.route('/')
def wake():
    return render_template('stream.html', events=g.store.events())
