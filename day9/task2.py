def vowels(string):
    vowels="aeiouAEIOU"
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
string=input("Enter a string:")
print("the vowels are",vowels(string))
