from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms import validators


class EventForm(FlaskForm):
    event_name = StringField("Name: ", [
        validators.DataRequired("Please enter name of Event."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    event_date = DateField("Date: ", [validators.DataRequired("Please enter date of Event.")])


    submit = SubmitField("Save")