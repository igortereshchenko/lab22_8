from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from Forms.UserForm import UserForm
from Forms.ContestForm import ContestForm
from Forms.EventForm import EventForm
from Forms.PlaceForm import PlaceForm
from Forms.PeopleFormEdit import PeopleFormEdit
from Forms.EventFormEdit import EventFormEdit
from Forms.ContestFormEdit import ContestFormEdit
from Forms.PlaceFormEdit import PlaceFormEdit
from Forms.CountryForm import CountryForm


from sqlalchemy.sql import func
import plotly
import plotly.graph_objs as go

import json

from Forms.UserForm import UserForm

app = Flask(__name__)
app.secret_key = 'key'

# ENV = 'dev'

# if ENV == 'dev':
#     app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Trouble228@localhost/LABA2'
# else:
#     app.debug = False
#     app.config['SECRET_KEY'] = 'laba2artemenko'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bqqxbvrfzdedks:b793bb6be49332e3500bd2293b1d9f640210e06c2d95d81f854b2f062c0302ea@ec2-174-129-254-223.compute-1.amazonaws.com:5432/darktthgk7vm7s'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Contest(db.Model):
    tablename = 'contest'
    contest_name = db.Column(db.String(20), primary_key=True)
    event_name = db.Column(db.String(20), db.ForeignKey('event.event_name'))


class People(db.Model):
    tablename = 'People'
    people_email = db.Column(db.String(20), primary_key=True)
    people_name = db.Column(db.String(20))
    people_phone = db.Column(db.String(20))
    people_birthday = db.Column(db.Date)

    people_event = db.relationship('Event')


class association(db.Model):
    __tablename__ = 'associate_table'
    left_name = db.Column(db.String(20), db.ForeignKey('event.event_name'), primary_key=True)
    right_name = db.Column(db.String(20), db.ForeignKey('place.place_name'), primary_key=True)


class Event(db.Model):
    __tablename__ = 'event'
    event_name = db.Column(db.String(20), primary_key=True)
    people_email = db.Column(db.String(20), db.ForeignKey('people.people_email'))
    event_date = db.Column(db.Date)

    place_name_fk = db.relationship("Place", secondary='associate_table')
    event_contest = db.relationship('Contest')


class CountyHasPlace(db.Model):
    __tablename__ = 'county_has_place'
    place_name = db.Column(db.String(20), db.ForeignKey('place.place_name'), primary_key=True)
    country_name = db.Column(db.String(20), db.ForeignKey('country.country_name'), primary_key=True)


class Place(db.Model):
    __tablename__ = 'place'
    place_name = db.Column(db.String(20), primary_key=True)
    place_adress = db.Column(db.String(100))

    event_name_fk = db.relationship("Event", secondary='associate_table')

    country_name_fk = db.relationship("Country", secondary='county_has_place')


class Country(db.Model):
    __tablename__ = 'country'
    country_name = db.Column(db.String(20), primary_key=True)
    country_population = db.Column(db.Integer)
    country_balance = db.Column(db.Integer)
    country_government = db.Column(db.String(30))

    place_name_fk = db.relationship('Place', secondary='county_has_place')


# создание всех таблиц
db.create_all()

# очистка всех таблиц
db.session.query(CountyHasPlace).delete()
db.session.query(Country).delete()
db.session.query(association).delete()
db.session.query(Contest).delete()
db.session.query(Event).delete()
db.session.query(People).delete()
db.session.query(Place).delete()


# # # создане объектов
#

ukraine = Country(country_name='Ukraine',
                  country_balance=1000,
                  country_government='Verhovna Rada',
                  country_population=60000
                  )

germany = Country(country_name='Germany',
                  country_balance=200,
                  country_government='Bundesregierung',
                  country_population=80000
                  )

poland = Country(country_name='Poland',
                 country_balance=30000,
                 country_government='Polska',
                 country_population=50000000
                 )

england = Country(country_name='England',
                  country_balance=40000,
                  country_government='Government',
                  country_population=70000000
                  )

portugal = Country(country_name='Portugal',
                   country_balance=50000,
                   country_government='Portu',
                   country_population=30000000
                   )

