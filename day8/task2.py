def check_sign(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

num = int(input("Enter a number: "))
check_sign(num)
