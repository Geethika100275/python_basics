def SumOfDigits():
    number= input("Enter the number")
    digits=list(number)
    total=0
    
    for num in digits:
        total+=int(num)
    return total
print(SumOfDigits())
