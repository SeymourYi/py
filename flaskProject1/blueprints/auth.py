from flask import Blueprint, render_template, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from blueprints.form import RegisterForm,LoginForm
from exts import mail,db
from flask_mail import Message
from flask import request
from models import EmailCaptchaModel, UserModel
import string
import random

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("-7/76",methods=['get','post'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在！")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                # cookie：
                # cookie中不适合存储太多的数据，只适合存储少量的数据
                # cookie一般用来存放登录授权的东西
                # flask中的session，是经过加密后存储在cookie中的
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误！")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))
@bp.route("/captcha/email")
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get("email")
    # 4/6：随机数组、字母、数组和字母的组合
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    # I/O：Input/Output
    message = Message(subject="注册验证码测试", recipients=[email], body=f"您的验证码是:{captcha},此验证码为测试验证码，仅用于测试，并无实际意义。")
    mail.send(message)
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code": 200, "message": "", "data": None})


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # 表单验证：flask-wtf: wtforms
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route('/mail/text')
def mail_text():
    message = Message(subject="邮箱测试", recipients=["2258540932@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功！"