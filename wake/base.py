from datetime import datetime
from urlparse import urljoin

from flask import Blueprint, render_template, abort, request, url_for
from werkzeug.contrib.atom import AtomFeed

from been import Been


blueprint = Blueprint('wake', __name__)


been = blueprint.been = Been()
store = blueprint.store = been.store


@blueprint.app_template_filter('relativetime')
def relative_time(timestamp):
    delta = (datetime.now() - datetime.fromtimestamp(timestamp))
    delta_s = delta.days * 86400 + delta.seconds
    if delta_s < 60:
        return "less than a minute ago"
    elif delta_s < 120:
        return "about a minute ago"
    elif delta_s < (60 * 60):
        return str(delta_s / 60) + " minutes ago"
    elif delta_s < (120 * 60):
        return "about an hour ago"
    elif delta_s < (24 * 60 * 60):
        return "about " + str(delta_s / 3600) + " hours ago"
    elif delta_s < (48 * 60 * 60):
        return "1 day ago"
    else:
        return str(delta_s / 86400) + " days ago"


@blueprint.route('/')
def index():
    return render_template('stream.html', events=store.collapsed_events())


@blueprint.route('/post/<slug>')
def by_slug(slug):
    events = list(store.events_by_slug(slug))
    if not events:
        abort(404)
    return render_template('stream.html', events=events)


@blueprint.route('/recent.atom')
def recent_feed():
    entries = []
    for source_id, source in store.get_sources().iteritems():
        if not source.get('syndicate'):
            continue

        for event in store.events(source=source_id):
            entries.append({
                'title': event['title'],
                'content': unicode(event['content']),
                'content_type': 'html',
                'author': event.get('author', ''),
                'url': urljoin(request.url_root,
                               url_for('by_slug', slug=event.get('slug', ''))),
                'updated': datetime.fromtimestamp(event['timestamp']),
                'published': datetime.fromtimestamp(event['timestamp']),
            })

    entries.sort(key=lambda e: e['published'], reverse=True)

    feed = AtomFeed('Recent Posts', feed_url=request.url, url=request.url_root,
                    generator=('Wake', None, None))
    for entry in entries:
        feed.add(**entry)
    return feed.get_response()
