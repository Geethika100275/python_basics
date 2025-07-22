def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("Simple Calculator\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation: ")

    a = (int(input("Enter first number: ")))
    b = (int(input("Enter second number: ")))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        if b != 0:
            result = divide(a, b)
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Invalid choice.")
        return

    print(f"Result: {result}")

main()
