'''
Module for running gui program
'''
import tkinter as tk
from tkinter import ttk, filedialog, Toplevel, Label
from collections import namedtuple
from ds_messenger import DirectMessenger
from Profile import Profile, Post
from file_class import File


class Body(tk.Frame):
    '''
    Serves as the body for the chat GUI
    '''
    def __init__(self, root, recipient_selected_callback=None):
        '''
        Assigns class attributes
        '''
        tk.Frame.__init__(self, root)
        self.root = root
        self._contacts = [str]
        self._select_callback = recipient_selected_callback
        self._draw()
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the Body instance

    def node_select(self, event):
        '''
        Triggers events when clicked
        '''
        try:
            index = int(self.posts_tree.selection()[0])
            entry = self._contacts[index]
            if self._select_callback is not None:
                self._select_callback(entry)
        except IndexError:
            pass

    def insert_contact(self, contact: str):
        '''
        Inserts contacts and calls _insert_contact_tree
        '''
        self._contacts.append(contact)
        id_num = len(self._contacts) - 1
        if contact is not None:
            self._insert_contact_tree(id_num, contact)

    def _insert_contact_tree(self, id, contact: str):
        '''
        Inserts contacts into contact tree
        '''
        if len(contact) > 25:
            entry = contact[:24] + "..."
        id = self.posts_tree.insert('', id, id, text=contact)

    def insert_user_message(self, message:str):
        '''
        Inserts user message into chat
        '''
        self.entry_editor.insert('end', message + '\n', 'entry-right')

    def insert_contact_message(self, message:str):
        '''
        Inserts contact message into chat
        '''
        self.entry_editor.insert('end', message + '\n', 'entry-left')

    def get_text_entry(self) -> str:
        '''
        Gets text entry
        '''
        return self.message_editor.get('1.0', 'end').rstrip()

    def delete_text_entry(self):
        '''
        Deletes text entry
        '''
        self.message_editor.delete("1.0","end")

    def set_text_entry(self, text:str):
        '''
        Sets text entry
        '''
        self.message_editor.delete(1.0, tk.END)
        self.message_editor.insert(1.0, text)

    def _draw(self):
        '''
        Draws chat gui
        '''
        posts_frame = tk.Frame(master=self, width=250, background="#4F563E")
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP,
                             expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self, background="#4F563E")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        editor_frame = tk.Frame(master=entry_frame, background="#4F563E")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, width=10,
                                background="#4F563E")
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        message_frame = tk.Frame(master=self, background="#4F563E")
        message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        self.message_editor = tk.Text(message_frame, width=0, height=5,
                                      background="#4F563E")
        self.message_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                                 expand=True, padx=0, pady=0)

        self.entry_editor = tk.Text(editor_frame, width=0, height=5)
        self.entry_editor.tag_configure('entry-right', justify='right',
                                        background="#65634F", foreground="white",
                                        font="Arial")
        self.entry_editor.tag_configure('entry-left', justify='left',
                                        background="#B7B099", foreground="#625643",
                                        font="Arial")
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                               expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame,
                                              command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT,
                                    expand=False, padx=0, pady=0)


class Footer(tk.Frame):
    def __init__(self, root, command1, command2, command3, user):
        '''
        Assigns class attributes
        '''
        tk.Frame.__init__(self, root)
        self.root = root
        self.command1 = command1
        self.command2 = command2
        self.command3 = command3
        self.current_contact = user
        self._draw()

    def send_msg(self):
        '''
        Assigns call back to send_msg
        '''
        if self.command1 is not None:
            self.command1()

    def add_contact(self):
        '''
        Assigns call back to add_contact
        '''
        if self.command2 is not None:
            self.command2()

    def delete_contact(self):
        '''
        Assigns call back to delete_contact
        '''
        if self.command3 is not None:
            self.command3()

    def _draw(self):
        '''
        Draws footer buttons
        '''
        save_button = tk.Button(master=self,
                                text="Send",
                                font="Arial",
                                width=8,
                                command=self.send_msg,
                                bg="#A49548")
        # You must implement this.
        # Here you must configure the button to bind its click to
        # the send_click() function.
        add_user = tk.Button(master=self,
                             text="Add Contact",
                             font="Arial",
                             width=8,
                             command=self.add_contact,
                             bg="#A49548")

        delete_user = tk.Button(master=self,
                                text="Delete Contact",
                                font="Arial",
                                width=8,
                                command=self.delete_contact,
                                bg="#A49548")

        delete_user.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6)
        add_user.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6 )
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=6, pady=6)
        self.footer_label = tk.Label(master=self, text=self.current_contact,
                                     font="Arial")
        self.footer_label.pack(fill=tk.BOTH, side=tk.TOP, padx=5, pady=5)

