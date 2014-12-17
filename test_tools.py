# coding: utf8
__author__ = 'JinXing'


from matrix.models import db, User, Area


def add_area():
    _id = Area.query.count() + 1
    short_name = "area" + str(_id)
    name = "第%d区" % _id
    intro = "%s简介" % name

    a = Area(1, short_name, name, intro)
    db.session.add(a)
    db.session.commit()
    db.session.close()


def add_user():
    user_id = User.query.count() + 1
    account = "user" + str(user_id)
    name = "用户" + str(user_id)
    email = account + "@xmatrix.com"
    salt = str(user_id)
    password = account + "password"
    u = User(account, name, email, salt, password)
    db.session.add(u)
    db.session.commit()
    db.session.close()