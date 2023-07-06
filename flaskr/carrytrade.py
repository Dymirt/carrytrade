from flask import Flask
from flask import render_template
from .forex_data import forex_dict

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template('index.html', forex_dict=forex_dict())