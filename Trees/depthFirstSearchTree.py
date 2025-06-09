# Depth-first search

from os import listdir
from os.path import isfile, join

# Implementing a tree search with recursion
def printnames(dir):

    # Loop through every file and folder in the current folder
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)

        if isfile(fullpath):
            # If it is a file, print out the name
            print(file)
        else:
            # If it is a folder, call this function recursively on it to look for files and folders
            printnames(fullpath)

# Calling our function with our parameter starting directory
printnames("C:/users/alexa/desktop/")
