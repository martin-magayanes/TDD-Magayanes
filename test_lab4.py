import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return round(a*b, 2)
        
calc = Calculator("Base Calculator")

@pytest.fixture

def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Change the calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)

    assert True
    
def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True

# Test for Substract Function

def test_lab4_substruct():
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(1.0, 2.5) == -1.5
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-5, -6) == 1
    
# Test for Multiply Function    

def test_lab4_multiply():
    assert calc.multiply(5, 0) == 0
    assert calc.multiply(3.2, 5.6) == 17.92
    assert calc.multiply(-3, 6) == -18
    assert calc.multiply(6.2, -9.4) == -58.28