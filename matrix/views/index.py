# coding: utf8
from matrix import app
from werkzeug.utils import secure_filename
from matrix.utils import redirect_download
from flask import render_template


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/about", endpoint="about")
def about():
    return u"About"


@app.route("/download/<filename>", endpoint="download")
def download(filename):
    filename = secure_filename(filename)
    return redirect_download("http://127.0.0.1/download/%s" % filename)