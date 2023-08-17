# from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Mock user database (replace with a real database)
users = {'Crypto User 1': '123456'}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('dashboard'))
    else:
        print('Login failed. Please try again.')
        return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    # User is logged in, show dashboard
    # user_data =
    # return render_template('dashboard.html', user_data=user_data)
    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# @app.route('/')
# def hello_world():
#     return 'Hello, world!'
