# app.py
from waitress import serve
from app import app  # Replace 'app' with the actual name of your Flask app module

serve(app, host='127.0.0.1', port=5000)

from flask import Flask, render_template
from py5paisa import FivePaisaClient
import config


# app.py
def create_app():
    from other_module import some_function
    app = Flask(__name__)
    # Your app setup code here
    return app


app = Flask(__name__)

# Initialize 5paisa client
cred = {
    "APP_NAME": config.APP_NAME,
    "APP_SOURCE": config.APP_SOURCE,
    "USER_ID": config.USER_ID,
    "PASSWORD": config.PASSWORD,
    "USER_KEY": config.USER_KEY,
    "ENCRYPTION_KEY": config.ENCRYPTION_KEY
}

email = {
    "email": config.email
}

passwd = {
    "passwd": config.passwd
}

client = FivePaisaClient(cred=cred)

try:
    client.login()
    print("Login successful")
except Exception as e:
    print(f"Login failed: {e}")

client.get_market_status()

@app.route('/')
def index():
    holdings = client.holdings()
    margin = client.margin()
    positions = client.positions()
    order_book = client.order_book()
    trade_book = client.get_trade_book()
    market_status = client.get_market_status()  # Fetch market status
    return render_template('index.html', holdings=holdings, margin=margin, positions=positions, order_book=order_book, trade_book=trade_book, market_status=market_status)

if __name__ == '__main__':
    app.run(debug=True)
