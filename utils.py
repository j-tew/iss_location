import requests

# Get the latitude and longitude of the ISS
def get_iss_position() -> dict:
    '''Request the API and return the latitude and longitude position of the ISS.'''
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()
    return data['iss_position']

# Use the Map API to draw map
def get_map() -> str:
    '''Return a string to be used for the source of the map image'''
    position = get_iss_position()
    source = f"https://maps.locationiq.com/v3/staticmap?key=pk.e7e306a47fec92f64bfe2d12ed9f44ba&zoom=4&size=1280x720&markers=icon:large-blue-cutout|{position['latitude']},{position['longitude']}"
    return source

# Get the country the ISS is passing over
def get_country():
    '''Return the name of the country the ISS is passing over'''
    position = get_iss_position()
    data = {
        'key': 'pk.e7e306a47fec92f64bfe2d12ed9f44ba',
        'lat': position['latitude'],
        'lon': position['longitude'],
        'format': 'json',
    }
    response = requests.get("https://us1.locationiq.com/v1/reverse.php", params=data)
    location = response.json()
    try:
        address = location['address']
        return address['country']
    except KeyError:
        return 'Over Water'

# Get a list of crew members on the ISS
def get_crew():
    '''Return a tuple with the size of the crew and list of crew members aboard the ISS'''
    response = requests.get('http://api.open-notify.org/astros.json')
    data = response.json()
    return data['number'], data['people']
