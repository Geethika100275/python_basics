def reverse_num(num):
    reverse=0
    while num > 0 :
         digit=num%10
         reverse=reverse*10+digit
         num//=10
    return reverse
num=(int(input("enter a number:")))
print("the reversed number is " , reverse_num(num))
        
   
