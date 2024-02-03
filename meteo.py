from geopy.geocoders import Nominatim
import requests
import json

loc = Nominatim(user_agent="Geopy Library")

# entering the location name
getLoc = loc.geocode("4012 Carol avenue Fremont California")

# printing address
print(getLoc.address)
latitude =getLoc.latitude
longitude=getLoc.longitude
# printing latitude and longitude
#print("Latitude = ",latitude , "\n")
#print("Longitude = ",longitude,"\n" )

url= "https://api.meteomatics.com/2024-02-03T13:00:00Z--2024-12-30T13:00:00Z:P1D/t_2m:F/"+str(latitude)+","+str(longitude)+"/json"
#print(url)
username = 'none_raja_sahayu'
password = '3uxV9V9Ec1'
response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    # Print the response content
    #print(response.text)
    json_data=response.text
    #print(json_data)
    data=json.loads(json_data)
    temperature_values = [entry['value'] for entry in data['data'][0]['coordinates'][0]['dates']]
    # Calculate average temperature
    average_temperature = sum(temperature_values) / len(temperature_values)
else:
    print(f"Error: {response.status_code} - {response.text}")
#print(value)

print(average_temperature)

# calling the Nominatim tool and create Nominatim class
url= "https://api.meteomatics.com/2024-02-03T13:00:00Z--2024-12-30T13:00:00Z:P1D/precip_24h:mm/"+str(latitude)+","+str(longitude)+"/json"
#print(url)
username = 'none_raja_sahayu'
password = '3uxV9V9Ec1'
response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    # Print the response content
    #print(response.text)
    json_data=response.text
    #print(json_data)
    data=json.loads(json_data)
    percepitation_values = [entry['value'] for entry in data['data'][0]['coordinates'][0]['dates']]
    # Calculate average temperature
    average_percipitation = sum(percepitation_values) / len(percepitation_values)
else:
    print(f"Error: {response.status_code} - {response.text}")
#print(value)

print(average_percipitation)
