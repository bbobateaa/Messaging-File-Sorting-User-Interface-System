import tkinter as tk
from tkinter import messagebox
from file_class import File

class GUIMaker:
    
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your GUI", font=("Arial", 15))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text='Show messagebox', font=('Arial', 13), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show message", font=('Arial', 15), background='#717874')
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get():
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

GUIMaker()