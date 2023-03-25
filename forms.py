from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')
    header_image_url = StringField('(Optional) Header Image URL')
    bio = StringField('(Optional) Bio')

class ChangePasswordForm(FlaskForm):
    """Form for change user password."""

    current_password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6), EqualTo('repeat_password', message='Passwords must match')])
    repeat_password = PasswordField('Current password', validators=[DataRequired(), Length(min=6)])
   
class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
