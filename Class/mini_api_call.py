import requests
#depart date of flight
#list of flights on said date
#duration of flight
url = "https://api.travelpayouts.com/v2/prices/month-matrix"

querystring = {"currency":"usd","show_to_affiliates":"true","origin":"NYC","destination":"LAX", "depart_date":"2024-10-09", }

headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}

response = requests.request("GET", url, headers=headers, params=querystring)

flight_data = response.json()
# print(response.json())

# for item in fight_data:
flight = flight_data['data']

flight[0][depart_date]
