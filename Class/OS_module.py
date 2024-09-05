#count items (files & directories) in specified directory
#take directory as input
#display total number of items (both files & directories)
#BONUS: count the number of files and directories separately HINT: use OS module

import os

def item_counter(): 
    directory = input("Insert full directory path:") #ask for full dir path
    # for item in directory:
    #    len(directory)         #i was trying something and it wasn't working
    # print('item_count')

    items_count = os.listdir(directory)  #get the list of all files and directories in the specified directory.

    #setting up count variables 
    file_count = 0 

    dir_count = 0

    for item in items_count: #iterate trough the directory
        item_path = os.path.join(directory, item)  #combines paths. Appends the items found inside the dir to the end of it's path (so it'll be like saying its within this dir) 
        if os.path.isfile(item_path): #if is a file add 1 to file count 
         file_count += 1 
        elif os.path.isdir(item_path): #if is a directory add 1 to dir count
         dir_count += 1

    print(f"The directory '{directory}' contains:") 
    print(f"{file_count} files")
    print(f"{dir_count} directories")
    
item_counter()