from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms.user_form import QuestionnaireForm, QuestionnaireFormUpdate, StudentForm, StudentFormUpdate, DepartamentForm, \
    DepartamentFormUpdate, CarForm, CarFormUpdate

import plotly.graph_objs as go
import plotly
import json

import plotly
import json
from flask_sqlalchemy import SQLAlchemy
import plotly.graph_objs as go
from sqlalchemy.sql import func

app = Flask(__name__)
app.secret_key = 'key'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bd@localhost/postgres'
else:
    app.debug = False
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgres://ysddjibomrqxyq:50528618c5ff45de5797f6383377f9c939bb22c0922bedfe3fa2f79aa73bc7b9@ec2-23-21-249-0.compute-1.amazonaws.com:5432/dfc1evd9hjiukk'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class ormDepartament(db.Model):
    __tablename__ = 'Departament'

    departament_of_the_institute_data = db.Column(db.String(40), nullable=False)
    department_number = db.Column(db.String(20), primary_key=True)

    students_ = db.relationship('ormStudent')


class ormStudent(db.Model):
    __tablename__ = 'Student'

    email = db.Column(db.String(30), primary_key=True)
    answers_on_questions = db.Column(db.String(40), db.ForeignKey('Questionnaire.answers_on_questions'), nullable=False)
    department_number = db.Column(db.String(20), db.ForeignKey('Departament.department_number'), nullable=False)
    car_name = db.Column(db.String(40), db.ForeignKey('Car.car_name'), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    patronymic = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(40), nullable=False)


class ormQuestionnaire(db.Model):
    __tablename__ = 'Questionnaire'

    questions = db.Column(db.String(30), nullable=False)
    answers_on_questions = db.Column(db.String(40), primary_key=True)

    students__ = db.relationship('ormStudent')


class ormCar(db.Model):
    __tablename__ = 'Car'

    car_name = db.Column(db.String(40), primary_key=True)
    color = db.Column(db.String(40), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    students___ = db.relationship('ormStudent')


# db.drop_all()
# db.session.query(ormStudent).delete()
# db.session.query(ormDepartament).delete()
# db.session.query(ormQuestionnaire).delete()
# db.session.query(ormCar).delete()
#
# db.create_all()
#
# Student1 = ormStudent(email='ihor.riasyk@gmail.com', answers_on_questions='a)', department_number='132',
#                       car_name='name car1', surname='Riasyk',
#                       name='Ihor', patronymic='Sergeevich', gender='male')
# Student2 = ormStudent(email='alexandar.buts@gmail.com', answers_on_questions='b)', department_number='133',
#                       car_name='name car2', surname='Buts',
#                       name='Alexandar', patronymic='Alexandrovich', gender='male')
# Student3 = ormStudent(email='andiy.hladkiy@gmail.com', answers_on_questions='c)', department_number='133',
#                       car_name='name car3', surname='Hladkiy',
#                       name='Andriy', patronymic='Pavlovich', gender='male')
#
# Departament1 = ormDepartament(departament_of_the_institute_data='FPM', department_number='132')
# Departament2 = ormDepartament(departament_of_the_institute_data='IPSA', department_number='133')
# Departament3 = ormDepartament(departament_of_the_institute_data='ITS', department_number='134')
#
# Questionnaire1 = ormQuestionnaire(questions='test quaestion?1', answers_on_questions='a)')
# Questionnaire2 = ormQuestionnaire(questions='test quaestion?2', answers_on_questions='b)')
# Questionnaire3 = ormQuestionnaire(questions='test quaestion?3', answers_on_questions='c)')
#
# Car1 = ormCar(car_name='name car1', color='green', model='model1', price=15000, year=2016)
# Car2 = ormCar(car_name='name car2', color='yellow', model='model2', price=16000, year=2017)
# Car3 = ormCar(car_name='name car3', color='black', model='model3', price=35000, year=2019)
#
# Departament1.students_.append(Student1)
# Departament2.students_.append(Student2)
# Departament3.students_.append(Student3)
#
# Questionnaire1.students__.append(Student1)
# Questionnaire2.students__.append(Student2)
# Questionnaire3.students__.append(Student3)
#
# Car1.students___.append(Student1)
# Car2.students___.append(Student2)
# Car3.students___.append(Student3)
#
# db.session.add_all([Student1, Student2, Student3])
# db.session.add_all([Departament1, Departament2, Departament3])
# db.session.add_all([Questionnaire1, Questionnaire2, Questionnaire3])
# db.session.add_all([Car1, Car2, Car3])
#
# db.session.commit()


# main page
@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


# car page
@app.route('/shop', methods=['GET'])
def shop():
    result = db.session.query(ormCar).all()

    return render_template('shops.html', car_name=result)


@app.route('/new_shops', methods=['GET', 'POST'])
def new_shops():
    form = CarForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('shops_form.html', form=form, form_name="New Shops",
                                   action="new_shops")
        else:
            new_user = ormCar(
                car_name=form.car_name.data,
                color=form.color.data,
                model=form.model.data,
                price=form.price.data,
                year=form.year.data
            )
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('shop'))

    return render_template('shops_form.html', form=form, form_name="New Shops", action="new_shops")


