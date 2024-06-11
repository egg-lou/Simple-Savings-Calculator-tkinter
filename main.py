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

        widget_classes = {
            "title_label": (CustomLabel, {"text": "Savings Calculator"}),
            "amount_label": (CustomLabel, {"text": "Amount: "}),
            "amount_entry": (CustomEntry, {}),
            "percentage_label": (CustomLabel, {"text": "Percent to save: "}),
            "percentage_entry": (CustomEntry, {}),
            "months_label": (CustomLabel, {"text": "Months: "}),
            "months_dropdown": (CustomDropdown, {"values": [str(i) for i in range(1, 13)]}),
            "result_label": (CustomLabel, {"text": "You will save: Php 0.00"}),
            "calculate_button": (CustomButton, {"text": "Calculate", "command": self.calculate}),
            "reset_button": (CustomButton, {"text": "Reset", "command": self.reset})
        }

        self.widgets = {name: cls(self.main_frame,
                                  bold.get_font() if name == "title_label" else normal.get_font()).create(**args)
                        for name, (cls, args) in widget_classes.items()}

    def configure_widgets(self):
        grid_configs = {
            "title_label": {"row": 0, "column": 0, "columnspan": 2, "pady": 10},
            "amount_label": {"row": 1, "column": 0, "padx": 5, "sticky": 'e'},
            "amount_entry": {"row": 1, "column": 1, "padx": 5, "sticky": 'w'},
            "percentage_label": {"row": 2, "column": 0, "padx": 5, "sticky": 'e'},
            "percentage_entry": {"row": 2, "column": 1, "padx": 5, "sticky": 'w'},
            "months_label": {"row": 3, "column": 0, "padx": 5, "sticky": 'e'},
            "months_dropdown": {"row": 3, "column": 1, "padx": 5, "sticky": 'w'},
            "result_label": {"row": 4, "column": 0, "columnspan": 2, "pady": 2},
            "calculate_button": {"row": 5, "column": 0, "sticky": 'w'},
            "reset_button": {"row": 5, "column": 1, "sticky": 'e'}
        }

        for name, config in grid_configs.items():
            self.widgets[name].grid(**config)

        self.widgets['calculate_button'].green_config()
        self.widgets['reset_button'].red_config()

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
        self.widgets['months_dropdown'].current(0)
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
