from flask import Blueprint, flash, request, render_template, session, redirect, url_for
from extensions import db
import random
import validators
from . import pricescrap
from serp import search_product
from models import *


views_bp = Blueprint(
    'views', __name__, url_prefix='/')


def home(email=None):
    email = session.get('email')
    global title, price, img, site, userd, url1
    if request.method == 'POST':
        page = request.form
        try:
            if 'traceprice' in page:
                product = Product()
                product.user = User.query.filter_by(email=email).first()
                product.img = request.form['img']
                product.site = request.form['site']
                product.title = request.form['title']
                product.initial_price = float(request.form['price'].replace(',', '')[1:])
                product.desired_price = float(request.form['dprice'])
                product.url = request.form['url']
                if request.form.get("google_product_id", None):
                    product.google_product_id = request.form.get("google_product_id")
                db.session.add(product)
                db.session.commit()
                user = User.query.filter_by(email=email).first()
                notification = Notification()
                notification.message = f"Product {product.title} added successfully."
                notification.user_id = user.id
                notification.product_id = product.id
                db.session.add(notification)
                db.session.commit()
                return redirect(url_for('views.dashboard'))
            else:
                query = page['search']
                results = []

                if not validators.url(query):
                    search_results = search_product(query)[0:5]
                    for search_result in search_results:
                        result = {
                            'site': search_result['source'],
                            'img': search_result['thumbnail'],
                            'title': search_result['title'],
                            'price': search_result['price'],
                            'url': search_result['link'],
                            'google_product_id': search_result['product_id']
                        }
                        results.append(result)

                else:
                    url = query
                    site, title, price, img, url1 = pricescrap.price(url)
                    results.append({
                        'site': site,
                        'title': title,
                        'price': price,
                        'img': img,
                        'url': url1
                    })

            # flash(site)
            # flash(img)
            # flash(title)
            # flash(price)
            # return redirect(url_for('views.home', results=results))
            return render_template("website/newindex.html", results=results)
        except Exception as e:
            print(e)
    elif request.method == 'GET':
        return render_template("website/newindex.html", email=email, results=None)



def dashboard():
    global userd
    try:
        email = session.get('email')
        # con = mysql.connection.cursor()
        # con.execute('select url, site, img , title, initial_price,desired_price,new_price from prod where email="%s";'%(email))
        # rs = con.fetchall()
        user = User.query.filter_by(email=email).first()
        products = Product.query.filter_by(user_id=user.id).all()
        product_details = []
        for product in products:

           product = {
               'url': product.url,
               'site': product.site,
               'img': product.img,
               'title': product.title,
               'initial_price': str(product.initial_price),
               'desired_price': str(product.desired_price),
               'new_price': str(product.new_price),
               'product_id': product.id
           }
           product_details.append(product)


        return render_template("website/dashboard.html", products=products)
    except :
        flash("!Something went wrong , Try Again...")
        return render_template("website/dashboard.html")


views_bp.add_url_rule('home', 'home', home, methods=['GET', 'POST'])
views_bp.add_url_rule('dashboard', 'dashboard', dashboard, methods=['GET', 'POST'])
