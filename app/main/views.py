from flask import render_template,redirect,url_for,flash
from . import main
from .forms import RegisterForm,LoginForm,BlogForm,CommentForm
from ..models import User,Blog,Comment
from ..extensions import db
from flask_login import login_user,logout_user,current_user
from ..request import get_quote

@main.route('/')
@main.route('/home')
def index_page():
    blogs = Blog.query.all()
    comments = Comment.query.all()
    quotes = get_quote()
    return render_template('index.html',blogs=blogs,quotes=quotes,comments=comments)

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
        return redirect(url_for('main.login_page'))

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

@main.route('/blog', methods=['GET','POST'])
def blog_page():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(blog=form.blog.data,user_id=current_user.id)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.index_page', blogs=new_blog))

    return render_template('blog.html', form=form)

@main.route('/comment',methods=['GET','POST'])
def comment_page():
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.index_page'))
    return render_template('comment.html',form=form)

@main.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!',category= 'info')
    return redirect(url_for('main.index_page'))

@main.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    user_to_delete = Blog.query.get_or_404(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    flash('Blog deleted Successfully',category='success')
    return redirect(url_for('main.index_page'))

@main.route("/delete_comment/<int:id>",methods=['GET','POST'])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted Successfully',category='success')
    return redirect(url_for('main.index_page'))