from tkinter import ttk


class MonthsDropdown(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self['values'] = list(range(1, 13))
        self.current(0)
        self.bind('<Delete>', lambda event: "break")
        self.bind('<BackSpace>', lambda event: "break")
