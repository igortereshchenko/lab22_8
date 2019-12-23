from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iftysdsitdzwda:2977781e219a7a1fa528d991fa97cb28a4fd66fb30907079f3f6560f914af552@ec2-174-129-255-10.compute-1.amazonaws.com:5432/dci7r4hl6v22to'

db = SQLAlchemy(app)


#lab 2 part ===========================

hosted = db.Table('hosted',
    db.Column('hostname', db.String(64), db.ForeignKey('host.hostname'), primary_key=True),
    db.Column('site_adress', db.String(64), db.ForeignKey('sites.site_adress'), primary_key=True))


class Host(db.Model):

    __tablename__ = 'host'
    hostname = db.Column('hostname', db.String(64), primary_key=True)
    price = db.Column('price', db.Float, primary_key=False)
    speed = db.Column('speed', db.Float, primary_key=False)
    os_type = db.Column('os_type', db.String(64), primary_key=False)
    hosted = db.relationship('Sites', secondary=hosted, lazy='subquery',
        backref=db.backref('host', lazy=True))
    def __init__(self, hostname, price, speed, os_type):

        self.hostname = hostname
        self.price = price
        self.speed = speed
        self.os_type = os_type

    def __repr__(self):

        return '<block: hostname=%r; price=%r; speed=%r; os_type=%r>' % \
        self.hostname, self.price, self.speed, self.os_type


#lab 2 part end =======================


class Users(db.Model):

    __tablename__ = 'users'
    nickname = db.Column('nickname', db.String(64), primary_key=True)
    login = db.Column('login', db.String(64), primary_key=False)
    password = db.Column('password', db.String(64), primary_key=False)

    def __init__(self, nickname, login, password):

        self.nickname = nickname
        self.login = login
        self.password = password

    def __repr__(self):

        return '<users: nickname=%r; login=%r; password=%r>' % \
        self.nickname, self.nickname, self.nickname



class Styles(db.Model):

    __tablename__ = 'styles'
    style_name = db.Column('style_name', db.String(64), primary_key=True)
    code = db.Column('code', db.String(64), primary_key=False)
    premium = db.Column('premium', db.Boolean(64), primary_key=False)
    '''
    blocks = db.relationship('block', lazy=True)
    '''
    def __init__(self, style_name, code, premium):

        self.style_name = style_name
        self.code = code
        self.premium = premium

    def __repr__(self):

        return '<styles: style_name=%r; code=%r; premium=%r>' % \
        self.style_name, self.code, self.premium


hosting = db.Table('hosting',
    db.Column('site_adress', db.String(64), db.ForeignKey('sites.site_adress'), primary_key=True),
    db.Column('hostname', db.String(64), db.ForeignKey('server.hostname'), primary_key=True)
)


class Sites(db.Model):

    __tablename__ = 'sites'
    site_adress = db.Column('site_adress', db.String(64), primary_key=True)
    site_name = db.Column('site_name', db.String(64), primary_key=False)

    def __init__(self, site_adress, site_name):

        self.site_adress = site_adress
        self.site_name = site_name

    def __repr__(self):

        return '<sites: site_adress=%r; site_name=%r>' % \
        self.site_adress, self.site_name


topics = db.Table('topics',
    db.Column('style_name', db.String(64), primary_key=True),
    db.Column('block_name', db.String(64), primary_key=True),
    db.Column('block_type', db.String(64), primary_key=True),
    db.Column('topic_name', db.String(64), db.ForeignKey('topic_analitycs.topic_name'), primary_key=True),
    db.ForeignKeyConstraint(('style_name', 'block_name', 'block_type'),
                            ('block.style_name', 'block.block_name', 'block.block_type'))
    )



class TopicAnalitycs(db.Model):

    __tablename__ = 'topic_analitycs'
    topic_name = db.Column('topic_name', db.String(64), primary_key=True)
    words = db.Column('words', db.Integer, primary_key=False)
    paragraphs = db.Column('paragraphs', db.Integer, primary_key=False)
    focus_time = db.Column('focus_time', db.Time(64), primary_key=False)
    sentences = db.Column('sentences', db.Integer, primary_key=False)
    images = db.Column('images', db.Float, primary_key=False)

    def __init__(self, topic_name, words, paragraphs, focus_time, sentences, images):

        self.topic_name = topic_name
        self.words = words
        self.paragraphs = paragraphs
        self.focus_time = focus_time
        self.sentences = sentences
        self.images = images

    def __repr__(self):

        return '<topic_analitycs: topic_name=%r; words=%r; paragraphs=%r; focus_time=%r; sentences=%r; sentences=%r; images=%r>' % \
        self.topic_name, self.words, self.paragraphs, self.focus_time, self.sentences, self.images


class Block(db.Model):

    __tablename__ = 'block'
    style_name = db.Column('style_name', db.String(64), db.ForeignKey('styles.style_name'), primary_key=True)
    block_name = db.Column('block_name', db.String(64), primary_key=True)
    block_type = db.Column('block_type', db.String(64), primary_key=True)
    code = db.Column('code', db.String(64), primary_key=False)
    source = db.Column('source', db.String(64), primary_key=False)
    topics = db.relationship('TopicAnalitycs', secondary=topics, lazy='subquery',
        backref=db.backref('blocks', lazy=True))

    def __init__(self, style_name, block_name, block_type, code, source):

        self.style_name = style_name
        self.block_name = block_name
        self.block_type = block_type
        self.code = code
        self.source = source

    def __repr__(self):

        return '<block: style_name=%r; block_name=%r; block_type=%r; code=%r; source=%r; sentences=%r>' % \
        self.style_name, self.block_name, self.block_type, self.code, self.source

