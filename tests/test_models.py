# coding: utf8
__author__ = 'JinXing'

# TODO: models 单元测试

import unittest
import os

import datetime
import time

from matrix import app
from matrix import models
from matrix.models import db


class ModelsTest(unittest.TestCase):
    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
        app.config["SQLALCHEMY_ECHO"] = False
        db.create_all()

    def tearDown(self):
        db.session.close_all()
        db.drop_all()

    def test_get_utc_datetime(self):
        self.assertEqual(models.get_utc_datetime(), datetime.datetime.utcnow())
        self.assertEqual(models.get_utc_datetime(time.time()), datetime.datetime.utcnow())
        # n1 = datetime.datetime.now()
        # n2 = datetime.datetime.utcnow()
        # self.assertEqual(models.get_utc_datetime(n1), n2)
        try:
            models.get_utc_datetime("not a time type")
        except TypeError, e:
            self.assertIsInstance(e, TypeError)

    def test_add_del_user(self):
        u = models.User("jason", "阿森", "xing@jinxing.me", "salt", "md5(salt+md5(password))")
        db.session.add(u)
        db.session.commit()

        r = models.User.query.all()
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0].name, "jason")
        self.assertEqual(r[0].user_id, 1)
        db.session.close()

        db.session.delete(u)
        db.session.commit()
        r = models.User.query.all()
        self.assertEqual(len(r), 0)
        db.session.close()