# # legacy_calculator.py before refactoring
#
# def calculate(operation, x, y):
#     if operation == 'add':
#         result = x + y
#     elif operation == 'subtract':
#         result = x - y
#     else:
#         raise ValueError("Invalid operation")
#     return result

# legacy_calculator.py after refactoring
class Calculator:
    def __init__(self):
        self.operations = {
            'add': self.add,
            'subtract': self.subtract
        }

    def calculate(self, operation, x, y):
        try:
            return self.operations[operation](x, y)
        except KeyError:
            raise ValueError("Invalid operation")

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

def calculate(operation, x, y):
    calc = Calculator()
    return calc.calculate(operation, x, y)
