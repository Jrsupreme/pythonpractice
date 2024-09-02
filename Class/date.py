#ask user to input the name of their date.
#ask user to input their budget.
#print restaurant menu(from class activity (may or may not neeed adjustment)).
#ask for input for food.
#ask for input for drink.
#ask for input for date's food.
#ask for input for date's drink.
#tell user how much money they have left after they eat and drink.
#user pays bill.
#print how much money left.
#tell user if second date is true or false based on decisions.
import time
from restaurant_menu import food_menu #to keep the script more simple and organized I'm importing the menu.

date = input("Insert the name of your date: ") #ask for the name of the date and stores it in the date variable.
budget = float(input("Insert your budget: $")) #ask for budget and stores it in the budget variable.

def print_menu(menu): #making this into a function allows for manipulation of what and how is being printed while also encapsulating it for cleaner and more readable code. 
    print("\nRestaurant Menu") #\n prints the following in a new line aka a liner breaker.
    for category in menu: #loop through the main dictionaries.
        print(f"\n{category.capitalize()}:") #prints the categories starting with capital letter. 
        for item in menu[category]: #Nested loop, loops through sub dictionaties.
         details=menu[category][item] #Stores item withing a category into the details variable making recalling specific attributes or values from each item simpler.
         print(f"-{item.capitalize()}: {details['description']}  $ {details['price']:.2f} \n Cal: {details['calories']} Vegan: {details['is_vegan']}\n") #prints item name and specified details. :.2f specifies that I want the price to have two decimal places


def order_item(menu, budget): # This function simulates placing an order from a menu, considering the user's budget.
    ordered_items=[] #empty list to store ordered items.
    while True:
        item=input("Enter what you want to order (or type 'done' to finish): ") #ask for item to order and stores item in item variable.
        if item=='done': #If the user types 'done', the loop breaks, and the function ends.
            break 
            for item in menu:
                price=menu[item]["price"] #stores the item's price into the price variable.
                if budget>=price:
                    budget-=price #subtract the price from the budget and update the budget with the result.
                    ordered_items.append(item) #appends the items ordered into the ordered_items list. 
                    print(f"Added {item.capitalize()} to your order. You have ${budget:.2f} left.") #tells user the item they added to their order and how much budget they got left.
                else:
                    print(f"Insufficient funds. You only have ${budget:.2f} left.") #This else statement handles the case where the user's budget is insufficient to purchase an item.
        else:
            print("Item not found on the menu. Choose again or type 'done' to finish.")
    return ordered_items, budget    #tells the function to end, and return the values of the variables budget and ordered_items to the part of the code that called the function.

def pay_the_bill(budget): #Function to encapsulate the cheackout proccess of the date.
    while True: #ensures the loop keep running until criteria is met.
        bill_answer=input("\nDo you agree to pay the bill? (yes/no): ").lower() #saving the user's input into 'bill_answer' also added .lower so that the input is transform into lower case(just in case user input a cap character).
        if bill_answer=="yes":
            print(f"Thank you for your payment. You have ${budget:.2f}.")
            break
        elif bill_answer=="no":
            print("You must agree to pay the bill to continue with the date")
        else:
            print("Invalid answer. Please answer with either 'yes' or 'no'.")

#Start of the date
print(f"\nWelcome to your lovely date with {date}.") #welcome message

time.sleep(3) #added sleep/pause to allow the user to read the welcome message before being presented with the menu.

print("\nLet's start ordering!") #added \n for clearer readability.

time.sleep(2)

print_menu(food_menu) #recalling function to print the menu.

print("\nOrder for yourself:") #Letting the user know who they are ordering for (in this cases themselves)
budget=order_item(food_menu, budget) #This calls the order_item function to allow for the order of items. It updates the budget variable with the remaining balance after the order.

print("\nOrder for your date:") #Letting the user know who they are ordering for (in this case their date)
budget = order_item(food_menu, budget) # Same here as in line 66.

#cheackout stage
pay_the_bill(budget) #Recalling the checkout function to end the date.

