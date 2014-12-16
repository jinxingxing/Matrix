# coding: utf8
__author__ = 'JinXing'
from flask import render_template
import re


def redirect_download(url):
    return render_template("download.html", download_url=url)


def tr(s, n):
    result = s[0:n]
    if len(s) > n:
        result += "..."
    return result


_available_name_re = re.compile(r"[a-zA-Z0-9\-._]+$")


def is_name(s):
    return bool(_available_name_re.match(s))