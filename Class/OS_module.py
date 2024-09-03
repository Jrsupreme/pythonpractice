#count items (files & directories) in specified directory
#take directory as input
#display total number of items (both files & directories)
#BONUS: count the number of files and directories separately HINT: use OS module

import os

def item_counter(directory)

directory = input("Insert the directory path: ")

items_count = os.listdir(directory) 

file_count = 0

dir_count = 0

for item in items_count:
    item_path = os.path.join(directory, item) 
    if os.path.isfile(item_path):
        file_count = + 1
    elif os.path.isdir(item_path)
        dir_count = + 1

print(f"The directory '{directory}' contains:")
print(f"{file_count} files")
print(f"{directory_count} directories")