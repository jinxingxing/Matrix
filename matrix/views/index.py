from matrix import app


@app.route("/")
def index():
    return "Index Page X"