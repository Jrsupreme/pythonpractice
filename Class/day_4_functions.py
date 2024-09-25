#create a function that converts fahrenheit degree to celcius degrees
#Prompt user to input the temperature in fahrenheit 
#use the fahrenheit to celcius formula to transform the temperature
#print result
# round up the asnwer to .1 decimal place

fahrenheit = float(input("Type in the temperature in fahrenheit: ")) #defining user input as a variable and formating the input to be a float since temperature can have a decimal.

def fahrenheit_to_celcius(fahrenheit):

 #celcius = (fahrenheit - 32 * 5 / 9)
 celcius = (fahrenheit - 32) * 5 / 9  #def celcius variable with the formula to convert F to C 

 print(f"{fahrenheit} F is {celcius:.1f} C") #celcius":.1f" to round up answer to one decimal place

fahrenheit_to_celcius(fahrenheit)