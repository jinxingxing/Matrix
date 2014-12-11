#coding: utf8
from matrix import app


@app.route("/")
def index():
    return u"欢迎来到 Matrix"

