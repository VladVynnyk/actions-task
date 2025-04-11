

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    raise ValueError("Cannot divide by zero")
    
def power(a, b):
    return a ** b

def modulo(a, b):
    if b != 0:
        return a % b
    raise ValueError("Cannot modulo by zero")

def floor_division(a, b):
    if b != 0:
        return a // b
    raise ValueError("Cannot floor divide by zero")

def absolute(a):
    return abs(a)
