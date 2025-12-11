name=input("enter a word:")
reverse_word=""
for char in name:
    reverse_word=char+reverse_word
if reverse_word==name:
        print("the string is palindrome")
else:
    print("not palindrome")
