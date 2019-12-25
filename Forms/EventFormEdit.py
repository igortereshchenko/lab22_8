from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField
from wtforms import validators


class EventFormEdit(FlaskForm):
    event_name = HiddenField("Name: ", [validators.Length(3, 20, "Name should be from 3 to 20 symbols")])
    event_date = DateField("Date: ")


    submit = SubmitField("Save")