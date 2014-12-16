# coding: utf8
__author__ = 'JinXing'


from flask import request
from matrix import app


@app.route("/area/")
def area():
    return request.method + u" AREA"


@app.route("/areas/<area_name>")
@app.route("/areas/", defaults={"area_name": 1})
def show_area(area_name):
    return u"AREA " + str(area_name)
