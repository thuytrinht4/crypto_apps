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
    # user_data as a dummy data
    user_data = {
        'username': 'Crypto User 1',
        'user_id': 1,
        'email': 'crypto_user1@gemini_test.com',
        'portfolio': [
            {'cryptocurrency': 'Bitcoin', 'amount_owned': 1.5,
             'current_price': 45000, 'value': 67500},
            {'cryptocurrency': 'Ethereum', 'amount_owned': 5.0,
             'current_price': 3200, 'value': 16000},
            # Add more holdings as needed
        ]
    }
    # return render_template('dashboard.html', user_data=user_data)
    return render_template('dashboard.html', user_data=user_data)


@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# @app.route('/')
# def hello_world():
#     return 'Hello, world!'
