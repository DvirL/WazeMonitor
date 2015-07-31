from converters import *

def main():
    start_address = '8 Hamavdil Street, Ramat Gan, Israel'
    destenation_address = '9 Hatmarim Street, Ramat Gan'

    address_to_cords_converter = AddressToCordsConverter(GET_CORDS_URL)   

    start_cords = address_to_cords_converter.convert(start_address)
    destenation_cords = address_to_cords_converter.convert(destenation_address)

    cords_to_route_calculator = CordsToRouteCalculator(GET_ROUTE_URL)

    trip_time = cords_to_route_calculator.calculate(start_cords,destenation_cords)
    
    print 'Time (minutes):',trip_time

if __name__ == '__main__':
    main()