class NewContactDialog(tk.simpledialog.Dialog):
    '''
    Class for New Contact Dialog menu
    '''
    def __init__(self, root, title=None, user=None, pwd=None, server=None):
        '''
        Class attributes
        '''
        self.root = root
        self.server = server
        self.user = user
        self.pwd = pwd
        super().__init__(root, title)

    def body(self, frame):
        '''
        Builds body of new contact
        '''
        self.server_label = tk.Label(frame, width=30, text="DS Server Address", font="Arial")
        self.server_label.pack()
        self.server_entry = tk.Entry(frame, width=30)
        self.server_entry.insert(tk.END, self.server)
        self.server_entry.pack()

        self.username_label = tk.Label(frame, width=30, text="Username", font="Arial")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.insert(tk.END, self.user)
        self.username_entry.pack()

        # You need to implement also the region for the user to enter
        # the Password. The code is similar to the Username you see above
        # but you will want to add self.password_entry['show'] = '*'
        # such that when the user types, the only thing that appears are
        # * symbols.
        #self.password...
        self.password_label = tk.Label(frame, width = 30, text = "Password", font="Arial")
        self.password_label.pack()
        self.password_entry = tk.Entry(frame, width=30)
        self.password_entry['show'] = '*'
        self.password_entry.insert(tk.END, self.pwd)
        self.password_entry.pack()

    def apply(self):
        '''
        Gets username, password, and server
        '''
        self.user = self.username_entry.get()
        self.pwd = self.password_entry.get()
        self.server = self.server_entry.get()

