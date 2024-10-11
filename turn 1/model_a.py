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

# calculator_refactored.py

class Calculator:
	def __init__(self, addition, subtraction):
		self.addition = addition
		self.subtraction = subtraction

	def add(self, x, y):
		return self.addition.calculate(x, y)

	def subtract(self, x, y):
		return self.subtraction.calculate(x, y)


# Step 3: Write unit tests

# test_calculator_refactored.py

import pytest
# from calculator_refactored import Calculator
# from operations import Addition, Subtraction

class TestCalculator:

	@pytest.fixture
	def calculator(self):
		return Calculator(Addition(), Subtraction())

	def test_add(self, calculator):
		assert calculator.add(10, 20) == 30

	def test_subtract(self, calculator):
		assert calculator.subtract(30, 20) == 10

if __name__ == "__main__":
	pytest.main()
