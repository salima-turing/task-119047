# Step 1: Break down the monolith and introduce modules

# calculator.py (legacy code)

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


# Step 2: Refactor to use separate modules for operations

# operations.py

class Addition:
    def calculate(self, x, y):
        return x + y


class Subtraction:
    def calculate(self, x, y):
        return x - y


class Multiplication:
    def calculate(self, x, y):
        return x * y


# calculator_refactored.py

class Calculator:
    def __init__(self, addition, subtraction, multiplication):
        self.addition = addition
        self.subtraction = subtraction
        self.multiplication = multiplication

    def add(self, x, y):
        return self.addition.calculate(x, y)

    def subtract(self, x, y):
        return self.subtraction.calculate(x, y)

    def multiply(self, x, y):
        return self.multiplication.calculate(x, y)


# Step 3: Write unit tests

# test_calculator_refactored.py

import pytest


# from calculator_refactored import Calculator
# from operations import Addition, Subtraction

class TestCalculator:

    @pytest.fixture
    def calculator(self):
        return Calculator(Addition(), Subtraction(), Multiplication())

    def test_add(self, calculator):
        assert calculator.add(10, 20) == 30

    def test_subtract(self, calculator):
        assert calculator.subtract(30, 20) == 10

    def test_multiply(self, calculator):
        assert calculator.multiply(10, 20) == 200
        assert calculator.multiply(0, 100) == 0
        assert calculator.multiply(-5, 6) == -30


if __name__ == "__main__":
    pytest.main()
