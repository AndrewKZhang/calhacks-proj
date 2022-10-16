class SingleAirlineResult:
    # the origin station code of this flight
    origin_station_code: str

    # the destination station code of this flight
    destination_station_code: str

    # departure time
    departure_time: str

    # arrival time:
    arrival_time: str

    # class of service
    # TODO: should turn this into enumerator
    class_of_service: str

    marketing_carrier_code: str

    operating_carrier_code: str