import pyowm
import .location

def getForecastatCurrentLocation():

    coords = location.getCoords()

    owm = pyowm.OWM('1ee670f6f625062851ef5a24383c88c8')
    forecast = owm.three_hours_forecast_at_coords(coords['location']['lat'], coords['location']['lng']).get_forecast().get_weathers()
    return forecast


def main():
    forecast = getForecastatCurrentLocation()
    for w in forecast:
        print(w.get_temperature(unit='fahrenheit'))


if __name__ == "__main__":
    main()


