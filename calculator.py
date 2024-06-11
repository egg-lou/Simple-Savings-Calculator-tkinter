from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def calculate(self, **kwargs):
        pass


class SavingsCalculator(Calculator):
    def calculate(self, **kwargs):
        amount = kwargs.get('amount')
        percentage = kwargs.get('percentage')
        months = kwargs.get('months')

        if amount is None or percentage is None or months is None:
            raise ValueError('Amount, percentage, and months must not be None')

        if amount <= 0:
            raise ValueError('Amount must be greater than 0')
        if not 0 < percentage <= 100:
            raise ValueError('Percentage must be between 0 and 100')
        return amount * (percentage / 100) * months