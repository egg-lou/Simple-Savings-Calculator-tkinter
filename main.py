import tkinter as tk
from tkinter import messagebox
from widgets import (CustomLabel, CustomEntry, MonthsDropdown, CustomButton)
from logic import SavingsCalculator
from utils import FontManager


class App:
    def __init__(self, master):
        self.master = master
        self.savings_calculator = SavingsCalculator()
        self.configure_master()
        self.create_widgets()
        self.configure_widgets()
        self.pack_widgets()

    def configure_master(self):
        self.master.title("Savings Calculator")
        self.master.geometry("400x200")
        self.master.resizable(False, False)

    def create_widgets(self):
        self.amount_input = tk.Frame(self.master)
        self.percentage_input = tk.Frame(self.master)
        self.months_input = tk.Frame(self.master)
        self.button_frame = tk.Frame(self.master)

        self.title_label = CustomLabel(text="Savings Calculator", font=bold.get_font())
        self.amount_label = CustomLabel(self.amount_input, text="Amount: ", font=normal.get_font())
        self.percentage_label = CustomLabel(self.percentage_input, text="Percent to save: ", font=normal.get_font())
        self.months_label = CustomLabel(self.months_input, text="Months: ", font=normal.get_font())
        self.result_label = CustomLabel(text="", font=bold.get_font())

        self.amount_entry = CustomEntry(self.amount_input)
        self.percentage_entry = CustomEntry(self.percentage_input)
        self.months_dropdown = MonthsDropdown(self.months_input)

        self.calculate_button = CustomButton(self.button_frame, command=self.calculate, text="Calculate")
        self.reset_button = CustomButton(self.button_frame, command=self.reset, text="Reset")

    def configure_widgets(self):
        self.calculate_button.pack(side="right", padx=5)
        self.reset_button.pack(side="right", padx=5)

        self.amount_label.grid(row=0, column=0, padx=5, sticky='e')
        self.amount_entry.grid(row=0, column=1, padx=5, sticky='w')
        self.percentage_label.grid(row=1, column=0, padx=5, sticky='e')
        self.percentage_entry.grid(row=1, column=1, padx=5, sticky='w')
        self.months_label.grid(row=2, column=0, padx=5, sticky='e')
        self.months_dropdown.grid(row=2, column=1, padx=5, sticky='w')

    def pack_widgets(self):
        self.title_label.pack(pady=10)
        self.amount_input.pack(padx=10, pady=5)
        self.percentage_input.pack(padx=10, pady=5)
        self.months_input.pack(padx=10, pady=5)
        self.button_frame.pack(pady=10)

    def calculate(self):
        try:
            amount = float(self.amount_entry.get())
            percentage = float(self.percentage_entry.get())
            months = int(self.months_dropdown.get())
            result = self.savings_calculator.calculate(amount, percentage, months)
            self.result_label.config(text=f"You will save: Php {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.reset()

    def reset(self):
        self.amount_entry.delete(0, "end")
        self.percentage_entry.delete(0, "end")
        self.months_dropdown.set(1)
        self.result_label.config(text="")
        self.amount_entry.focus_set()


root = tk.Tk()
normal = FontManager("Helvetica", 12, "normal")
bold = FontManager("Helvetica", 14, "bold")
root.option_add("Label.Font", normal.get_font())
app = App(root)
root.mainloop()