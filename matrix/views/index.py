# coding: utf8
from matrix import app
from werkzeug.utils import secure_filename
from matrix.utils import redirect_download


@app.route("/index/")
def index():
    return u"欢迎来到 Matrix"


@app.route("/about")
def about():
    return u"About"


@app.route("/download/<filename>")
def download(filename):
    filename = secure_filename(filename)
    return redirect_download("http://127.0.0.1/%s" % filename)