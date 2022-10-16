import os
from flask import Flask, render_template, request
from datetime import datetime

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    
    @app.route('/')

    @app.route("/travel_info/origin/<origin>/destination/<destination>/start_date/<start_date>/end_date/<end_date>")
    def travelInfo(origin, destination, start_date, end_date):

        return {
            "origin": origin,
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date
        }


    return app
