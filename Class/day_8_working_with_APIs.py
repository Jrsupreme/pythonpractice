#fetch data from api
#display result

import requests
#I noticed that when retrieving data from this api the only thing that changed was the end of the url, so I'm going to store said url as a variable and have the end part of it be defined later on thrugh another variable.
base_url = "https://dad-jokes7.p.rapidapi.com/dad-jokes/" 
#this api can display random jokes or joke of the day, I'll leave up to the user to choose
print("Dad jokes")
print("1. type '1' for random dad jokes")
print("2. type '2' for the dad joke of the day")
print("3. type '3' to exit")
choice = input("type in your choice: ")
if choice == "1":
    joke_type = "random"   
elif choice == "2":
    joke_type = "joke-of-the-day"    
elif choice == "3":
    print("Exiting...")
    exit() #exit if user user choose to exit
else:
    print("invalid choice") #for some error or mispelling handling
    exit() #exit if input is invalid
    

#this function is what determines what we retrieve from the api based on the variable set by the user input
def get_dad_joke(joke_type): 
    #The API url from which we are making the request
    url = f"{base_url}{joke_type}"
    #Our creadentials
    headers = {  
	"x-rapidapi-key": "8ccef19d23msh0b552b4b8e8f3d4p1f0d83jsn1dcaa35670f2",
	"x-rapidapi-host": "dad-jokes7.p.rapidapi.com"
     }
    #Our response
    response = requests.get(url, headers=headers)
    #if the response was succesful return the joke
    if response.status_code == 200:
        joke = response.json()
        return joke
    else: #if the return was not succesful do not return anything 
        print(f"Failed to retrieve joke {response.status_code}")
        return none 
#Get the joke
dad_joke = get_dad_joke(joke_type)

#This if statement will catch any error having to do with the API not returning the joke, therefore only Displaying the joke if retrieval was successful or displaying a "no joke available" other wise.
if dad_joke:
     print(f"Here's your dad joke: {dad_joke["joke"]}")
else:
    print("No joke available")





#response = requests.get(url, headers=headers)

#print(response.json())