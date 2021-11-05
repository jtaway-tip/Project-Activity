import requests

ip = requests.get('https://api.ipify.org').content.decode('utf8')

parsed_data = requests.get(f'https://ipapi.co/{ip}/json/').json()

geolocation = ["IP Address: ", "Version: ", "City: ", "Region: ", "Country: ", "Internet Service Provider: ", "Autonomous System Lookup: "]
json_data = ["ip", "version", "city", "region", "country_name", "org", "asn"]

for i in range(len(geolocation)):
    print(geolocation[i] + parsed_data[json_data[i]])