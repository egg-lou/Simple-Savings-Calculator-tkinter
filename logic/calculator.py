from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def calculate(self, amount, percentage, months):
        pass