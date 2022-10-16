from ctypes import Union
from datetime import timedelta
from nntplib import NNTPDataError
from time import strftime, strptime
from typing import NamedTuple
from app.controller.utils import get_data
from app.model.AirlineResult import AirlineResult
from app.model.HotelResult import HotelResult


class TravelInfoResult(NamedTuple):
    """
    The data that is returned from computing
    TravelInfo for a given duration from a date range
    """
    # the Data for the entire AirlineResults
    airline_results: list[list[AirlineResult]]

    # the data for the entire Hotel results in this duration
    hotel_results: list[list[HotelResult]]

    # the data for the combination of lowest hotel and airline result
    min_price: float

    min_airline: AirlineResult

    min_hotel: HotelResult

def calculateTravelInfo(start_date, \
    end_date, duration, start_airport, end_airport):
    # TODO: 1. transform the date objects so that we can loop date range candidates
    start_date = strptime(start_date, "%Y-%M-%D")
    end_date = strptime(end_date, "%Y-%M-%D")
    duration = int(duration)
    airline_results = []
    hotel_results = []
    for start_date in range(start_date, start_date + timedelta(days=duration), timedelta(days=1)):
        start_str = start_date.strftime("%Y-%M-%D")
        end_str = end_date.strftime("%Y-%M-%D")
        airline_results.append(calculateSingleRoundAirInfo(start_str, end_str, start_airport, end_airport))
        # might be wrong because of city format
        hotel_results.append(calculateSingleRoundHotelResult(start_str, end_str, end_airport))
    # TODO: 2. loop through the candidate windows and call the helper methods defined below
    # TODO: 3. Put them together into the ResultPObject defined above
    # TODO: 4. perform analysis and 
    #          alculate the minimum pay of airline 
    #          and the hotel and put them into the object
    # then return it to the entry point
    # TODO: add flags to track if user only wants hotel or airline only
    # Note we only have 20 api calls for free user, upgrade or create another account
    return TravelInfoResult(
        airline_results,
        hotel_results,
        None,
        None
    )

def processAirLineData(object):
    result = []
    flights = {}
    if "data" in object and "flight" in object["data"]:
        flights = object["data"]["flight"]
    for i in range(len(flights)):
        singleAirlineResult = processRoundAirLineData(flights[str(i)])
        result.append(singleAirlineResult)

def processRoundAirLineData(object):
    return None
    
def calculateSingleRoundAirInfo(start_date, end_date, start_airport, end_airport) -> AirlineResult:
    # TODO calculate single round info based on inputs
    # TODO 1. call the api in utils.py
    # TODO 2. correctly populate SingleAirLineResult here in a helper method
    # TODO OR write a helper method in the constructor
    # TODO 3. put them together and returns to the calculateTracelInfo
    itineraryType = "ROUND_TRIP"
    classOfService = "ECONOMY"
    result = processAirLineData(get_data(start_airport, end_airport, start_date, itineraryType, classOfService, end_date))

    return None

def calculateSingleRoundHotelResult(start_date, end_date, city) -> HotelResult:
    # TODO 1. make sure the city is in GeoId format,
    #  either by calling search_location api or find another way
    # TODO 2. call the hotel api in the utils.py
    # TODO 3. populate the HotelResult object and returns it
    return None
