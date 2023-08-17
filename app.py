# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # Mock user database (replace with a real database)
# users = {'username': 'password'}

# @app.route('/')
# def home():
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']

#     if username in users and users[username] == password:
#         return 'Login successful!'
#     else:
#         return 'Login failed. Please try again.'

# # if __name__ == '__main__':
# #     app.run(debug=True)

from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'
