from flask import Flask
from .site.route import site

app=Flask(__name__)

app.register_blueprint(site)