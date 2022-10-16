from re import search
import requests
import json

def format_data(obj):
	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)
	return text

def get_data(sourceAirportCode, destination, date, itineraryType, classOfService, returnDate):
	params = {
		"sourceAirportCode": sourceAirportCode,
		"destinationAirportCode": destination,
		"date": date,
		"itineraryType": itineraryType,
		"sortOrder": 'ML_BEST_VALUE',
		"numAdults": '1',
		"numSeniors": '0',
		"classOfService": classOfService,
		"returnDate": returnDate,
		"currencyCode": 'USD'
	}
	headers = {
		'X-RapidAPI-Key': '59576dae5emshfefac06552d356bp15f4fcjsn870f5cdb3612',
		'X-RapidAPI-Host': 'tripadvisor16.p.rapidapi.com'
	}
	response = requests.get(f"https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights", params=params, headers=headers)
	if response.status_code == 200:
		return format_data(response.json())
	else:
		print(
		f"Hello person, there's a {response.status_code} error with your request")


def get_hotel_data(checkIn, checkOut):
	params = {
		"geoId": '60713',
		"checkIn": checkIn,
		"checkOut": checkOut,
		"pageNumber": '1',
		"currencyCode": 'USD',
		"priceMin": '1'
	}
	headers = {
		'X-RapidAPI-Key': '59576dae5emshfefac06552d356bp15f4fcjsn870f5cdb3612',
		'X-RapidAPI-Host': 'tripadvisor16.p.rapidapi.com'
	}
	response = requests.get(f"https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels", params=params, headers=headers)
	if response.status_code == 200:
		format_data(response.json())
	else:
		print(
		f"Hello person, there's a {response.status_code} error with your request")

def search_location(location):
	params = {"query": location}
	headers = {
		'X-RapidAPI-Key': '59576dae5emshfefac06552d356bp15f4fcjsn870f5cdb3612',
		'X-RapidAPI-Host': 'tripadvisor16.p.rapidapi.com'
	}
	response = requests.get(f"https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchLocation", params=params, headers=headers)
	if response.status_code == 200:
		format_data(response.json())
	else:
		print(
		f"Hello person, there's a {response.status_code} error with your request")

