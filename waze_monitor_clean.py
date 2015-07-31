import requests

GET_CORDS_URL = "https://www.waze.com/SearchServer/mozi?q={0}&lang=eng&lon=-73.96888732910156%20&lat=40.799981900731964&origin=livemap"
GET_ROUTE_URL = "https://www.waze.com/il-RoutingManager/routingRequest?from=x%3A{0}+y%3A{1}&to=x%3A{2}+y%3A{3}&at=0&returnJSON=true&returnGeometries=true&returnInstructions=true&timeout=60000&nPaths=3&options=AVOID_TRAILS%3At";
# GET_ROUTE_URL = "https://www.waze.com/RoutingManager/routingRequest?from=x%3a{0}+y%3A{1}&to=x%3A{2}+y%3A{3}&returnJSON=true"

def address_to_cords(address):
    request_url = GET_CORDS_URL.format(address)
    response = requests.get(request_url)
    response_json = response.json()
    # print response_json
    response_json = response_json[0]
    return response_json['location']['lon'], response_json['location']['lat']

def get_route(start_address, end_address):
    start_cords = address_to_cords(start_address)
    print 'start cords:', start_cords
    end_cords = address_to_cords(end_address)
    print 'end cords:', end_cords
    request_url = GET_ROUTE_URL.format(start_cords[0], start_cords[1], end_cords[0], end_cords[1])
    print request_url
    # request_url = "https://www.waze.com/RoutingManager/routingRequest?from=x%3A-73.9922319+y%3A40.7379049&to=x%3A-73.9451895+y%3A40.8134374&at=0&returnJSON=true&returnGeometries=true&returnInstructions=true&timeout=60000&nPaths=3&options=AVOID_TRAILS%3At"
    response = requests.get(request_url)
    response_json = response.json()
    # print response_json
    # if not 'alternatives' in response_json:
    #     print response_json
    #     raise Exception('No alternatives')
    # return response_json['alternatives'][0]['response']
    return response_json['alternatives'][0]['response']

def calc_route_time(route_response):
    results = route_response['results']
    total = 0
    for x in results:
        total += x['crossTime']
    return total / 60

def main():
    # route_response = get_route('122 5th Ave, New York, NY 10011', '2244 Adam Clayton Powell Jr Blvd, New York, NY 10027')
    route_response = get_route('9 Hatmarim Street, Ramat Gan', '8 Hamavdil Street, Ramat Gan, Israel')
    print 'Time (minutes):', calc_route_time(route_response)

if __name__ == '__main__':
    main()
