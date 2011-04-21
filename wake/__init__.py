from flask import Flask
from urllib import quote_plus
from wake.filters import relative_time, markup_tweet, markup_markdown

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.filters["relativetime"] = relative_time
app.jinja_env.filters["tweet"] = markup_tweet
app.jinja_env.filters["markdown"] = markup_markdown
app.jinja_env.filters["quoteplus"] = lambda s: quote_plus(s.encode('utf8'))

import wake.views
