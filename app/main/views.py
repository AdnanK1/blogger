from flask import render_template,redirect,url_for,flash
from . import main
from .forms import RegisterForm,LoginForm,BlogForm
from ..models import User
from ..extensions import db
from flask_login import login_user,logout_user

@main.route('/')
@main.route('/home')
def index_page():

    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password1.data
        new_user = User(username=username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.index_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html',form=form)

@main.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'You are loggied in as: {attempted_user.username}',category='success')
            return redirect(url_for('main.index_page'))
        else:
            flash('Username and password are not matching! Please try again', category='danger')

    return render_template('login.html', form=form)

@main.route('/blog')
def blog_page():
    form = BlogForm()
    return render_template('blog.html', form=form)

@main.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!',category= 'info')
    return redirect(url_for('main.index_page'))
