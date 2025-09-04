def sum_natural(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

num = int(input("Enter a number: "))
print("Sum of first", num, "natural numbers is:", sum_natural(num))
