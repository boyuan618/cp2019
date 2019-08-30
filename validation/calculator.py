def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def dec2bin(num):
    a = ''
    if num > 1:
        a += dec2bin(num//2)
    return a + str(num%2)
    
