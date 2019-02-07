import os
import json

import flask
from flask import send_from_directory, flash, jsonify
from flask import Flask, render_template, url_for, redirect, request, session, g
from flask_migrate import Migrate

from models import app, db
from models import Words, Shlokas

Migrate(app, db)

#count the number of shlokas in the scripture
@app.route('/', methods=['GET','POST'])
def home():
    number = Shlokas.query.filter_by(scripture = "Bhagvad Gita").distinct(Shlokas.chapter).count()
    return jsonify(number)

#create an api for a list of all shlokas in the db    
@app.route('/shlokas', methods=['GET','POST'])
def display_shlokas():
    shlokas = Shlokas.query.filter_by(scripture="Bhagvad Gita").all()
    return jsonify([i.serialize for i in shlokas])

@app.route('/shloka_number', methods=['GET','POST'])
def number_of_shlokas():
    num_shlokas = Shlokas.query.filter_by(chapter = 1).count()
    print(num_shlokas)
    return jsonify(num_shlokas)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")