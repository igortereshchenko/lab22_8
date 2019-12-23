from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField, IntegerField
from wtforms import validators


class QuestionnaireForm(Form):
    questions = StringField("content of the question: ", [
        validators.DataRequired("Please enter content of the question."),
        validators.Length(5, 30, "Name should be from 5 to 20 symbols")
    ])

    answers_on_questions = StringField("content of answer: ", [  # primary key
        validators.DataRequired("Please enter content of answer."),
        validators.Length(1, 40, "Name should be from 5 to 20 symbols")
    ])

    submit = SubmitField("Save")


class QuestionnaireFormUpdate(Form):
    questions = StringField("content of the question: ", [
        validators.DataRequired("Please enter content of the question."),
        validators.Length(5, 30, "Name should be from 5 to 20 symbols")
    ])

    submit = SubmitField("Save")


class StudentForm(Form):
    email = StringField("email: ", [  # primary key in table Student
        validators.Email("Please enter email."),
    ])

    answers_on_questions = StringField("content of answer: ", [  # primary key in table Questionnaire
        validators.DataRequired("Please enter content of answer."),
        validators.Length(1, 40, "Name should be from 1 to 40 symbols")
    ])

    department_number = StringField("department number: ", [  # primary key for table Departament
        validators.DataRequired("Please enter department number.")
    ])

    surname = StringField("surname: ", [
        validators.DataRequired("Please enter surname."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")])

    name = StringField("name: ", [
        validators.DataRequired("Please enter name."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")
    ])

    patronymic = StringField("patronymic name: ", [
        validators.DataRequired("Please enter patronymic name."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")
    ])

    gender = StringField("gender: ", [
        validators.DataRequired("Please enter gender."),
        validators.Length(10, 40, "Name should be from 10 to 40 symbols")
    ])

    submit = SubmitField("Save")


class StudentFormUpdate(Form):
    surname = StringField("surname: ", [
        validators.DataRequired("Please enter surname."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")])

    name = StringField("name: ", [
        validators.DataRequired("Please enter name."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")
    ])

    patronymic = StringField("patronymic name: ", [
        validators.DataRequired("Please enter patronymic name."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")
    ])

    gender = StringField("gender: ", [
        validators.DataRequired("Please enter gender."),
        validators.Length(10, 40, "Name should be from 10 to 40 symbols")
    ])

    submit = SubmitField("Save")


class DepartamentForm(Form):
    departament_of_the_institute_data = StringField("Departament of the institute name: ", [
        validators.DataRequired("Please enter departament of the institute name."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")
    ])

    department_number = StringField("department number: ", [  # primary key for table Departament
        validators.DataRequired("Please enter department number.")
    ])

    submit = SubmitField("Save")


class DepartamentFormUpdate(Form):
    departament_of_the_institute_data = StringField("Departament of the institute name: ", [
        validators.DataRequired("Please enter departament of the institute name."),
        validators.Length(5, 40, "Name should be from 5 to 40 symbols")
    ])

    submit = SubmitField("Save")


class CarForm(Form):
    car_name = StringField("car name: ", [ # primary key for table Car
        validators.DataRequired("Please enter car name."),
        validators.Length(3, 40, "Name should be from 3 to 40 symbols")
    ])

    color = StringField("color name: ", [
        validators.DataRequired("Please enter color name."),
        validators.Length(3, 15, "Name should be from 3 to 15 symbols")
    ])

    model = StringField("model name: ", [
        validators.DataRequired("Please enter model name.")
    ])

    price = IntegerField("price number: ", [
        validators.DataRequired("Please enter price number.")
    ])

    year = IntegerField("year number: ", [
        validators.DataRequired("Please enter department number.")
    ])

    submit = SubmitField("Save")


class CarFormUpdate(Form):
    model = StringField("model name: ", [
        validators.DataRequired("Please enter model name.")
    ])

    price = IntegerField("price number: ", [
        validators.DataRequired("Please enter price number.")
    ])

    submit = SubmitField("Save")
