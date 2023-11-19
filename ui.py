'''
Runs all functions in ui
'''
# ui.py

# Starter code for assignment 2 in ICS 32 Programming
# with Software Libraries in Python

# Replace the following placeholders with your information.

# Helen Chau
# chauh4@uci.edu
# 84334175

# IMPORTS
from pathlib import Path
from Profile import *
from file_class import *
from LastFM import LastFM
from OpenWeather import OpenWeather
from transclude import transclude_msg
import ds_client
from gui import *

# INPUTS
USER_INPUT = """
Please select the following commands:
C - Create a new file
O - Open an existing file
D - Delete a file
R - Read a file
L - View contents of a directory either by search or default
S - Send Messages to other users
Q - Quit Program
Enter command: """

USER_INPUT2 = """
Please select the following commands:
C - Create a new file
O - Open an existing file
E - Edit current file
U - Upload post(s) or bio or both to online server
P - Print specified or all contents of current file
D - Delete a file
R - Read a file
L - View contents of a directory \
either by search or default
S - Send Messages to other users
Q - Quit Program
Enter command: """

FILE_OPTION = """
Enter a file option:
l - print files in directory
r - print all files and subdirectories
f - print files in given directory
s - search for file by keyword
e - search for file by suffix
You can also add multiple options at once like this: \
(r s e)
Enter command: """

EDIT_INPUT = """
Enter what you would like to edit from this profile:

usr - Edit username (This is only for file profile! Not online server profile)
pwd - Edit password (This is only for file profile! Not online server profile)
bio - Edit bio
addpost - add another post
delpost - delete a specifed post by its index
ip - change the IP address of your desired server

You can also add multiple options at once \
and in any order like this: \
(usr pwd addpost delpost bio)
Enter command: """

PRINT_INPUT = """
Enter what you would like to print from this profile:

server - Print server IP address
usr - Print username
pwd- Print password
bio - Print bio
posts - Print all posts
post - Print specific post by post number
all - Print everything in profile

You can also add multiple options at once like this: \
(usr pwd bio post all)
Enter command: """

# COMMAND MESSAGES
COMMAND2 = "\nGreat! Please enter an existing file: "
DIRECTORY = "\nGreat! Please enter an existing directory: "

# EXTRA MESSAGES
PRINT_SUCESS = "Sucess! File has been created."
USER = "Enter a username (spaces automatically removed): "
PASSW = "Enter a password (spaces automatically removed): "
BIO = "Enter a bio or press enter for none: "
POST = "Enter a post: "
SERVER = "Enter a valid IP address for the profile to connect to: "
POST_OPTION = "Would you like to add this post to the server? (Yes or No): "
UPLOAD = "Would you like to upload post or edit your bio? \
(post or bio or both): "
NEW_POST = "Enter a new post: "
OLD_POST = "Choose saved post by id: "
SERVER_OPTION = "post bio both"
NEW_SERVER = "Enter new server \
(WARNING: Data may be erased from previous server): "
UPLOAD_POST = "\nUpload (new post) or (saved post): "
SUFFIX = "Enter suffix to search by: "
SEARCH = "Enter keyword to search by: "
COMMAND_CHECK = "E P U"
CHECKER = "C O"
LOGIN_REMIND = "\nDon't forget your username and password! \
You will need it to login to upload to the server.\n"
NO_BIO = "\nSince you did not enter a bio, \
only your post is getting sent! \
Use the 'E' command to update bio or \
'U' command to upload one."
POST_INDEX = "\nEnter post index number: "
TRAN_OP = "\nWould you like to transclude your message? (Yes or No): "
P_CHOICE = "\nWould you like to add a post? (Yes or No): "
POST_ADD = "Would you like to add this post? (Yes or No): "
BIO_NOPOST = "Successful Bio update but unsuccessful post upload!"
P_NOTFOUND = "Successful bio update but no post found to upload!"

