import tkinter as tk


class CustomLabel(tk.Label):
    def __init__(self, master=None, text='', **kwargs):
        kwargs['font'] = kwargs.get('font', ('Arial', 20))
        super().__init__(master, text=text, **kwargs)
