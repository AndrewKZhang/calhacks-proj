import imp
import os

from app.controller.utils import get_data
from flask import Flask, render_template, request
from flask_cors import CORS
from datetime import datetime
from app.config import DevelopmentConfig
from app.controller.tranvelInfo import calculateTravelInfo

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(DevelopmentConfig)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/travel_info/<origin>/<destination>/<start_date>/<end_date>/<duration>")
def travelInfo(origin, destination, start_date, end_date, duration):
    itineraryType = "ROUND_TRIP"
    classOfService = "ECONOMY"
    # convert to json
    return calculateTravelInfo(start_date, end_date, duration, origin, destination), 200

