from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from extensions import db


class Notification(db.Model):
    __tablename__ = "notification"
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_read = db.Column(db.Boolean, default=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
