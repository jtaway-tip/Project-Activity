import requests #requests module allows us to send HTTP requests using Python
from flask import Flask, render_template, request

ip = requests.get('https://ip4.seeip.org/').content.decode('utf8') #getting the ip adress using api.ipify api

parsed_data = requests.get(f'https://ipapi.co/{ip}/json/').json() #using ipapi.co for the geolocation of the IP address

ip = parsed_data['ip']
version = parsed_data['version']
city = parsed_data['city']
region = parsed_data['region']
country = parsed_data['country_name']
isp = parsed_data['org']
asn = parsed_data['asn']


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', ip_html = ip, version_html = version, city_html = city, region_html=region, country_html = country, isp_html = isp, asn_html = asn)

@app.route('/', methods=['POST'])
def getvalue():
    ipadd = request.form.get("ipadd")
    data_parsed = requests.get(f'https://ipapi.co/{ipadd}/json/').json()
    
    add = data_parsed['ip']
    versions = data_parsed['version']
    citys = data_parsed['city']
    regions = data_parsed['region']
    countrys = data_parsed['country_name']
    isps = data_parsed['org']
    asns = data_parsed['asn']
    return render_template('results.html', ip_htmls = add, version_htmls = versions, city_htmls = citys, region_htmls = regions, country_htmls = countrys, isp_htmls = isps, asn_htmls = asns)

@app.route('/about')
def about():  
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)