# from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Mock user database (replace with a real database)
users = {'test1': '123456'}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return 'Login successful!'
    else:
        return 'Login failed. Please try again.'

# @app.route('/')
# def hello_world():
#     return 'Hello, world!'
