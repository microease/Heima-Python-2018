# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    # sqlalemy配置参数
    SQLALCHEMY_DATABASE_URL = "mysql://root:mysql@127.0.0.1:3306/author_book"
    # 设置sqlalchemy自动更新数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)
db = SQLAlchemy(app)


class Author(db.Model):
    # 作者
    __tablename__ = "tbl_author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_author.id"))


if __name__ == '__main__':
    app.run(debug=True)
