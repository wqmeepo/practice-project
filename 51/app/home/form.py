from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, ValidationError, Length
from app.models import User


class RegisterForm(FlaskForm):
    '''
    register form
    '''
    username = StringField(
        label='ACCOUNT : ',
        validators=[
            DataRequired('account is required'),
            Length(min=3, max=50, message='username length between 3 and 50')
        ],
        description='username',
        render_kw={
            'type': 'text',
            'placeholder': 'please input account_name',
            'class': 'validata-username',
            'size': 38,
        }
    )
    phone = StringField(
        label='PHONE : ',
        validators=[
            DataRequired('phone number is required'),
            Regexp('1[345789][0-9]{9}', message='bad format')
        ],
        description='phone-number',
        render_kw={
            'type': 'text',
            'placeholder': 'input phone number',
            'size': 38,
        }
    )
    email = StringField(
        label="EMAIL ：",
        validators=[
            DataRequired("email must be valid！"),
            Email("format！")
        ],
        description="user-email",
        render_kw={
            "type": "email",
            "placeholder": "input email！",
            "size": 38,
        }
    )
    password = PasswordField(
        label="PASSWORD ：",
        validators=[
            DataRequired("pw can not be None！")
        ],
        description="password",
        render_kw={
            "placeholder": "input password！",
            "size": 38,
        }
    )
    re_password = PasswordField(
        label="RE_PASSWORD ：",
        validators=[
            DataRequired("re_pw can not be None！"),
            EqualTo(password, message='not same password')
        ],
        description="confirm password",
        render_kw={
            "placeholder": "input re_password！",
            "size": 38,
        }
    )
    submit = SubmitField(
        render_kw={
            'class': 'btn login',
        }
    )

    @staticmethod
    def validateEmail(self, filed):
        '''
        if eamil is exist
        :param filed: email
        :return: None
        '''
        email = filed.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError('email exist')

    @staticmethod
    def validatePhone(self, field):
        '''
        if phone is exist
        :param field:
        :return:
        '''
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError('phone exist')
