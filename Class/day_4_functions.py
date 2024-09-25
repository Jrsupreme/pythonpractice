#create a function that converts fahrenheit degree to celcius degrees
#Prompt user to input the temperature in fahrenheit 
#use the fahrenheit to celcius formula to transform the temperature
#print result
# round up the asnwer to .1 decimal place

fahrenheit = float(input("Type in the temperature in fahrenheit: "))

def fahrenheit_to_celcius(fahrenheit):

 celcius = (fahrenheit - 32) * 5 / 9 

 print(f"{fahrenheit} F is {celcius:.1f} C")

fahrenheit_to_celcius(fahrenheit)