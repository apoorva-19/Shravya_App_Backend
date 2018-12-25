import os
import psycopg2

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# DATABASE_URL = os.environ['DATABASE_URL']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
#  Heroku database
#  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dxpaploifbkaro:01cff4e4f0f77751bc2044db6d939dbf90f2dec6b61e0b3e6404928a4feb69a4@ec2-54-243-240-104.compute-1.amazonaws.com:5432/d24al1m741r689'
#  Local database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:shravya123@localhost/shravya'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#database for storing words
class Words(db.Model):

    __tablename__ = 'words'

    word = db.Column(db.String(20), primary_key=True)
    recording = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    recorder = db.Column(db.String(45))

    def __init__(self, word):
        self.word = word
        
#database for storing original and parsed shlokas
class Shlokas(db.Model):

    __tablename__ = 'shlokas'

    #Format for shloka id [##(Two character scripture code)##(chapter number)###(Verse number)]
    shloka_id = db.Column(db.String(7), primary_key=True)
    scripture = db.Column(db.String(45))
    chapter = db.Column(db.Integer, default=0)
    verse = db.Column(db.Integer)
    org_shloka = db.Column(db.String(200))
    parsed_shloka =db.Column(db.String(200))

    def __init__(self, shloka_id, scripture, chapter, verse, org_shloka):
        self.shloka_id = shloka_id
        self.scripture = scripture
        self.chapter = chapter
        self.verse = verse
        self.org_shloka = org_shloka