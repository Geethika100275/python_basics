def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome_substring(string):
    n = len(string)
    longest = ""
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest

user_input = input("Enter a string: ")
result = longest_palindrome_substring(user_input)

if result:
    print("The longest palindrome substring is:", result)
else:
    print("No palindrome found.")

