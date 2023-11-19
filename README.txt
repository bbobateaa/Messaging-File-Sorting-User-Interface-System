Messaging File Sorting User Interface System
Helen Chau
helenkachau@gmail.com

The purpose of my program is to allow the user to use a GUI to send messages to any valid user they choose! They must first load a valid dsu file or they can create one before continuing to the GUI messenger. The user must click a recipient before messaging, typing in the chat box without clicking a recipient will not allow the user to send a message since there is no user to send it to. The program also automatically saves all retrieved chats and contacts so the user can just load the profile file they used into the program and see their previous chats. The user can also create a new profile file in the file settings menu but they would have to close the program to log in to another file.

I used tkinkter in my program to make the GUI and created a window pop-up that is raised first above the chat GUI which collects the user file. If the user does not choose any file, then the window pop-up remains, and the user cannot continue to the GUI without loading or creating a file. All usernames also must be unique from other users!

My program also supports deleting contacts but any data with that contact will be erased and cannot be retrieved! When the user is sent a new message from another, the profile module saves it and writes it in their profile file. Messages from others are highlighted in red while the messages from the user are highlighted in green.

How my program is able to send messages to another user is with the dm.send from the DirectMessenger Class I created in ds_messenger.py, it takes the username and password and server as its parameters. Then I use dm.send to send the message that is entered in the widget text box to send to the server and then I display that message in the entry output and the profile for loading. Each time the user clicks on a new recipient, the chat entry is refreshed and loads any messages that match the recipient, if there are none then it will remain empty until the user inputs messages. Overall, this program was quite difficult to implement but using tkinkter widgets helped with implementing the GUI.