# insert into People (people_email, people_name, people_phone, people_birthday) values ('aaa@gmail.com', 'aaa', '+47447474774', '1835-1-23');
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('bbb@gmail.com', 'bbb', '+399489384334', '487-2-21');
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('ccc@gmail.com', 'ccc', '+23232332323', '1637-6-23');
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('ddd@gmail.com', 'ddd', '+39842349238492', '1-1-1');
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('eee@gmail.com', 'eee', '+304930432432', '1049-1-1');
#
#
aaa = People(people_email='aaa@gmail.com',
             people_name='aaa',
             people_phone='+47447474774',
             people_birthday="1835-01-23"
             )

bbb = People(people_email='bbb@gmail.com',
             people_name='bbb',
             people_phone='+399489384334',
             people_birthday='487-2-21'
             )

ccc = People(people_email='ccc@gmail.com',
             people_name='ccc',
             people_phone='+23232332323',
             people_birthday='1637-6-23'
             )

ddd = People(people_email='ddd@gmail.com',
             people_name='ddd',
             people_phone='+39842349238492',
             people_birthday='1-1-1'
             )

eee = People(people_email='eee@gmail.com',
             people_name='eee',
             people_phone='+304930432432',
             people_birthday='1049-1-1'
             )

# insert into Event (event_name, people_email, event_date) values ('mg', 'ddd@gmail.com', '1051-1-4');
#
# insert into Event (event_name, people_email, event_date) values ('christmas', 'bbb@gmail.com', '1619-3-8');
#
# insert into Event (event_name, people_email, event_date) values ('new year', 'aaa@gmail.com', '1994-12-2');
#
# insert into Event (event_name, people_email, event_date) values ('oktoberfest', 'ddd@gmail.com', '538-10-29');
#
# insert into Event (event_name, people_email, event_date) values ('football', 'ddd@gmail.com', '1-1-1');

mg = Event(event_name='mg',
           people_email='ddd@gmail.com',
           event_date='1051-1-4')

christmas = Event(event_name='christmas',
                  people_email='bbb@gmail.com',
                  event_date='1619-3-8'
                  )

new_year = Event(event_name='new year',
                 people_email='aaa@gmail.com',
                 event_date='1994-12-2'
                 )

oktoberfest = Event(event_name='oktoberfest',
                    people_email='ddd@gmail.com',
                    event_date='538-10-29'
                    )

football = Event(event_name='football',
                 people_email='ddd@gmail.com',
                 event_date='1-1-1'
                 )

# insert into Place (place_name, place_adress) values ('museum', 'Киевская, Киев, Ковальський провулок, 5, 5-26');
#
# insert into Place (place_name, place_adress) values ('club', 'Hindenburgstraße 7a, 57072 Siegen');
#
# insert into Place (place_name, place_adress) values ('restaurant', 'Hindenburgstraße 12, 57072 Siegen');
#
# insert into Place (place_name, place_adress) values ('stadion', 'Leimbachstadion, Leimbachstraße 263, 57074 Siegen');
#
# insert into Place (place_name, place_adress) values ('theatre', 'Morleystraße 1, 57072 Siegen');

museum = Place(place_name='museum',
               place_adress='Киевская, Киев, Ковальський провулок, 5, 5-26'
               )

club = Place(place_name='club',
             place_adress='Hindenburgstraße 7a, 57072 Siegen'
             )

restaurant = Place(place_name='restaurant',
                   place_adress='Hindenburgstraße 12, 57072 Siegen'
                   )

stadion = Place(place_name='stadion',
                place_adress='Leimbachstadion, Leimbachstraße 263, 57074 Siegen'
                )

theatre = Place(place_name='theatre',
                place_adress='Morleystraße 1, 57072 Siegen')

# insert into Contest (contest_name, event_name) values ('bier', 'football');
#
# insert into Contest (contest_name, event_name) values ('present', 'new year');
#
# insert into Contest (contest_name, event_name) values ('speed', 'christmas');
#
# insert into Contest (contest_name, event_name) values ('bottle of wine', 'christmas');
#
# insert into Contest (contest_name, event_name) values ('bierpong', 'oktoberfest');

bier = Contest(contest_name='bier',
               event_name='football'
               )

present = Contest(contest_name='present',
                  event_name='new year'
                  )

speed = Contest(contest_name='speed',
                event_name='christmas'
                )

bottle_of_wine = Contest(contest_name='bottle of wine',
                         event_name='christmas'
                         )

bierpong = Contest(contest_name='bierpong',
                   event_name='oktoberfest'
                   )

ddd.people_event.append(mg)
bbb.people_event.append(christmas)
aaa.people_event.append(new_year)
ddd.people_event.append(oktoberfest)
ddd.people_event.append(football)

