def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", add(a, b))
elif op == "-":
    print("Result =", sub(a, b))
elif op == "*":
    print("Result =", mul(a, b))
elif op == "/":
    print("Result =", div(a, b))
else:
    print("Invalid operator")
