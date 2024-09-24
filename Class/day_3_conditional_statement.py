#check if user input is even or odd number
#take user input
#check if it is odd or even
#if even say input is even 
#if odd say input is odd

user_input = int(input("enter a number: "))

if int(user_input) % 2 == 0: #if the number is diviable by 2 then is even
    print(f"{user_input} is even")
else:
    print(f"{user_input} is odd")  #otherwise is odd