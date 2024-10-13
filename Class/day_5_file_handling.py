#read file a file
#print each line of the file with its line number
import os #need function to check if file exist from this module

file = open("/home/ubuntu/python/python_practice/Class/day_5_sample.txt", "r") #take input to make script re-usable
#print(file.read())
 #check if file path exist
line_number = 0 #line count
for line in file:
    line_number +=1
    print(f"{line_number} {line}")


#for line_count, line in enumerate(file, start=1): #itereate line by line
 #line_number +=1 #add 1 per line
 #print(f"{line_number}") #print each line plus a line number
 #print(f"{line_count} {line}")
file.close() #close the file is good practice to close the file after being done with it.
# else:
#     print(f"{fp} does not exist") #if file doesn't exist say so
