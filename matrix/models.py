# coding: utf8
__author__ = 'JinXing'

import datetime
import time

from matrix import app as matrix_app
from matrix.utils import tr
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy(matrix_app)

# __all__ = ["my_db_text_factory", "get_utc_datetime", "User", "Area", "AreaMember", "Topic", "Reply"]


def my_db_text_factory(s):
    # sqlite 插入的字符串必须是 unicode
    if isinstance(s, unicode):
        return s
    return unicode(s, "utf8")

    #
    # if isinstance(s, unicode):
    #     return s
    #
    # # 测试是否为 utf8 编码
    # try:
    #     s.decode("utf8")
    # except UnicodeDecodeError, e:
    #     raise (UnicodeDecodeError, u"数据入库前请先使用utf8编码或者直接使用 unicode\n" + str(e))
    #
    # return s


def get_utc_datetime(t=None):
    if t is None:
        return datetime.datetime.utcnow()
    elif isinstance(t, datetime.datetime):
        # fixme: 这个转换会造成微秒精度的丢失
        return datetime.datetime.utcfromtimestamp(time.mktime(t.timetuple()))
    elif isinstance(t, (int, float)):
        return datetime.datetime.utcfromtimestamp(t)
    else:
        raise TypeError("unknown time type `%r`" % type(t))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(80), unique=True, doc=u"账户名", index=True)
    name = db.Column(db.String(80), unique=True, doc=u"用户昵称", index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    salt = db.Column(db.String(16))
    password = db.Column(db.String(128))

    def __init__(self, account, name, email, salt, password):
        self.account = my_db_text_factory(account)
        self.name = my_db_text_factory(name)
        self.email = my_db_text_factory(email)
        self.salt = my_db_text_factory(salt)
        self.password = my_db_text_factory(password)

    def __repr__(self):
        return "<User: %r, %s, %s, %s>" % (self.id, self.account, self.alias, self.email)


class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    short_name = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    intro = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, creator, short_name, name, intro):
        self.creator = creator
        self.short_name = my_db_text_factory(short_name)
        self.name = my_db_text_factory(name)
        self.intro = my_db_text_factory(intro)
        self.create_time = get_utc_datetime()

    def __repr__(self):
        return "<Area: %r, %s, %s>" % (self.id, self.short_name, self.intro)


class AreaMember(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.Integer, db.ForeignKey('area.id'), nullable=False, index=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    position = db.Column(db.Integer, nullable=False)
    join_time = db.Column(db.DateTime, nullable=False)
    members = db.relationship("User", backref="area_member", lazy='joined', uselist=False)

    def __init__(self, area, user, position):
        self.area = area
        self.user = user
        self.position = position
        self.join_time = get_utc_datetime()

    def __repr__(self):
        return "<AreaUser: %d, %d, %d>" % (self.area, self.user, self.position)


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.Integer, db.ForeignKey('area.id'), nullable=False, index=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, area, user, content):
        self.area = area
        self.user = user
        self.content = my_db_text_factory(content)
        self.create_time = get_utc_datetime()

    def __repr__(self):
        return "<Topic: %r, %d, %d, %s>" % (self.id, self.area, self.user, tr(self.content, 16))


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    topic = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False, index=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    quote_reply = db.Column(db.Integer, db.ForeignKey('reply.id'), nullable=True)
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, topic, user, content, quote_reply=None):
        self.topic = topic
        self.user = user
        self.content = my_db_text_factory(content)
        self.create_time = get_utc_datetime()
        if quote_reply is not None:
            self.quote_reply = quote_reply

    def __repr__(self):
        return "<Reply: %r, %d, %d, %d, %s>" % (
            self.id, self.topic, self.user, self.quote_reply, tr(self.content, 16))