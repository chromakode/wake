from been.couch import CouchStore
from flask import render_template
from wake import app

store = CouchStore().load()

@app.route('/')
def wake():
    return render_template('stream.html', events=store.collapsed_events())
