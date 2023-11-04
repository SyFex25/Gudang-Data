from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect, url_for, session
from models import db
app = Flask(__name__)

app.secret_key = 'Gudang_Data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/testing_beth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def display_all():
    return render_template('index.html')