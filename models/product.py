from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from extensions import db


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(1024), nullable=False)
    site = Column(String(256), nullable=False)
    img = Column(String(1024), nullable=False)
    title = Column(String(512), nullable=False)
    initial_price = Column(Float)
    desired_price = Column(Float)
    new_price = Column(Float, default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notifications = db.relationship("Notification", backref="product")
    google_product_id = db.Column(String(256), nullable=True)
