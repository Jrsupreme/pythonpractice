import requests

print("Hey I got riddles for you!")
print("I got them by difficulty or random how would you like them: ")
answer1 = input("type: difficulty or random ")
if answer1 == random:
    url = "https://riddlie.p.rapidapi.com/api/v1/riddles/random"
elif answer1 == difficulty:
 difficulty = input("select one of the following difficulties: easy, medium or hard:" 
    if difficulty = easy:
        url = "https://riddlie.p.rapidapi.com/api/v1/riddles/bylevel/easy"
    elif difficulty = medium:
        url = 
else: 
    print("Invalid asnwer")
querystring = 
{"flag":"0"}
{'difficultyLevel': 'medium'}
headers = {
	"x-rapidapi-key": "8ccef19d23msh0b552b4b8e8f3d4p1f0d83jsn1dcaa35670f2",
	"x-rapidapi-host": "riddlie.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())