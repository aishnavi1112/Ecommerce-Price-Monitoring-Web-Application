from flask import Blueprint, flash, request, render_template, session, redirect, url_for
from extensions import db
import random
from . import pricescrap
from models import *
product_bp = Blueprint(
    'product', __name__, url_prefix='/product')


def stop_tracking_product():
    product_id = request.args.get("product_id")

    Product.query.filter_by(id=product_id).delete()
    db.session.commit()
    return redirect(url_for('views.dashboard'))


product_bp.add_url_rule('/stop_tracking', 'stop_tracking', stop_tracking_product , methods=['GET', 'POST'])
