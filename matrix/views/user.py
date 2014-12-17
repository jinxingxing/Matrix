# coding: utf8
__author__ = 'JinXing'

from flask import render_template

from matrix import app
from matrix.models import User


@app.route("/user/<account>", endpoint="user")
def show_user(account):
    user = User.query.filter_by(account=account).first_or_404()
    return render_template("show_user.html", user=user)