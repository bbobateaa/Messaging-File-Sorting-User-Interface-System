# file_class.py

# File class code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Helen Chau
# chauh4@uci.edu
# 84334175

from pathlib import Path
from pathlib import PurePosixPath
from Profile import *
import os


class File():
    '''
    File class that provides functions for using files
    or interacting with the file system
    '''
    def __init__(self) -> None:
        pass

    def create_file(self, file, name: str):
        '''
        Creates a dsu file with provided name and directory path
        '''
        # Checks for operating system's use of slash
        slash = ''
        try:
            for i in file:
                if i == "/" or i == "\\":
                    slash = i
            # Puts created file together and outputs namex
            if file.endswith(slash):
                name = file + name + ".dsu"
            else:
                name = file + slash + name + ".dsu"
            # Creates file in directory
            f = open(name, "a")
            return name
        except IndexError:
            "ERROR"

    def delete_file(self, file):
        '''
        Deletes any file ending with .dsu in the given directory path
        '''
        # Deletes files ending with .dsu
        myfile = Path(file)
        if file.endswith(".dsu"):
            myfile.unlink()
            print(f"{file} DELETED")
        else:
            raise DsuFileError

    def read_file(self, file):
        '''
        Reads content of a file that ends with .dsu in the given directory path
        '''
        # Reads user's inputted file
        myfile = Path(file)
        # chcks if file ends with dsu.
        if file.endswith(".dsu"):
            with open(file, "r") as myfile:
                text = myfile.read()
                # checks for text
                if len(text) == 0:
                    print("EMPTY")
                else:
                    print(text.strip())
        else:
            print("ERROR")

    def recursive_file(self, my_file):
        '''
        Sorts files recursively, providing the user
        all the existing directories and subdirectories
        along with all files and subfiles in the
        given main directory path
        '''
        # Sorts all files by file, then directory
        files = sorted([item for item in my_file], key=os.path.isdir)
        your_file = []
        # for loop appends all files that are inside files to your_file
        for file in files:
            your_file.append(file)
            if not file.is_file():
                # if for loop encounters a existing directory or folder
                # it will loop the directory in the recursive function
                r = self.recursive_file(file.iterdir())
                # appends subdirectory files
                for i in r:
                    your_file.append(i)
        # returns files
        return your_file

    def files(self, my_file):
        '''
        Sorts through given directory path and returns only files to the user
        '''
        # this filters system to output only files
        files = (item for item in my_file if item.is_file())
        your_file = []
        for file in files:
            your_file.append(file)
        return your_file

    def search(self, my_file, search):
        '''
        Searches through given directory path with a keyword and returns
        any files that have a keyword match to the user
        '''
        # this searches for files matching user's specific keyword
        your_search = []
        for currentPath in my_file:
            name = PurePosixPath(currentPath).name
            if search in name:
                your_search.append(currentPath)
        return your_search

    def suffix(self, my_file, file_extension):
        '''
        Searches through given directory path by suffix or file extension
        and returns any files that end with the given suffix
        '''
        # this searches for files matching user's specific file type
        your_suffix = []
        for currentPath in my_file:
            suffix = PurePosixPath(currentPath).suffix
            if file_extension in suffix:
                your_suffix.append(currentPath)
        return your_suffix

    def file_checker(self, file, name):
        '''
        Checks if given file already exists in the directory
        '''
        slash = ''
        try:
            for i in file:
                if i == "/" or i == "\\":
                    slash = i
            # Puts created file together and outputs namex
            if file.endswith(slash):
                name = file + name + ".dsu"
            else:
                name = file + slash + name + ".dsu"
            return name
        except IndexError:
            "ERROR"

    def white_space(self, user_input):
        '''
        Checks for just white space in input and if it does,
        it will return False
        '''
        # function checks for white space
        count = 0
        for i in user_input:
            if i == " ":
                count += 1
        if count == len(user_input):
            return False
        else:
            return True
