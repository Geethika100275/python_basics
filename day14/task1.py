def recursive_sum(n):
    if n == 1:
        return 1
    else:
       return n + recursive_sum(n - 1)

num = int(input("Enter a number: "))
result = recursive_sum(num)
print(f"Sum from 1 to {num} is  {result}")
