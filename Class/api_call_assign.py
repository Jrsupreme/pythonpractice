import requests

print("Hey I got riddles for you!")
print("Would you like a random riddle or the riddle of the day?")
answer1 = input("Type in 'day' or 'random': ").lower()

# Set the correct URL based on the user's choice
if answer1 == 'random':
    url = "https://riddlie.p.rapidapi.com/api/v1/riddles/random"
elif answer1 == 'day':
    url = "https://riddlie.p.rapidapi.com/api/v1/riddles/rod"
else:
    print("Invalid answer, showing a random riddle by default.")
    url = "https://riddlie.p.rapidapi.com/api/v1/riddles/random"

# Set up querystring and headers
querystring = {'flag': '0'}
headers = {
    "x-rapidapi-key": "8ccef19d23msh0b552b4b8e8f3d4p1f0d83jsn1dcaa35670f2",
    "x-rapidapi-host": "riddlie.p.rapidapi.com"
}

# Make the request to the API
response = requests.get(url, headers=headers, params=querystring)

# Get the JSON response
riddle_data = response.json()

# Extract the riddle question and answer
riddle_question = riddle_data.get('riddle')
riddle_answer = riddle_data.get('answer')

# Check for the riddle question and answer
if riddle_question: #Checking if the riddle was pulled from the API 
    print(f"Riddle: {riddle_question}")
else:
    print("Riddle not found.")

if riddle_answer: #checks if riddle answer was pulled
    # Ask the user for their answer
    user_guess = input("Your answer: ").lower() #.lower for consistency

    # Compare user's answer with the correct answer
    if user_guess == riddle_answer.lower():
        print("Congratulations! You got it right!")
    else:
        print(f"That is NOT the correct answer. The correct answer is: {riddle_answer}")
else:
    print("Answer not found.") #if the answer wasn't pulled