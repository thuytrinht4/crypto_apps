import locale
from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

# Set a temporary secret key for testing
app.secret_key = 'temporary_test_key'

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


@app.template_filter('format_currency')
def format_currency(value, decimal_num=0):
    formatted_value = locale.format_string(
        f"%.{decimal_num}f", value, grouping=True)
    return formatted_value


# Mock user database (replace with a real database)
dummy_users = {
    'Crypto User 1': {'password': '123456'},
    'Crypto User 2': {'password': '123456'},
    # Add more users...
}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    # if username in users and users[username] == password:
    if username in dummy_users and dummy_users[username]['password'] == password:
        session['user_id'] = username  # Store user_id in session
        return redirect(url_for('dashboard'))
    else:
        print('Login failed. Please try again.')
        return redirect(url_for('home'))


@app.route('/dashboard')
def dashboard():
    # User is logged in, show dashboard
    # user_data as a dummy data
    dummy_user_data = {
        'Crypto User 1': {
            'user_name': 'Victor del Rosal',
            'email': 'crypto_user1@gemini_test.com',
            'eft': {
                'etf_name': 'ETF-5',
                'etf_detail': 'Portfolio with Top 5 Cryptocurrencies'},
            'total_fund': 10000,
            'portfolio': [
                {'cryptocurrency': 'Bitcoin', 'amount_owned': 0.2485,
                 'current_price': 26500, 'value': 6585},
                {'cryptocurrency': 'Ethereum', 'amount_owned': 1.5341,
                 'current_price': 1650, 'value': 2531},
                {'cryptocurrency': 'Binance', 'amount_owned': 1.9755,
                 'current_price': 218, 'value': 431},
                {'cryptocurrency': 'Ripple', 'amount_owned': 679,
                 'current_price': 0.5, 'value': 339},
                {'cryptocurrency': 'Cardano', 'amount_owned': 450,
                 'current_price': 0.25, 'value': 114}
                # Add more cryptocurrency data
            ]
        },
        'Crypto User 2': {
            'user_name': 'Tuan Trinh',
            'email': 'crypto_user1@gemini_test.com',
            'eft': {
                'etf_name': 'ETF-2',
                'etf_detail': 'Portfolio with Top 2 Cryptocurrencies'},
            'total_fund': 10000,
            'portfolio': [
                {'cryptocurrency': 'Bitcoin', 'amount_owned': 0.2726,
                 'current_price': 26500, 'value': 7223},
                {'cryptocurrency': 'Ethereum', 'amount_owned': 1.6829,
                 'current_price': 1650, 'value': 2777}
                # Add more cryptocurrency data
            ]
        }
    }
    # Add more users...

    if 'user_id' in session:
        user_id = session['user_id']
        user_data = dummy_user_data.get(user_id)
        if user_data:
            session['total_fund'] = user_data['total_fund']
            return render_template('dashboard.html', user_data=user_data)
        else:
            return "User not found"
    else:
        return redirect(url_for('home'))
    # return render_template('dashboard.html', user_data=user_data)
    # return render_template('dashboard.html', user_data=user_data)


@app.route('/logout')
def logout():
    # Redirect to the desired URL after logout (e.g., home page)
    return redirect(url_for('home'))

# @app.route('/')
# def hello_world():
#     return 'Hello, world!'


if __name__ == '__main__':
    app.run(debug=True)
