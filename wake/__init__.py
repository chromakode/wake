from flask import Flask
from wake.filters import relative_time, markup_tweet, markup_markdown

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.filters["relativetime"] = relative_time
app.jinja_env.filters["tweet"] = markup_tweet
app.jinja_env.filters["markdown"] = markup_markdown

import wake.views
