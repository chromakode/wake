from flask import Flask

from base import blueprint


app = Flask(__name__)
app.register_blueprint(blueprint)
app.jinja_env.trim_blocks = True
