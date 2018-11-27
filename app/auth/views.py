from flask import render_template, url_for, redirect, request
from flask_login import login_user, current_user, login_required

from . import auth
from .. import db
from .forms import LoginForm, RegisterForm, AboutUser
from ..models import User
from flask import flash

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.profile', nickname=user.nickname))
        flash('Incorrect login or password')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(nickname=form.nickname.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.information', nickname=user.nickname))
    return render_template('auth/register.html', form=form)

@auth.route('/<nickname>/info', methods=['GET', 'POST'])
def information(nickname):
    form = AboutUser()
    if form.validate_on_submit():
        user = User.query.filter_by(nickname=nickname).first()
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.age = form.age.data
        user.country = form.country.data
        user.city = form.city.data
        user.about = form.about_me.data
        db.session.commit()
        flash('Now You can login')
        return redirect(url_for('auth.login'))
    return render_template('auth/information.html', form=form, nickname=nickname)

