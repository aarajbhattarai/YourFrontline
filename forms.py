from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField,TextAreaField,SubmitField,validators
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired('Please provide your name')])
    email = EmailField("Email", validators=[DataRequired('Please provide your email'),Email()])
    subject = StringField("Subject", validators=[DataRequired('Please provide the subject')])
    number= StringField("Number",validators=[DataRequired('Please provide your number')])
    message = TextAreaField("Message",validators=[DataRequired('What do you want to say to us')])
    submit = SubmitField("Send")