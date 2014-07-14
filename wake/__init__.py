from flask import Flask
from wake.filters import relative_time


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.filters["relativetime"] = relative_time


import wake.views
