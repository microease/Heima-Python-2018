# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand

manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ''
