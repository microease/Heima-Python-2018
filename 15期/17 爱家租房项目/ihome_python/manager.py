# coding:utf-8
from ihome import create_app, db
from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 创建flask应用对象
app = create_app("develop")
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
