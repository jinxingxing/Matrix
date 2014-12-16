# coding: utf8
__author__ = 'JinXing'


import unittest
from matrix import app
from matrix import utils


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_redirect_download(self):
        with app.test_request_context():
            url = "http://127.0.0.1/10m.bin"
            r = utils.redirect_download(url)
        self.assertIn("<html>", r)
        self.assertIn(url, r)

    def test_tr(self):
        self.assertEqual(utils.tr("123", 3), "123")
        self.assertEqual(utils.tr("1234", 3), "123...")

    def test_is_name(self):
        self.assertEqual(utils.is_name("name"), True)
        self.assertEqual(utils.is_name("name-._"), True)
        self.assertEqual(utils.is_name("name-._*"), False)


# unittest.main()