import os
import json

import flask
from flask import send_from_directory, flash
from flask import Flask, render_template, url_for, redirect, request, session, g
from flask_migrate import Migrate

from models import app, db
from models import Words, Shlokas

Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)