# ERROR MESSAGES
ERROR_INPUT = "ERROR: Invalid input, try again and enter correct input shown"
ERROR_LOGIN = "ERROR: Invalid password or username has already been taken"
ERROR_FORMAT = "ERROR: Did you put the correct input or format instructed?"
ERROR_CHECKER = "ERROR: E and U and P commands \
are only available after opening or creating a file"
ERROR_COMMAND = "ERROR: INVALID COMMAND"
ERROR_POST = "ERROR: Not a valid option (enter 'new post' or 'saved post')"
ERROR_WHITE = "ERROR: You cannot enter just whitespace!"
ERROR_SERVER = "ERROR: You must enter a server!"
ERROR_UPDATE = "\nERROR: Post or bio was not a successful upload/update!"


def start():
    '''
    Starts the main function of ui3.py
    '''
    try:
        # assigned class object
        file = File()
        profile = Profile()
        # set for checking for valid commands
        com_set = ['C', 'O', 'E', 'P', 'D', 'R', 'L']
        # assigned port
        port = 3021
        # checker if C command has ran
        c_check = False
        # takes user input
        command = input(USER_INPUT)
        # checks if command is C or Q
        if command == "C" or "O":
            checker = command
        count = 1
        if command == "Q":
            quit()
        # while loop stops when user enters "Q" for input
        while command != "Q":
            if count == 0:
                # checks if C or O has ran
                if checker == "C" or checker == "O":
                    # outputs second menu if ran
                    command = input(USER_INPUT2)
                else:
                    # outputs first menu otherwise
                    command = input(USER_INPUT)
                    # checks again if user entered C or O
                    if command == "C" or command == "O":
                        checker = command
                count = 1
            # checks if user entered admin mode
            if count == 1:
                # Checks if command matches a command
                if command == "C" and len(command) > 0:
                    command2 = input(DIRECTORY)
                    command2 = command2.replace(" ", "")
                    # checks if user entered input
                    while len(command2) == 0:
                        # keeps asking for input until entered
                        print("ERROR - you must enter a directory")
                        command2 = input(DIRECTORY)
                        command2 = command2.replace(" ", "")
                    if len(command2) > 0:
                        if os.path.exists(command2) is False:
                            raise NotADirectoryError
                            break
                    # assigns directory to path
                    path = command2
                    name = input("Enter a name for your file: ")
                    # checks if user has entered name
                    if file.white_space(name) is False:
                        while file.white_space(name) is False:
                            print("ERROR - you must enter a name")
                            name = input("Enter a name for your file: ")
                    # checks if file user wants to create already exists
                    filechecker = file.file_checker(path, name)
                    if os.path.exists(filechecker) is False:
                        # runs create file
                        port = 3021
                        server = input(SERVER)
                        # checks for white space
                        while file.white_space(server) is False:
                            print("ERROR: you must enter a server!")
                            server = input(SERVER)
                        profile.dsuserver = server.replace(" ", "")
                        user = input(USER)
                        while file.white_space(user) is False:
                            print("ERROR: you must enter a username!")
                            user = input(USER)
                        user = user.replace(" ", "")
                        passw = input(PASSW)
                        while file.white_space(passw) is False:
                            print("ERROR: you must enter a password!")
                            passw = input(PASSW)
                        passw = passw.replace(" ", "")
                        # checks if username and password already exist
                        user_check = ds_client.pass_user(server, port, user, passw)
                        if user_check is True:
                            print(LOGIN_REMIND)
                            # takes bio and post input
                            userbio = input(BIO)
                            # asks user if they want to enter a post
                            p_choice = input(P_CHOICE)
                            if p_choice == "Yes":
                                # asks user if they want to use transclusion
                                tran = input(TRAN_OP)
                                if tran == "Yes" or tran == "yes":
                                    # calls transclude function
                                    post_input = transclude_msg()
                                else:
                                    # if not, then normal post
                                    post_input = input(POST)
                                    # checks for white space in post
                                    while file.white_space(post_input) is False:
                                        print(ERROR_WHITE)
                                        post_input = input(POST)
                            else:
                                post_input = ''
                            # makes post object with input
                            your_post = Post(post_input)
                            profile._posts = []
                            # runs create file after all inputs taken
                            your_file = file.create_file(path, name)
                            profile.username = user
                            profile.password = passw
                            # checks if post and bio have anything
                            if len(userbio) > 0:
                                profile.bio = userbio
                            else:
                                profile.bio = ''
                            if post_input is not False:
                                # adds post if post_input isn't False
                                profile.add_post(your_post)
                                # asks user if they want to upload to server
                                post_option = input(POST_OPTION)
                                if post_option == "Yes" or "yes":
                                    # uploads to server if not just white space
                                    while file.white_space(post_input) is False:
                                        print(ERROR_WHITE)
                                        post_input = input("Enter a post")
                                        # creates post object to
                                        # add to post list
                                    your_post = Post(post_input)
                                    profile._posts = []
                                    profile.add_post(your_post)
                                    # sends to server
                                    if len(userbio) > 0:
                                        sending = ds_client.send(profile.dsuserver, port, user, passw, post_input, userbio)
                                    else:
                                        # sends to server without bio
                                        print(NO_BIO)
                                        sending = ds_client.send(profile.dsuserver, 3021, user, passw, post_input)
                            else:
                                print(ERROR_UPDATE)
                            # saves profile
                            profile.save_profile(your_file)
                            # assigns path to file for E or P commands
                            path = your_file
                            holder = profile.get_posts()
                            # outputs confirmation profile has been created
                            print(f"\nProfile successfully created: ")
                            print(f"{your_file}")
                            print(f"Username: {profile.username}")
                            print(f"Password: {profile.password}")
                            print(f"Bio: {profile.bio}")
                            print(f"Post(s):")
                            for i in holder:
                                print(i)
                            token = ds_client.get_token(profile.dsuserver, port, user, passw, post_input, userbio)
                            if token is not False:
                                print(f"Here is your token: {token}")
                        else:
                            print(ERROR_LOGIN)
                            checker = ''
                    else:
                        # if file exists, then O command is run
                        command = "O"
                        c_check = True
                        command2 = filechecker

                if command == "O":
                    # command for loading profile
                    # if C command has a already exisitng file, then load runs
                    if c_check is False:
                        # if not, then command O takes input
                        command2 = input(COMMAND2)
                    path = command2
                    profile._posts = []
                    # loads profile
                    profile.load_profile(path)
                    # confirmation message that profile is loaded
                    print(f"\n{path} has been loaded!\n")
                    print(f"Server: {profile.dsuserver}")
                    print(f"Username: {profile.username}")
                    print(f"Password: {profile.password}")
                    print(f"Bio: {profile.bio}")
                    print("Post(s):")
                    holder = profile.get_posts()
                    for i in holder:
                        print(i)
                elif (checker == "C" or checker == "O") and command == "E":
                    # checks if command is E
                    print(f"\nActive Profile: {path}")
                    edit = input(EDIT_INPUT)
                    edit = edit.split(" ")
                    # iterates for options
                    for i in edit:
                        # if user enters Q, then quit program
                        if i == "Q":
                            quit()
                        # checks if user entered usr
                        if i == "usr":
                            user_pass = input("Enter new username: ")
                            user_pass = user_pass.replace(" ", "")
                            if len(user_pass) == 0:
                                while len(user_pass) == 0:
                                    print("ERROR: You must enter a username")
                                    user_pass = input("Enter new username: ")
                                    user_pass = user_pass.replace(" ", "")
                            profile.username = user_pass
                            print(f'Username has been updated! {user_pass}\n')
                        # checks if user entered pwd
                        elif i == "pwd":
                            user_pwd = input("Enter new password: ")
                            user_pwd = user_pwd.replace(" ", "")
                            if len(user_pwd) == 0:
                                while len(user_pwd) == 0:
                                    print("ERROR: You must enter a password")
                                    user_pwd = input("Enter new password: ")
                                    user_pwd = user_pwd.replace(" ", "")
                            profile.password = user_pwd
                            print(f'Password has been updated! {user_pwd}\n')
                        # checks if user entered bio
                        elif i == "bio":
                            update_bio = input("Enter new bio: ")
                            while file.white_space(update_bio) is False:
                                print(ERROR_WHITE)
                                update_bio = input("Enter new bio: ")
                            profile.bio = update_bio
                            print(f'Bio has been updated: "{update_bio}"')
                        # checks if user entered addpost
                        elif i == "addpost":
                            # asks user if they want to transclude post
                            tran = input(TRAN_OP)
                            if tran == "Yes" or tran == "yes":
                                # calls transclude function
                                post = transclude_msg()
                            elif tran == "No" or tran == "no":
                                # normal post if no
                                post = input(NEW_POST)
                                # checks for white space
                                while file.white_space(post) is False:
                                    print(ERROR_WHITE)
                                    post = input(NEW_POST)
                            else:
                                print(ERROR_INPUT)
                                post = False
                            if post is not False:
                                # asks user if they would like
                                # to add the finished post
                                post_op = input(POST_ADD)
                                if post_op == "Yes":
                                    # creates post object and
                                    # add it to post lists
                                    your_post = Post(post)
                                    profile.add_post(your_post)
                                    print(f'Post has been added: "{post}"')
                                else:
                                    # discards post if no
                                    print("Post draft discarded!")
                        # checks if user entered delpost
                        elif i == "delpost":
                            id = 0
                            print("Post(s):")
                            if len(profile.get_posts()) > 0:
                                for j in profile.get_posts():
                                    print(f"{id}: {j}")
                                    id += 1
                                num = int(input("Enter post index number: "))
                                # checks if num is less or
                                # greater than post amount
                                if num+1 > len(profile.get_posts()) or num < 0:
                                    print("ERROR: Invalid Index")
                                    raise ValueError
                                else:
                                    print("\nDeleted Post: ", end='')
                                    print(f"{profile.get_posts()[num]}\n")
                                    profile.del_post(num)
                            else:
                                print("There are no posts to delete")
                        elif i == "ip":
                            # asks user for new ip address
                            server = input(NEW_SERVER)
                            while file.white_space(server) is False:
                                print(ERROR_SERVER)
                                server = input(NEW_SERVER)
                                server = server.replace(" ", "")
                            profile.dsuserver = server
                            print(f"Updated server: {profile.dsuserver}\n")
                        else:
                            print(f'{ERROR_INPUT}\nInvalid Input: "{i}"')
                            raise ValueError
                        # saves profile at end of loop
                        profile.save_profile(path)
                elif (checker == "C" or checker == "O") and command == "U":
                    # upload function for uploading to server
                    server = profile.dsuserver
                    upload_option = input(UPLOAD)
                    if upload_option in SERVER_OPTION:
                        # asks user to login
                        print("\nLOGIN:")
                        user = input("Enter valid username: ")
                        passw = input("Enter valid password: ")
                        # checks if user and password are correct
                        usr_check = ds_client.pass_user(server, port, user, passw)
                        if usr_check is True:
                            # prints out confirmation if successful
                            print("\nLogin successful!")
                            if upload_option == "post":
                                # asks user if they like to upload
                                # new post or saved post
                                post_option = input(UPLOAD_POST)
                                if post_option == "new post":
                                    # asks user if they want to use transclude
                                    tran = input(TRAN_OP)
                                    if tran == "Yes" or tran == "yes":
                                        # calls transclude function
                                        post = transclude_msg()
                                    elif tran == "No" or tran == "no":
                                        post = input(NEW_POST)
                                        # checks for white space
                                        while file.white_space(post) is False:
                                            print(ERROR_WHITE)
                                            post = input(NEW_POST)
                                    else:
                                        post = False
                                        print(ERROR_INPUT)
                                    if post is not False:
                                        # asks user if they like
                                        # to upload finished post
                                        post_op = input(POST_ADD)
                                        if post_op == "Yes":
                                            # creates post object
                                            your_post = Post(post)
                                            profile.add_post(your_post)
                                            # sends post to server
                                            sending = ds_client.send(server, port, user, passw, your_post)
                                            # confirmation message
                                            if sending is True:
                                                print(f'Uploaded post: "{your_post}"')
                                            else:
                                                print(ERROR_UPDATE)
                                        else:
                                            # discards post
                                            print("Post draft discarded!")
                                    else:
                                        print(ERROR_UPDATE)
                                elif post_option == "saved post":
                                    # gets user's saved posts in profile
                                    id = 0
                                    print("Post(s):")
                                    if len(profile._posts) > 0:
                                        for j in profile.get_posts():
                                            print(f"{id}: {j}")
                                            id += 1
                                        num = int(input(POST_INDEX))
                                        if num+1 > len(profile._posts) or num < 0:
                                            raise IndexError
                                        post = profile.get_posts()[num]
                                    else:
                                        print("No saved posts. Create one!")
                                        # asks user if they want
                                        # to use transclude
                                        tran = input(TRAN_OP)
                                        if tran == "Yes" or tran == "yes":
                                            # calls transclude function
                                            post = transclude_msg()
                                        elif tran == "No" or tran == "no":
                                            # normal post
                                            post = input(NEW_POST)
                                            while file.white_space(post) is False:
                                                print(ERROR_WHITE)
                                                post = input(NEW_POST)
                                        else:
                                            post = False
                                            print(ERROR_INPUT)
                                        # creates post object and adds it
                                        your_post = Post(post)
                                        profile.add_post(your_post)
                                        profile.save_profile(path)
                                    if post is not False:
                                        # asks user for confirmation
                                        # to add post
                                        post_op = input(POST_ADD)
                                        if post_op == "Yes" or post_op == "yes":
                                            # sends post
                                            sending = ds_client.send(server, port, user, passw, post)
                                            if sending is True:
                                                # confirmation
                                                print(f'Successfully uploaded post: "{post}"')
                                            else:
                                                print(ERROR_UPDATE)
                                        else:
                                            print("Post draft discarded!")
                                    else:
                                        print(ERROR_UPDATE)
                                else:
                                    print(ERROR_POST)

                            elif upload_option == "bio":
                                # uploads bio to server
                                update = input("Enter new bio: ")
                                # checks for white space
                                while file.white_space(update) is False:
                                    print(ERROR_WHITE)
                                    update = input("Enter new bio: ")
                                # sends bio to server
                                sending = ds_client.send(server, port, user, passw, message=None, bio=update)
                                if sending is True:
                                    print(f'Bio has been updated: "{update}"')

                            elif upload_option == "both":
                                # asks user if they want to
                                # upload new post or saved post
                                post_option = input(UPLOAD_POST)
                                if post_option == "new post":
                                    # asks user if they want to use transclude
                                    tran = input(TRAN_OP)
                                    if tran == "Yes" or tran == "yes":
                                        # calls transclude function
                                        post = transclude_msg()
                                    elif tran == "No" or tran == "no":
                                        # normal post
                                        post = input(NEW_POST)
                                        # checks for white space
                                        while file.white_space(post) is False:
                                            print(ERROR_WHITE)
                                            post = input(NEW_POST)
                                    else:
                                        post = False
                                        print(ERROR_INPUT)
                                    if post is not False:
                                        post_op = input(POST_OPTION)
                                        if post_op == "Yes":
                                            # sends post to server
                                            sending_post = ds_client.send(server, port, user, passw, post)
                                            your_post = Post(post)
                                            profile.add_post(your_post)
                                        else:
                                            print("Post draft discarded!")
                                            sending_post = None
                                    else:
                                        sending_post = False
                                    if sending_post is False:
                                        # outputs error msg to user if failed
                                        print("ERROR: Post failed to upload\n")
                                    update = input("Enter new bio: ")
                                    # checks for white space in bio
                                    while file.white_space(update) is False:
                                        print(ERROR_WHITE)
                                        update = input("Enter new bio: ")
                                    # sends bio to server
                                    sending_bio = ds_client.send(server, port, user, passw, message=None, bio=update)
                                    if sending_bio is True and sending_post is True:
                                        # confirmation
                                        print("Successful upload/update!")
                                        print(f'Bio: "{update}")')
                                        print(f'Post: "{your_post}"')
                                    elif sending_bio is True:
                                        # confirmation but tells user
                                        # that post did not upload
                                        print(BIO_NOPOST)
                                        print(f'Bio: {update}')
                                    elif sending_post is None:
                                        pass
                                    else:
                                        print(ERROR_UPDATE)
                                elif post_option == "saved post":
                                    # gets saved posts
                                    id = 0
                                    print("Post(s):")
                                    if len(profile.get_posts()) > 0:
                                        for j in profile.get_posts():
                                            print(f"{id}: {j}")
                                            id += 1
                                        num = int(input(POST_INDEX))
                                        if num+1 > len(profile._posts) or num < 0:
                                            raise IndexError
                                        else:
                                            post = profile.get_posts()[num]
                                    else:
                                        # if no posts, then create one
                                        print("No saved posts. Create one!")
                                        # asks user if they want
                                        # to use transclude
                                        tran = input(TRAN_OP)
                                        if tran == "Yes" or tran == "yes":
                                            # calls transclude function
                                            post = transclude_msg()
                                        elif tran == "No" or tran == "no":
                                            post = input(NEW_POST)
                                            # checks for white space
                                            while file.white_space(post) is False:
                                                print(ERROR_WHITE)
                                                post = input(NEW_POST)
                                        else:
                                            post = False
                                            print(ERROR_INPUT)
                                        # creates post object
                                        your_post = Post(post)
                                        profile.add_post(your_post)
                                        profile.save_profile(path)
                                    if post is not False:
                                        # asks user for confirmation to send post
                                        post_op = input(POST_OPTION)
                                        if post_op == "Yes" or post_op == "yes":
                                            # sends post to server
                                            sending_post = ds_client.send(server, port, user, passw, post)
                                        else:
                                            print("Post draft discarded!")
                                            sending_post = None
                                    else:
                                        sending_post = False
                                    update = input("Enter new bio: ")
                                    # checks for white space
                                    while file.white_space(update) is False:
                                        print(ERROR_WHITE)
                                        update = input("Enter new bio: ")
                                    # sends bio to server
                                    sending_bio = ds_client.send(server, port, user, passw, message=None, bio=update)
                                    if sending_bio is True and sending_post is True:
                                        # confirmation
                                        print("Successful upload/update!")
                                        print(f'Bio: "{update}"')
                                        print(f'Post: "{post}"')
                                    elif sending_bio is True:
                                        # confirmation but lets user know
                                        # that post did not send
                                        print(P_NOTFOUND)
                                        print(f'Bio: {update}')
                                    elif sending_post is None:
                                        pass
                                    else:
                                        print(ERROR_UPDATE)
                                else:
                                    print(ERROR_INPUT)
                            else:
                                print(ERROR_INPUT)
                        else:
                            print(ERROR_LOGIN)
                    else:
                        print(ERROR_INPUT)

                elif (checker == "C" or checker == "O") and command == "P":
                    # checks if command is P
                    printer = input(PRINT_INPUT)
                    printer = printer.split(" ")
                    # iterates for options
                    for i in printer:
                        print()
                        # checks if user entered Q
                        if i == "Q":
                            quit()
                        # checks if user entered usr
                        if i == "usr":
                            print(f"Username: {profile.username}")
                        # checks if user entered pwd
                        elif i == "pwd":
                            print(f"Password: {profile.password}")
                        # checks if user entered bio
                        elif i == "bio":
                            print(f"Bio: {profile.bio}")
                        # checks if user entered posts
                        elif i == "posts":
                            if len(profile._posts) > 0:
                                id = 0
                                print("Posts:")
                                for j in profile.get_posts():
                                    print(f"{id}: {j}")
                                    id += 1
                            else:
                                print("ERROR: There are no posts here")
                        # checks if user entered post
                        elif i == "post":
                            if len(profile._posts) > 0:
                                num = int(input("Enter the post's number: "))
                                if num+1 > len(profile._posts) or num < 0:
                                    print("ERROR: Invalid index")
                                    break
                                else:
                                    print(f"Post {num}:", end=' ')
                                    print(f"{profile.get_posts()[num]}")
                            else:
                                print("ERROR: There are no posts here")
                        elif i == "server":
                            print(f"Server: {profile.dsuserver}")
                        # checks if user entered all
                        elif i == "all":
                            print("Printing all profile contents:")
                            print(f"Server: {profile.dsuserver}")
                            print(f"Username: {profile.username}")
                            print(f"Password: {profile.password}")
                            print(f"Bio: {profile.bio}")
                            print(f"Post(s): {profile._posts}")
                        else:
                            print(f'{ERROR_INPUT}\nInvalid Input: "{i}"')
                            break

                elif command == "D":
                    # checks if command is D
                    command2 = input(COMMAND2)
                    path = command2
                    # deletes file
                    file.delete_file(path)

                elif command == "R":
                    # checks if command is R
                    command2 = input(COMMAND2)
                    path = command2
                    # reads file
                    file.read_file(path)
                elif command == "S":
                    main_gui()

                elif command == "L":
                    # checks if command is L
                    command2 = input(DIRECTORY)
                    dir_check = os.path.isdir(command2)
                    if dir_check is True:
                        l_option = input(FILE_OPTION)
                        p_file = Path(command2).iterdir()
                        r_file = sorted(p_file, key=os.path.isdir)
                        # Checks what user enters for options
                        for i in range(0, len(l_option)):
                            options = l_option[i].split(" ")
                            if options[0] == "l":
                                pass
                            if options[0] == "r":
                                r_file = file.recursive_file(r_file)
                            if options[0] == "f":
                                r_file = file.files(r_file)
                            if options[0] == "s":
                                search_key = input(SEARCH)
                                r_file = file.search(r_file, search_key)
                            if options[0] == "e":
                                suffix_key = input(SUFFIX)
                                r_file = file.suffix(r_file, suffix_key)
                            else:
                                print(f'{ERROR_INPUT}\nInvalid Input: {i}')
                                break
                        # Prints out user's desired files
                        print("Here are your files/directories:")
                        for i in r_file:
                            print(i)
                    else:
                        raise NotADirectoryError
                elif (checker not in CHECKER) and (command in COMMAND_CHECK):
                    print(ERROR_CHECKER)
                else:
                    if command != "Q" and command not in com_set:
                        # checks if user entered invalid command
                        print(ERROR_COMMAND)
                # reassigns count to 0
                count = 0
            else:
                print(ERROR_FORMAT)
    # exceptions
    except FileNotFoundError:
        print("ERROR: This is not a valid file.")
        start()
    except NotADirectoryError:
        print("ERROR: This is not a valid directory.")
        print("Make sure there are no spaces after!")
        start()
    except IndexError:
        print("ERROR: This is not a valid index.")
        start()
    except DsuFileError:
        print("ERROR: This is not a valid Dsu file.")
        start()
    except DsuProfileError:
        print("ERROR: This is not a valid Dsu Profile.")
        start()
    except ValueError:
        print("ERROR: Did you put the correct input or format instructed?")
        start()
    except TypeError:
        print("ERROR: This is not a valid input")
        start()
    except KeyboardInterrupt:
        print("Goodbye! Any changes may have not been saved!")
