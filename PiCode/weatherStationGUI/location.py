import googlemaps
import requests

google = googlemaps.Client('AIzaSyDN9lat99cxgU-39dU6SpJBZPYSMWWcpUQ')

def getCoords():

	coords = google.geolocate()
	return coords

def getCity(coords):
	try:
		g = google.reverse_geocode((coords['location']['lat'], coords['location']['lng']))
		return "{}, {}".format(g[0]['address_components'][2]['long_name'], g[0]['address_components'][4]['long_name'])
	except:
		return 'unknown city'
	

if __name__ == '__main__':
	coords = getCoords()
	print("lat: {}, long: {}, accuracy: {} meters".format(coords['location']['lat'], coords['location']['lng'], coords['accuracy']))
	print(getCity(coords))

