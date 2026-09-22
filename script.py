def sum(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("Unable to handle division operation with strings")
    if isinstance(a, list) or isinstance(b, list):
        raise ValueError("Unable to handle division operation with lists")
    return a / b

