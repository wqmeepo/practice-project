from app.home import home
from app import db
from app.home.form import RegisterForm
from app.models import User, Goods, Orders, Cart, OrdersDetail
from flask import render_template, url_for, redirect, flash, session, request, make_response
from werkzeug.security import generate_password_hash
from functools import wraps
import random
import string
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


def rndColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def geneText():
    return ''.join(random.sample(string.ascii_letters + string.digits, 4))


def draw_line(draw, num, width, height):
    for num in range(num):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)


def getVerifyCode():
    code = geneText()
    width, height = 120, 50
    im = Image.new('RGB', (width, height), color='white')
    font = ImageFont.truetype('app/static/fonts/arial.ttf', 40)
    draw = ImageDraw.Draw(im)
    for item in range(4):
        draw.text((5 + random.randint(-3, 3) + 23 * item, 5 + random.randint(-3, 3)), code[item], rndColor(), font)
    return im, code


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/code')
def getCode():
    image, code = getVerifyCode()
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端
    response = make_response(buf_str)
    response.headers['content-type'] = 'image/gif'
    #   验证码存在session内
    session['image'] = code
    return response


@home.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('home.index'))
    form = RegisterForm()  # 实例化注册表单
    if form.validate_on_submit():
        data = form.data
        user = User(
            username=data['username'],
            email=data['email'],
            password=generate_password_hash(data['password']),
            phone=data['phone']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('home/register.html', form=form)
