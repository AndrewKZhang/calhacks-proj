class HotelResult:

    # the id for this hotel
    id: int

    # the name of the hotel
    title: str

    # the primary info of this hotel
    primary_info: str

    # the secondary info of this hotel
    secondary_info: str

    # this hotel is sponsored in the api
    is_sponsored: bool

    # the provider of this result
    provider: str

    # the price for display of this hotel
    price_for_display: float

    # the detailed pricing of this hotel
    price_detailed: str

    def __init__(self) -> None:
        pass
