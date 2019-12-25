from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms import validators


class PlaceForm(FlaskForm):
    place_name = StringField("Name: ", [
        validators.DataRequired("Please enter name of place."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    place_adress = StringField("Adress: ", [
        validators.DataRequired("Please enter your place adress."),
        validators.Length(3, 100, "Name should be from 3 to 100 symbols")
    ])

    submit = SubmitField("Save")