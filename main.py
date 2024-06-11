import tkinter as tk
from tkinter import messagebox
from widgets import (MonthsDropdown, CustomButton)
from logic import SavingsCalculator
from utils import FontManager


class App:
    def __init__(self, master):
        self.master = master
        self.savings_calculator = SavingsCalculator()
        self.configure_master()
        self.create_widgets()
        self.configure_widgets()

    def configure_master(self):
        self.master.title("Savings Calculator")
        self.master.geometry("400x320")
        self.master.resizable(False, False)

    def create_widgets(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=10, pady=10)

        self.title_label = tk.Label(self.main_frame, text="Savings Calculator", font=bold.get_font())
        self.amount_label = tk.Label(self.main_frame, text="Amount: ", font=normal.get_font())
        self.amount_entry = tk.Entry(self.main_frame)
        self.percentage_label = tk.Label(self.main_frame, text="Percent to save: ", font=normal.get_font())
        self.percentage_entry = tk.Entry(self.main_frame)
        self.months_label = tk.Label(self.main_frame, text="Months: ", font=normal.get_font())
        self.months_dropdown = MonthsDropdown(self.main_frame)
        self.result_label = tk.Label(self.main_frame, text="You will save: Php 0.00", font=bold.get_font())
        self.calculate_button = CustomButton(self.main_frame, command=self.calculate, text="Calculate", font=normal.get_font())
        self.calculate_button.green_config()
        self.reset_button = CustomButton(self.main_frame, command=self.reset, text="Reset", font=normal.get_font())
        self.reset_button.red_config()

    def configure_widgets(self):
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.amount_label.grid(row=1, column=0, padx=5, sticky='e')
        self.amount_entry.grid(row=1, column=1, padx=5, sticky='w')
        self.percentage_label.grid(row=2, column=0, padx=5, sticky='e')
        self.percentage_entry.grid(row=2, column=1, padx=5, sticky='w')
        self.months_label.grid(row=3, column=0, padx=5, sticky='e')
        self.months_dropdown.grid(row=3, column=1, padx=5, sticky='w')
        self.result_label.grid(row=4, column=0, columnspan=2, pady=2)
        self.calculate_button.grid(row=5, column=0, sticky='w')
        self.reset_button.grid(row=5, column=1, sticky='e')

        for i in range(6):
            self.main_frame.rowconfigure(i, minsize=50)
            self.main_frame.columnconfigure(0, minsize=20)
            self.main_frame.columnconfigure(1, minsize=20)

    def calculate(self):
        try:
            amount_str = self.amount_entry.get()
            if not amount_str.replace('.', '', 1).isdigit():
                raise ValueError("Amount must be a number and greater than 0.")
            amount = float(amount_str)

            percentage_str = self.percentage_entry.get()
            if not percentage_str.replace('.', '', 1).isdigit():
                raise ValueError("Percentage is not a number.")
            percentage = float(percentage_str)

            months = int(self.months_dropdown.get())
            result = self.savings_calculator.calculate(amount=amount, percentage=percentage, months=months)
            result = round(result, 2)
            self.result_label.config(text=f"You will save: Php {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.reset()

    def reset(self):
        self.amount_entry.delete(0, "end")
        self.percentage_entry.delete(0, "end")
        self.months_dropdown.set(1)
        self.result_label.config(text="You will save: Php 0.00")
        self.amount_entry.focus_set()


root = tk.Tk()
normal = FontManager("Helvetica", 12, "normal")
bold = FontManager("Helvetica", 14, "bold")
root.option_add("Label.Font", normal.get_font())
app = App(root)
root.mainloop()
