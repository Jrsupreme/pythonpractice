import requests
  
  
  
print("Hey I got riddles for you!")
print("Would you like a random riddle or the riddle of the day?")
answer1 = input("type in 'day' or 'random': ").lower()
if answer1 == 'random':
    url = "https://riddlie.p.rapidapi.com/api/v1/riddles/random"
elif answer1 == 'day':
    url = "https://riddlie.p.rapidapi.com/api/v1/riddles/rod"
else:
     print("Invalid asnwer")
       

querystring: {'flag':'0'}

    response = requests.get(url, headers=headers, params=querystring) 
    response.raise_for_status()  # Will raise an HTTPError for bad responses
    riddle_data = response.json()
            
    # Extract the riddle question and answer
    riddle_question = riddle_data.get('riddle')
    riddle_answer = riddle_data.get('answer')
    print("Sorry, could not retrieve the riddle properly.")
    
  
    headers = {
        "x-rapidapi-key": "8ccef19d23msh0b552b4b8e8f3d4p1f0d83jsn1dcaa35670f2",
        "x-rapidapi-host": "riddlie.p.rapidapi.com"
    }
