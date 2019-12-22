from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, HiddenField
from wtforms import validators
from datetime import date


class DisciplineForm(Form):
    discipline_id = HiddenField()

    discipline_name = StringField("name: ", [
        validators.DataRequired("Please enter discipline name."),
        validators.Length(3, 255, "Name should be from 3 to 255 symbols")
    ])

    discipline_group = StringField("Group: ", [
        validators.DataRequired("Please enter discipline Group."),
        validators.Length(3, 255, "Context should be from 3 to 255 symbols")])

    submit = SubmitField("Save")