football.event_contest.append(bier)
new_year.event_contest.append(present)
christmas.event_contest.append(speed)
christmas.event_contest.append(bottle_of_wine)
oktoberfest.event_contest.append(bierpong)

mg.place_name_fk.append(museum)
christmas.place_name_fk.append(club)
new_year.place_name_fk.append(restaurant)
oktoberfest.place_name_fk.append(stadion)
football.place_name_fk.append(theatre)

museum.country_name_fk.append(ukraine)
club.country_name_fk.append(poland)
restaurant.country_name_fk.append(portugal)
stadion.country_name_fk.append(england)
theatre.country_name_fk.append(germany)

db.session.add_all([aaa, bbb, ccc, ddd, eee,
                    mg, christmas, new_year, oktoberfest, football,
                    ukraine, germany, poland, england, portugal,
                    museum, club, restaurant, stadion, theatre,
                    bier, present, speed, bottle_of_wine, bierpong,

                    ])

db.session.commit()


@app.route('/shop', methods=['GET', 'POST'])
def get_county():
    result = db.session.query(Country).all()

    return render_template('all_country.html', result=result)


@app.route('/get')
def insert_countries_get():
    Ukr = Country(
        country_name='Ukr',
        country_balance=228,
        country_government='Gove1',
        country_population=4000
    )
    Rus = Country(
        country_name='Rus',
        country_balance=1488122,
        country_government='Gove1',
        country_population=5431
    )
    USA = Country(
        country_name='USA',
        country_balance=23123,
        country_government='Gove1',
        country_population=5431
    )
    db.session.add_all([Ukr, Rus, USA])
    db.session.commit()
    return render_template('success.html')


@app.route('/insert', methods=['GET', 'POST'])
def insert_countries():
    form = CountryForm()

    if request.method == 'POST':
        print('asd')

        if form.validate() and form.check_balance_on_submit() and form.check_population_on_submit():

            new_country = Country(
                country_name=form.country_name.data,
                country_population=form.country_population.data,
                country_balance=form.country_balance.data,
                country_government=form.country_government.data,
            )
            print('test')
            db.session.add(new_country)
            db.session.commit()
            return redirect('/')
        else:
            if not form.check_balance_on_submit():
                form.country_balance.errors = ['should be >0']
            if not form.check_population_on_submit():
                form.country_population.errors = ['0<country_population<100']

            return render_template('country_insert_form.html', form=form)

    else:
        return render_template('country_insert_form.html', form=form)


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    query1 = (
        db.session.query(
            Country.country_name,
            Country.country_balance.label('balance')
        )
    ).all()

    country_name, country_balance = zip(*query1)
    bar = go.Bar(
        x=country_name,
        y=country_balance
    )

    data = {
        "bar": [bar]
    }
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('plot.html', graphsJSON=graphs_json)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    query1 = (
        db.session.query(
            People.people_name,
            func.count(Event.event_name).label('event_name')
        ).join(Event, People.people_email == Event.people_email).
            group_by(People.people_name)
    ).all()

    print(query1)

    query2 = (
        db.session.query(
            Event.event_name,
            func.count(Contest.contest_name).label('contest_name')
        ).join(Contest, Event.event_name == Contest.event_name).
            group_by(Event.event_name)
    ).all()

    print(query2)

    people_name, event_name = zip(*query1)
    bar = go.Bar(
        x=people_name,
        y=event_name
    )

    event_name, contest_name = zip(*query2)
    pie = go.Pie(
        labels=event_name,
        values=contest_name
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphs_json)


@app.route('/edit_people/<string:email>', methods=['GET', 'POST'])
def edit_people(email):
    form = PeopleFormEdit()
    result = db.session.query(People).filter(People.people_email == email).one()

    if request.method == 'GET':

        form.people_name.data = result.people_name
        form.people_email.data = result.people_email
        form.people_birthday.data = result.people_birthday
        form.people_phone.data = result.people_phone

        return render_template('edit_people.html', form=form, form_name=email)
    elif request.method == 'POST':

        result.people_name = form.people_name.data
        result.user_email = form.people_email.data
        result.people_birthday = form.people_birthday.data.strftime("%Y-%m-%d"),
        result.people_phone = form.people_phone.data

        db.session.commit()
        return redirect('/people')


