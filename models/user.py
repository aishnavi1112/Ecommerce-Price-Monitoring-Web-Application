from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from extensions import db
from models.notification import Notification


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(256), nullable=False, unique=True)
    name = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    mobile = Column(String(256), nullable=True)
    products = db.relationship('Product', backref='user')
    notifications = db.relationship('Notification', backref='user')
