import tkinter as tk
from tkinter import ttk


class BaseWidget:
    def __init__(self, master, font, **kwargs):
        self.widget = None
        self.master = master
        self.kwargs = kwargs
        self.font = font

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def grid(self, **kwargs):
        self.widget.grid(**kwargs)

    def config(self, **kwargs):
        self.widget.config(**kwargs)


class CustomLabel(BaseWidget):
    def create(self, text):
        self.widget = tk.Label(self.master, text=text, font=self.font, **self.kwargs)


class CustomEntry(BaseWidget):
    def create(self):
        self.widget = tk.Entry(self.master, font=self.font, **self.kwargs)

    def get(self):
        return self.widget.get()

    def delete(self, start, end):
        self.widget.delete(start, end)

    def insert(self, index, string):
        self.widget.insert(index, string)


class CustomButton(BaseWidget):
    def create(self, text, command):
        self.widget = tk.Button(self.master, text=text, font=self.font, command=command, **self.kwargs)

    def green_config(self):
        self.config(bg="green", fg="white")

    def red_config(self):
        self.config(bg="red", fg="white")


class CustomDropdown(BaseWidget):
    def create(self, values):
        self.widget = ttk.Combobox(self.master, values=values, font=self.font, **self.kwargs)
        self.widget.current(0)
        self.widget.bind('<Delete>', lambda event: "break")
        self.widget.bind('<BackSpace>', lambda event: "break")

    def get(self):
        return self.widget.get()

    def set(self, index):
        self.widget.set(index)
