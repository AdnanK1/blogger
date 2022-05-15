from flask import render_template,redirect,url_for
from . import main

@main.route('/')
@main.route('/home')
def index_page():

    return render_template('index.html')

@main.route('/register')
def register_page():

    return render_template('register.html')

@main.route('/login')
def login_page():

    return render_template('login.html')