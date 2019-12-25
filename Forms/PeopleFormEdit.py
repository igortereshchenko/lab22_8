from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField
from wtforms import validators


class PeopleFormEdit(FlaskForm):
    people_name = StringField("Name: ", [validators.Length(3, 20, "Name should be from 3 to 20 symbols")])
    people_email = HiddenField("Email: ", [validators.Email("Wrong email format")])
    people_birthday = DateField("Birthday: ")
    people_phone = StringField("Phone: ", [validators.Length(20)])


    submit = SubmitField("Save")