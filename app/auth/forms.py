from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Regexp

from app.models import User


class LoginForm(FlaskForm):

    """Class for login form"""

    email = StringField('email', validators=[DataRequired(), Email(), Length(1,64)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me in logged in')
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):

    """Class for registration have two functions which checking nickname or email in db for availability.
        If nickname or email are busy, user see message about it."""

    nickname = StringField('nickname', validators=[DataRequired(), Length(1,64), \
                                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Name must have only letter, number, dots and undescope')])
    email = StringField('email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password', message='Password must match')])
    submit = SubmitField('Register')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('Nickname alredy registered.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email alredy is use.')


class AboutUser(FlaskForm):

    """Form is called after registration user. Has several required fields """

    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[Length(min=0, max=50)])
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Save')
