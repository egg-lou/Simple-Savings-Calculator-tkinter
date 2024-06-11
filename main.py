import tkinter as tk
from tkinter import messagebox
from calculator import SavingsCalculator
from font_manager import FontManager
from widgets import CustomButton, CustomLabel, CustomEntry, CustomDropdown


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

        self.title_label = CustomLabel(self.main_frame, bold.get_font())
        self.title_label.create("Savings Calculator")

        self.amount_label = CustomLabel(self.main_frame, normal.get_font())
        self.amount_label.create("Amount: ")

        self.amount_entry = CustomEntry(self.main_frame, normal.get_font())
        self.amount_entry.create()

        self.percentage_label = CustomLabel(self.main_frame, normal.get_font())
        self.percentage_label.create("Percent to save: ")

        self.percentage_entry = CustomEntry(self.main_frame, normal.get_font())
        self.percentage_entry.create()

        self.months_label = CustomLabel(self.main_frame, normal.get_font())
        self.months_label.create("Months: ")

        self.months_dropdown = CustomDropdown(self.main_frame, normal.get_font())
        self.months_dropdown.create(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])

        self.result_label = CustomLabel(self.main_frame, bold.get_font())
        self.result_label.create("You will save: Php 0.00")

        self.calculate_button = CustomButton(self.main_frame,  normal.get_font())
        self.calculate_button.create("Calculate", self.calculate)
        self.calculate_button.green_config()

        self.reset_button = CustomButton(self.main_frame, normal.get_font())
        self.reset_button.create("Reset", self.reset)
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
            amount = self.validate_input(self.amount_entry.get(), "Amount")
            percentage = self.validate_input(self.percentage_entry.get(), "Percentage")
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

    @staticmethod
    def validate_input(input_str, input_name):
        if not input_str.replace('.', '', 1).isdigit():
            raise ValueError(f"{input_name} must be a number and greater than 0.")
        return float(input_str)


root = tk.Tk()
normal = FontManager("Helvetica", 12, "normal")
bold = FontManager("Helvetica", 14, "bold")
root.option_add("Label.Font", normal.get_font())
app = App(root)
root.mainloop()
