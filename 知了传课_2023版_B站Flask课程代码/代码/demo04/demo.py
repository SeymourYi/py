from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# pip install flask-migrate
# from flask_migrate import Migrate


app = Flask(__name__)

# MySQL所在的主机名
HOSTNAME = "localhost"
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MySQL的用户名，读者用自己设置的
USERNAME = "root"
# 连接MySQL的密码，读者用自己的
PASSWORD = "root"
# MySQL上创建的数据库名称
DATABASE = "vue_text"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 在app.config中设置好连接数据库的信息，
# 然后使用SQLAlchemy(app)创建一个db对象
# SQLAlchemy会自动读取app.config中连接数据库的信息

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__="user"
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone())  # (1,)

        if __name__ == '__main__':
            app.run()
