# coding=utf-8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_script import Manager
from flask_migrate import Migrate,

app = Flask(__name__)


class Config(object):
    # sqlalemy配置参数
    SQLALCHEMY_DATABASE_URL = "mysql://root:mysql@127.0.0.1:3306/author_book"
    # 设置sqlalchemy自动更新数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)
db = SQLAlchemy(app)
# 创建Flask 脚本管理工具对象
manager = Manager(app)
# 创建数据库迁移工具对象
Migrate(app,db)
# 向manager对象中添加数据库的操作命令
manager.add_command()

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


@app.route("/")
def index():
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # app.run(debug=True)
    manager.run()


