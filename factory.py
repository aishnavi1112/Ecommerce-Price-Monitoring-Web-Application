import random
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from extensions import db, migrate
# import pricescrap
from apscheduler.schedulers.background import BackgroundScheduler
import os
from dotenv import load_dotenv
from models import *
load_dotenv()

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.environ.get('mysql_user')}:{os.environ.get('mysql_password')}@{os.environ.get('mysql_host')}:3306/{os.environ.get('mysql_db')}"

    print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.secret_key = "name11"

    db.init_app(app)
    migrate.init_app(app, db)

    return app
