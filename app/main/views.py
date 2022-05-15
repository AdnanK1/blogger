from flask import render_template,redirect,url_for
from . import main
from .forms import RegisterForm,LoginForm
from ..models import User
from ..extensions import db

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

    return render_template('register.html',form=form)

@main.route('/login')
def login_page():

    return render_template('login.html')