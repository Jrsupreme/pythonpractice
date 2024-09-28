#read file a file
#print each line of the file with its line number
import os #need function to check if file exist from this module

fp = input("input file path: ") #take input to make script re-usable

if os.path.exists(fp): #check if file path exist
    file = open(fp, "rt") #open the file and read txt mode
    line_number = 1 #line count
    for line_number, line in file: #itereate line by line
        line_number +=1 #add 1 per line
        print(f"{line_number} {line}") #print each line plus a line number
    file.close() #close the file is good practice to close the file after being done with it.
else:
    print(f"{fp} does not exist") #if file doesn't exist say so
