import os
from app.controller.TravelProject import get_data
from flask import Flask, render_template, request
from flask_cors import CORS
from datetime import datetime
from app.config import DevelopmentConfig

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(DevelopmentConfig)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/travel_info/origin/<origin>/destination/<destination>/start_date/<start_date>/end_date/<end_date>")
def travelInfo(origin, destination, start_date, end_date):
    itineraryType = "ROUND_TRIP"
    classOfService = "ECONOMY"
    return get_data(origin, destination, start_date, itineraryType, classOfService, end_date)

