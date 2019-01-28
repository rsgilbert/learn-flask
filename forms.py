#Backend - creating a form

from flask_wtf import Form  #base form class
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired('Please enter your first name')])
    last_name = StringField('Last name', validators=[DataRequired('Please enter your last name')])
    email = StringField('Email', validators=[DataRequired('Email address required'), Email("Wrong email")])
    password = PasswordField('Password', validators=[DataRequired('Please enter a valid password') ])
    submit = SubmitField('Sign up')

