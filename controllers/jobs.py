from extensions import db
from models import Product, User
from controllers import pricescrap
from flask import current_app
from serp import get_seller_price

def schedule_track(app):
    print("Running track price job....")
    with app.app_context():
        products = Product.query.all()
        if (products):
            links = []
            for product in products:
                links.append(product.url)
                if product.google_product_id:
                    current_price = get_seller_price(product.google_product_id, product.site)
                    product.new_price = current_price
                else:
                    site, title, current_price, img, url = pricescrap.price(product.url)
                    curr_price = current_price[1:].replace(',', '')
                    product.new_price = curr_price
                db.session.add(product)
            db.session.commit()



def track_price(app):
    print("Sending track emails to users.")
    with app.app_context():
        products = Product.query.all()

        if (products):
            for product in products:
                url = product.url
                img = product.img
                user = User.query.get(product.user_id)
                email = user.email
                current_price = product.new_price
                title = product.title
                if product.new_price != product.initial_price:
                    pricescrap.sendupdatemail(url, email, title, current_price)

