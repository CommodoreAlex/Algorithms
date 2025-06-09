# Tree, very similar to Breadth First Search- no infinite loops with trees, no need to utilize set or remember what we've checked

from os import listdir
from os.path import isfile, join
from collections import deque

# A function to print files under a parameter for a starting file path
def printnames(start_dir):
    search_queue = deque()               # We use deque to keep track of folders to search
    search_queue.append(start_dir)       

    # While the queue is not empty, pop off a folder to look through
    while search_queue:
        dir = search_queue.popleft()

        # Loop through every file and folder in this folder
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                # If it is a file, print out the file
                print(file)
            else:
                # If it is a folder, add it to the queue of folders to search
                search_queue.append(fullpath)

# Calling our function with our parameter
printnames("C:/Users/alexa/Desktop/")
            
