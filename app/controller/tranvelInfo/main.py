from ctypes import Union
from nntplib import NNTPDataError
from typing import NamedTuple
from app.model.AirlineResult import AirlineResult
from app.model.HotelResult import HotelResult


class TravelInfoResult(NamedTuple):
    """
    The data that is returned from computing
    TravelInfo for a given duration from a date range
    """
    # the Data for the entire AirlineResults
    airline_results: Union[AirlineResult]

    # the data for the entire Hotel results in this duration
    hotel_results: Union[HotelResult]

    # the data for the combination of lowest hotel and airline result
    min_price: float

    min_airline: AirlineResult

    min_hotel: HotelResult

def calculateTravelInfo(start_date, \
    end_date, duration, start_airport, end_airport):
    # TODO: 1. transform the date objects so that we can loop date range candidates
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
    
def calculateSingleRoundAirInfo(start_date, end_date, start_airport, end_airport) -> AirlineResult:
    # TODO calculate single round info based on inputs
    # TODO 1. call the api in utils.py
    # TODO 2. correctly populate SingleAirLineResult here in a helper method
    # TODO OR write a helper method in the constructor
    # TODO 3. put them together and returns to the calculateTracelInfo
    return None

def calculateSingleRoundHotelResult(start_date, end_date, city) -> HotelResult:
    # TODO 1. make sure the city is in GeoId format,
    #  either by calling search_location api or find another way
    # TODO 2. call the hotel api in the utils.py
    # TODO 3. populate the HotelResult object and returns it
    return None
