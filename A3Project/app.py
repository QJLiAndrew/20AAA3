from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__, template_folder="template")
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'dkf3sldkjfDF23fLJ3b'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'USER'
    user_name = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return self.user_name

with app.app_context():
    db.create_all()



def add_user(username, email, password):
    print("name: " + username + " email: " + email + " password: " + password)
    new_user = User(user_name=username, email=email, password=password)
    db.session.add(new_user)
    print("session.add() executed")
    db.session.commit()



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/gallary')
def gallary():
    return render_template("gallary.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/afterlogin')
def afterlogin():
    return render_template("afterlogin.html")

@app.route('/api/register', methods=['POST', 'GET'])
def register():
    print("I'm in!")
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        password_confirmation = request.form['confirmPassword']
        if password != password_confirmation:
            return render_template("register.html")
        password_hashed = bcrypt.generate_password_hash(password)
        password_hashed_str = password_hashed.decode('utf-8')
        try:
            add_user(username, email, password_hashed_str)
            return redirect(url_for('login'))
        except exc.IntegrityError:
            return render_template('register.html')
    else:
        return render_template("register.html")

@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print("start login!")
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(user_name=username).first()
        if(not user):
            print("no such user")
            return render_template("login.html")
        elif not bcrypt.check_password_hash(user.password, password):
            print("password incorrect")
            return render_template("login.html")
        else:
            print("successfully logged in")
            session["user"] = username
            return redirect(url_for('afterlogin', username=username))
    else:
        return render_template("login.html")
@app.route("/paying")
def paying():
    return render_template("paying.html")

app.run(host='0.0.0.0', port=81, debug=True)