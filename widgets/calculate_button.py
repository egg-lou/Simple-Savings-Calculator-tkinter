import tkinter as tk


class CalculateButton(tk.Button):
    def __init__(self, master=None, command=None, **kwargs):
        super().__init__(master, command=command, text="Calculate", **kwargs)
