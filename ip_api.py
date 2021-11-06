import requests #requests module allows us to send HTTP requests using Python

ip = requests.get('https://api.ipify.org').content.decode('utf8') #getting the ip adress using api.ipify api

parsed_data = requests.get(f'https://ipapi.co/{ip}/json/').json() #using ipapi.co for the geolocation of the IP address

geolocation = ["IP Address: ", "Version: ", "City: ", "Region: ", "Country: ", "Internet Service Provider: ", "Autonomous System Lookup: "] #array for the names for geolocation
json_data = ["ip", "version", "city", "region", "country_name", "org", "asn"] #array for label for the json data

for i in range(len(geolocation)):
    print(geolocation[i] + parsed_data[json_data[i]]) #printing the geolocation and the parsed data