from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, Label, BooleanField, DateTimeField, FloatField
from wtforms import validators


#lab 2 part ==========================



class HostForm(Form):

    hostname = StringField("Hostname: ", [validators.data_required("Please, enter hostname.")])
    price = FloatField("Price: ", [validators.NumberRange(min = 0, message = "0 < price")])
    speed = FloatField("Speed: ", [validators.NumberRange(min = 1, max = 10, message = "1 < speed < 10")])
    os_type = StringField("Os type: ", [validators.Optional()])


    submit = SubmitField("Enter")


#lab 2 part end ======================


class UsersForm(Form):

    nickname = StringField("Nickname: ", [validators.data_required("Please, enter user nickname.")])
    login = StringField("Login: ", [validators.Optional()])
    password = StringField("Password: ", [validators.Optional()])

    submit = SubmitField("Enter")


class SitesForm(Form):

    site_adress = StringField("Site adress: ", [validators.URL("Please, enter site adress.")])
    site_name = StringField("Site name: ", [validators.Optional()])

    submit = SubmitField("Enter")


class StylesForm(Form):

    style_name = StringField("Style name: ", [validators.data_required("Please, enter style name.")])
    code = StringField("Code: ", [validators.Optional()])
    premium = BooleanField("Premium: ", [validators.Optional()])

    submit = SubmitField("Enter")

class TopicAnalitycsForm(Form):

    topic_name = StringField("Topic name: ", [validators.data_required("Please, enter topic name.")])
    words = IntegerField("Words: ", [validators.Optional()])
    paragraphs = IntegerField("Paragraphs: ", [validators.Optional()])
    focus_time = DateTimeField("Focus time: ", [validators.Optional()])
    sentences = IntegerField("Sentences: ", [validators.Optional()])
    images = FloatField("Images: ", [validators.Optional()])

    submit = SubmitField("Enter")

class BlockForm(Form):

    style_name = StringField("Style name: ", [validators.data_required("Please, enter type name.")])
    block_name = StringField("Block name: ", [validators.data_required("Please, enter block name.")])
    block_type = StringField("Block type: ", [validators.data_required("Please, enter block type.")])
    code = StringField("Code name: ", [validators.Optional()])
    source = StringField("Source name: ", [validators.Optional()])


    submit = SubmitField("Enter")


class DashboardForm(Form):
    hostname = StringField("Topic name: ", [validators.data_required("Please, enter hostname.")])
    price = FloatField("Price: ", [validators.Optional()])
    