class MainApp(tk.Frame):
    '''
    Class for running main program of GUI
    '''
    def __init__(self, root):
        '''
        Assigns class attributes
        '''
        tk.Frame.__init__(self, root)
        self.root = root
        self.username = None
        self.password = None
        self.server = None
        self.friend_list = None
        self.your_msg = None
        self.friend_msg = None
        self.recipient = None
        self.path = None
        self.pro = Profile()
        self.file = File()
        self.login_page()
        # You must implement this! You must configure and
        # instantiate your DirectMessenger instance after this line.
        #self.direct_messenger = ... continue!

        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the root frame
        self._draw()

    def close(self):
        '''
        Closes login window if success
        '''
        self.login.destroy()
        self.root.deiconify()

    def login_page(self):
        '''
        Creates login page and shows this before gui window
        '''
        self.root.withdraw()
        self.login = Toplevel()
        # set the title
        self.login.title("Login to your Profile")
        self.login.resizable(width=False,
                            height=False)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width = 400
        height = 300

        divide_width = screen_width/2
        divide_height = screen_height/2

        self.login.configure(width=width,
                            height=height,
                            bg="#4F563E")

        x = divide_width - (width/2)
        y = divide_height - (height/2)

        self.login.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.start = Label(self.login,
                        text="Please load or create file to continue",
                        justify=tk.CENTER,
                        font=("Bell Gothic Std Black", 20),
                        bg="#4F563E")

        self.start.place(relheight=0.15,
                    relx=0.1,
                    rely=0.2)

        self.load = tk.Button(self.login,
                        text="Load File",
                        font="Arial",
                        width=8,
                        command=self.load_exist_file,
                        bg="#4F563E")

        self.load.place(relx=0.1,
                        rely=0.55)

        self.create = tk.Button(self.login,
                                text="Create File",
                                font="Arial",
                                width=8,
                                command=self.create_file,
                                bg="#4F563E")
        self.create.place(relx=0.6,
                          rely=0.55)

    def send_message(self):
        '''
        Sends messages to server
        '''
        self.dm = DirectMessenger(self.server, self.username, self.password)
        # You must implement this!
        if self.recipient is not None:
            entry_msg = self.body.get_text_entry()
            self.body.delete_text_entry()
            rec = self.dm.send(entry_msg, self.recipient)
            if rec is True:
                self.body.insert_user_message(entry_msg)
                msg_info = Post(self.username, entry_msg, recipient=self.recipient)
                self.pro.your_msg.append(msg_info)
                self.pro.save_profile(self.path)
            else:
                return False
        else:
            print("recipeint not sleected")

    def add_contact(self):
        '''
        Adds contact to treeview
        '''
        # You must implement this!
        # Hint: check how to use tk.simpledialog.askstring to retrieve
        # the name of the new contact, and then use one of the body
        # methods to add the contact to your contact list)
        user = tk.simpledialog.askstring("Username", "Enter new contact")
        if user not in self.pro.friend_list:
            self.body.insert_contact(user)
            self.pro.friend_list.append(user)
            self.pro.save_profile(self.path)

    def delete_contact(self):
        '''
        Deletes entered contact if matches available ones
        '''
        child_list = []
        if self.recipient is not None:
            for child in self.body.posts_tree.get_children():
                child_list.append([self.body.posts_tree.item(child)["text"], child])
            for del_child in child_list:
                if self.recipient == del_child[0]:
                    self.body.posts_tree.delete(del_child[1])
                    self.body.entry_editor.delete("1.0", "end")
                    self.friend_list.remove(self.recipient)
                    self.pro.save_profile(self.path)

    def recipient_selected(self, recipient):
        '''
        Loads messages etc. if recipient selected
        '''
        all_msg = []
        self.recipient = recipient
        self.body.entry_editor.delete("1.0", "end")
        self.load_file(self.path)
        direct_messages = namedtuple('direct_messages',
                                      'type_sender timestamp message recipient')
        for user_msg in self.your_msg:
            if user_msg['recipient'] == self.recipient:
                all_msg.append(direct_messages(type_sender="user",
                                timestamp=user_msg['timestamp'],
                                message=user_msg['entry'],
                                recipient=user_msg['recipient']))
        for f_msg in self.friend_msg:
            if f_msg['recipient'] == self.recipient:
                all_msg.append(direct_messages(type_sender="contact",
                                timestamp=f_msg['timestamp'],
                                message=f_msg['entry'],
                                recipient=f_msg['recipient']))
        all_msg.sort(key=lambda x: float(x.timestamp))
        for message in all_msg:
            if getattr(message, 'type_sender') == "user":
                self.body.insert_user_message(getattr(message, 'message'))
            elif getattr(message, 'type_sender') == "contact":
                self.body.insert_contact_message(getattr(message, 'message'))
        self.pro.save_profile(self.path)

    def configure_server(self):
        '''
        Configures server account
        '''
        ud = NewContactDialog(self.root, "Configure Account",
                              self.username, self.password, self.server)
        self.username = ud.user
        self.password = ud.pwd
        self.server = ud.server
        self.pro.username = ud.user
        self.pro.password = ud.pwd
        self.pro.dsuserver = ud.server
        # You must implement this!
        # You must configure and instantiate your
        # DirectMessenger instance after this line.
        self.dm = DirectMessenger(self.server, self.username, self.password)
        self.pro.save_profile(self.path)

    def load_exist_file(self):
        '''
        Loading file that exists
        '''
        load = filedialog.askopenfilename(filetypes=[("Dsu file", ".dsu")])
        if len(load) == 0:
            load = None
        if load is not None:
            self.load_file(load)
            child_list = []
            for child in self.body.posts_tree.get_children():
                child_list.append(self.body.posts_tree.item(child)["values"])
            for friend in self.pro.friend_list:
                if friend not in child_list:
                    self.body.insert_contact(friend)
            self.close()
        else:
            quit

    def load_file(self, file):
        '''
        Loading profile of recipient
        '''
        loaded_profile = self.pro.load_profile(file)
        self.username = self.pro.username
        self.password = self.pro.password
        self.friend_list = self.pro.friend_list
        self.your_msg = self.pro.your_msg
        self.friend_msg = self.pro.friend_msg
        self.server = self.pro.dsuserver
        self.path = file

    def check_new(self):
        '''
        Checks for new messages
        '''
        self.dm = DirectMessenger(self.server, self.username, self.password)
        # You must implement this!
        if self.path is not None:
            new_dm = self.dm.retrieve_new()
            if new_dm is not False:
                for new in new_dm:
                    if new.recipient == self.recipient:
                        self.body.insert_contact_message(new.message)
                        msg_info = Post(self.username, new.message, new.timestamp, new.recipient)
                        self.pro.friend_msg.append(msg_info)
            else:
                return False
        self.after(5, self.check_new)

    def create_file(self):
        '''
        Creates a file
        '''
        filename = filedialog.asksaveasfile(filetypes=[("dsu file", ".dsu")])
        if filename is not None:
            username = tk.simpledialog.askstring("Username", "Enter unique username")
            password = tk.simpledialog.askstring("Password", "Enter safe password")
            ip_address = tk.simpledialog.askstring("IP Address", "Enter valid IP address")
            if username is not None and password is not None:
                self.pro.username = username
                self.pro.password = password
                self.pro.dsuserver = ip_address
                self.path = filename.name
                self.server = ip_address
                self.username = username
                self.password = password
                profile = self.pro.save_profile(filename.name)
                if profile is True:
                    self.close()
        else:
            quit

    def save_file(self):
        '''
        Saves file
        '''
        self.pro.save_profile(self.path)

    def delete_file(self):
        '''
        Deletes file
        '''
        filename = filedialog.askopenfile()
        self.file.delete_file(filename.name)

    def _draw(self):
        '''
        Builds menu
        '''
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)

        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='Create Profile',
                              command= self.create_file,
                              background='#717874',
                              foreground='white')
        menu_file.add_command(label="Save Profile",
                              command= self.save_file)
        menu_file.add_command(label='Close Program',
                              background="#AC5F4D",
                              foreground="white",
                              command=self.close)

        settings_file = tk.Menu(menu_bar, background="#A49548")
        menu_bar.add_cascade(menu=settings_file, label='Settings')
        settings_file.add_command(label='Configure DS Server',
                                  command=self.configure_server)

        # The Body and Footer classes must be initialized and
        # packed into the root window.
        self.body = Body(self.root,
                         recipient_selected_callback=self.recipient_selected)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.footer = Footer(self.root, command1=self.send_message,
                              command2=self.add_contact,
                              command3=self.delete_contact,
                              user=self.username)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)


def main_gui():
    '''
    Runs main program of GUI
    '''
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Distributed Social Messenger")

    # This is just an arbitrary starting point. You can change the value
    # around to see how the starting size of the window changes.
    main.geometry("720x480")

    # adding this option removes some legacy behavior with menus that
    # some modern OSes don't support. If you're curious, feel free to comment
    # out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the
    # widgets used in the program. All of the classes that we use,
    # subclass Tk.Frame, since our root frame is main, we initialize
    # the class with it.
    app = MainApp(main)

    # When update is called, we finalize the states of all widgets that
    # have been configured within the root frame. Here, update ensures that
    # we get an accurate width and height reading based on the types of widgets
    # we have used. minsize prevents the root window from resizing too small.
    # Feel free to comment it out and see how the resizing
    # behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    id = main.after(2000, app.check_new)
    print(id)

    # And finally, start up the event loop for the program (you can find
    # more on this in lectures of week 9 and 10).
    main.mainloop()

if __name__ == "__main__":
    main_gui()