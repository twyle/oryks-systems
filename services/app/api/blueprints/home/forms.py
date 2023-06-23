from wtforms import Form
from wtforms.validators import DataRequired, Email
from wtforms import EmailField

class RegistrationForm(Form):
    email = EmailField('Email Address', [DataRequired(), Email()])
