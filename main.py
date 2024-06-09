import tkinter as tk
from widgets import (CustomLabel, AmountEntry, PercentageEntry, MonthsDropdown, CalculateButton)
from logic import SavingsCalculator
from utils import FontManager

class App:
    def __init__(self, master):

        # Root Configuration
        self.master = master
        self.font_manager = FontManager("Arial", 12, "normal")
        self.master.geometry("700x400")
        self.master.title("Savings Calculator")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # Widgets
        self.amount_entry = AmountEntry(master, font=self.font_manager.get_font(), fg=self.font_manager.get_color())
        self.percentage_entry = PercentageEntry(master, font=self.font_manager.get_font(), fg=self.font_manager.get_color())
        self.months_dropdown = MonthsDropdown(master)
        self.calculate_button = CalculateButton(master, self.calculate, font=self.font_manager.get_font(), fg=self.font_manager.get_color())
        self.savings_calculator = SavingsCalculator()

        # Labels
        self.title_label = CustomLabel(master, text="Savings Calculator", font=("Arial", 13, "bold"))
        self.amount_label = CustomLabel(master, text="Enter Amount", font=self.font_manager.get_font())
        self.percentage_label = CustomLabel(master, text="Enter Percentage", font=self.font_manager.get_font())
        self.months_label = CustomLabel(master, text="Select Months", font=self.font_manager.get_font())
        self.result_label = CustomLabel(master, text="Result", font=self.font_manager.get_font())

        # Grid Configuration
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.amount_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.amount_entry.grid(row=1, column=1, sticky=tk.E, padx=10, pady=10)
        self.percentage_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        self.percentage_entry.grid(row=2, column=1, sticky=tk.E, padx=10, pady=10)
        self.months_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        self.months_dropdown.grid(row=3, column=1, sticky=tk.E, padx=10, pady=10)
        self.calculate_button.grid(row=4, column=0, columnspan=3, sticky=tk.E+tk.W, padx=10, pady=10)
        self.result_label.grid(row=5, column=0, columnspan=3, sticky=tk.E+tk.W, padx=10, pady=10)

    def calculate(self):
        amount = float(self.amount_entry.get())
        percentage = float(self.percentage_entry.get())
        months = int(self.months_dropdown.get())
        result = self.savings_calculator.calculate(amount, percentage, months)
        self.result_label.config(text=f"Result: {result}")


root = tk.Tk()
app = App(root)
root.mainloop()
