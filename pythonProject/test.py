import requests, json
import urllib.request
def system(country, continent, dns, dns_type,):
    if dns_type == "https":
        rLocal_server = requests.get(f'https://{dns}/XARY/Database/system.json')
    if dns_type == "http":
        rLocal_server = requests.get(f'http://{dns}/XARY/Database/system.json')
    rXARY_server = requests.get('http://turcotechnology.c1.biz/App/XARY/Database/ethernet.json')
    print ("connected to Turco Technology server for system information")
    with urllib.request.urlopen(rXARY_server) as url:
        main_response = json.loads(url.read())
        country_response = json.loads(main_response['Authorized Country'])
        Country = country_response[f'{country}']
        continent_response = json.loads(main_response['Authorized Continent'])
        Continent = continent_response[f'{continent}']
        bool(Continent)
        bool(Country)
        if Country == True and Continent == True:
            return True
        else:
            return False
        pass