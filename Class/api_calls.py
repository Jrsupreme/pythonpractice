#syntax for api reqeust:
    #request.method(url,params={key:value},args)
     #example: 

import requests

url = "https://livescore6.p.rapidapi.com/v2/search"

querystring = {"Category":"soccer","Query":"chel"}

headers = {
	"x-rapidapi-key": "8ccef19d23msh0b552b4b8e8f3d4p1f0d83jsn1dcaa35670f2",
	"x-rapidapi-host": "livescore6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
raw=response.json()

print(raw.keys())
print(raw.values())
print(raw.items())