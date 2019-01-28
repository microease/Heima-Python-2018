# coding=utf-8
import unittest
from autor_book import Author, db,app


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://"

    def test_add_author(self):
        # 测试添加作者的数据库操作
        author = Author(name="张", email="itcast@itcast.cn", mobile="13838384381")
        db.session.add(author)
