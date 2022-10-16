from ctypes import Union
from turtle import st

from app.model.SingleAirLineResult import SingleAirlineResult


class AirlineResult:
    """
    a single result of the airline search:
    round trip only based on the api we are using

    """

    
    # if the length is larger than 0, meaning layovers is happenning
    first_trip: Union[SingleAirlineResult]

    # same as above 
    second_trp: Union[SingleAirlineResult]

    # set based on if the first trip and second is in same airline
    is_roundtrip: bool
    



    def __init__(self) -> None:
        pass

    