@app.route('/edit_shops/<string:x>', methods=['GET', 'POST'])
def edit_shops(x):
    form = CarFormUpdate()
    user = db.session.query(ormCar).filter(ormCar.car_name == x).one()

    if request.method == 'GET':
        return render_template('shops_form_update.html', form=form, form_name="Edit shops")

    else:
        if form.validate() == False:
            return render_template('shops_form_update.html', form=form, form_name="Edit shops")
        else:
            user.model = form.model.data
            user.price = form.price.data
            db.session.commit()

            return render_template('ok.html')


@app.route('/delete_shops/<string:x>', methods=['GET'])
def delete_shops(x):
    result = db.session.query(ormCar).filter(ormCar.car_name == x).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('ok.html')


# departament page
@app.route('/departament', methods=['GET'])
def departament():
    result = db.session.query(ormDepartament).all()

    return render_template('departaments.html', department_number=result)


@app.route('/new_departament', methods=['GET', 'POST'])
def new_departament():
    form = DepartamentForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('departament_form.html', form=form, form_name="New Departament",
                                   action="new_departament")
        else:
            new_user = ormDepartament(
                departament_of_the_institute_data=form.departament_of_the_institute_data.data,
                department_number=form.department_number.data
            )
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('departament'))

    return render_template('departament_form.html', form=form, form_name="New Departament", action="new_departament")


@app.route('/edit_departments/<string:x>', methods=['GET', 'POST'])
def edit_departament(x):
    form = DepartamentFormUpdate()
    user = db.session.query(ormDepartament).filter(ormDepartament.department_number == x).one()

    if request.method == 'GET':
        return render_template('departament_form_update.html', form=form, form_name="Edit departament")

    else:
        if form.validate() == False:
            return render_template('departament_form_update.html', form=form, form_name="Edit departament")
        else:
            user.departament_of_the_institute_data = form.departament_of_the_institute_data.data

            db.session.commit()

            return redirect(url_for('departament'))


@app.route('/delete_departments/<string:x>', methods=['GET'])
def delete_departament(x):
    result = db.session.query(ormDepartament).filter(ormDepartament.department_number == x).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('ok.html')


# student
@app.route('/students', methods=['GET'])
def clients():
    result = db.session.query(ormStudent).all()

    return render_template('students.html', students=result)


