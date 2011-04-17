from been.couch import CouchStore
from flask import render_template, abort
from wake import app

store = CouchStore().load()

@app.route('/')
def wake():
    return render_template('stream.html', events=store.collapsed_events())

@app.route('/<slug>')
def by_slug(slug):
    events = list(store.events_by_slug(slug))
    if not events:
        abort(404)
    return render_template('stream.html', events=events)

