import requests

GET_CORDS_URL = "https://www.waze.com/SearchServer/mozi?q={0}&lang=eng&lon=-73.96888732910156%20&lat=40.799981900731964&origin=livemap"
GET_ROUTE_URL = "https://www.waze.com/il-RoutingManager/routingRequest?from=x%3A{0}+y%3A{1}&to=x%3A{2}+y%3A{3}&at=0&returnJSON=true&returnGeometries=true&returnInstructions=true&timeout=60000&nPaths=3&options=AVOID_TRAILS%3At";

class AddressToCordsConverter(object):
    '''A class to hold the object converting addresses to cordinations. '''
    def __init__(self,cords_url):
        self.cords_url = cords_url

    def convert(self,address):
        request_url = self.cords_url.format(address)
        response = requests.get(request_url)
        response_json = response.json()
        response_json = response_json[0]
        return response_json['location']['lon'], response_json['location']['lat']

class CordsToRouteCalculator(object):
    '''A class to hold the object calculating routes according to cordinations '''
    def __init__(self,route_url):
        self.route_url = route_url

    def extract_minutes_from_response(self,route_response):
        results = route_response['results']
        total = 0
        for x in results:
            total += x['crossTime']
        return total / 60

    def get_route_response(self,start_cords,destenation_cords):
        request_url = self.route_url.format(start_cords[0], start_cords[1], destenation_cords[0], destenation_cords[1])
        response = requests.get(request_url)
        response_json = response.json()
        route_response = response_json['alternatives'][0]['response']
        return route_response

    def calculate(self,start_cords,destenation_cords):
        response = self.get_route_response(start_cords,destenation_cords)
        time = self.extract_minutes_from_response(response)
        return time