import tkinter as tk


class CustomButton(tk.Button):
    def __init__(self, master=None, command=None, text='', **kwargs):
        super().__init__(master, command=command, text=text, **kwargs)

    def green_config(self):
        self.config(bg="green", fg="white")

    def red_config(self):
        self.config(bg="red", fg="white")
