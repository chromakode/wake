from datetime import datetime
from urlparse import urljoin

from flask import render_template, abort, request, url_for
from werkzeug.contrib.atom import AtomFeed

from been import Been
from wake import app


been = Been()
store = been.store


@app.route('/')
def wake():
    return render_template('stream.html', events=store.collapsed_events())


@app.route('/<slug>')
def by_slug(slug):
    events = list(store.events_by_slug(slug))
    if not events:
        abort(404)
    return render_template('stream.html', events=events)


@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recent Posts', feed_url=request.url, url=request.url_root,
                    generator=('Wake', None, None))
    sources = store.get_sources()
    for event in store.events():
        if sources[event['source']].get('syndicate'):
            feed.add(event['title'],
                     unicode(event['content']),
                     content_type='html',
                     author=event.get('author', ''),
                     url=urljoin(request.url_root, url_for('by_slug', slug=event.get('slug', ''))),
                     updated=datetime.fromtimestamp(event['timestamp']),
                     published=datetime.fromtimestamp(event['timestamp']))
    return feed.get_response()
