import tkinter as tk
from tkinter import messagebox
from calculator import SavingsCalculator
from font_manager import FontManager
from widgets import CustomButton, CustomLabel, CustomEntry, CustomDropdown


class App:
    def __init__(self, master):
        self.main_frame = None
        self.widgets = None
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

        self.widgets = {
            "title_label": CustomLabel(self.main_frame, bold.get_font()),
            "amount_label": CustomLabel(self.main_frame, normal.get_font()),
            "amount_entry": CustomEntry(self.main_frame, normal.get_font()),
            "percentage_label": CustomLabel(self.main_frame, normal.get_font()),
            "percentage_entry": CustomEntry(self.main_frame, normal.get_font()),
            "months_label": CustomLabel(self.main_frame, normal.get_font()),
            "months_dropdown": CustomDropdown(self.main_frame, normal.get_font()),
            "result_label": CustomLabel(self.main_frame, bold.get_font()),
            "calculate_button": CustomButton(self.main_frame, normal.get_font()),
            "reset_button": CustomButton(self.main_frame, normal.get_font())
        }

        dropdown_values = [str(i) for i in range(1, 13)]

        self.widgets["title_label"].create("Savings Calculator")
        self.widgets["amount_label"].create("Amount: ")
        self.widgets["amount_entry"].create()
        self.widgets["percentage_label"].create("Percent to save: ")
        self.widgets["percentage_entry"].create()
        self.widgets["months_label"].create("Months: ")
        self.widgets["months_dropdown"].create(dropdown_values)
        self.widgets["result_label"].create("You will save: Php 0.00")
        self.widgets["calculate_button"].create("Calculate", self.calculate)
        self.widgets["calculate_button"].green_config()
        self.widgets["reset_button"].create("Reset", self.reset)
        self.widgets["reset_button"].red_config()

    def configure_widgets(self):
        self.widgets["title_label"].grid(row=0, column=0, columnspan=2, pady=10)
        self.widgets["amount_label"].grid(row=1, column=0, padx=5, sticky='e')
        self.widgets["amount_entry"].grid(row=1, column=1, padx=5, sticky='w')
        self.widgets["percentage_label"].grid(row=2, column=0, padx=5, sticky='e')
        self.widgets["percentage_entry"].grid(row=2, column=1, padx=5, sticky='w')
        self.widgets["months_label"].grid(row=3, column=0, padx=5, sticky='e')
        self.widgets["months_dropdown"].grid(row=3, column=1, padx=5, sticky='w')
        self.widgets["result_label"].grid(row=4, column=0, columnspan=2, pady=2)
        self.widgets["calculate_button"].grid(row=5, column=0, sticky='w')
        self.widgets["reset_button"].grid(row=5, column=1, sticky='e')

        for i in range(6):
            self.main_frame.rowconfigure(i, minsize=50)
            self.main_frame.columnconfigure(0, minsize=20)
            self.main_frame.columnconfigure(1, minsize=20)

    def calculate(self):
        try:
            amount = self.validate_input(self.widgets['amount_entry'].get(), "Amount")
            percentage = self.validate_input(self.widgets['percentage_entry'].get(), "Percentage")
            months = int(self.widgets['months_dropdown'].get())
            result = self.savings_calculator.calculate(amount=amount, percentage=percentage, months=months)
            result = round(result, 2)
            self.widgets['result_label'].config(text=f"You will save: Php {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.reset()

    def reset(self):
        self.widgets['amount_entry'].delete(0, "end")
        self.widgets['percentage_entry'].delete(0, "end")
        self.widgets['months_dropdown'].widget.current(0)
        self.widgets['result_label'].config(text="You will save: Php 0.00")

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
