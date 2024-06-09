from .calculator import Calculator


class SavingsCalculator(Calculator):
    def calculate(self, amount, percentage, months):
        if amount <= 0:
            raise ValueError('Amount must be greater than 0')
        if not 0 <= percentage <= 100:
            raise ValueError('Percentage must be between 0 and 100')
        return amount * (percentage / 100) * months
    