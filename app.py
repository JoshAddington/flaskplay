import os
from flask import Flask, render_template, jsonify, config
from flask.ext.sqlalchemy import SQLAlchemy
from mapper import get_boroughs
#from models import Station, Bike
from stock_scraper import get_data

application = app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)


@app.route("/")
def index():
        return render_template("index.html")

@app.route('/citibike')
def citibike():
        return render_template('citibike-mapbox.html')

@app.route('/boroughs')
def boroughs():
        return jsonify(get_boroughs())

@app.route('/data')
def data():
        return jsonify(get_data())

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
