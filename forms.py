from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class GreetingForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Hello')
