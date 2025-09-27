num = int(input("enter the number"))

binary = bin(num)[2:]
empty=""    
for i in binary:
    if i =="0":
        empty+="1"
    else:
        empty+="0"
decimal = int(empty,2)
print(empty)
print(decimal)
     

    
