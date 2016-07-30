#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, httplib, re
from geopy.geocoders import Nominatim

def get_lat_and_lon_from_address(address):
    geolocator = Nominatim()
    return geolocator.geocode(address)

if __name__ == '__main__':
    if len(sys.argv)>1:
        address_arg = sys.argv[1]
        lat_and_lon = get_lat_and_lon_from_address(address_arg)
        geoURL = "https://pokevision.com/#/@" + str(lat_and_lon.latitude) + "," + str(lat_and_lon.longitude)
        connection = httplib.HTTPSConnection("pokevision.com")
        connection.request("GET", "/#/@" + str(lat_and_lon.latitude) + "," + str(lat_and_lon.longitude))
        response = connection.getresponse()
        if response and response.status == 200:
            data = response.read()
            connection.close()
            regex = "<option.*?>(.*?)</option>"
            pokemons_list = re.findall(regex, data)
            print(pokemons_list)
        else:
            print("Error getting response from server")
    else:
        print("There are not arguments")