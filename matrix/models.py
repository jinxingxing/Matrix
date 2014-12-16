# coding: utf8
__author__ = 'JinXing'

from matrix import app
from matrix.utils import tr
from flask.ext.sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.sqlite.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


def my_db_text_factory(s):
    if isinstance(s, unicode):
        return s.encode("utf8")

    # 测试是否为 utf8 编码
    try:
        s.decode("utf8")
    except UnicodeDecodeError, e:
        raise (UnicodeDecodeError, u"数据入库前请先使用utf8编码或者直接使用 unicode\n" + str(e))

    return s


text_factory = my_db_text_factory


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, doc=u"登陆名", index=True)
    alias = db.Column(db.String(80), unique=True, doc=u"昵称", index=True)
    email = db.Column(db.String(120), unique=True, index=True)

    def __init__(self, name, alias, email):
        self.name = my_db_text_factory(name)
        self.alias = my_db_text_factory(alias)
        self.email = my_db_text_factory(email)

    def __repr__(self):
        return "<User: %r, %s, %s, %s>" % (self.user_id, self.name, self.alias, self.email)


class Area(db.Model):
    area_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    short_name = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)

    def __init__(self, name, description):
        self.name = my_db_text_factory(name)
        self.description = my_db_text_factory(description)

    def __repr__(self):
        return "<Area: %r, %s, %s>" % (self.area_id, self.name, self.description)


class AreaUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False, index=True)
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False, index=True)
    permission = db.Column(db.Integer, nullable=False, doc=u"权限")

    def __init__(self, area, user, permission):
        self.area = area
        self.user = user
        self.permission = permission

    def __repr__(self):
        return "<AreaUser: %d, %d, %d>" % (self.area, self.user, self.permission)


class Topic(db.Model):
    topic_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False, index=True)
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False, index=True)
    content = db.Column(db.Text)

    def __init__(self, area, user):
        self.area = area
        self.user = user

    def __repr__(self):
        return "<Topic: %r, %d, %d, %s>" % (self.topic_id, self.area, self.user, tr(self.content, 16))


class Reply(db.Model):
    reply_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    topic = db.Column(db.Integer, db.ForeignKey('topic.topic_id'), nullable=False, index=True)
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False, index=True)
    quote_reply = db.Column(db.Integer, db.ForeignKey('reply.reply_id'), nullable=True)
    content = db.Column(db.Text)

    def __init__(self, topic, user, content, quote_reply=None):
        self.topic = topic
        self.user = user
        self.content = content
        if quote_reply is not None:
            self.quote_reply = quote_reply

    def __repr__(self):
        return "<Reply: %r, %d, %d, %d, %s>" % (
            self.reply_id, self.topic, self.user, self.quote_reply, tr(self.content, 16))