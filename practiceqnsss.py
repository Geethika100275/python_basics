while True:
    
    print("safe calculator")
    try:
        num=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=num/num2
    except ValueError:
        print("pls enter a valid number")
    except ZeroDivisionError:
        print("number cant be divided by zero")

    
    else:
        print(result)
    
    choice=input("do you want to stop:")
    if choice=="yes":
    
        print("stopped")
        break
