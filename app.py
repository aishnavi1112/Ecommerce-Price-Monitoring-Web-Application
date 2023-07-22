from factory import create_app
from controllers.user import user_bp
from controllers.views import views_bp
from controllers.product import product_bp
from controllers.notification import notification_bp
from extensions import db
from apscheduler.schedulers.background import BackgroundScheduler
from controllers import pricescrap
from controllers.jobs import *
app = create_app()

with app.app_context():
    db.create_all()

app.register_blueprint(user_bp)
app.register_blueprint(views_bp)
app.register_blueprint(product_bp)
app.register_blueprint(notification_bp)
# schedule_track(app)
# track_price(app)

#
# @app.route("/", methods=['POST', 'GET'])
# def login():
#     try:
#         if request.method == 'POST':
#             credentials = request.form
#             u = credentials['user']
#             p = credentials['password']
#             if u == "" or p == "" :
#                 flash("!All fields are required")
#                 return render_template("website/login.html")
#             else :
#                 cur = mysql.connection.cursor()
#                 cur.execute('select * from user where email="%s" and password="%s";'%(u, p))
#                 rs = cur.fetchall()
#
#                 if rs[0][3] == u and rs[0][1] == p :
#
#                     session['email'] = u
#                     import pdb; pdb.set_trace()
#                     return redirect(url_for('home',email=userd))
#
#         elif request.method == 'GET':
#             return render_template("website/login.html")
#     except:
#         flash("!Something went wrong , Try Again...")
#         return render_template("website/login.html")
#
#
# @app.route("/signup", methods=['GET', 'POST'])
# def signup():
#     try:
#         if request.method == 'POST':
#             details = request.form
#             n = details['name']
#             u = details['user']
#             p = details['pas']
#             cpas = details['cpas']
#             m = details['mob']
#             if n == "" or u == "" or p == "" or cpas == "" or m == "" :
#                 flash("!All fields are required")
#                 return render_template("website/signup.html")
#             else:
#                 if p != cpas:
#                     flash("!Password did not match")
#                     return render_template("website/signup.html")
#                 else:
#                     cur = mysql.connection.cursor()
#                     rs =cur.execute('insert into user(name,email,password,mobile) values("%s","%s","%s","%s");'%(n,u,p,m))
#                     mysql.connection.commit()
#                     return redirect(url_for('login'))
#         if request.method == 'GET':
#             return render_template("website/signup.html")
#     except Exception as e:
#         print("error",e)
#         flash("!Something went wrong , Try Again...")
#         return render_template("website/signup.html")
#
#
#
# @app.route("/profile", methods=['POST', 'GET'])
# def profile():
#
#     email = session.get('email')
#     try:
#         if request.method == 'GET':
#             cur = mysql.connection.cursor()
#             cur.execute('select name,mobile,email from user where email="%s";'%(email))
#             rs = cur.fetchall()
#
#             name,mobile,email = rs[0]
#
#             return render_template("website/profile.html", user=name,  mob=mobile , email=email,)
#         elif request.method == 'POST':
#             details = request.form
#             n = details['name']
#             u = details['user']
#             m = details['mob']
#             cur = mysql.connection.cursor()
#             cur.execute('update user set name="%s",email="%s",phone="%s" where email="%s" and password="%s";' %(n, u, m, userd, passd))
#             mysql.connection.commit()
#             userd = u
#             return render_template("website/profile.html", user=n, email=u, mob=m)
#     except :
#         flash("!Something went wrong , Try Again...")
#         return render_template("website/profile.html", user=name, email=email, mob=mobile)
#
#
# @app.route("/home", methods=['POST', 'GET'])
# def home():
#
#     email = session.get('email')
#     global title, price, img, site, userd, url1
#     if request.method == 'POST':
#         page = request.form
#         try:
#             url = page['search']
#             url1 = url
#             s, t, p, i, u = pricescrap.price(url)
#             site, title, price, img, url1 = s, t, p, i, u
#             print(s, i, t, p)
#             flash(s)
#             flash(i)
#             flash(t)
#             flash(p)
#             return redirect(url_for('home', url=u))
#
#         except :
#             email = session.get('email')
#             img = request.form['img']
#             site = request.form['site']
#             title = request.form['title']
#             price = request.form['price'][1:].replace(',','')
#             desired_price = request.form['dprice']
#             url = request.args['url']
#
#             con = mysql.connection.cursor()
#             con.execute('insert into prod(title,email,site,url,img,initial_price,desired_price) values("%s","%s","%s","%s","%s","%s","%s")'\
#                         %(title, email, site, url, img,  price, desired_price))
#             mysql.connection.commit()
#             return redirect(url_for('dashboard'))
#             #return redirect(url_for('track_price', site=site1,img=img1,title=title1,price=pr,dprice=dprice))
#     elif request.method == 'GET':
#         return render_template("website/newindex.html",email=email)
#
#
# @app.route("/sites")
# def sites():
#     return render_template("website/sites.html")
#
#
# @app.route("/about")
# def about():
#     return render_template("website/about.html")
#
#
# @app.route("/home/track_price")
# def track_price():
#     site1 = request.args['site']
#     img1 = request.args['img']
#     title1 = request.args['title']
#     price1 = request.args['price']
#     dprice = request.args['dprice']
#     flash(site1)
#     flash(img1)
#     flash(title1)
#     flash(price1)
#     flash(dprice)
#     return render_template("website/track_price.html")
#
#
# @app.route("/dashboard")
# def dashboard():
#     global userd
#     try:
#         email = session.get('email')
#         con = mysql.connection.cursor()
#         con.execute('select url, site, img , title, initial_price,desired_price,new_price from prod where email="%s";'%(email))
#         rs = con.fetchall()
#         products=[]
#
#         for row in rs:
#
#            url,site,img,title,initial_price,desired_price,new_price = row
#            product = {
#                'url':url , 'site':site ,  'img' : img ,'title':title, 'initial_price':initial_price,
#                'desired_price':desired_price,'new_price':new_price
#            }
#            products.append(product)
#         #    import pdb;pdb.set_trace()
#
#         return render_template("website/dashboard.html" ,products=products)
#     except :
#         flash("!Something went wrong , Try Again...")
#         return render_template("website/dashboard.html")
#
#
#
# @app.route("/forgetpass", methods=['POST', 'GET'])
# def forgetpass():
#     try:
#         if request.method == 'POST':
#             email = request.form['foremail']
#             code = random.randint(111111, 999999)
#             pricescrap.forgetpassmail(email, code)
#             session['email'] = email
#             session['code'] = str(code)
#             return redirect(url_for('newpass'))
#         elif request.method == 'GET':
#             return render_template("website/forgetpass.html")
#     except :
#         flash("!Something went wrong , Try Again...")
#         return render_template("website/forgetpass.html")
#
#
# @app.route("/profile/newpass", methods=['POST', 'GET'])
# def newpass():
#     try:
#         email = session['email']
#         code = session['code']
#         if request.method == 'POST':
#             code1 = request.form['code']
#             newp = request.form['pas']
#             rnewp = request.form['cpas']
#             if code == code1 and newp == rnewp:
#                 con = mysql.connection.cursor()
#                 con.execute('update user set password="%s" where email="%s"'%(newp, email))
#                 mysql.connection.commit()
#                 con.close()
#                 return redirect(url_for('login'))
#             else:
#                 flash("!Something went wrong , Try Again...")
#                 return render_template("website/newpass.html")
#         elif request.method == 'GET':
#             return render_template("website/newpass.html")
#     except :
#         flash("!Something went wrong , Try Again...")
#         return redirect(url_for('forgetpass'))
#
#

schd = BackgroundScheduler(daemon=True)
# schd.add_job(schedule_track, 'interval', [app], minutes=180)
# schd.add_job(track_price, 'interval', [app], minutes=180)
# schd.add_job(sendmail, "interval", seconds=10)
schd.start()

#
#
# # if __name__ == "__main__":
# #     app.secret_key = "name11"
# #     # app.run(debug=True)
    