from flask_wtf import Form
from wtforms import StringField, SubmitField, HiddenField, IntegerField
from wtforms import validators
from datetime import date


class HouseForm(Form):
    house_id = HiddenField()

    address = StringField("address: ", [
        validators.DataRequired("Please enter house price.")
    ])

    price = IntegerField("Price: ", [
        validators.DataRequired("Please enter House price."),
        validators.NumberRange(1, 1000, "Price should be between 1 and 1000")])

    year = IntegerField("year: ", [
        validators.DataRequired("Please enter House year."),
        validators.NumberRange(2016, None, "Year should be more than 2016")])

    floor_count = IntegerField("floor_count: ", [
        validators.DataRequired("Please enter floor_count.")])

    submit = SubmitField("Save")
