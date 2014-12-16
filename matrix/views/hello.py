from matrix import app
from werkzeug.utils import secure_filename
from matrix.utils import redirect_download


@app.route("/hello")
def hello():
    return "Hello World!X"