@app.route('/edit_event/<string:name>', methods=['GET', 'POST'])
def edit_event(name):
    form = EventFormEdit()
    result = db.session.query(Event).filter(Event.event_name == name).one()

    if request.method == 'GET':

        form.event_name.data = result.event_name
        form.event_date.data = result.event_date

        return render_template('edit_event.html', form=form, form_name=name)
    elif request.method == 'POST':

        result.event_name = form.event_name.data
        result.event_date = form.event_date.data.strftime("%Y-%m-%d"),

        db.session.commit()
        return redirect('/event')


@app.route('/edit_contest/<string:name>', methods=['GET', 'POST'])
def edit_contest(name):
    form = ContestFormEdit()
    result = db.session.query(Contest).filter(Contest.contest_name == name).one()

    if request.method == 'GET':

        form.contest_name.data = result.contest_name

        return render_template('edit_contest.html', form=form, form_name='Edit Contest')
    elif request.method == 'POST':

        result.contest_name = form.contest_name.data

        db.session.commit()
        return redirect('/contest')


@app.route('/edit_place/<string:name>', methods=['GET', 'POST'])
def edit_place(name):
    form = PlaceFormEdit()
    result = db.session.query(Place).filter(Place.place_name == name).one()

    if request.method == 'GET':

        form.place_name.data = result.place_name
        form.place_adress.data = result.place_adress

        return render_template('edit_place.html', form=form, form_name='Edit Place')
    elif request.method == 'POST':

        result.place_name = form.place_name.data
        result.place_adress = form.place_adress.data

        db.session.commit()
        return redirect('/place')


@app.route('/create_people', methods=['POST', 'GET'])
def create_people():
    form = UserForm()

    if request.method == 'POST':
        new_people = People(
            people_name=form.people_name.data,
            people_birthday=form.people_birthday.data.strftime("%Y-%m-%d"),
            people_email=form.people_email.data,
            people_phone=form.people_phone.data,
        )
        db.session.add(new_people)
        db.session.commit()
        return redirect('/people')
    elif request.method == 'GET':
        return render_template('create_people.html', form=form)


@app.route('/delete_people/<string:email>', methods=['GET', 'POST'])
def delete_people(email):
    result = db.session.query(People).filter(People.people_email == email).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/people')


@app.route('/create_contest', methods=['POST', 'GET'])
def create_contest():
    form = ContestForm()

    if request.method == 'POST':
        new_contest = Contest(
            contest_name=form.contest_name.data,
        )
        db.session.add(new_contest)
        db.session.commit()
        return redirect('/contest')
    elif request.method == 'GET':
        return render_template('create_contest.html', form=form)


@app.route('/delete_contest/<string:name>', methods=['GET', 'POST'])
def delete_contest(name):
    result = db.session.query(Contest).filter(Contest.contest_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/contest')


@app.route('/create_event', methods=['POST', 'GET'])
def create_event():
    form = EventForm()

    if request.method == 'POST':
        new_event = Event(
            event_name=form.event_name.data,
            event_date=form.event_date.data.strftime("%Y-%m-%d")
        )
        db.session.add(new_event)
        db.session.commit()
        return redirect('/event')
    elif request.method == 'GET':
        return render_template('create_event.html', form=form)


@app.route('/delete_event/<string:name>', methods=['GET', 'POST'])
def delete_event(name):
    result = db.session.query(Event).filter(Event.event_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/event')


@app.route('/create_place', methods=['POST', 'GET'])
def create_place():
    form = PlaceForm()

    if request.method == 'POST':
        new_place = Place(
            place_name=form.place_name.data,
            place_adress=form.place_adress.data
        )
        db.session.add(new_place)
        db.session.commit()
        return redirect('/place')
    elif request.method == 'GET':
        return render_template('create_place.html', form=form)


@app.route('/delete_place/<string:name>', methods=['GET', 'POST'])
def delete_place(name):
    result = db.session.query(Place).filter(Place.place_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/place')


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


@app.route('/people', methods=['GET'])
def all_peolpe():
    result = db.session.query(People).all()

    return render_template('all_people.html', result=result)


@app.route('/contest', methods=['GET'])
def all_contest():
    result = db.session.query(Contest).all()

    return render_template('all_contest.html', result=result)


@app.route('/event', methods=['GET'])
def all_event():
    result = db.session.query(Event).all()

    return render_template('all_event.html', result=result)


@app.route('/place', methods=['GET'])
def all_place():
    result = db.session.query(Place).all()

    return render_template('all_place.html', result=result)


if __name__ == "__main__":
    app.debug = True
    app.run()