@app.route('/new_students', methods=['GET', 'POST'])
def new_students():
    form = StudentForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('student_form.html', form=form, form_name="New student", action="new_students")
        else:
            new_user = ormStudent(
                email=form.email.data,
                answers_on_questions=form.answers_on_questions.data,
                department_number=form.department_number.data,
                surname=form.surname.data,
                name=form.name.data,
                patronymic=form.patronymic.data,
                gender=form.gender.data
            )
            db.session.add(new_user)
            db.session.commit()

            return render_template('ok.html')

    return render_template('student_form.html', form=form, form_name="New student", action="new_students")


@app.route('/edit_students/<string:x>', methods=['GET', 'POST'])
def edit_students(x):
    form = StudentFormUpdate()

    user = db.session.query(ormStudent).filter(ormStudent.email == x).one()

    if request.method == 'GET':
        return render_template('student_form_update.html', form=form, form_name="Edit student")

    else:
        if form.validate() == False:
            return render_template('student_form_update.html', form=form, form_name="Edit student")
        else:
            user.surname = form.surname.data
            user.name = form.name.data
            user.patronymic = form.patronymic.data
            user.gender = form.gender.data
            db.session.commit()

            return render_template('ok.html')


@app.route('/delete_students/<string:x>', methods=['GET'])
def delete_students(x):
    result = db.session.query(ormStudent).filter(ormStudent.email == x).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('ok.html')


# questionnaire page
@app.route('/questionnaire', methods=['GET'])
def questionnaires():
    result = db.session.query(ormQuestionnaire).all()

    return render_template('questionnaires.html', questionnaire=result)


@app.route('/new_questionnaire', methods=['GET', 'POST'])
def new_questionnaires():
    form = QuestionnaireForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('questionnaire_form.html', form=form, form_name="New questionnaire")

        else:
            new_user = ormQuestionnaire(
                questions=form.questions.data,
                answers_on_questions=form.answers_on_questions.data
            )
            db.session.add(new_user)
            db.session.commit()

            return render_template('ok.html')

    return render_template('questionnaire_form.html', form=form, form_name="New questionnaire")


@app.route('/edit_questionnaire/<string:x>', methods=['GET', 'POST'])
def edit_questionnaires(x):
    form = QuestionnaireFormUpdate()
    user = db.session.query(ormQuestionnaire).filter(ormQuestionnaire.answers_on_questions == x).one()

    if request.method == 'GET':

        # user_id =request.args.get('present_name')
        # db = PostgreDB()
        # user = db.sqlalchemy_session.query(ormPresents).filter(ormPresents.present_name == x).one()

        # fill form and send to user
        # form.questions.data = user.questions
        # form.answers_on_questions.data = user.answers_on_questions

        return render_template('questionnaire_form_update.html', form=form, form_name="Edit questionnaire")


    elif request.method == 'POST':

        if form.validate() == False:
            return render_template('questionnaire_form_update.html', form=form, form_name="Edit questionnaire")
        else:

            # update fields from form data
            user.questions = form.questions.data
            # user.answers_on_questions = form.answers_on_questions.data
            db.session.commit()

            return render_template('ok.html')


@app.route('/delete_questionnaire/<string:x>', methods=['GET'])
def delete_questionnaires(x):
    # user_id = request.form['present_name']

    result = db.session.query(ormQuestionnaire).filter(ormQuestionnaire.answers_on_questions == x).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('ok.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    query1 = (
        db.session.query(
            ormCar.price,
            func.count(ormCar.car_name).label('car')
        ).
            outerjoin(ormStudent).
            group_by(ormCar.price)
    ).all()

    query2 = (
        db.session.query(
            ormQuestionnaire.answers_on_questions,
            func.count(ormStudent.gender).label('gender')
        ).
            outerjoin(ormStudent).
            group_by(ormQuestionnaire.answers_on_questions)
    ).all()

    names, skill_counts = zip(*query1)
    bar = go.Bar(
        x=names,
        y=skill_counts
    )

    skills, user_count = zip(*query2)
    pie = go.Pie(
        labels=skills,
        values=user_count
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)


#     =================================================================================================

if __name__ == '__main__':
    app.run(debug=True)
