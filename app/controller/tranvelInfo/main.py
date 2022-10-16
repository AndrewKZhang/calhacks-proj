from ctypes import Union
from nntplib import NNTPDataError
from typing import NamedTuple
from app.controller.utils import get_data
from app.model.AirlineResult import AirlineResult
from app.model.HotelResult import HotelResult
import datetime
from utils import search_location


class TravelInfoResult(NamedTuple):
    """
    The data that is returned from computing
    TravelInfo for a given duration from a date range
    """
    # the Data for the entire AirlineResults
    airline_results: list[AirlineResult]

    # the data for the entire Hotel results in this duration
    hotel_results: list[HotelResult]

    # the data for the combination of lowest hotel and airline result
    min_price: float

    min_airline: AirlineResult

    min_hotel: HotelResult

def calculateTravelInfo(start_date, \
    end_date, duration, start_airport, end_airport):
    # TODO: 1. transform the date objects(assuming that START_DATE and END_DATE are Date
    #          Objects) so that we can loop date range candidates
    # TODO: 2. loop through the candidate windows and call the helper methods defined below
    # TODO: 3. Put them together into the ResultPObject defined above
    # TODO: 4. perform analysis and 
    #          alculate the minimum pay of airline 
    #          and the hotel and put them into the object
    # then return it to the entry point
    # TODO: add flags to track if user only wants hotel or airline only
    # Note we only have 20 api calls for free user, upgrade or create another account



    return TravelInfoResult(
        None,
        None,
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
    returns = []
    result = search_location(city)
    if "data" in result and "0" in result["data"] and "documentId" in result["data"]["0"]:
        GeoId = result["data"]["0"]["documentId"]
    else:
        return None

    # TODO 2. call the hotel api in the utils.py
    hotel_api = get_hotel_data(start_date, end_date)
    datas = {}
    if "data" in hotel_api and "data" in hotel_api["data"]:
        datas = hotel_api["data"]["data"]
    else:
        return None
    for i in range(len(datas)):
        returns.append(hotelHelper(datas[str(i)]))

    # TODO 3. populate the HotelResult object and returns it
    return returns

def hotelHelper(object):
    result = HotelResult()
    result.id = object["id"]
    result.title = object["title"]
    result.primary_info = object["primaryInfo"]
    result.secondary_info = object["secondaryInfo"]
    result.is_sponsored = object["isSponsored"]
    result.provider = object["provider"]
    result.price_detailed = object["priceDetails"]
    result.price_for_display = object["priceForDisplay"]
    return result
