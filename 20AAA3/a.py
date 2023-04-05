from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__,template_folder="template")

@app.route('/')
def afterlogin():
    return render_template('afterlogin.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/paying')
def paying():
    return render_template("paying.html")
app.run()