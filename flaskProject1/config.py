SECRET_KEY = "ASDASWD"

HOSTNAME = "localhost"
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MySQL的用户名，读者用自己设置的
USERNAME = "root"
# 连接MySQL的密码，读者用自己的
PASSWORD = "root"
# MySQL上创建的数据库名称
DATABASE = "text0"
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱设置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2963637346@qq.com"
MAIL_PASSWORD = "ywmlolrifsurddfc"
MAIL_DEFAULT_SENDER = "2963637346@qq.com"