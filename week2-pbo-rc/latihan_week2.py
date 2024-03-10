from abc import ABC, abstractmethod
import math

class Calculator:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value
        
    def __sub__(self, other):
        return self.value - other.value
    
    def __imul__(self, other):
        return self.value * other.value
    
    def __truediv__(self, other):
        if other != 0:
            return self.value / other
        else:
            return "Error: Division by zero"

    def __pow__(self, power):
        return self.value ** power

    def log(self):
        return math.log(self.value)


a = Calculator(10)

print(a + 5)
print(a - 3)
print(a * 4)
print(a / 5)
print(a ** 2)
print(a.log())
