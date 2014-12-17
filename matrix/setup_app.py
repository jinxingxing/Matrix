# coding: utf8
__author__ = 'JinXing'
from flask import Flask
from .config import *

app = Flask(__name__, static_url_path=MATRIX_STATIC_PATH)
__version__ = '0.0.1'

app.config["SQLALCHEMY_DATABASE_URI"] = MATRIX_DATABASE_URI
app.config["SQLALCHEMY_ECHO"] = True


@app.add_template_filter
def timeformat(value, format_='%Y-%m-%d %H:%M'):
    return value.strftime(format_)