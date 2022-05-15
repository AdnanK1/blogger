from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired,ValidationError
from ..models import User

class RegisterForm(FlaskForm):
    username = StringField(label='Username:',validators=[Length(min=3,max=15),DataRequired()])
    email = StringField(label='Email Address:',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=2), DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist!')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exist!')

class LoginForm(FlaskForm):
    username = StringField(label= 'Username:', validators=[DataRequired()])
    password = PasswordField(label= 'Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class BlogForm(FlaskForm):
    blog = TextAreaField(label='Please add your blog',validators=[DataRequired()])
    submit = SubmitField(label='Submit')