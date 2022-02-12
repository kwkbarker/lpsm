from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from lpsm.models import User

class RegistrationForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists.')
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email address already registered. Please log in.')
        
    username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email:", validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    confirmation = PasswordField(label='Confirm Password:', validators=[EqualTo('password'), DataRequired()])
    city = StringField(label="Location:", validators=[DataRequired()])
    submit = SubmitField(label='Create Account')

class ListingForm(FlaskForm):
    title = StringField(label="Title:", validators=[DataRequired()])
    description = StringField(label="Description:", validators=[DataRequired()])
    cover_grade = RadioField(label="Cover Grade:", validators=[DataRequired()])
    vinyl_grade = RadioField(label="Vinyl Grade:", validators=[DataRequired()])
    