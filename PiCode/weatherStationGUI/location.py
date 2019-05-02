import googlemaps
import requests

google = googlemaps.Client('AIzaSyDN9lat99cxgU-39dU6SpJBZPYSMWWcpUQ')

def getCoords():

	coords = google.geolocate()
	return coords

def getCity(coords):
	try:
		g = google.reverse_geocode((coords['location']['lat'], coords['location']['lng']))
		city = ''
		state = ''
		for i in (g[0]['address_components']):
			if i['types'] == ['locality', 'political']:
				city = i['long_name']
			elif i['types'] == ['administrative_area_level_1', 'political']:
				state = i['short_name']
		if not state:
			state = 'unknown state'
		if not city:
			city = 'unknown city'

		return "{}, {}".format(city, state)
	except:
		return 'unknown city'
	

if __name__ == '__main__':
	coords = getCoords()
	print("lat: {}, long: {}, accuracy: {} meters".format(coords['location']['lat'], coords['location']['lng'], coords['accuracy']))
	print(getCity(coords))

