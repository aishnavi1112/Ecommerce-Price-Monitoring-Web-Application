from flask import Blueprint, flash, request, render_template, session, redirect, url_for
from extensions import db
import random
from . import pricescrap
from models import *
user_bp = Blueprint(
    'user', __name__, url_prefix='')


def login():
    try:
        if request.method == 'POST':
            credentials = request.form
            email = credentials['user']
            password = credentials['password']
            if email == "" or password == "":
                flash("!All fields are required")
                return render_template("website/login.html")
            else:
                user = User.query.filter_by(email=email).first()
                if user.email == email and user.password == password:
                    session['email'] = email
                    return redirect(url_for('views.home', email=email))

        elif request.method == 'GET':
            return render_template("website/login.html")
    except Exception as e:
        print("Error while logging in.", e)
    return render_template("website/login.html", error="Invalid Credentials. Please try again.")

def signup():
    try:
        if request.method == 'POST':
            details = request.form
            name = details['name']
            email = details['user']
            password = details['pas']
            cpas = details['cpas']
            mobile = details['mob']
            if name == "" or email == "" or password == "" or cpas == "" or mobile == "" :
                flash("!All fields are required")
                return render_template("website/signup.html")
            else:
                if password != cpas:
                    flash("!Password did not match")
                    return render_template("website/signup.html")
                else:
                    user = User()
                    user.name = name
                    user.email = email
                    user.password = password
                    user.mobile = mobile
                    db.session.add(user)
                    db.session.commit()
                    # cur = mysql.connection.cursor()
                    # rs =cur.execute('insert into user(name,email,password,mobile) values("%s","%s","%s","%s");'%(n,u,p,m))
                    # mysql.connection.commit()
                    return redirect(url_for('user.login'))
        if request.method == 'GET':
            return render_template("website/signup.html")
    except Exception as e:
        print("error", e)
        flash("!Something went wrong , Try Again...")
        return render_template("website/signup.html")


def forgetpass():
    try:
        if request.method == 'POST':
            email = request.form['foremail']
            code = random.randint(111111, 999999)
            pricescrap.forgetpassmail(email, code)
            session['email'] = email
            session['code'] = str(code)
            return render_template("website/newpass.html")
        elif request.method == 'GET':
            return render_template("website/forgetpass.html")
    except :
        flash("!Something went wrong , Try Again...")
        return render_template("website/forgetpass.html")


def profile():

    email = session.get('email')
    try:
        if request.method == 'GET':
            user = User.query.filter_by(email=email).first()

            name, mobile, email = user.name, user.mobile, user.email

            return render_template("website/profile.html", user=name,  mob=mobile , email=email)
        elif request.method == 'POST':
            details = request.form
            n = details['name']
            u = details['user']
            m = details['mob']
            user = User.query.filter_by(email=email).first()
            user.name = n
            user.mobile = m
            user.email = u
            db.session.add(user)
            db.session.commit()
            return render_template("website/profile.html", user=n, email=u, mob=m)
    except :
        flash("!Something went wrong , Try Again...")
        return render_template("website/profile.html", user=name, email=email, mob=mobile)


def newpass():
    try:
        email = session['email']
        code = session['code']
        if request.method == 'POST':
            code1 = request.form['code']
            newp = request.form['pas']
            rnewp = request.form['cpas']
            if code == code1 and newp == rnewp:
                user = User.query.filter_by(email=email).first()
                user.password = newp
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('user.login'))
            else:
                flash("!Something went wrong , Try Again...")
                return render_template("website/newpass.html")
        elif request.method == 'GET':
            return render_template("website/newpass.html")
    except :
        flash("!Something went wrong , Try Again...")
        return redirect(url_for('forgetpass'))




user_bp.add_url_rule('/', 'login', login, methods=['GET', 'POST'])
user_bp.add_url_rule('/signup', 'signup', signup, methods=['GET', 'POST'])
user_bp.add_url_rule('/forgetpass', 'forgetpass', forgetpass, methods=['GET', 'POST'])
user_bp.add_url_rule('/profile', 'profile', profile, methods=['GET', 'POST'])
user_bp.add_url_rule('/profile/newpass', 'newpass', newpass, methods=['GET', 'POST'])
