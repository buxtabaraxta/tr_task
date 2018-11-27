from flask import render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user

from ..auth.forms import AboutUser
from . import main
from .. import db

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/profile/<nickname>')
def profile(nickname):

    return render_template('main/profile.html', nickname=current_user.nickname)

@main.route('/edir_profile/<nickname>', methods=['GET', 'POST'])
@login_required
def edit_profile(nickname):
    """Causes form with information about user. If user put data when have registration. This data will be displayed"""

    form = AboutUser()
    if form.validate_on_submit():
        current_user.city = form.city.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('main.profile', nickname=current_user.nickname))
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.age.data = current_user.age
        form.country.data = current_user.country
        form.city.data = current_user.city
        form.about_me.data = current_user.about_me
    return render_template('main/edit_profile.html', nickname=nickname, form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))