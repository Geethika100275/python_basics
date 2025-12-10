# 4. Reverse a Number

# Input: 1234
# Output: 4321
def reverse():
    number=int(input("enter a number:"))
     
    rev=0
    while number>0:
        
       digit=number%10
       rev=rev*10+digit
       number=number//10
    return rev
print(reverse())
    
