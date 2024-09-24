#Print the frist 10 numbers each one in a new line
#add 2 to each number in each line

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(numbers)

# print(*numbers) #wild
#print(*numbers, sep= ", ")

#print(*numbers, sep= "\n")
# #numbers_format = *numbers, sep= "\n"

for number in numbers:
  number*=2
  print(f"{number} * 2 = {number * 2}")
    # #print(*numbers, sep= "\n","2",x) #Trying to figure out how to print the response as seen on the asignment
    
    # #print(numbers_format,"*2=",number)
    # print(numbers_format)
