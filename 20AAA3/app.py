from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__,template_folder="template")

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

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")


app.run()