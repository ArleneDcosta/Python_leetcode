from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLACHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)

class Owner(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    pets = db.relationship('Pet',backref = 'owner')


class Pet(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer,db.ForeignKey('owner.id'))
#Below represents many to many
#Data gets populated automatically in these tables due to many to many
friendships = db.Table('friendships',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('friend_id', db.Integer, db.ForeignKey('user.id'))
)
#It makes to have different name for backref_name and property name
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    friends = db.relationship('User', secondary='friendships',
        primaryjoin='User.id==friendships.c.user_id',
        secondaryjoin='User.id==friendships.c.friend_id',
        backref=db.backref('friend_of', lazy='dynamic'))



